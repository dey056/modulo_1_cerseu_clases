"""Problema 5"""
sueldo = int(input("Ingrese su sueldo: "))
modulo_sueldo = sueldo % 2
if modulo_sueldo == 0:
    print("Su sueldo es par")
if modulo_sueldo == 1:
    print("Su sueldo es impar")
    