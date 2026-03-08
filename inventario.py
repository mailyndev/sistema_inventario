from database import conectar

def agregar_producto(nombre, cantidad, precio):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
    valores = (nombre, cantidad, precio)

    cursor.execute(sql, valores)
    conexion.commit()

    print("Producto agregado correctamente")

    cursor.close()
    conexion.close()


def ver_productos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    resultados = cursor.fetchall()

    for producto in resultados:
        print(producto)

    cursor.close()
    conexion.close()
    return resultados #devolvemos la lista
    
def actualizar_producto(producto_id, nombre=None, cantidad=None, precio=None):
    conexion = conectar()
    cursor = conexion.cursor()

    # Creamos la lista de campos a actualizar
    campos = []
    valores = []

    if nombre is not None:
        campos.append("nombre = %s")
        valores.append(nombre)
    if cantidad is not None:
        campos.append("cantidad = %s")
        valores.append(cantidad)
    if precio is not None:
        campos.append("precio = %s")
        valores.append(precio)

    if campos:  # Solo actualizamos si hay campos
        sql = f"UPDATE productos SET {', '.join(campos)} WHERE id = %s"
        valores.append(producto_id)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Producto actualizado correctamente")
    else:
        print("No se proporcionaron campos para actualizar")

    cursor.close()
    conexion.close()
    
def eliminar_producto(producto_id):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "DELETE FROM productos WHERE id = %s"
    cursor.execute(sql, (producto_id,))
    conexion.commit()

    print("Producto eliminado correctamente")

    cursor.close()
    conexion.close()
    