import sys
from prueba.guille import mifuncion
# from guille import saludo, otra_funcion
# from guille import *



# print(sys.version)

print(mifuncion(3))
_myVar = 8
# print(_myVar)

#!nombre de variable no valido (guion medio)
#myy-var = 5

my_var = 4

MyVards = 4

myVaaa = 4

#! x,y,z = 9 NO VALIDO
# x,y,z = 9,45,2


fruits = ['apple2', 'banana2', 'cherry2']
# fruits.remove("apple")
# fruits.remove("apple")
fruits.append("mango")
print(fruits)

v=r=t=6
print(v)
print(r)
v= 99
# v= str(v)

#?PARA PONER VARIABLES EN TEXTO
print(f"el precio es {v:.2f} dolares")

#! q|e|r="fsfdsf" NO VALIDO

print('Hello','World')

def arrancar(valor):
    global a
    a = valor
    

arrancar("ureeee")

print(a)
a = "Hello World"
print(len(a))

asd=("apple", "banana", "cherry") #tupla

grdf= {"name" : "John", "age" : 36} #dict

myset = {'apple', 'banana', 'cherry'} #set
myset2 = {'a', 'b', 'c'} #set

fruits2 = ['apple2', 'banana2', 'cherry2']
resultado = " ".join(fruits2)
print(resultado)
# Sí existe el método join() en Python.
# Es muy útil para unir elementos de un iterable en una sola cadena, usando un separador.
# Los elementos del iterable deben ser cadenas, de lo contrario, obtendrás un error.

# myset.discard NO lanza error, si no encuentra el elemento a borrar no hace nada
# myset.remove LANZA EXCEPCION (se usa tanto en set como en array, la tupla no admite esos metodos q la modifiquen)

print(myset.union(myset2))
 
ree = False
print(type(v))

"""
tipos de datos: str , int, float, tuple, dict (objeto=diccionario), list (array), bool, complex (numero complejo), set
"""
y = {'type' : 'fruit', 'name' : 'banana'}
y.update({'age': 'no tiene'}) #update sirve para reemplazar e insertar en un diccionario
y.pop("type")
# y.clear()
print(y.values()) #valor
print(y.items()) #clave-valor
# y.keys()
# y.copy()

#ACCEDER A TODOS LOS OBJETOS ANIDADOS (PUEDO ANIDAR HASTA EL NIVEL Q QUIERA)
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}

for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])



a = 50
b = 10
if a==b:
  print("1")
elif a > b: #else if
  print("2")
else:
  print("3")


x = ' Welcome '.replace("e","E")
print(x)
print(len(x))
print(x[3:])

# mifuncion()

# for x in fruits:
#     print(x)

# [print(x) for x in fruits]

numeros = [8,6,8,4,21,6,6,1,0]
numeros.sort() # NO DEVUELVE NADA SORT -> None
# numeros.reverse()
print(numeros)

copia = list(numeros) #para copiar listas sin la referencia?
# copia2 = numeros.copy()
copia3 = numeros[:]

print(copia3)

list4 = numeros.copy()
list4.extend(copia)
print(list4)