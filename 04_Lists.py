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
print("\nEjercicio 1 ************************************************************\n")
empty_list = list() #Crea la lista a partir de la funcion list
print(len(empty_list)) #Imprimira 0 ya que es una lista vacia

#Usando corchetes
empty_list = [] #Crea la lista vacia, sin elementos en los corchetes
print(len(empty_list)) #Imprimira 0 ya que es una lista vacia

#*********************************** Listas con valores iniciales. Usar len para encontrar el tamaño de una lista #***********************************
print("\nEjercicio 2 ************************************************************\n")
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

# Las listas pueden tener items de distintos tipos de datos
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

#*********************************** Acceder a elementos de la lista usando indexaso positivo ***********************************
#Podemos acceder a los elementos de una lista comenzando desde el indice 0 que sería el primer elemento y así susesivamente
print("\nEjercicio 3 ************************************************************\n")
#Ejemplo: index=0    index=1  index=2  index=3 
fruits = ['banana', 'orange', 'mango', 'lemon'] #Lista de frutas
first_fruit = fruits[0]
print('First Fruit:',first_fruit,'\n')#banana
second_fruit = fruits[1]
print('Second Fruist:',second_fruit,'\n')#orange
third_fruit = fruits[2]
print('Third Fruit:',third_fruit,'\n')#mango
fourth_fruit = fruits[3]
print('Fourth Fruit:',fourth_fruit,'\n')#lemon
#Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print('Last Fruit is:',last_fruit,'\n')#Lemon

#*********************************** Acceder a elementos de la lista usando indexaso negativo ***********************************
#Indexado negativo, significa comenzar desde el final, -1 se refiere al ultimo item, -2 se refiere al penultimo item.
print("\nEjercicio 4 ************************************************************\n")
#Ejemplo: index=-4   index=-3  index=-2 index=-1 
fruits = ['banana', 'orange', 'mango', 'lemon'] #Lista de frutas
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print('First Fruit:',first_fruit,'\n')#banana
print('Last Fruit:',last_fruit,'\n')#lemon
print('Seconds Last Fruit:',second_last,'\n')#mango

#*********************************************** Desempaquetando Items de la lista **********************************************
print("\EJEMPLO ************************************************************\n")
lst = ['item1','item2','item3','item4','item5']
first_item,second_item,third_item, *rest = lst
print('First Item:',first_item,'\n')#item1
print('Second Item:',second_item,'\n')#item2
print('Third Item:',third_item,'\n')#item3
print('Rest of Items:',rest,'\n')#['item4', 'item5'] 

print("\nEjercicio 5 ************************************************************\n")
fruits = ['banana','orange','mango','lemon'] #Lista de frutas
first_fruit,second_fruit,third_fruit, *rest = fruits
print('First Fruit:',first_fruit,'\n')#banana
print('Second Fruit:',second_fruit,'\n')#orange
print('Third Fruit:',third_fruit,'\n')#mango
print('Rest Of Fruit:',rest,'\n')#['lemon']

print("\nEjercicio 6 ************************************************************\n")
first,second,third,*rest,nineth,tenth = [1,2,3,4,5,6,7,8,9,10]
print('First value:',first,'\n')#1
print('Second value:',second,'\n')#2
print('Third value:',third,'\n')#3
print('Rest of values',rest,'\n')#[4, 5, 6, 7, 8] 
print('Nineth value:',nineth,'\n')#9
print('Tenth value',tenth,'\n')#10

print("\nEjercicio 7 ************************************************************\n")
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr,fr,bg,sw,*scandic,es = countries
print(gr,'\n')#Germany
print(fr,'\n')#France
print(bg,'\n')#Belgium
print(sw,'\n')#Sweden
print(scandic,'\n')#['Denmark', 'Finland', 'Norway', 'Iceland'] 
print(es,'\n')#Estonia

#*********************************************** Rebanar(Slicing) items de una lista ***********************************************
'''
Indexación positiva: Podemos especificar un rango de indices, especificando un inicio, fin y paso, el valor de retorno
sera una lista nueva. (Valores por defecto start = 0, end = len(list) - 1 (last item), step = 1)
'''
print("\Ejercicio 8 ************************************************************\n")
fruits = ['banana','orange','mango','lemon'] #Lista de frutas
all_fruits = fruits[0:4]#Regresa todos los valores de la lista
print(all_fruits)#['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[0:]#Si no se especifica donde detenerse, tomara el resto en adelante
print(all_fruits)#['banana', 'orange', 'mango', 'lemon']

