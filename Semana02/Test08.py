"""
Requisitos:

1.Crear cuatro variables, entre enteros, floats, booleans, string
2.Realizar el uso de condicionales de las variables, para dos casos true y dos casos false
3.En casos de True imprimir el valor de las otras dos variables
4.En dos condicionales compararlo con un numero por ejemplo la var entero le puedes poner mayor o menor que cero o otro numero
"""

var1 = 35
var2 = 10.245
var3 = True
var4 = False
nombre = "Julia"
edad = 30
if var3:
    print ("Mi nombre es {} y mi edad es {}".format(nombre, edad))
if var4:
    print ("Mi nombre es {} y mi edad es {}".format(var1, nombre))
print("El valor de mi variable 1 es: {}".format(var1))
print("El valor de mi variable 2 es: {}".format(var2))
if var1 > var2:
    print("El valor de mi variable 1 es {} mayor que mi variable 2 {}".format(var1, var2))
if var1 < var2:
    print("El valor de mi variable 2 es {} mayor que mi variable 1 {}".format(var1, var2))
