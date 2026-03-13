
while True:
    nombre = input("Ingrese el nombre del producto: ").strip() 
    if nombre.replace(" ", "").isalpha():  
        break 
    else:
        print("Error: ingrese solo letras, sin números ni símbolos.")


while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))  
        if precio < 0:
            print("Error: el precio no puede ser negativo.")
            continue  
        break  
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")  


while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))  
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
            continue  
        break  
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")  


costo_total = precio * cantidad  



print("====== Información del Producto ======")
print("Producto:", nombre)
print("Precio: $", precio)
print("Cantidad:", cantidad)
print("Total: $", costo_total)


print("===Resumen===")
print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad} | Total: ${costo_total}")