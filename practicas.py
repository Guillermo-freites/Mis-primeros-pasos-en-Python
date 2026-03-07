usuario = input("¿Como te llamas? ")
edad = input("¿Cual es tu edad? ")
experiencia = input("Y ¿Cuantos años de experiencia tienes programando?")

print(f"Bienvenido al Curso, {usuario}; de {edad} años y {experiencia} años de experiencia en Python" )

if (experiencia == "0"):
    print("No te preocupes, comenzaremos de 0 y haremos de ti un excelente programador")

else:
    print("Perfecto! Empecemos con un examen para valorar tu nivel")