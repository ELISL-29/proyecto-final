# Tienda de Ropa con FastAPI

Aplicación web moderna para gestionar inventario de ropa usando FastAPI y diseño responsive.

## Instalación

1. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

Ejecuta el servidor con:
```
uvicorn main:app --reload
```

Abre tu navegador en `http://127.0.0.1:8000` para ver la tienda.

## Funcionalidades

- **Página principal**: Muestra productos en tarjetas con diseño moderno
- **Compra**: Formulario para ingresar código y comprar prendas
- **Mensajes**: Muestra confirmaciones de éxito o errores
- **Responsive**: Diseño optimizado para móvil y desktop

## Estructura

- `main.py`: Servidor FastAPI
- `templantes.html/index.html`: Plantilla principal
- `static.css`: Estilos CSS modernos
- `requirements.txt`: Dependencias