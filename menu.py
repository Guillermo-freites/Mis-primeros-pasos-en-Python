# Basic Calculator

valor = int(input("Ingrese su primer valor: "))
valor2 = int(input("Ingrese su segundo valor: "))
operacion = input("Ingrese su operacion (+,-,*,/): ")

if operacion == "+":
    print(valor+valor2)
if operacion == "-":
    print(valor-valor2)
if operacion == "*":
    print(valor*valor2)
if operacion == "/":
    print(valor/valor2)

while True:
    valor = int(input("Ingrese su primer valor: "))
    valor2 = int(input("Ingrese su segundo valor: "))
    operacion = input("Ingrese su operacion (+,-,*,/): ")

    if operacion == "+":
        print(valor+valor2)
    if operacion == "-":
        print(valor-valor2)
    if operacion == "*":
        print(valor*valor2)
    if operacion == "/":
        print(valor/valor2)   

