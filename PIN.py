
pin_correcto = "2580"
puk_correcto = "19111992"


for intento in range (3):
    pin = input("Ingrese PIN: ")

    if pin == pin_correcto:
        print("Movil desbloqueado")
        break
    else:
        print(f"PIN Incorrecto. Te quedan {2 - intento} intentos")
else:
    print("Su tarjeta SIM ha sido bloqueada! Debe ingresar su PUK")

    for intento in range (3):
        puk = input("Ingrese su PUK: ")

        if puk == puk_correcto:
            print("PUK CORRECTO.")
            pin = input("Ingrese nuevo PIN: ")
            pin_correcto = input("Confirme nuevo PIN: ")
            break
        else:
            print(f"PUK incorrecto. Le quedan {2 - intento} intentos")
    else: 
        print("Su tarjeta SIM ha sido inhabilitada")

