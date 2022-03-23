#!/usr/bin/python3

#Manejo de funciones en python

def cuadrado(x):
    return x*x

numero = input("Ingrese un número: ")

numero = int(numero)
res= cuadrado(numero)

print("El valor es : ", res)

lista = [1, 2, 3, 5, 7, 9]

for i, elemento in enumerate(lista):
    print("Elemento", i, "en lista =", elemento, "su cuadrado =", cuadrado(elemento))

cuadrados = [cuadrado(x) for x in lista]
print(cuadrados)