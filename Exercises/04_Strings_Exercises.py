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