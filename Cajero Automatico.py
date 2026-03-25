#   CAJERO AUTOMATICO

# LISTAS

Opciones = ["Realizar una operacion", "Ver Saldo", "Salir"]
Operaciones = ["Realizar un retiro", "Realizar un ingreso", "Realizar un pago", "Volver"] 
Pagos = ["Servicios", "Impuestos", "Aranceles Administrativos", "Volver"]
Servicios = ["Luz", "Agua", "Gas", "Internet", "Telefonia", "Alquiler", "Volver"]
Impuestos = ["I. R. P. F.", "I. V. A.", "I. N. S. S.", "Volver"]
Aranceles = ["Tramites", "Renovaciones", "Volver"]
Tramites = ["DNI", "Pasaporte", "NIE", "Nacionalidad", "Volver"]
Renovaciones = ["DNI", "Pasaporte", "NIE", "Volver"]
Menu_Saldo = ["Volver", "Salir"]
Cuentas = ["Ahorro", "Corriente", "Credito de la Tarjeta", "Volver"]
Retiros = [20, 50, 100, 150, 200, "Otra cantidad", "Volver"]

#FUNCIONES

#VALIDACION INICIO DE SESION

import csv 

def valid_user():
    Ident = input(" INGRESE SU DNI/NIE/NIF: ")

    try:
        with open('UsuariosCajero.csv', mode='r', encoding='utf-8') as archivo:
            lector = list(csv.DictReader(archivo))

            for fila in lector:

                if fila['DNI/NIE'] == Ident:

                    if fila['ESTADO'] == 'SUSPENDIDA':
                        print("❌CUENTA SUSPENDIDA TEMPORALMENTE. Contacte con su Oficina para gestionar su desbloqueo")
                        return 0, "Desconocido", False
                    
                    intentos = 3

                    while intentos > 0:
                        input_pin = input(f"🔐 Intentos restantes: {intentos}, Ingrese su PIN: ")
                        if fila['PIN'] == input_pin:
                            print(f" ✅ Bienvenido/a {fila['NOMBRE']}!")
                            print(f"El estado de su cuenta es {fila['ESTADO']}")
                            print(f"Su saldo es: {fila['SALDO']}")
                            return float(fila['SALDO']), fila ['NOMBRE'], True, fila ['DNI/NIE']

                        else:
                            intentos -= 1
                            print("❌ PIN incorrecto.")

                        if intentos == 0:
                            print("❌CUENTA SUSPENDIDA TEMPORALMENTE POR INTENTOS FALLIDOS. Contacte con su Oficina para gestionar su desbloqueo")
                            update_database(Ident, fila['SALDO'], "SUSPENDIDA")
                            return 0, "Bloqueado", False, Ident

            print("❌El DNI/NIE no se encuentra en nuestra base de datos.")
            return 0, "Desconocido", False, None

    except FileNotFoundError:
        print("ERROR ❌ No se encontro el archivo 'UsuariosCajero.csv'.")
        return 0, "Desconocido", False, None

#IMPR GRABADORA DE DATOS

