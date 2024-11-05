#******************* STRINGS ********************

#Declaración de variables ---------------------------------------------------------------------------------------------------------------------
print("Ejercicio 1 ************************************************************\n")
my_string = "Mi String 1" #Una String puede ser declarada entre comillas dobles
my_other_string = 'Mi String 2' #Una String puede ser declarada entre comillas simples

#Imprimir la longitud del contenido de una variable de tipo string -------------------------------------------------------------------------------------------
print("\nEjercicio 2 ************************************************************\n")
print("La longitud del contenido de mi variable my_string es:",len(my_string),"caracteres") #Imprime la longitud del contenido de la variable my_string
print("La longitud del contenido de mi variable my_other_string es:",len(my_other_string),"caracteres") ##Imprime la longitud del contenido de la variable my_string

#Concatenación de strings usando el signo "+" -------------------------------------------------------------------------------------------
print("\nEjercicio 3 ************************************************************\n")
print("Se concatena el contenido de my_string + espacio + my_other_string:",my_string + " " + my_other_string)

#String con un salto de linea-----------------------------------------------------------------------------------------------------------------
print("\nEjercicio 4 ************************************************************\n")
my_new_line_string = "Este es un string\ncon un salto de linea" #El comando \n inserta un salto de linea en un string
print(my_new_line_string) #Se imprime el contenido de la variable "my_new_line_string"

#String con una tabulación---------------------------------------------------------------------------------------------------------------------
print("\nEjercicio 5 ************************************************************\n")
my_tab_line_string = "\tEste es un string con una tabulación" #El comando \t inserta una tabulación en un string
print(my_tab_line_string) #Se imprime el contenido de la variable "my_tab_line_string"

#String escapado--------------------------------------------------------------------------------------------------------------------------------------
print("\nEjercicio 6 ************************************************************\n")
my_esc_line_string = "\\t Este es un string \\n escapado" #Si se coloca una \ justo antes de un \t o \n, ignora el comando e imprime "\t" o "\n"
print(my_esc_line_string) #Se imprime el contenido de la variable "my_esc_line_string"

#Formateo------------------------------------------------------------------------------------------------------------------------------
print("\nEjercicio 7 ************************************************************\n")
fname, lname, age = "Alfredo", "Arredondo", 33 #Se crean las variables fname, lname, age y se le asigna .
print("Mi nombre es {} {} y mi edad es {}".format(fname,lname,age)) #Para agregar las variables de la tupla usando el .format(), hay que usar {} en los luigares que se agregara el contenido de la variable.
print("Mi nombre es %s %s y mi edad es %d" %(fname,lname,age)) #Para agregar las variables de la tupla usando el %() hay que agregar %s para colocar un string o un %d para un entero, un %f para un flotante, etc.

print("Mi nombre es " + fname + " " + lname + " y mi edad es " + str(age)) #Esta forma es igual que las anteriores, sin embargo es menos optima utilizarla, se recomiendan más cualquiera de las anteriores

#Forma vieja de formateo en python----------------------------------------------------------------------------------------------------------------------------
# Strings only
print("\nEjercicio 8 ************************************************************\n")
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
print("\nEjercicio 9 ************************************************************\n")
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas'] #Se crea un arreglo con las librerias de Python
formated_string = 'The following are python libraries:%s' % (python_libraries) #Se crea una variable con el formato
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

#Forma nueva de formateo en Python - valida a partir del Python_v3 -------------------------------------------------------------------------------------------
#string only
print("\nEjercicio 10 ************************************************************\n")
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

