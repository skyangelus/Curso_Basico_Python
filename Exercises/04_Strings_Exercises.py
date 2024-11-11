#Ejercisio No.1: Concatena el string 'Thirty', 'Days', 'Of', 'Python' a un solo string, 'Thirty Days Of Python'
print('***Ejercisio No.1: Concatena el string \'Thirty\', \'Days\', \'Of\', \'Python\' a un solo string, \'Thirty Days Of Python\'***\n')
first_word = 'Thirty'
second_word = 'Days'
third_word = 'Of'
fourt_word = 'Python'
space = ' '

complete_sentence = first_word + space + second_word + space  + third_word + space  + fourt_word
print(complete_sentence)

#Ejercicio No.2 Concatena la cadena 'Coding', 'For' , 'All' a un solo string, 'Coding For All'.
print('\n***Ejercicio No.2: Concatena la cadena \'Coding\', \'For\' , \'All\' a un solo string, \'Coding For All\'.***\n')
first_word = 'Coding'
second_word = 'For'
third_word = 'All'
space = ' '

complete_sentence = first_word + space + second_word + space  + third_word
print(complete_sentence)

#Ejercicio No.3: Declara una varible llamada "company" y asignala a un valor inicia "Coding For All"
print('\n***Ejercicio No.3: Declara una varible llamada "company" y asignale un valor inicial de "Coding For All***\n')
company = 'Coding For All'

#Ejercicio No.4: Imprime la variagle "company" usando el comando print()
print('\n***Ejercicio No.4: Imprime la variagle "company" usando el comando print()***\n')
print(company)

#Ejercicio No.5: Imprime la longitd de la cadena "company" usando el metodo len() y print()
print('\n***Ejercicio No.5: Imprime la longitd de la cadena "company" usando el metodo len() y print()***\n')
print('The lenght of the company string is: ' + str(len(company)))

#Ejercicio No.6: cambia todos los caracteres a mayusculas usando el metodo upper()
print('\n***Ejercicio No.6: cambia todos los caracteres a mayusculas usando el metodo upper()***\n')
print(company.upper())

#Ejercicio No.7: Cambia todos los caracteres a minusculas usando el metodo lower()
print('\n***Ejercicio No.7: Cambia todos los caracteres a minusculas usando el metodo lower()***\n')
print(company.lower())

#Ejercicio No.8: Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All
print('\n***Ejercicio No.8: Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All***\n')
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Ejercicio No.9: Corta la primera palabra de la cadena Coding For All.
print(company[7:])

#Ejercicio No.10: Verifica si la cadena Coding For All contiene la palabra Coding usando el metodo index(), find() u otro metodo.
print('\n***Ejercicio No.10: Verifica si la cadena Coding For All contiene la palabra Coding usando el metodo index(), find() u otro metodo.***\n')
if company.index('Coding') != -1:
    print('True')
print(company.find('Coding'))

#Ejercicio No.11: Remplaza la palabra "Coding" en la cadena "Coding For All" por "Python"
print('\n***#Ejercicio No.11:  Remplaza la palabra "Coding" en la cadena "Coding For All" por "Python".***\n')
print(company.replace('Coding','Python'))

#Ejercicio No.12: Cambia "Python for Everyone" a "Python For All" usando el metodo "Replace()"
print('\n***#Ejercicio No.12:  Cambia "Python for Everyone" a "Python For All" usando el metodo "Replace()".***\n')

company = 'Python for Everyone'
print(company.replace('Everyone','All'))

#Ejercicio No.13: Divida la cadena 'Coding For All' usando el espacio como separador (split())
print('\n***#Ejercicio No.13: Divida la cadena \'Coding For All\' usando el espacio como separador (split()).***\n')
company = 'Coding For All'
print(company.split())
print(company.split()[0])
print(company.split()[1])
print(company.split()[2])

#Ejercicio No.14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" Corta la cadena en las comas
print('\n***#Ejercicio No.14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" Corta la cadena en las comas.***\n')
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

#Ejercicio No.15: Cual es el caracter en el index 0 en la cadena 'Coding For All'
print('\n***#Ejercicio No.15: Cual es el caracter en el index 0 en la cadena \'Coding For All\'***\n')
print(company[0])

