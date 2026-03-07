tareas = ['cuna' , 'coche' , 'panales' , 'biberones' , 'banera' , 'mecedora']

while True:
        
    tarea = input("Seleccione tarea: ")

    if tarea == "1":
        print("La cuna se compra en IKEA, de segunda mano, reservala en su web antes de que se agote")
    elif tarea == "2":
        print("El coche lo puedes buscar en 'El Corte Ingles'")
    elif tarea == "3":
        print("Los panales compralos en Hiperusera")
    elif tarea == "4":
        print("Ya tienes 2 biberones, pero buscalos en el Corre")
    elif tarea == "5":
        print("La banera buscala en IKEA tambien, revisa su web a ver si tienen")
    elif tarea == "6":
        print("La mecedora es una pijada, buscala en Amazon")
    else:
        print("Esta tarea no esta disponible")

    marcar = input("Deseas marcar alguna tarea como completada? s/n: ")

    
