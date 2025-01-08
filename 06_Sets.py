'''
"Set" (Conjunto) es una colección de elementos distintos, no ordenados ni indexados. 
En Python, un conjunto (set) se utiliza para almacenar elementos únicos 
y es posible encontrar la unión, intersección, diferencia, diferencia simétrica, subconjunto, superconjunto y conjunto disjunto 
entre conjuntos.
'''
#********************************************************** Creación de un set(conjunto) **********************************************************
'''
Usamos set() para construir la función

Crear un set vacio
# syntax
st = set()

Crear un set con valores iniciales
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
'''
print('\n*************************** Ejemplo 1:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(f'Printing the set fruits: {fruits}')#{'orange', 'mango', 'banana', 'lemon'}

#********************************************************** Obtener el tamaño de un set **********************************************************
'''
Usamos len() para obtener el tamaño de un "set"

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
'''

print('\n*************************** Ejemplo 2:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('The fruits set lenght is: ',len(fruits))#4

#********************************************************** Accediendo a elemento en un set **********************************************************
'''
Usamos ciclos para acceder a elementos dentro de un set. Esto se vera en la sección de ciclos
'''

#********************************************************** Verificando un elemento en un set **********************************************************
'''
Para verificar si un elemento existe dentro de un set usamos el operador "in"

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
'''

print('\n*************************** Ejemplo 3:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Does exist the mango item in Fruits?','mango'in fruits)#True

#********************************************************** Agregando elementos a un set **********************************************************
'''
Para agregar un elemento se utiliza add()

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
'''

print('\n*************************** Ejemplo 4:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

print(f'Fruits set items:{fruits}') #{'banana', 'mango', 'lemon', 'orange', 'lime'}

'''
Se pueden agregar multiples elementos usando update(). El update() tomara los elemento que esten en una "lista".

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
'''

print('\n*************************** Ejemplo 5:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'} #Es un conjunto
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot') #Es una lista
fruits.update(vegetables)

print(f'Fruits set + vegetables list:{fruits}')#{'banana', 'mango', 'lemon', 'onion', 'tomato', 'orange', 'carrot', 'potato', 'cabbage'}

#********************************************************** Removiendo elementos a un set **********************************************************
'''
Podemos remover un element de un set usando el metodo remove(). Si el elemento no es encontrado, el metodo remove() mostrara un
error. Por eso es bueno verificar que el elemento exista en el set requerido. De otra manera el metodo discard() no lanza error.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
'''

print('\n*************************** Ejemplo 6:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('lemon')#Delete the 'lemon' item

print(fruits)#{'banana', 'mango', 'orange'}

'''
El método pop() elimina un elemento al azar de una lista y regresa el elemento eliminado
'''
print('\n*************************** Ejemplo 7:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # remueve un elemento al azar del set

print('\n*************************** Ejemplo 8:********************************')
#Si se esta interesado en el elemento al azar que se elimino, entonces usamos
fruits = {'banana', 'orange', 'mango', 'lemon'}
Item_Removed = fruits.pop()  # remueve un elemento al azar del set
print(f'The set without the random item removed:{fruits}') #Imprime el set pero ya sin el elemento eliminado al azar
print(f'The random item removed was: {Item_Removed}')#Imprime el elemento que fue eliminado al azar

#********************************************************** Limpiando elementos a un set **********************************************************
'''
Si queremos limpiar o vaciar el set, usamos el metodo clear()

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
'''

print('\n*************************** Ejemplo 9:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()#Clear the fruits set
print(fruits)#Pint the empty set - set()

#********************************************************** Eliminando un set **********************************************************
'''
Si queremos borrar el set usamos el operador "del"

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
'''

print('\n*************************** Ejemplo 10:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits #Borra el set fruits

#********************************************************** Convirtiendo listas a set **********************************************************
'''
Podemos convertir Listas a Set y Set a Listas. Convertir de Listas a Set elimina los elemento duplicados y deja elementos unicos.

# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - El orden es al azar ya que los Set no son ordenados.
'''

print('\n*************************** Ejemplo 11:********************************')
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(f'Print the Set fruits converted to List: {fruits}')#{'mango', 'lemon', 'banana', 'orange'}

#********************************************************** Uniendo Sets **********************************************************
'''
Podemos unir dos Sets usando el metodo union() o updated()

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
'''

print('\n*************************** Ejemplo 12:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}

print('Set fruits + Set vegetables:',fruits.union(vegetables))#{'orange', 'tomato', 'lemon', 'mango', 'carrot', 'onion', 'cabbage', 'banana', 'potato'}

'''
El método updated() insert un set dentro del otro set

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
'''

print('\n*************************** Ejemplo 13:********************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables) #El contenido del set vegetables es agregado al set fruits
print(fruits)#{'tomato', 'onion', 'cabbage', 'orange', 'banana', 'potato', 'lemon', 'mango', 'carrot'}

#********************************************************** Encontrando la intersección de los Sets **********************************************************
'''
La intersección regresa un set de elementos los cuales estan en ambos sets

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
'''

print('\n*************************** Ejemplo 14:********************************')
whole_numbers = {0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection = whole_numbers.intersection(even_numbers)
print(intersection) #{0, 2, 4, 6, 8, 10}

print('\n*************************** Ejemplo 15:********************************')
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
intersection = python.intersection(dragon)
print(intersection) #{'n', 'o'}

#********************************************************** Comprobación de subconjuntos y superconjuntos **********************************************************
'''
Un conjunto puede ser un subconjunto o superconjunto

    subconjunto(subset): issubset()
    superconjunto(superset): issuperset()

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
'''

print('\n*************************** Ejemplo 16:********************************')
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print('Is whole_numbers subset of even_numbers?',whole_numbers.issubset(even_numbers))#False
print('Is whole_numbers superset of even_numbers?',whole_numbers.issuperset(even_numbers))#True

print('\n*************************** Ejemplo 17:********************************')
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print('Is python subset of dragon?',python.issubset(dragon))#False

#********************************************************** Comprobando la diferencia entre dos sets **********************************************************
'''
Regresa la diferencia entres dos sets

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
'''

print('\n*************************** Ejemplo 18:********************************')
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.difference(even_numbers)) #{1, 3, 5, 7, 9}

print('\n*************************** Ejemplo 19:********************************')
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.difference(dragon)) #{'t', 'p', 'y'}
print(dragon.difference(python)) #{'r', 'd', 'a', 'g'}

#********************************************************** Encontrando diferencia simetrica entre dos sets **********************************************************
'''
Regresa la diferencia simetrica entre dos sets. Significa que regresa un set que contiene todos los elementos de ambos sets,
excepto los elementos que estan presenten en ambos sets, matematicamente: (A/B) U (B/A)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
'''

print('\n*************************** Ejemplo 20:********************************')
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}

print(whole_numbers.symmetric_difference(some_numbers))#{0, 6, 7, 8, 9, 10}

print('\n*************************** Ejemplo 21:********************************')
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.symmetric_difference(dragon))#{'d', 'p', 'a', 'r', 'h', 'g', 't', 'y'}

#********************************************************** Uniendo sets **********************************************************
'''
Si dos conjuntos no tienen un elemento o elementos en común, los llamamos conjuntos disjuntos. 
Podemos comprobar si dos conjuntos son conjuntos o disjuntos utilizando el método isdisjoint().

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
'''

print('\n*************************** Ejemplo 22:********************************')
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}

print(even_numbers.isdisjoint(odd_numbers))#True, No tienene elementos en comun

print('\n*************************** Ejemplo 23:********************************')
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.isdisjoint(dragon))#False, tienene en comun {'o', 'n'}