
nombre = input("Ingrese el nombre del producto: ")


while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except:
        print("Error: Debe ingresar un número válido para el precio.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except:
        print("Error: Debe ingresar un número entero válido para la cantidad.")


costo_total = precio * cantidad

print("----- Información del Producto -----")
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", costo_total)

print("Resumen")
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

