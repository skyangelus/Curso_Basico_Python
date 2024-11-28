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