"""
Requisitos:

1.Crear cuatro variables, entre enteros, floats, booleans, string
2.Realizar el uso de condicionales de las variables, para dos casos true y dos casos false
3.En casos de True imprimir el valor de las otras dos variables
4.En dos condicionales compararlo con un numero por ejemplo la var entero le puedes poner mayor o menor que cero o otro numero
"""
#creando variables
var1 = 15
var2 = 0
var3 = 10.57
var4 = False

if var1: #True
    print("Me llamo Deysi Martinez")
if var2: #False
    print("{} es menor que {}".format(var1, var3))
if var3 < var1: #True
    print("Mi variable 3 es {} y es menor que mi variable 1 {}".format(var3, var1))
if var4: #False
    print("El cielo es verde")
