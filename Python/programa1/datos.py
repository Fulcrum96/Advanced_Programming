#! /usr/bin/python
# -*- encoding: utf-8 -*-

# Programa que ve tipos de datos en Python

# Uno de los tipos más básicos y útiles de python son las listas
"""
Las listas son una estructura de datos dinámica
que pueden ser del mismo tipo o de tipo distintos
Ojo: en Python no existen arreglos, las listas pueden funcionar como arreglos
De hecho hay listas de listas que pudisen ser manejadas como "matrices"
Aunque si van a manejar operaciones especificas de vectores o matrices
La biblioteca numpy es la que rifa
"""

lista = [1, 2, 5, 7, 9]
print("Lista=", lista)

a = 2
b = 2.5
c = "Juan"
d = 'J'

l1 = [a, 2.8, b, 3, c, d]
print(l1) 

print(type(lista), type(l1))

print("La segunda posicion de lista", lista[1])
print("La última posicion de l1", lista[-1])

contador = 0

tamano=len(l1)

#Forma clásica para recorrer listas
#no recomendada
while contador<tamano:
	print("l1[", contador, "]=",l1[contador])
	contador=contador+1

#se recomienda utilizar la estructura de control for
# esta itera sobre una coleccion de objetos
for x in l1:
	print(x)

l1[0]= "Ya casi nos vamos"

#para agregar elementos a la lista se utiliza el método append()
l1.append("Viendo commits")


print(l1)

#se pueden construir listas desde cero hay dos formas
l2 = []
l3 = list()

print(l2, l3)

#se pueden crear listas por definicion
# comprehesion list

#a = [ x, x in range(1, 100)]
a = range(1,100)
print(a)

pares = [x>10, x in a]
print(pares)
