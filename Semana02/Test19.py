"""
DEYSI MARTINEZ
"""

var1 = 29 #entera
var2 = 12 #entera
var3 = 4.56 #float
var4 = 3.27 #float
var5 = "Deysi" #string
var6 = "Martinez" #string
var7 = "578" #string numerica
var8 = False #boolean

if var8:
    print("Hola Pythonistas")
if var7:
    print("Mi nombre es {} {} y estos son mis resultados: ".format(var5, var6))
#obtener y mostrar suma de variable entera con variable string numerica
suma_1 = var1 + int(var7)
print("Suma de una variable entera y variable string numerica: {}".format(suma_1))

#suma de variables enteras, variable string numerica y variables flotantes
suma_2 = var1 + var2 + int(var7) + var3 + var4
print("Suma de dos variables enteras, string numerica y variables flotantes: {}".format(f"{suma_2:.2f}"))

#modulo de variables enteras
var_int_mod = var1 % var2
print("Modulo de dos variables enteras: {}".format(var_int_mod))

#mostrar parte entera de la division de las dos variables int
division_1 = var1 / var2
print("Parte entera de la division de dos variables enteras: {}".format(int(division_1)))

#obtener una potencia teniendo como base una flotante y como potencia un entero
potencia_1 = var3 ** var2
print("Potencia de base flotante y potencia entera: {}".format(f"{potencia_1:.2f}"))
