# HOROSCOPO CHINO 2.0

#Lista

Signos = ["Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente"]
Elementos = ["Metal ⚙️", "Agua  💧", "Madera  🪵", "Fuego 🔥" "Tierra 🌍"]

#Recopilacion de datos

while True:
    try: 
        nacimiento = int(input("Ingrese su año de Nacimiento, o presione 0 para salir: " )) 
      
        if nacimiento == 0:
            print("Gracias por usar tu calculador del Horoscopo Chino")
            break    

        if nacimiento < 1900 or nacimiento > 2030:
            print("Este año no esta dentro de nuestro calendario mistico, por favor intentalo de nuevo. ")
            continue

        diferencia = nacimiento - 2026
        indice = diferencia % 12

        ultimo_digito = nacimiento % 10
        indice_elemento = ultimo_digito // 2

        print(f"Tu signo del Horoscopo Chino es: {Signos[indice]} y Elemento de: {Elementos[indice_elemento]}")

    except ValueError: 

        print("❌ Valor incorrecto, por favor ingresa solo numeros")