#Ejercicio No.16: Cual es el ultimo indice en de la cadena "Coding For All"
print('\n***#Ejercicio No.16: Cual es el ultimo indice en de la cadena "Coding For All"***\n')
l_index = len(company) -1
print(f'The last indx from the string {company} is: {l_index}')

#Ejercicio No.17: Que caracter esta en el indice 10 de la cadena "Coding For All"
print('\n***#Ejercicio No.17: Que caracter esta en el indice 10 de la cadena "Coding For All"***\n')
print(company[10])

#Ejercicio No.18: Crea un acronimo o abreviación para el nombre 'Python For Everyone'
print('\n***#Ejercicio No.18: Crea un acronimo o abreviación para el nombre "Python For Everyone"***\n')
company = 'Python For Everyone' #Crea la cadena a la que se le hara un acronimo
acro = "" #crea la variable que va a recibir el acronimo
new_string = company.replace(" ","") #Crea una nueva cadena donde Reemplaza los espacios con vacio "PythonForEveryone"
for i in range(0,len(new_string)-1): #Ciclo for que se repetira desde cero hasta el index final de la nueva cadena
    if new_string[i].isupper() == True: #Si el caracter en la posición i es una mayuscula la guardara en la variable acro
        acro += new_string[i] #Guarda los caracteres mayusculas en la variable acro
print(acro) #Imprime el acronimo PFE (Python For Everone)
        
#Ejercicio No.19: Crea un acronimo o abreviación para el nombre "Coding For All"
print('\n***#Ejercicio No.19: Crea un acronimo o abreviación para el nombre "Coding For All"***\n')
company = 'Coding For All'
acro = ""
new_string = (company.replace(" ",""))

for i in range(0,len(new_string)-1):
    if new_string[i].isupper() == True:
        acro += new_string[i]
print(acro)

#Ejercicio No.20: Usar el indice para determinar la posición del la primera ocurrencia del caracter "C" en "Coding for All"
print('\n***#Ejercicio No.20: Usar el indice para determinar la posición del la primera ocurrencia del caracter "C" en "Coding for All"***\n')
print('The index with the letter C in the string is:', company.index('C'))

#Ejercicio No.21: Usar el indice para determinar la posición del la primera ocurrencia del caracter "F" en "Coding for All"
print('\n***#Ejercicio No.20: Usar el indice para determinar la posición del la primera ocurrencia del caracter "F" en "Coding for All"***\n')
print('The index with the letter F in the string is:', company.index('F'))

#Ejercicio No.22: Usar el indice para determinar la posición del la primera ocurrencia del caracter "I" en "Coding for All"
#Ejercicio No.21: Usar el indice para determinar la posición del la primera ocurrencia del caracter "F" en "Coding for All"
print('\n***#Ejercicio No.20: Usar el indice para determinar la posición del la primera ocurrencia del caracter "F" en "Coding for All"***\n')
print('The index whithe the letter F in the string is:', company.index('F'))
print('The index with the letter F in the string is:', company.rindex('i'))

#Ejercicio No.23: Usar el index o find para encontrar la posición de la primera ocurrencia de la palabra "because" en la siguiente oración "You cannot end a sentence with because because because is a conjunction"
print('\n***#Ejercicio No.23: Usar el index o find para encontrar la posición de la primera ocurrencia de la palabra "because" en la siguiente oración "You cannot end a sentence with because because because is a conjunction"***\n')
sen = 'You cannot end a sentence with because because because is a conjunction'
print(f'La posición de la primera ocurrencia de la palabra "because" en la oración es indice:[{sen.index('because')}]')

#Ejercicio No.24: Usar el index o find para encontrar la posición de la ultima ocurrencia de la palabra "because" en la siguiente oración "You cannot end a sentence with because because because is a conjunction"
print('\n***#Ejercicio No.24: Usar el index o find para encontrar la posición de la ultime ocurrencia de la palabra "because" en la siguiente oración "You cannot end a sentence with because because because is a conjunction"***\n')
sen = 'You cannot end a sentence with because because because is a conjunction'
print(f'La posición de la ultima ocurrencia de la palabra "because" en la oración es indice:[{sen.rindex('because')}]')

#Corta la frace 'because because because' en la siguiente oración "You cannot end a sentence with because because because is a conjunction"
print('\n***#Corta la frace "because because because" en la siguiente oración "You cannot end a sentence with because because because is a conjunction"***\n')
print(sen[0:sen.index('because'):1],sen[sen.rindex('because')::1])
