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
#         index=-4  index=-3  index=-2  index=-1
fruits = ('banana', 'orange', 'mango', 'lemon')#Creación de la tupla
first_fruit = fruits[-(len(fruits))]#Fist fruit:banana
second_fruit = fruits[-3]#Second fruit:orange
last_fruit = fruits[-1]#Last fruit:lemon

print(f'Fist fruit: {first_fruit}\nSecond fruit: {second_fruit}\nLast fruit: {last_fruit}')

#********************************************************** Rebanar(Slicing) elementos de una tulpa **********************************************************
'''
Podemos rebanar las tuplas especificando un rango de indices donde inicia y donde termina la tupla. El valor de retorno sera una
tupla nueva con los elemento especificados.

Rango de indices positivos

#Syntaxis
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
'''

print('\n***************************Ejemplo 6:********************************')
#         index=0   index=1   index=2  index=3
fruits = ('banana', 'orange', 'mango', 'lemon')#Creación de la tupla
all_items = fruits[0:4] #Todas las frutas
all_fruits = fruits[0:] #Todas las frutas
Orange_Mango = fruits[1:3] #('orange', 'mango')
Orange_to_the_rest = fruits[1:] #('orange', 'mango', 'lemon')

print(f'All fruits: {all_items}\nAll fruits: {all_fruits}\nOrange and Mango: {Orange_Mango}\nOrange to the rest: {Orange_to_the_rest}')

'''
Rango de indices negativos

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
'''

print('\n***************************Ejemplo 7:********************************')
#         index=-4  index=-3  index=-2  index=-1
fruits = ('banana', 'orange', 'mango', 'lemon')#Creación de la tupla
all_fruits = fruits[-4:] #Todos los items
Orange_Mango = fruits[-3:-1] #('orange', 'mango')
Orange_to_the_rest = fruits[-3:] #('orange', 'mango', 'lemon')
print(f'All fruits: {all_fruits}\nOrange and Mango: {Orange_Mango}\nOrange to the rest: {Orange_to_the_rest}')

#********************************************************** Cambiando Tuplas a Listas **********************************************************
'''
Podemos cambiar las tuplas a listas y listas a tuplas. La tupla es inmutable (No se puede editar). Si queremos modificar una tupla, 
tenemos que cambiarla primero a lista.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
'''

print('\n***************************Ejemplo 8:********************************')
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits) #converte tuple to list
fruits[0] = 'apple'
print(f'Tuple \"fruits\" converted to List: {fruits}') #['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits) #convert to tuple
print(f'List \"fruits\" converted to Tuple: {fruits}') #('banana', 'orange', 'mango', 'lemon')

#********************************************************** Verificando un elemento en una tupla **********************************************************
'''
Podemos verificar si un elemento existe o no en una tupla usando "in", regresa un valor boleano.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
'''

print('\n***************************Ejemplo 9:********************************')
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) #True
print('apple' in fruits) #False
#fruits[0] = 'apple' #Error ya que las tuplas no pueden ser modificadas

#********************************************************** Uniendo Tuplas **********************************************************
'''
Podemos unir dos o más tuplas usando el operador "+"

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
'''

print('\n***************************Ejemplo 10:********************************')
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

print(fruits_and_vegetables)

#********************************************************** Borrando Tuplas **********************************************************
'''
No es posible remover solo un elemento de las tuplas, pero es posible eliminar la tupla completa usando "del"

# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
'''

print('\n***************************Ejemplo 11:********************************')
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
#print(f'Fruits: {fruits}') #Error ya que ya se elimino la tupla y ya no puedeo imprimirse