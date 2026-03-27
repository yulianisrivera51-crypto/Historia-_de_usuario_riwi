print("Bienvenido a el inventario.")

# calculate quantity and prince for the total of the product
def calculoTotalProducto (cantidad, precio ):
    resultado = cantidad * precio
    return resultado

# request user data
validarProducto = True
while validarProducto:
    nombreProducto = input("Ingresa el nombre del Producto: ").strip()

    if nombreProducto and not nombreProducto.isdigit():
        validarProducto = False

    elif nombreProducto.isdigit():
        print("Error: no se permiten solo numeros en el inventario.")
    
    else:
        print("Error: el nombre del producto no puede estar vacio.")

validarPrecio = True  
while validarPrecio:
    try:
        precio = float(input("Ingresa el precio del producto: "))

        if precio > 0:
            validarPrecio = False

        else:
            print("Error: el precio del producto es positivo.")

    except ValueError:
        print("Error: porfavor ingrese un numero valido")

validarCantidad = True
while validarCantidad:
    try:
        cantidad = int(input("Ingresa la cantidad del producto: "))

        if cantidad > 0:
            validarCantidad = False

        else:
            print("Error: la cantidad del producto es positivo.")

    except ValueError:
        print("Error: porfavor ingrese un numero valido")

# show data
print(f"""
producto: {nombreProducto}
precio: {precio}
cantidad: {cantidad}
Costo Total: {calculoTotalProducto(cantidad, precio)}""")
