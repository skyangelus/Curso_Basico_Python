'''
Un diccionario es una colección de tipos de datos emparejados (clave: valor) no ordenados y modificables (mutables).
'''
#********************************************************** Creación de un diccionario **********************************************************
'''
Para crear un diccionario utilizamos llaves, {} o la función incorporada dict().

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
'''

print('\n*************************** Ejemplo 1:********************************')
person = {
    'first_name':'Asabneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript','React','Node','MongoDB','Python'],
    'address':{
        'street':'Space Street',
        'Zipcode':'02210'
    }
}
print(len(person))#7

#********************************************************** Accediendo a elementos del diccionario **********************************************************
'''
Podemos acceder a los elementos de un diccionario referenciando su nombre clave

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
'''

print('\n*************************** Ejemplo 2:********************************')
person = {
    'first_name':'Asabneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript','React','Node','MongoDB','Python'],
    'address':{
        'street':'Space Street',
        'Zipcode':'02210'
    }
}

print(f'First name:{person['first_name']}')#Asabneh
print(f'Country:{person['country']}')#Finland
print(f'Skils:{person['skills']}')#['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(f'First Skill:{person['skills'][0]}')#JavaScript
print(f'Address - Street:{person['address']['street']}')#Space Street
#print(f'City:{person['city']}')#Error ya que no hay ninguna clave llamada city

'''
Acceder a un elemento por el nombre de la clave genera un error si la clave no existe. 
Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get. 
El método get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.
'''

print('\n*************************** Ejemplo 3:********************************')
person = {
    'first_name':'Asabneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript','React','Node','MongoDB','Python'],
    'address':{
        'street':'Space Street',
        'Zipcode':'02210'
    }
}
print(f'First name:{person.get('first_name')}')#Asabneh
print(f'Country:{person.get('country')}')#Finland
print(f'Skils:{person.get('skills')}')#['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(f'First Skill:{person.get('skills')[0]}')#JavaScript
print(f'Address - Street:{person.get('address')}')#{'street': 'Space Street', 'Zipcode': '02210'}
print(f'City:{person.get('city')}')#None - Nos indica que no existe un nombre clave 'city' en el diccionario

#********************************************************** Agregando elementos a un diccionario **********************************************************