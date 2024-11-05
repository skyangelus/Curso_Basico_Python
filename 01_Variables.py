#Como crear variables en Python
my_sring_variable = "My first String Variable" #Así se declara una variable en Python. Python detecta automaticamente el tipo de dato
print(my_sring_variable) #Se imprime el contenido de la variable en la consola

my_int_variable = 15 #Así se declara una variable de tipo int
print(my_int_variable)#Se imprime el contenido de la variable en la consola

my_bool_variable = False #Así se declara ua variable de tipo boolean
print(my_bool_variable)#Se imprime el contenido de la variable en la consola

#La funcion print, soporta distintos argumentos dentro de los mismo parentesis. Lo llamamos "Concatenación de variables en print"
print(my_sring_variable,my_bool_variable,my_int_variable)#En una sola linea de print, separados por comas, le pasamos el contenido de las tres variables que tenemos

#Si queremos convertir el contenido de una variable o un dato a string, se usa la función str()
first_var_integer = 28 #Declaro una variable de tipo int
print(type(first_var_integer))#imprimo el tipo de variable que declare y me devuelve <class 'int'>
print(type(str(first_var_integer)))#Convierto a string el contenido de la variable e imprimo el tipo y me devuelve <class 'str'>

second_var_integer = 28
var_to_string = str(second_var_integer)#Convertimos la variable second_var_integer a string y lo almacenamos en una nueva variable
print(type(var_to_string))#Imprimimos el tipo de variable y nos indica  que ya es un string <class 'str'>

#Si se quiere contar la cantidad de caracteres que tiene una variable, se puede usar la sentencia len()
print(len(my_sring_variable)) #Al imprimirla en la consola, indica que tiene 24 caracteres
first_name = "Alfredo"
last_name = "Arredondo"
print("my fist name lenght is:",len(first_name),"letters")
print("my last name lenght is:",len(last_name),"letters")

#En un print se puede ingresar texto como primer parametro y luego concatenar el valor de una variable
cur_age = 33
print("My current age is:", cur_age, "years old")

#Declaración de variables en una sola linea
f_name,l_name, email, age = "Alfredo", "Arredondo", "alfredoarredondo@live.com.mx",33 #Se declaran las variables separadas por comas y espues del igual, se les otorga el valor deseado en el mismo orden en que se declararon las variables
print('My name is',f_name,l_name,", my email is:",email,"and my current age is",cur_age,"years old")#en el print se pueden usar como variables independientes

#Manejo de entradas (inputs)
f_name = input("Ingresa tu primero nombre: ")
l_name = input("ingresa tu apellido paterno: ")
email = input("ingresa tu email: ")

print('hola', f_name, l_name,". Tu email es:",email)