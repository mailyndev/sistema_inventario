import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from inventario import agregar_producto, ver_productos, actualizar_producto, eliminar_producto

def ventana_agregar():
    # Nueva ventana para agregar producto
    win = tk.Toplevel()
    win.title("Agregar Producto")
    win.geometry("300x250")

    # Etiquetas y entradas
    tk.Label(win, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(win)
    entry_nombre.pack()

    tk.Label(win, text="Cantidad:").pack(pady=5)
    entry_cantidad = tk.Entry(win)
    entry_cantidad.pack()

    tk.Label(win, text="Precio:").pack(pady=5)
    entry_precio = tk.Entry(win)
    entry_precio.pack()

    # Función que se ejecuta al presionar el botón "Guardar"
    def guardar():
        nombre = entry_nombre.get()
        cantidad = entry_cantidad.get()
        precio = entry_precio.get()

        if not nombre or not cantidad or not precio:
            tk.messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        try:
            cantidad = int(cantidad)
            precio = float(precio)
            agregar_producto(nombre, cantidad, precio)
            tk.messagebox.showinfo("Éxito", "Producto agregado correctamente")
            win.destroy()  # cerrar ventana
        except ValueError:
            tk.messagebox.showerror("Error", "Cantidad y precio deben ser números")

    # Botón para guardar
    tk.Button(win, text="Guardar", command=guardar).pack(pady=10)


def ventana_productos():
    productos = ver_productos()

    win = tk.Toplevel()
    win.title("Gestión de Productos")
    win.geometry("600x400")

    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tabla = ttk.Treeview(frame, columns=("ID","Nombre","Cantidad","Precio"), show="headings")

    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio", text="Precio")

    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=220)
    tabla.column("Cantidad", width=100, anchor="center")
    tabla.column("Precio", width=100, anchor="center")

    tabla.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # -------------------------
    # REFRESCAR TABLA
    # -------------------------
    def refrescar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)

        for prod in ver_productos():
            tabla.insert("", "end", values=(prod[0], prod[1], prod[2], f"{prod[3]:.2f}"))

    refrescar_tabla()

    # -------------------------
    # EDITAR PRODUCTO
    # -------------------------
    def editar_producto():
        seleccion = tabla.focus()

        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un producto")
            return

        datos = tabla.item(seleccion)["values"]
        prod_id, nombre, cantidad, precio = datos

        form = tk.Toplevel()
        form.title("Editar Producto")
        form.geometry("300x250")

        tk.Label(form, text="Nombre").pack()
        entry_nombre = tk.Entry(form)
        entry_nombre.pack()
        entry_nombre.insert(0, nombre)

        tk.Label(form, text="Cantidad").pack()
        entry_cantidad = tk.Entry(form)
        entry_cantidad.pack()
        entry_cantidad.insert(0, cantidad)

        tk.Label(form, text="Precio").pack()
        entry_precio = tk.Entry(form)
        entry_precio.pack()
        entry_precio.insert(0, precio)

        def guardar():
            nuevo_nombre = entry_nombre.get()
            nuevo_cantidad = entry_cantidad.get()
            nuevo_precio = entry_precio.get()

            actualizar_producto(
                prod_id,
                nuevo_nombre,
                int(nuevo_cantidad),
                float(nuevo_precio)
            )

            refrescar_tabla()
            form.destroy()

        tk.Button(form, text="Guardar Cambios", command=guardar).pack(pady=10)

    # -------------------------
    # ELIMINAR PRODUCTO
    # -------------------------
    def eliminar_producto_gui():
        seleccion = tabla.focus()

        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un producto")
            return

        datos = tabla.item(seleccion)["values"]
        prod_id, nombre = datos[0], datos[1]

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Eliminar el producto {nombre}?"
        )

        if confirmar:
            eliminar_producto(prod_id)
            refrescar_tabla()

    # -------------------------
    # BOTONES
    # -------------------------
    frame_botones = tk.Frame(win)
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Editar Producto", command=editar_producto).pack(side="left", padx=10)

    tk.Button(frame_botones, text="Eliminar Producto", command=eliminar_producto_gui).pack(side="left", padx=10)

