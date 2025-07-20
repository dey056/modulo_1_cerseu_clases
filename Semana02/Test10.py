"""
Conversion de datos
"""

#Creacion de variables

var_str = "54796"
nombre = "Johanna"
modulo = 2
prom = 18.956

#Conversion de string a entero (si se puede)
var_int = int(var_str)
print(var_int)
print(type(var_int))

#Conversion de entero a string (si se puede)
var_mod = str(modulo)
print(var_mod)
print(type(var_mod))

#Conversion de flotante a entero

var_entera = int(prom)
print(var_entera)
print(type(var_entera))

#Conversion de un string de letras a entero
var_nom = int(nombre) #no lo puede convertir a entero porque el nombre tiene puras letras
print(type(var_nom))