orange_and_mango = fruits[1:3]#comienza desde el index[1] y termina en el index[2], no se imprime el item index[3]
print(orange_and_mango)#['orange', 'mango'] No incluye el primer item index[0]

orange_mango_lemon = fruits[1:]#Comienza desde el index[1], y termina hasta el final de la lista
print(orange_mango_lemon)#['orange', 'mango', 'lemon']

orange_and_lemon = fruits[::2]#Se usa un tercer argumento, el step. Comienza a imprimir cada dos elementos. Por eso se salta los primeros dos elementos y solo imprime los dos ultimos de la lista
print(orange_and_lemon)#['banana', 'mango']

'''
Indexación negativa: Podemos especificar un rango de indices negativos especificando el inicio, fin y el step, el valor de retorno
sera una nueva lista.
'''
print("\Ejercicio 9 ************************************************************\n")
fruits = ['banana','orange','mango','lemon']#Lista de frutas

all_fruits = fruits[-4:]#Regresa todas las frutas
print(all_fruits)#['banana', 'orange', 'mango', 'lemon']

orange_and_mango = fruits[-3:-1]#No incluye el ultimo indice index[-1]
print(orange_and_mango)#['orange', 'mango']

orange_mango_lemon = fruits[-3:]#Comienza desde el index[-3] hasta el final de la lista
print(orange_mango_lemon)#['orange', 'mango', 'lemon']

reverse_fruit = fruits[::-1]#No especificamos el inicio, ni el fin, pero el step lo usamos para que recorra la lista de atras hacia adelante con valores negativos, hasta recorrer toda la lista
print(reverse_fruit)#['lemon', 'mango', 'orange', 'banana']

#******************************************************* Modificando listas ********************************************************
'''
La lista es una colección ordenada de items muteable o modificable.
'''
print("\Ejercicio 10 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits) #['avocado', 'orange', 'mango', 'lemon']

fruits[1] = 'apple'#['avocado', 'apple', 'mango', 'lemon']
print(fruits)
last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)#['avocado', 'apple', 'mango', 'lime']

