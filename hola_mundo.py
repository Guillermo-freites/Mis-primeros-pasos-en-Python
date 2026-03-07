edad = int(input("Ingresa tu edad: "))
if edad <= 34:
    print ("Estas en la flor de la vida")
elif edad >=36:
    print ("Estas envejeciendo")
elif edad == 35:
    print ("JUSTO EN DONDE TE QUERIA")
else:
    print ("ERROR DE EDAD")

def saludo():
    print("¡Hola, mundo!")
saludo()  # Imprime "¡Hola, mundo!"

def saludo(nombre):
    print(f"Hola {nombre}")
saludo("Baranda e piscina")  # Imprime "Hola, Baranda e piscina"
saludo("Joselyn")  # Imprime "Hola, Joselyn"

fecha_mes = int(input("Ingresa el dia del mes que quieres consultar: "))
if fecha_mes <= 5:
    print("Estas bien chama")
elif fecha_mes >= 6 and fecha_mes <= 15:
    print("Falta poco para el SPM")
elif fecha_mes >= 16 and fecha_mes <= 18:
    print("Tienes el periodo marica")
elif fecha_mes >= 19 and fecha_mes <= 21:
    print("Estas solo manchando, ya puedes comer platano")
elif fecha_mes >= 22 and fecha_mes <= 30:
    print("Dale guayaba, pero mosca con una vaina que estas ovulando")
else:
    print("Tu no me entiendes")

fecha_mes = int(input("Ingresa el dia del mes que quieres consultar: "))
mensajes = "Tu no me entiendes"
(range(1,6), "Estas bien chama")
(range(7,16), "Falta poco para el SPM")
(range(17,22), "Estas solo manchando, pero ya puedes comer platano")
(range(23,30), "Dale guayaba, pero mosca con una vaina que estas ovulando")
print(next((msg for r, msg in mensajes if fecha_mes in r), "Tu no me entiendes."))
