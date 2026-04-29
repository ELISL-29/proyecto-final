# Programa de inventario de ropa usando diccionario
# Cada clave es un código de prenda con precio y stock

inventario = {
    'C001': {'nombre': 'Remera blanca', 'precio': 499.90, 'stock': 10},
    'C002': {'nombre': 'Pantalón jean', 'precio': 1299.00, 'stock': 5},
    'C003': {'nombre': 'Camisa a cuadros', 'precio': 799.50, 'stock': 7},
    'C004': {'nombre': 'Chaqueta impermeable', 'precio': 1599.99, 'stock': 3},
    'C005': {'nombre': 'Shorts deportivos', 'precio': 599.00, 'stock': 8}
}


def mostrar_inventario():
    print('\nLista completa de ropa en inventario:')
    print('-' * 40)
    for codigo, datos in inventario.items():
        print(f"Código: {codigo} | Producto: {datos['nombre']} | Precio: ${datos['precio']:.2f} | Stock: {datos['stock']}")
    print('-' * 40)


def buscar_producto():
    codigo = input('Ingrese el código de ropa a buscar: ').strip().upper()
    if codigo in inventario:
        datos = inventario[codigo]
        print(f"\nCódigo encontrado: {codigo}")
        print(f"Producto: {datos['nombre']}")
        print(f"Precio: ${datos['precio']:.2f}")
        print(f"Stock disponible: {datos['stock']}")
    else:
        print('\nCódigo no encontrado en el inventario.')


def procesar_compra():
    codigo = input('Ingrese el código de la prenda que desea comprar: ').strip().upper()
    if codigo not in inventario:
        print('\nEl código no existe. Intente nuevamente.')
        return

    datos = inventario[codigo]
    print(f"\nProducto: {datos['nombre']}")
    print(f"Precio: ${datos['precio']:.2f}")
    print(f"Stock actual: {datos['stock']}")

    if datos['stock'] <= 0:
        print('Lo siento, no hay stock disponible para este producto.')
        return

    confirmar = input('¿Desea confirmar la compra? (s/n): ').strip().lower()
    if confirmar == 's':
        if datos['stock'] > 0:
            inventario[codigo]['stock'] -= 1
            print('Compra confirmada. Se restó 1 unidad del stock.')
            print(f"Stock restante para {codigo}: {inventario[codigo]['stock']}")
        else:
            print('No se puede completar la compra. Stock insuficiente.')
    else:
        print('Compra cancelada.')


def mostrar_menu():
    print('\n=== Menú de Inventario ===')
    print('1. Mostrar lista completa de inventario')
    print('2. Buscar producto por código')
    print('3. Comprar producto')
    print('4. Salir')


def main():
    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            buscar_producto()
        elif opcion == '3':
            procesar_compra()
        elif opcion == '4':
            print('GRACIAS POR SU COMPRA. !vuelva pronto!')
            break
        else:
            print('Opción inválida. Por favor seleccione una opción válida.')


if __name__ == '__main__':
    main()