#Numbers only
print("\nEjercicio 11 ************************************************************\n")
a = 4 #Se crea una variable a
b = 3 #Se crea una variable b
print('{} + {} = {}'.format(a, b, a + b)) #Le imprime el contenido de a y b y luego imprime el resultado a + b
print('{} - {} = {}'.format(a, b, a - b)) #Le imprime el contenido de a y b y luego imprime el resultado a - b
print('{} * {} = {}'.format(a, b, a * b)) #Le imprime el contenido de a y b y luego imprime el resultado a * b
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal - Le imprime el contenido de a y b y luego imprime el resultado de a / b con dos decimales
print('{} % {} = {}'.format(a, b, a % b)) #Le imprime el contenido de a y b y luego imprime el residuo del resultado de a / b
print('{} // {} = {}'.format(a, b, a // b)) #Le imprime el contenido de a y b y luego imprime el resultado a / b pero sin decimales, solo el valor entero
print('{} ** {} = {}'.format(a, b, a ** b)) #Le imprime el contenido de a y b y luego imprime el resultado a ^ b

# Strings  and numbers
print("\nEjercicio 12 ************************************************************\n")
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

#String Interpolation/ f-string - valida a partir del Python_v3.6+-------------------------------------------------------------------------------------------

#Otra forma de formatear un smtring, es con f-string. El string comienza con una f y podemos injectar los datos en su posción correspondiente
print("\nEjercicio 13 ************************************************************\n")
a = 4
b = 3

print(f'{a} + {b} = {a + b}') #Le imprime el contenido de a y b y luego imprime el resultado a + b
print(f'{a} - {b} = {a - b}') #Le imprime el contenido de a y b y luego imprime el resultado a - b
print(f'{a} * {b} = {a * b}') #Le imprime el contenido de a y b y luego imprime el resultado a * b
print(f'{a} / {b} = {a / b}') #Le imprime el contenido de a y b y luego imprime el resultado de a / b
print(f'{a} / {b} = {a / b:.2f}')# limits it to two digits after decimal - Le imprime el contenido de a y b y luego imprime el resultado de a / b con dos decimales
print(f'{a} % {b} = {a % b}') #Le imprime el contenido de a y b y luego imprime el residuo del resultado de a / b
print(f'{a} // {b} = {a // b}') #Le imprime el contenido de a y b y luego imprime el resultado a / b pero sin decimales, solo el valor entero
print(f'{a} ** {b} = {a ** b}') #Le imprime el contenido de a y b y luego imprime el resultado a ^ b

#Strings de Python como secuencia de caracteres----------------------------------------------------------------------------------------------------------------
'''
Los String de Python son secuentas de caracteres, y comparten sus metodos basicos de acceso con otras secuencias de ordenamiento e Python -listas an tuplas.
La forma más simple de extraer un solo caracter de un string (y un mimbro individual de cualquier secuencia) es desempaquetandolos in sus variables correspondientes
'''
print("\nEjercicio 14 ************************************************************\n")
language = 'Python'
a,b,c,d,e,f = language #Desempaquetando la secuencia de caracteres en variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Accesando a caracteres de un String por Indice (Index)----------------------------------------------------------------------------------------------------------------
'''
En programación la cuenta inicia en cero. En otras palabras, la primera letra de un string es el indice cero y la ultima letra de una cadena es la longitud del string menos uno
'''
print("\nEjercicio 15 ************************************************************\n")
language = 'Python'
first_letter = language[0] # Toma el caracter "P" y lo guarda en la variable "first_letter"
print(first_letter) #Imprime "P"
second_letter = language[1] # Toma el caracter "y" y lo guarda en la variable "second_letter"
print(second_letter) #Imprime "y"
last_letter = language[len(language) - 1] #Obtiene el ultimo caracter de la cadena que es la "n" y lo guarda en la variable "last_letter"
print(last_letter) #Imprime "n"

'''
Si queremos iniciar desde el final de la palabra, osea desde la derecha, podemos usar indices negativos. -1 es el ultimo indice
'''
print("\nEjercicio 16 ************************************************************\n")
language = 'Python'
last_letter = language[-1] #Toma el ultimo caracter de la cadena "n" y lo guarda en la variable "last_letter"
print(last_letter) #Imprime "n"
second_last = language[-2] #Toma el penultimo caracter de la cadena "o" y lo guarda en la variable "second_last"
print(second_last) #Imprime "o"

#segmentar la cadena en Python-------------------------------------------------------------------------------------------------------------------------------------
'''
En Python podemos segmentar cadenas en subcadenas
'''
print("\nEjercicio 17 ************************************************************\n")
language = 'Python'
first_three = language[0:3] #Inicia en el caracter con indice 0 y sube hasta caracter con el indice 3, pero no incuye, ni guarda el caracter de la posición 3
print(first_three) #Imprime "Pyt"
last_three = language[3:6] #Inicia en el caracter con indice 3 y sube hasta caracter con el indice 6 (que esta vacio), pero no incuye, ni guarda el caracter de la posición 6 (que esta vacio)
print(last_three) #Imprime "hon"

# Another way
last_three = language[3:len(language)] #Mismo resultado que el anterior, pero usando la longitud de la cadena en lugar de un número fijo
print(last_three)   # hon
last_three = language[-3:] #Comienza desde la derecha y el -1 es el caracter final, entonces el -3 es "h" y despues de : esta vacio, eso indica que desde -3 hasta el final de la cadena
print(last_three)   # hon
last_three = language[3:] #Comienza desde el caracter 3 que es "h" y despues de : esta vacio, eso indica que desde el caracter del index 3 hasta el final de la cadena
print(last_three)   # hon

#Voltear una cadena en Python-------------------------------------------------------------------------------------------------------------------------------------
'''
Podemos dar vuelta a una cadena facilmente de la siguiente manera
'''
print("\nEjercicio 18 ************************************************************\n")
greeting = 'Hello World' #Declaramos la cadena de texto
print(greeting[::-1]) #Imprime "dlroW olleH"

#Omitir caracteres durante la segmentación-------------------------------------------------------------------------------------------------------------------------------------
'''
Es posible omitir caracteres durante la segmentación pasando el argumento de paso al método de corte.
'''
print("\nEjercicio 19 ************************************************************\n")
language = 'Python'
skip_and_slice = language[0:6:2] # 0 indica el indice del caracter en donde inicia "P", el 6 indica la longitud de la cadena de caracteres y el 2 indica cada cuantos caracteres deltro de la cadena imprimira P[0] Se imprime, y[1] no se imprime, t[2] Se imprime, h[3] no se imprime, o[4] se imprime y n[5] no se imprime.
print(skip_and_slice) #Pint "Pto"

#Metodos String--------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Hay muchos métodos de cadena que nos permiten formatear cadenas. Vea algunos de los métodos de cadena en el ejemplo siguiente:
'''
print("\nEjercicio 20 ****** Uso de capitalize(): Convierte el primer caracter de la cadena a letra capital\n")
    #capitalize(): Convierte el primer caracter de la cadena a letra capital
challenge = 'thirty days of python'
print(challenge.capitalize()) #Print "Thirty days of python"

print("\nEjercicio 21 ****** Uso de count(): Devuelve las apariciones de la subcadena en la cadena, count(substring, start=.., end=..). El inicio es una indexación inicial para el recuento y el final es el último índice que se cuenta.\n")
    #count(): Devuelve las apariciones de la subcadena en la cadena, count(substring, start=.., end=..). El inicio es una indexación inicial para el recuento y el final es el último índice que se cuenta.
challenge = 'thirty days of python'
print(challenge.count('y')) #Cuenta cuantas veces aparece la letra "y" en la cadena completa "challenge"
print(challenge.count('y',7,14)) #Cuenta cuantas veces aparece la letra "y" en la cadena "challenge", pero solo entre el indice challenge[7] y el indice challenge[14]
print(challenge.count('th')) #Cuenta cuantas veces aparece "th" así juntos, en la cadena completa "challenge"

print("\nEjercicio 22 ****** Uso de endswitch(): Comprueba si una cadena termina con un final especificado.\n")
    #endswitch(): Comprueba si una cadena termina con un final especificado.
challenge = 'thirty days of python'
print(challenge.endswith('on')) #verifica si la cadena de texto "challenge" termina en "on" e imprime "True" ya que es verdad
print(challenge.endswith('tion')) #verifica si la cadena de texto "challenge" termina en "tion" e imprime "False" ya que es es falso, no termina en tion

print("\nEjercicio 23 ****** Uso de expandtabs(): Podemos modificar el tamaño de la tabulación que agregamos con \\t, el tamaño de tabulación predeterminado es 8. Si usamos solo la función expandtabs(), toma el argumento del tamaño por defecto, osea expandtabs() = expandtabs(8).\n")
    #expandtabs(): Reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento del tamaño de la tabulación.
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) #Toma el tamaño por defecto de los tabuladores \t que es de 8, así que se imprime normal como si no se usara expandtabs()
print(challenge.expandtabs(10)) #Incremente al tamaño de las tabulaciones \t de 8 que es por defecto a 10.

print("\nEjercicio 24 ****** Uso de find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1.\n")
    #find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1.
challenge = 'thirty days of python'
print(challenge.find('y')) #Devuelve el indice de la primera vez que aparece "y" en la cadena "challenge", que es el indice 5. challenge[5]
print(challenge.find('th')) #Devuelve 0 ya que la primera vez que aparece "th" es en el indice challenge[0] con la t. Solo muestra el indice de donde comienza la subcadena, no de las demas letras
print(challenge.find('th',10,len(challenge)-1)) #Devuelve 17 ya que la primera vez que aparece "th" despues del indice 5 y hasta el final de la cedena es en el indice challenge[17], se salta el primer th, ya que la busqueda comienza a partir de challenge[5]
print(challenge.find('go')) #imprime -1 porque no encontro la subcadena 'go' en "challenge"

print("\nEjercicio 25 ****** Uso de rfind(): Devuelve el índice de la ultima aparición de una subcadena, si no se encuentra devuelve -1.\n")
    #rfind(): Devuelve el índice de la ultima aparición de una subcadena, si no se encuentra devuelve -1.
challenge = 'thirty days of python'
print(challenge.rfind('y')) #Devuelve el indice de la ultima vez que aparece "y" en la cadena "challenge", que es el indice 16. challenge[16]
print(challenge.rfind('th')) #Devuelve 17 ya que la ulyima vez que aparece "th" es en el indice challenge[17] con la t. Solo muestra el indice de donde comienza la subcadena, no de las demas letras
print(challenge.rfind('y',4,10)) #Devuelve un 9 ya que la ultima vez que aparece la letra "y" en la cedena "challenge" desde entre el index 4 y el indez 10 es en el index 9. challenge[9]
print(challenge.find('go')) #imprime -1 porque no encontro la subcadena 'go' en "challenge"

print("\nEjercicio 26 ****** Uso de format(): formatea la cadena en una salida más agradable.\n")
    #format(): formatea la cadena en una salida más agradable.
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area)) #Convierte las variables "radius" y "area" a string para imprimirlas
print(result) # The area of a circle with radius 10 is 314
result = 'The area of a circle with radius {} is {}'.format(radius, area) #imprime las variables "radius" y "area" con sus valores numéricos int y float respectivamente
print(result) # The area of a circle with radius 10 is 314

print("\nEjercicio 27 ****** Uso de index(): Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (el valor predeterminado es 0 y la longitud de la cadena es 1). Si no se encuentra la subcadena, genera un valueError. Es lo mismo que el metodo find() pero en lugar de devolver un -1 devuelve un error si no se encuentra\n")
    #index(): Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (el valor predeterminado es 0 y la longitud de la cadena es 1). Si no se encuentra la subcadena, genera un valueError.  Es lo mismo que el metodo find() pero en lugar de devolver un -1 devuelve un error si no se encuentra
challenge = 'thirty days of python'
sub_str = 'da'
print(challenge.index(sub_str))
print(challenge.index(sub_str,9)) #Error