def update_database(DNI, Saldo_act, Estado_act):
    filas_actualizadas = []

    try:
        with open('UsuariosCajero.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            columnas = lector.fieldnames

            for fila in lector:
                if fila['DNI/NIE'] == DNI:
                    fila ['SALDO'] = str(round(float(Saldo_act), 2))
                    fila ['ESTADO'] = Estado_act

                filas_actualizadas.append(fila)

        with open('UsuariosCajero.csv', mode='w', newline= '', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(filas_actualizadas)
    
    except Exception as e:
        print(f"❌ ERROR AL GUARDAR EN LA BASE DE DATOS {e}")



#IMPR LISTAS DE MENU
def mostrar_menu(lista_para_imprimir):
    for numero, texto in enumerate(lista_para_imprimir, start=1):
        print(f"{numero}.{texto}")

#IMPR ALGORITMO DE RETIROS
def retirado(lista_opciones, saldo):

    while True:
        try:
            mostrar_menu(Retiros)

            Importe = int(input("Ingrese importe a retirar: "))
                                       
            if Importe >= 1 and Importe <= 5:
                Importe_retirado = int(Retiros[Importe - 1])

                if Importe_retirado > Saldo or Importe_retirado <= 0:
                    print(f"❌ Importe incorrecto. Su saldo es: €{Saldo}")
                    continue
                       
                else:
                    return Importe_retirado    

            elif Importe == 6:
                Importe_retiro = int(input("Ingrese el importe exacto a retirar: "))
                if Importe_retiro > Saldo or Importe_retiro <= 0:
                    print(f"❌ Importe incorrecto. Su saldo es: €{Saldo}")
                    continue             
            
                else:
                    return Importe_retiro
            
            elif Importe == 7:
                return 0
            
            else:
                break

        except ValueError:
            print("❌ Seleccion incorrecta. Ingrese una opcion valida")
            continue
                                
#IMP ALGORITMO DE INGRESOS
def ingresado():
    while True:
        try:

            ingreso = float(input("Ingrese importe especifico a ingresar en cuenta: "))

            if ingreso <= 0:
                print("❌ Seleccion incorrecta. Ingrese un importe valido")
            
            else:
                return ingreso
    
        except ValueError:
            print("❌ Seleccion incorrecta. Ingrese una opcion valida")
            continue

#IMP PROCEDIMIENTO DE PAGOS
def proceso_pagos(pago_nombre, saldo):

    while True:
        try:

            print(f" ---- Realizando su pago de: {pago_nombre.upper()} ---- ")
            referencia = input("Ingrese el numero de Referencia: ")
            importe_pago = float(input(" Ingrese el importe exacto que desea pagar, €: "))

            if importe_pago > Saldo or importe_pago <= 0:
                print("Su pago no se puede realizar, ingrese un importe valido: ")
                continue

            else:
                print(f" Su pago de {pago_nombre} se ha procesado correctamente ✅")
                print(f" Ref: {referencia}")
                return importe_pago
            
        except ValueError:
            print("❌ Seleccion incorrecta. Ingrese una opcion valida")
            continue
            


#TITULO/ENCABEZADO
ancho_total = 40
texto_titulo = f" BIENVENIDO AL BANCO LUCAS GAEL"
texto_titulo_centrado = texto_titulo.center (ancho_total)
titulo = (f"""
          
---------------------------------------
{texto_titulo_centrado}
---------------------------------------""")


print(titulo)

Saldo, Usuario_Actual, Acceso, DNI = valid_user()

if not Acceso:
    print("Saliendo del sistema... ")
    import sys
    sys.exit()

while True:
    try:
        #Menu Principal
        print(" --- MENU PRINCIPAL --- ")
        
        mostrar_menu(Opciones)

        Seleccion1 = int(input("Seleccione una opcion: "))

        # Nivel 1 - Operaciones y Menu
        if Seleccion1 == 1:
            while True:
                try:
                    print(f" --- OPERACIONES --- ")
                    
                    mostrar_menu(Operaciones)

                    Seleccion_op = int(input("Por favor seleccione una opcion: "))

                    #RETIROS DE CUENTA

                    if Seleccion_op == 1:
                        while True:
                            try: 
                                mostrar_menu(Cuentas)

                                Seleccion_cuenta = int(input("Seleccione tipo de cuenta: "))

                                #Retiro Cuenta de Ahorro

                                if Seleccion_cuenta == 1:
                                    print(" --- RETIROS - CUENTA DE AHORROS ")

                                    saldo_final = retirado(Retiros, Saldo)

                                    Saldo -= saldo_final

                                    update_database(DNI, Saldo, "ACTIVA")

                                    if saldo_final > 0:
                                        print(f"RETIRO EXITOSO DE: €{saldo_final}")
                                        print(f"Su nuevo saldo es: €{Saldo}")
                                        break

                                #Retiro Cuenta Corriente

                                elif Seleccion_cuenta == 2:
                                    print(" --- RETIROS - CUENTA CORRIENTE ")

                                    saldo_final = retirado(Retiros, Saldo)

                                    Saldo -= saldo_final

                                    update_database(DNI, Saldo, "ACTIVA")

                                    if saldo_final > 0:
                                        print(f"RETIRO EXITOSO DE: €{saldo_final}")
                                        print(f"Su nuevo saldo es: €{Saldo}")
                                        break
                        
                                #Retiro Credito de Tarjeta
                                        
                                else:
                                    
                                    print(" --- RETIROS - CREDITO DE TARJETA ")

                                    saldo_final = retirado(Retiros, Saldo)

                                    Saldo -= saldo_final

                                    update_database(DNI, Saldo, "ACTIVA")

                                    if saldo_final > 0:
                                        print(f"RETIRO EXITOSO DE: €{saldo_final}")
                                        print(f"Su nuevo saldo es: €{Saldo}")
                                        break

                            except ValueError:
                                print("❌ Seleccion incorrecta. Ingrese una opcion valida")
                                continue
                    
                    #INGRESOS EN CUENTA

                    elif Seleccion_op == 2:
                        while True:
                            try:
                                print(" --- INGRESOS EN CUENTA ")

                                total_depositado = ingresado()

                                Saldo += total_depositado

                                update_database(DNI, Saldo, "ACTIVA")

                                print(f"INGRESO EXITOSO DE: €{total_depositado}")
                                print(f"Su nuevo saldo es: €{Saldo}")
                                break

                            except ValueError:
                                print("❌ Seleccion incorrecta. Ingrese una opcion valida")
                                continue
                    
                    #PAGO DE SERVICIOS

                    elif Seleccion_op == 3:
                        while True:
                            try:
                                print(" --- PAGO DE SERVICIOS ")
                                mostrar_menu(Pagos)
                                seleccion_pagos = int(input(" Ingrese el tipo de Pago que quiere realizar: "))

                                if seleccion_pagos == 1:
                                    
                                    mostrar_menu(Servicios)
                                    pagar_servicio = int(input(" Seleccione el servicio a pagar: "))

                                    if pagar_servicio >= 1 and pagar_servicio <= 6:

                                        nombre_pago = Servicios[pagar_servicio - 1]
                                        servicio_pagado = proceso_pagos(nombre_pago, Saldo)
                                        Saldo -= servicio_pagado

                                        update_database(DNI, Saldo, "ACTIVA")

                                    else:
                                        break
                                
                                elif seleccion_pagos == 2:

                                    mostrar_menu(Impuestos)
                                    pagar_impuesto = int(input("Ingrese el impuesto que desea pagar: "))

                                    if pagar_impuesto >= 1 and pagar_impuesto <= 3:

                                        nombre_pago = Impuestos[pagar_impuesto - 1]
                                        impuesto_pagado = proceso_pagos(nombre_pago, Saldo)                                    
                                        Saldo -= impuesto_pagado
                                    
                                        update_database(DNI, Saldo, "ACTIVA")

                                    else:
                                        break

                                elif seleccion_pagos == 3:

                                    mostrar_menu(Aranceles)
                                    pagar_aranceles = int(input("Ingrese el arancel administrativo que desea pagar: "))

                                    if pagar_aranceles == 1:

                                        mostrar_menu(Tramites)
                                        pagar_tramite = int(input("Ingrese el tramite que desea pagar: "))

                                        if pagar_tramite >= 1 and pagar_tramite <= 4:

                                            nombre_pago = Tramites[pagar_tramite - 1]
                                            tramite_pagado = proceso_pagos(nombre_pago, Saldo)
                                            Saldo -= tramite_pagado

                                            update_database(DNI, Saldo, "ACTIVA")

                                        else:
                                            break

                                    elif pagar_aranceles == 2:

                                        mostrar_menu(Renovaciones)
                                        pagar_renovacion = int(input(" Ingrese la renovacion de documento que desea pagar: "))

                                        if pagar_renovacion >= 1 and pagar_renovacion <= 3:

                                            nombre_pago = Renovaciones[pagar_renovacion - 1]
                                            renovacion_pagada = proceso_pagos(nombre_pago, Saldo)
                                            Saldo -= renovacion_pagada

                                            update_database(DNI, Saldo, "ACTIVA")

                                        else:
                                            break
                                    else:
                                        break
                                else:
                                    break
                                                    
                            except ValueError:
                                print("❌ Seleccion incorrecta. Ingrese una opcion valida")
                                continue 

                    else:
                        break
                    

                except ValueError:
                    print("❌ Seleccion incorrecta. Ingrese una opcion valida")
                    continue

        #Imprime Saldo
        elif Seleccion1 == 2:
            while True:
                try:
                    print (f"Su saldo actual es: {Saldo}")
                   
                    mostrar_menu(Menu_Saldo)

                    Seleccion_Saldo = int(input("Por favor seleccione una opcion: "))

                    if Seleccion_Saldo == 1:
                        break
                    elif Seleccion_Saldo == 2:
                        print(" ---- GRACIAS POR USAR NUESTROS CAJEROS AUTOMATICOS, BUENOS DIAS!!! ---- ")
                        exit()
                except ValueError:
                    print("❌ Seleccion incorrecta. Ingrese una opcion valida")
                    continue
        #Imprime Salida
        elif Seleccion1 == 3:
            print(" ---- GRACIAS POR USAR NUESTROS CAJEROS AUTOMATICOS, BUENOS DIAS!!! ---- ")
            break

        else:
            print("❌ Seleccion incorrecta. Ingrese una opcion valida")
            continue
    except ValueError:
        print("❌ Seleccion incorrecta. Ingrese una opcion valida")
        continue