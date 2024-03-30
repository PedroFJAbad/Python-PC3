class Producto:
    def __init__(self, nombre, codigo, precio, año):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}, Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados

# Ejemplo de uso
catalogo = Catalogo()

producto1 = Producto("Llanta", "001", 100, 2022)
producto2 = Producto("Batería", "002", 200, 2021)
producto3 = Producto("Aceite", "003", 50, 2022)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Todos los productos:")
catalogo.mostrar_productos()

año_filtrado = 2022
productos_filtrados = catalogo.filtrar_por_año(año_filtrado)
print(f"\nProductos filtrados por año {año_filtrado}:")
for producto in productos_filtrados:
    print(producto)