#******************************************************* Verificando Items en una lista *******************************************************
'''
Se puede verificar un item de una lista usando un operador. Por ejemplo
'''
print("\Ejercicio 11 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits #Verifica si el item 'banana' esta dentro de la lista fruit, si es así, devuelve un True o False y lo guarda en la variable does_exist
print(does_exist) #True
does_exist = 'lime' in fruits
print(does_exist)#False

#******************************************************* Agregando Items a una lista *******************************************************
'''
Para agregar un item al final de una lista se usa el método append()

#Sintaxys
lst = list() Se crea la lista
lst.append(item) se agrega el item deseado al final de la lista
'''
print("\Ejercicio 12 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon'] #Se crea y define la lista
fruits.append('apple') #se agrega el item apple al final de la lista
print(fruits) #['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits) #['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

#******************************************************* Insertando Items en una lista *******************************************************
'''
Podemos usar el método insert() para insertar un item en un indice especifico en una lista. Nota que los otros items son deplazados
a la derecha. El método insert() toma dos argumentos, index y el item a insertar.

syntaxis
lst = ['item1', 'item2']
lst.insert(index, item)
'''
print("\Ejercicio 13 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)#['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'apple')#inserta el elemento 'apple' en el indice 2, desplazando a la derecha 'mango' y 'lemon'
print(fruits)#['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3,'lime')#inserta el elemento 'lime' en el indice 3, desplazando a la derecha 'mango' y 'lemon'
print(fruits)

#******************************************************* Removiendo Items de una lista *******************************************************
'''
El método remove(), remueve un elemento de una lista

syntaxis
lst = ['item1','item2']
lst.remove(item)
'''
print("\Ejercicio 14 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print(fruits)#['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana') #Elimina el primer elemento de izquierda a derecha que coincida con 'banana'
print(fruits)#['orange', 'mango', 'lemon', 'banana']
fruits.remove('lemon')#Elimina el elemento 'lemon' de la lista
print(fruits)#['orange', 'mango', 'banana']

#******************************************************* Removiendo Items usando pop *******************************************************
'''
El método pop() remueve el item con el index especificado, o el ultimo item si no se especifíca el index

syntaxis
lst = ['item1', 'item2']
lst.pop() #remove the last item from the list
lst.pop(item) #remove the item[index] especificadoß
'''
print("\Ejercicio 15 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)#['banana', 'orange', 'mango', 'lemon']
fruits.pop() #remueve el elemento de la lista que es 'lemon'
print(fruits) #['banana', 'orange', 'mango']

fruits.pop(0) #remueve el elemento con índice = 0 que es 'banana'
print(fruits) #['orange', 'mango']

#******************************************************* Removiendo items usando del *******************************************************
'''
La palabra clave "del" remueve el indice especificado y también puede ser usada para borrar elementos en un rango de indice.
A su vez puede eliminar la lista completa.

#syntaxis
lst = ['item1', 'item2'] #Crea la lista
del lst[index] #Elimina un solo item con el indice especificado
del lst #Elimina la lista completa
'''
print("\Ejercicio 16 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']#creación de la lista
print(fruits)#['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[0]#Elimina el elemento con el indice 0 que sería 'banana'
print(fruits)#['orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[1]#Elimina el elemento con el indice 1 que sería 'mango'
print(fruits)#['orange', 'lemon', 'kiwi', 'lime']

del fruits[1:3]#Elimina los elementos que estan entre los indices dados pero sin eliminar el elemento con el indice 3, así que se elimina fruits[1] = 'lemon y fruits[2] = 'kiwi'
print(fruits)#['orange', 'lime']

del fruits#Elimina la lista por completo
#print(fruits) #NameError: name 'fruits' is not defined

#******************************************************* Limpiando elementos de una lista *******************************************************
'''
El método clear(), limpia los elementos de una lista

#syntaxis
lst = ['item1', 'item2'] #Creación de la lista
lst.clear() #Se limpia el contenido de la lista
'''
print("\Ejercicio 17 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']#Creación de la lista
print(fruits)#['banana', 'orange', 'mango', 'lemon']

fruits.clear()#Se limpia la lista
print(fruits) #Se imprime la lista vacia

#******************************************************* Copiar una lista *******************************************************
'''
Es posible copiar una lista a una nueva variable, haciendolo de la siguiente forma: lst1 = lst2. Ahora lst2 es referencia de lst1.
Todos los que hagamos en lst2 también modificaran lst1. Pero hay muchos casos en los que no queremos modificar la lista original, en
su lugar, hacemos una copia diferente. Una forma de evitar este problema es usando el método copy()

# syntax
lst = ['item1', 'item2'] #Crea la lista
lst_copy = lst.copy() #crea una copia e la lista lst y la guarda en la nueva lista lst_copy
'''
print("\Ejercicio 18 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon'] #Creación de la lista
fruits_copy = fruits.copy() #copia la lista fruits y la guarda en la lista fruist_copy

print('original list: ',fruits, '\ncopied list: ',fruits_copy)#original list:  ['banana', 'orange', 'mango', 'lemon'] copied list:  ['banana', 'orange', 'mango', 'lemon']

#******************************************************* Uniendo listas *******************************************************
'''
Hay muchas formas de unir listas en o concatener dos o más listas en Python.
'''

'''
Operador plus (+)
#Syntaxis
list3 = list1 + list2
'''
print("\Ejercicio 19 ************************************************************\n")
positive_number = [1, 2, 3, 4, 5] #Creación de la lista de números positivos
zero = [0] #Creación de la lista zero
negative_numbers = [-5, -4, -3, -2, -1] #Creación de la lista de números negativos
integers = negative_numbers + zero + positive_number #Concatenación de las tres listas y almanacedas en la lista enteros
print(integers) #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

'''
Union usando el método extend(). extend() permite agregar una lista al final de otra lista

# syntax
list1 = ['item1', 'item2'] #Se crea la primera lista
list2 = ['item3', 'item4', 'item5'] #Se crea la segunda lista
list1.extend(list2) #Se concatenan la lista2 a la lista1
'''
print("\Ejercicio 20 ************************************************************\n")
num1 = [0, 1, 2, 3] #Se crea la lista num1 
num2 = [4, 5, 6] #Se crea la lista num2
num1.extend(num2) #La lista num2 se concatena al final de la lista num1
print('Numbers:',num1)#Numbers: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5, -4, -3, -2, -1]#Se crea la lista negative_numbers
positive_number = [1, 2, 3, 4, 5]#Se crea la lista positive_numbers
zero = [0] #Se crea la lista zero
negative_numbers.extend(zero) #Se concatena la lista zero al final de la lista negative_numbers
negative_numbers.extend(positive_number) #Se concatena la lista positive_numbers al final de la lista negative_numbers
print('Integers: ', negative_numbers)#[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']#Se crea la lista fruits
vegetable = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']#Se crea la lista vegetables
fruits.extend(vegetable)#Se concatena la lista vegetales al final de la lista fruits
print('Fruits and Vegetables',fruits)#Fruits and Vegetables ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

#******************************************************* Contando Items de una lista *******************************************************
'''
Con el método count(), regresa el número de veces que se repite un item en una lista

# syntax
lst = ['item1', 'item2']#Se crea la lista
lst.count(item) #Cuenta cuantas veces se encuentra el intem dentro de la lista
'''
print("\Ejercicio 21 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Orange se encuentra:',fruits.count('orange'), 'vez')#Imprime cuantas veces se encuentra 'orange' en la lista fruits. 1

ages = [22,19,24,25,26,24,25,24]#Se crea la lista ages
print('El número 24 se repite: ',ages.count(24),' veces')#Imprime cuantas veces se repite el número 24 en la lista ages. 3

#******************************************************* Encontrando el index de un item *******************************************************
'''
El método index() regresa el indice de un elemento de la lista
# syntax
lst = ['item1', 'item2'] #Se crea la lista
lst.index(item) #indica el indice del item deseado
'''
print("\Ejercicio 22 ************************************************************\n")
frutas = ['banana', 'orange', 'mango', 'lemon']#Se crea la lista fruits
print('El indice del item orange es:',fruits.index('orange'))#Imprime el indice del elemento 'Orange'. 1

ages = [22, 19 , 24, 25, 26, 24, 25, 24]#Se crea la lista ages
print(ages.index(24))#Imprime el indice de la primera ocurrencia del número 24 en la lista. 2

#******************************************************* Revirtiendo una lista *******************************************************
'''
El método reverse(), invierte el orden de una lista
# syntax
lst = ['item1', 'item2']#Se crea la lista
lst.reverse()#Se invierte la lista lst
'''
print("\Ejercicio 23 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']#Se crea la lista fruits
print('Original fruit list:',fruits)#['banana', 'orange', 'mango', 'lemon']
fruits.reverse()#Se invierte el orden de la lista fruits
print('Reverse fruit list',fruits)#['lemon', 'mango', 'orange', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]#Se crea la lista ages
print('Original age list:',ages)#[22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print('Reverse age list:',ages)

#******************************************************* Ordenar elementos de una lista *******************************************************
'''
Para ordenar listas podemos usar el método sort(). El método sort() reordena los elementos de una lista en orden ascendente
y modifica la lista original. Si un argumento del método sort() reverse es igual a verdadero, organizará la lista en orden descendente.

#sort() este método modifica la lista original
# syntax
lst = ['item1', 'item2']  #Creación de la lista
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
'''

print("\Ejercicio 24 ************************************************************\n")
fruits = ['banana', 'orange', 'mango', 'lemon']#Creación de la lista fruits
print('Lista orginal:',fruits)#['banana', 'orange', 'mango', 'lemon']
fruits.sort()#Ordena de forma ascendente en orden alfabético
print('Lista ordenada ascendente alfabeticamente:',fruits)#['banana', 'lemon', 'mango', 'orange'
fruits.sort(reverse = True)#Ordena de forma descendente en orden alfabético
print('Lista ordenada descendente alfabeticamente',fruits,'\n')#['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]#Creación de la lista ages
print('Lista original:',ages)
ages.sort()#Prdena de forma ascendente de menor a mayor
print('Lista ordenada ascendente:',ages)
ages.sort(reverse=True)#Ordena de forma descendente de mayor a meno
print('Lista ordenada descendente:',ages)
