# MARIA JOSE NORIEGA MORENO
# CLAN: 8  COHORTE: 5
# inventario_ferreteria.py

print("=== Inventario de Ferretería ===")
nombre = input("Ingrese el nombre del producto: ")
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

costo_total = precio * cantidad
print("--- Producto registrado ---")
print("Producto:", nombre)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Costo total del inventario:", costo_total)