def ventana_actualizar():
    productos = ver_productos()
    if not productos:
        tk.messagebox.showinfo("Actualizar Producto", "No hay productos para actualizar")
        return

    win = tk.Toplevel()
    win.title("Actualizar Producto")
    win.geometry("500x350")

    # Frame para tabla
    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tabla = ttk.Treeview(frame, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings", selectmode="browse")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio", text="Precio")

    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=200, anchor="w")
    tabla.column("Cantidad", width=80, anchor="center")
    tabla.column("Precio", width=80, anchor="center")

    for prod in productos:
        tabla.insert("", "end", values=(prod[0], prod[1], prod[2], f"{prod[3]:.2f}"))

    # Scroll
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tabla.pack(fill="both", expand=True)

    # Función para abrir formulario de edición
    def editar():
        seleccion = tabla.focus()
        if not seleccion:
            tk.messagebox.showwarning("Actualizar Producto", "Seleccione un producto")
            return

        datos = tabla.item(seleccion)["values"]
        prod_id, nombre, cantidad, precio = datos

        form = tk.Toplevel()
        form.title("Editar Producto")
        form.geometry("300x250")

        tk.Label(form, text="Nombre:").pack(pady=5)
        entry_nombre = tk.Entry(form)
        entry_nombre.pack()
        entry_nombre.insert(0, nombre)

        tk.Label(form, text="Cantidad:").pack(pady=5)
        entry_cantidad = tk.Entry(form)
        entry_cantidad.pack()
        entry_cantidad.insert(0, cantidad)

        tk.Label(form, text="Precio:").pack(pady=5)
        entry_precio = tk.Entry(form)
        entry_precio.pack()
        entry_precio.insert(0, precio)

        def guardar_cambios():
            nuevo_nombre = entry_nombre.get()
            nuevo_cantidad = entry_cantidad.get()
            nuevo_precio = entry_precio.get()

            if not nuevo_nombre or not nuevo_cantidad or not nuevo_precio:
                tk.messagebox.showwarning("Error", "Todos los campos son obligatorios")
                return

            try:
                actualizar_producto(prod_id, nuevo_nombre, int(nuevo_cantidad), float(nuevo_precio))
                tk.messagebox.showinfo("Éxito", "Producto actualizado")
                form.destroy()
                win.destroy()
            except ValueError:
                tk.messagebox.showerror("Error", "Cantidad y precio deben ser números")

        tk.Button(form, text="Guardar", command=guardar_cambios).pack(pady=10)

    tk.Button(win, text="Editar Producto Seleccionado", command=editar).pack(pady=10)
    
def ventana_eliminar():
    productos = ver_productos()
    if not productos:
        tk.messagebox.showinfo("Eliminar Producto", "No hay productos para eliminar")
        return

    win = tk.Toplevel()
    win.title("Eliminar Producto")
    win.geometry("500x300")

    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tabla = ttk.Treeview(frame, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings", selectmode="browse")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio", text="Precio")

    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=200, anchor="w")
    tabla.column("Cantidad", width=80, anchor="center")
    tabla.column("Precio", width=80, anchor="center")

    for prod in productos:
        tabla.insert("", "end", values=(prod[0], prod[1], prod[2], f"{prod[3]:.2f}"))

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tabla.pack(fill="both", expand=True)

    def eliminar():
        seleccion = tabla.focus()
        if not seleccion:
            tk.messagebox.showwarning("Eliminar Producto", "Seleccione un producto")
            return
        datos = tabla.item(seleccion)["values"]
        prod_id, nombre, _, _ = datos

        if tk.messagebox.askyesno("Confirmar", f"¿Desea eliminar {nombre}?"):
            eliminar_producto(prod_id)
            tk.messagebox.showinfo("Éxito", "Producto eliminado")
            win.destroy()

    tk.Button(win, text="Eliminar Producto Seleccionado", command=eliminar).pack(pady=10)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("400x300")  # tamaño de la ventana

# Etiqueta de bienvenida
titulo = tk.Label(ventana, text="Bienvenido al Inventario", font=("Arial", 16))
titulo.pack(pady=20)

# Botones básicos
btn_agregar = tk.Button(ventana, text="Agregar Producto")
btn_ver = tk.Button(ventana, text="Ver Productos")
btn_actualizar = tk.Button(ventana, text="Actualizar Producto")
btn_eliminar = tk.Button(ventana, text="Eliminar Producto")

btn_agregar.pack(pady=5)
btn_ver.pack(pady=5)
btn_actualizar.pack(pady=5)
btn_eliminar.pack(pady=5)

# Conectar botones a funciones
btn_agregar.config(command=ventana_agregar)
btn_ver.config(command=ventana_productos)
btn_actualizar.config(command=ventana_actualizar)
btn_eliminar.config(command=ventana_eliminar)

# Ejecutar la ventana
ventana.mainloop()