import pkg.utils


# Función lambda para aplicar un descuento del 10%
descuento_10 = lambda total: pkg.utils.aplicar_descuento(total, 0.1)

# Crear algunos productos
producto1 = input('add product1:')
precio1 = input('add proce1:')
producto2 = input('add product2:')
precio2 = input('add proce2:')
producto3 = input('add product3:')
precio3 = input('add proce3:')

productos = [
    pkg.utils.crear_producto( producto1, precio1 ),
    pkg.utils.crear_producto( producto2, precio2 ),
    pkg.utils.crear_producto( producto3, precio3 )
]

# Crear un carrito vacío
carrito = []

# Agregar productos al carrito
pkg.utils.agregar_al_carrito(carrito, productos[0])
pkg.utils.agregar_al_carrito(carrito, productos[1])

# Calcular el total
total = pkg.utils.calcular_total(carrito)
print('Total sin descuento:', total)

# Aplicar descuento y mostrar el nuevo total
total_con_descuento = descuento_10(total)
print('Total con descuento del 10%:', total_con_descuento)