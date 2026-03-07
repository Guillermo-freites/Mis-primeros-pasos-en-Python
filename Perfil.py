#  CREADOR DE EXPEDIENTE DE ESTUDIANTES DE PROGRAMACION

# Validacion de datos

finalidad = ""

#Toma de datos

nombre = input("Buenos dias, ¿Como te llamas? ")
edad = int(input("Perfecto, y ¿Que edad tienes? "))
experiencia = int(input("Genial, y ¿Cuantos años de experiencia tienes en programacion? "))
lenguaje = input("Ahora, indicame por favor ¿Que lenguaje quieres aprender? ")
finalidad = input(" Para poder personalizar tu experiencia, selecciona el motivo por el cual quieres aprender a programar: A = Complementar Estudios, B = Trabajo o C = Hobby: ").lower()

while finalidad not in ["a", "b", "c"]:
    finalidad = input("❌ Dato invalido!! Por favor selecciona el motivo por el cual quieres aprender a programar: A = Complementar Estudios, B = Trabajo o C = Hobby: ").lower()

if finalidad == "a":
    finalidad_a = "Complementar Estudios"
elif finalidad == "b":
    finalidad_a = "Trabajo"
else: 
    finalidad_a = "Hobby"

meta = int(input("De acuerdo, ya que hemos logrado saber para que quieres programar, indicame en meses el tiempo estimado que te tomaria lograr tu objetivo: "))


#Ancho del programa

ancho_total = 45

#Titulo 

texto_titulo = f"EXPEDIENTE DE {nombre.upper()}"
texto_titulo_centrado = texto_titulo.center (ancho_total)
titulo = f"""

=============================================
{texto_titulo_centrado}
=============================================
""" 

#Muestra de datos recopilados

perfil = f"""
- Edad: {edad}
- Experiencia: {experiencia} años
- Lenguaje a estudiar: {lenguaje}
- Objetivo de estudio: {finalidad_a}
- Plazo para objetivos: {meta} meses
- Estado actual: Estudiante de {lenguaje} de camino a Junior
"""

#Resultado impreso

print(titulo)
print(perfil)

if (finalidad == "a" or finalidad == "b"):
    print("hoy comienza el primer dia de tu nueva vida profesional, que bien que tomas la iniciativa!!! ".upper()) 
    
else:
    print("Enhorabuena! El dia de hoy comienza tu camino en el fenomenal mundo de la programacion!!! ".upper())

print("mucho exito!!!".upper())


    