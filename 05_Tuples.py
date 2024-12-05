'''
Una tupla es una colección de distintos tipos de datoslos cales son ordenados y no se pueden cambiar (Inmutables). 
Las tuplas estan escritas con parentecis (). A diferencia que las listas usan corchetes [].
Una vez la tupla es creada, sus valores no pueden ser cambiados. No podemo agregar, insertar o remover metodos
en una tupla ya que es inmutable (No se puede modificar).

Metodos relacionados a las tuplas:
    tuple(): para crear una tupla vacia
    count(): para contar el número de elementos en una tupla
    index(): para encontrar el indice de un elemento especifico en una tupla
    Operator: para unir dos o más tuplas y crear una nueva tupla
'''

#********************************************************** Creación de una tupla **********************************************************
'''
Tupla vacía: Creación de una tupla vacía

#Syntaxis
empty_tuple = ()

#O usando la tupla contructor
empty_tuple = tuple()
'''

print('\n***************************Ejemplo 1:********************************')
empty_tuple = () #Se crea una tupla vacia
print('Tupla vacia:',empty_tuple)#Tupla vacia: ()

'''
Tupla con valores iniciales

#Syntaxis
tpl = ('item1', 'item2', 'item3')
'''

print('\n***************************Ejemplo 2:********************************')
fruits = ('banana', 'orange','mango','lemon')#Se crea la tupla 'fruits'
print('Frutas: ',fruits)#Frutas:  ('banana', 'orange', 'mango', 'lemon')

#********************************************************** Longitud de una tupla **********************************************************
'''
Se usa el método len() para obtener el tamaño de la tupla

#Syntaxis
tpl = ('item1', 'item2', 'item3')
print(len(tpl))
'''

print('\n***************************Ejemplo 3:********************************')
fruits = ('banana', 'orange', 'mango', 'lemon')#Se crea la tupla fruits
print(len(fruits))#4

#********************************************************** Accediendo a un elemento de un tupla **********************************************************
'''
Indexación positiva similar a la de la lista. Se puede usar indexación postiva o negativa para acceder a elemento de una tupla

# Syntax
       index=0  index=1  index=2
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
'''

print('\n***************************Ejemplo 4:********************************')
#         index=0   index=1   index=2   index=3
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]#First fruit: banana
second_fruit = fruits[1]#Second fruit:orange
last_index = len(fruits) - 1 #3
last_fruit = fruits[last_index]#Last Fruit: lemon

print(f'First fruit: {first_fruit}\nSecond fruit:{second_fruit}\nLast Fruit: {last_fruit}')

'''
Indexación negativa quiere decir que inicia desde el indice final, -1 se refiere al ultimo elemento, -2 es el penultimo elemento
y el negativo del temaño de la lista/tupla se refiere al primer elemento.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
'''
print('\n***************************Ejemplo 5:********************************')
#         index=-4  index=-3  index=-3  index=-1
fruits = ('banana', 'orange', 'mango', 'lemon')#Creación de la tupla
first_fruit = fruits[-(len(fruits))]#Fist fruit:banana
second_fruit = fruits[-3]#Second fruit:orange
last_fruit = fruits[-1]#Last fruit:lemon

print(f'Fist fruit:{first_fruit}\nSecond fruit:{second_fruit}\nLast fruit:{last_fruit}')

#********************************************************** Rebanar(Slicing) elementos de una tulpa **********************************************************