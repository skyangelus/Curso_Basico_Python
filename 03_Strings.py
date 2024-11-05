#******************* STRINGS ********************

#Declaración de variables ---------------------------------------------------------------------------------------------------------------------
my_string = "Mi String 1" #Una String puede ser declarada entre comillas dobles
my_other_string = 'Mi String 2' #Una String puede ser declarada entre comillas simples

#Imprimir la longitud del contenido de una variable de tipo string -------------------------------------------------------------------------------------------
print("La longitud del contenido de mi variable my_string es:",len(my_string),"caracteres") #Imprime la longitud del contenido de la variable my_string
print("La longitud del contenido de mi variable my_other_string es:",len(my_other_string),"caracteres") ##Imprime la longitud del contenido de la variable my_string

#Concatenación de strings usando el signo "+" -------------------------------------------------------------------------------------------
print("Se concatena el contenido de my_string + espacio + my_other_string:",my_string + " " + my_other_string)

#String con un salto de linea-----------------------------------------------------------------------------------------------------------------
my_new_line_string = "Este es un string\ncon un salto de linea" #El comando \n inserta un salto de linea en un string
print(my_new_line_string) #Se imprime el contenido de la variable "my_new_line_string"

#String con una tabulación---------------------------------------------------------------------------------------------------------------------
my_tab_line_string = "\tEste es un string con una tabulación" #El comando \t inserta una tabulación en un string
print(my_tab_line_string) #Se imprime el contenido de la variable "my_tab_line_string"

#String escapado--------------------------------------------------------------------------------------------------------------------------------------
my_esc_line_string = "\\t Este es un string \\n escapado" #Si se coloca una \ justo antes de un \t o \n, ignora el comando e imprime "\t" o "\n"
print(my_esc_line_string) #Se imprime el contenido de la variable "my_esc_line_string"

#Formateo------------------------------------------------------------------------------------------------------------------------------
fname, lname, age = "Alfredo", "Arredondo", 33 #Se crean las variables fname, lname, age y se le asigna .
print("Mi nombre es {} {} y mi edad es {}".format(fname,lname,age)) #Para agregar las variables de la tupla usando el .format(), hay que usar {} en los luigares que se agregara el contenido de la variable.
print("Mi nombre es %s %s y mi edad es %d" %(fname,lname,age)) #Para agregar las variables de la tupla usando el %() hay que agregar %s para colocar un string o un %d para un entero, un %f para un flotante, etc.

print("Mi nombre es " + fname + " " + lname + " y mi edad es " + str(age)) #Esta forma es igual que las anteriores, sin embargo es menos optima utilizarla, se recomiendan más cualquiera de las anteriores

#Forma vieja de formateo en python----------------------------------------------------------------------------------------------------------------------------
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas'] #Se crea un arreglo con las librerias de Python
formated_string = 'The following are python libraries:%s' % (python_libraries) #Se crea una variable con el formato
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

#Forma nueva de formateo en Python - valida a partir del Python_v3 -------------------------------------------------------------------------------------------
#string only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

#Numbers only
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
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

