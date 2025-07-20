"""
Requisitos:

1.Crear dos variables para los valores de nombre, profesion y ciudad
2.Crear dos variabes para la remuneracion de enero y febrero (mas de 1500)
3.Crear una variable donde se sumara el ingreso de los dos meses de enero y febrero
4.Mostrar en pantalla el mensaje de:

"Hola soy 'nombre' mi profesion es 'profesion' y mi remuneracion acumulada de los meses de enero y febrero es de 'remunaracion_total'"
"""

#Creando variables

nombre = "Deysi"
ciudad = "Lima"
profesion = "Ingeniera Forestal"

enero = 2500
febrero = 2800

total = enero + febrero

print ("Hola soy {} y vivo en la ciudad de {}, soy {} de profesion y mi remuneracion acumulada de los meses de enero y febrero es de {}".format(nombre, ciudad, profesion, total))


