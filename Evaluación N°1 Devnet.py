#Se definen los precios con un diccionario llamado "precios"
precios = {
    "10:00": 12000,
    "15:00": 12000,
    "21:00": 12000,
}

print("-------------------------------")
print("|          Horarios           |")
print("-------------------------------")
print("| Funcion matine     | 10:00  |")
print("-------------------------------")
print("| Funcion tarde      | 15:00  |")   
print("-------------------------------")
print("| Funcion vespertina | 21:00  |")
print("-------------------------------")

#Se utiliza una lista vacia llamada "entradas" 
entradas = []
while True:
    funcion = input("Ingrese el Horario de la funcion (o 'cancelar' para terminar): ")
    if funcion == 'cancelar':
        break
    if funcion in precios:
        cantidad = int(input(f"Ingrese la cantidad de entradas para la funcion de las {funcion}, que desea comprar: "))
        entradas.append((funcion, cantidad))
        break
    else:
        print("Horario no valido.")

#Se define la funcion con "def"
def calcular_costo_total(entradas):
    total = sum(precios[funcion] * cantidad for funcion, cantidad in entradas)
    return total

#Se usa costo total de las entradas y guarda ese valor en la variable
costo_total = calcular_costo_total(entradas)
print("total a pagar,", costo_total)
pago = int(input("Ingrese la cantidad de dinero con la que desea pagar: "))
if pago >= costo_total:
    vuelto = pago - costo_total 
    print("su vuelto seria,",vuelto)
else:
    int(input("El cantidad ingresada no es suficiente, intente de nuevo: "))
    if pago >= costo_total:
        vuelto = pago - costo_total 
        print("su vuelto seria,",vuelto)
    
#Print \n deja un espacio en blanco lo que mejora la legibilidad del resultado
print("\nTicket de compra:")
print("--------------------")
if funcion == "10:00":
    print("Funcion matiné 10:00 hrs")
    print("Cantidad de entradas", cantidad)
    print("Total a pagar: $", costo_total)
    print("Dinero Ingresado: $", pago)
    print("Vuelto $", vuelto)
if funcion == "15:00":
    print("Funcion tarde 15:00 hrs")
    print("Cantidad de entradas", cantidad)
    print("Total a pagar: $", costo_total)
    print("Dinero Ingresado: $", pago)
    print("Vuelto $", vuelto)
if funcion == "21:00":
    print("Funcion vespertino 21:00 hrs")
    print("Cantidad de entradas", cantidad)
    print("Total a pagar: $", costo_total)
    print("Dinero Ingresado: $", pago)
    print("Vuelto $", vuelto)