from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from urllib.parse import quote_plus
import os

app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2 para templates
templates = Jinja2Templates(directory="templates")

# Diccionario de inventario (igual al de TIENDA.py)
inventario = {
    'C001': {'nombre': 'Remera blanca', 'precio': 499.90, 'stock': 10},
    'C002': {'nombre': 'Pantalón jean', 'precio': 1299.00, 'stock': 5},
    'C003': {'nombre': 'Camisa a cuadros', 'precio': 799.50, 'stock': 7},
    'C004': {'nombre': 'Chaqueta impermeable', 'precio': 1599.99, 'stock': 3},
    'C005': {'nombre': 'Shorts deportivos', 'precio': 599.00, 'stock': 8}
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, mensaje: str = None, tipo: str = None):
    context = {
        "request": request,
        "inventario": inventario,
    }

    if mensaje is not None:
        context["mensaje"] = mensaje
    if tipo is not None:
        context["tipo"] = tipo

    template = templates.get_template("index.html")
    return HTMLResponse(template.render(context))

@app.post("/comprar")
async def comprar_prenda(codigo: str = Form(...)):
    codigo = codigo.upper().strip()
    if codigo not in inventario:
        mensaje = quote_plus("❌ Código no encontrado")
        return RedirectResponse(url=f"/?mensaje={mensaje}&tipo=error", status_code=303)

    if inventario[codigo]['stock'] <= 0:
        mensaje = quote_plus("❌ Stock agotado para este producto")
        return RedirectResponse(url=f"/?mensaje={mensaje}&tipo=error", status_code=303)
    
    # Restar 1 al stock
    nombre_prenda = inventario[codigo]['nombre']
    inventario[codigo]['stock'] -= 1
    mensaje = quote_plus(f"✅ ¡Gracias! Compraste {nombre_prenda}. Stock restante: {inventario[codigo]['stock']}")
    return RedirectResponse(url=f"/?mensaje={mensaje}&tipo=exito", status_code=303)