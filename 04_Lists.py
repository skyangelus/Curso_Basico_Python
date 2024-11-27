'''
Hay cuatro colecciones de tipos de datos en Python:
    Listas: Es una coleccion ordenada y modificable (mutable). Permite duplicar miembros
    Tuplas: Colección ordenada pero no modificable (inmutable). Permite duplicar miembros
    Set: Colección no ordenada, sin indice ni tampoco modificable pero permite agregar nuevos items al set y no permite miembros duplicados
    Diccionario: Colección no ordenada, modificable y tiene indice. No permite miembros duplicados

La lista es una colección de diferentes tipos de datos y que es modificable (mutable). Una lista puede estar vacia o tener 
items con distintos tipos de datos.

En Python se pueden crear listas de dos maneras:
'''

#********************************************************** Como crear una lista **********************************************************
#Crear la lista en una función
empty_list = list() #Crea la lista a partir de la funcion list
print(len(empty_list)) #Imprimira 0 ya que es una lista vacia

#Usando corchetes
empty_list = [] #Crea la lista vacia, sin elementos en los corchetes
print(len(empty_list)) #Imprimira 0 ya que es una lista vacia

#*********************************** Listas con valores iniciales. Usar len para encontrar el tamaño de una lista #***********************************
fruits = ['banana', 'orange', 'mango', 'lemon'] #Lista de frutas
vegetables = ['Tomato', 'Potato', 'Cobbage', 'Onion', 'Carrot'] #Lista de verduras
animal_products = ['milk', 'meat', 'butter', 'youghurt'] #Lista de productos de animales
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB'] #Lista de Tecnologias web
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] #Lista de paises

#Imprimir las listas y su tamaño
print('Fruits:',fruits)
print('Number of Fruits:',len(fruits),'\n')

print('Vegetables:',vegetables)
print('Number of Vegetables',len(vegetables),'\n')

print('Animal Products:',animal_products)
print('Nmber of animal products:',len(animal_products),'\n')

print('Web Technologies:', web_techs)
print('Number of Web Technologies:',len(web_techs),'\n')

print('Countries:',countries)
print('Number of Countries:',len(countries),'\n')