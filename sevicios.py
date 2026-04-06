def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """Muestra todos los productos"""
    if not inventario:
        print("Inventario vacío")
        return

    for p in inventario:
        print(p)


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza un producto"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """Elimina un producto"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario"""
    if not inventario:
        return None

    unidades = sum(p["cantidad"] for p in inventario)
    valor = sum(p["precio"] * p["cantidad"] for p in inventario)

    mas_caro = max(inventario, key=lambda p: p["precio"])
    mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades,
        "valor_total": valor,
        "producto_mas_caro": (mas_caro["nombre"], mas_caro["precio"]),
        "producto_mayor_stock": (mayor_stock["nombre"], mayor_stock["cantidad"])
    }
