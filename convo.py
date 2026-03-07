unidades = {
    "distancias" : {"km": 1000, "mt": 1, "cm": 0.01 },
    "pesos" : {"ton": 1000, "kg": 1, "gr": 0.001, "lb": 0.45359  },
    "tiempos" : {"hora": 60, "min": 1, "seg": 0.0166667 }, 
    "superficies" : {"km2": 1_000_000, "m2": 1, "cm2": 0.0001 },
    }
      

while True:

    unidad = input("Ingrese unidad a medir: ")

    if (unidad in unidades.values):
        seleccion = unidades.values(unidad)
        break
    else:
        print("Unidades no validas!")

        unidad_destino = input("Ingrese unidad destino: ")
  
    if unidad_destino in unidades.values:
        seleccion = unidades.values(unidad_destino)
        break
    else:
        print("Unidades no validas!")

 
valor_base = float(input("Ingrese valor base: "))

valor_base = valor_base*unidad
resultado = valor_base/unidad_destino

print(f"{valor_base} {unidad} = {resultado} {unidad_destino}")

