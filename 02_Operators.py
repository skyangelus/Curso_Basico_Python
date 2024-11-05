# ********** OPERADORES (Operators) **********


#******************** OEPRADORES ARITMETICOS ********************
print("SÚMA: 3 + 4 =",3 + 4) #Realiza una súma  ordinaria entre los números
print("RESTA: 15 - 9 =",15 - 9) #Realiza una resta ordinaria entre los números
print("MULTIPLICACIÓN: 3 * 4 =",3 * 4) #Realiza una multiplicación ordinaria entre los números
print("DIVISIÓN: 3 / 4 =",3 / 4)  #Realiza una división ordinaria entre los números y el resultado contiene números decimales en caso de que el resultado no sea un número entero
print("RESIDUO: 3 % 4 =",3 % 4) #Realiza una división orfinaría entre los números, pero el resultado, sera el residuo de la divición (Hasta antes de comenzar a colocar un punto decimal)
print("DIVICION SIN DECIMALES: 3 / 4 =",3 // 4) #Al usar // realiza una division entre los números, pero el resultado lo convierte a número entero, eliminando los decimales.
print("Exponente: 3 ^ 4 =",3 ** 4) #Realiza el calculo de elevar el primer número a la potencia del segundo y se usan dos asteriscos para indicar la potencia **

#Concatenación con cadenas de texto
print("Hola, mi nombre es" + " Alfredo")
'''
Las siguientes operaciones con cadenas no estan permitidas:
print("Hola, mi nombre es" - " Alfredo") No esta permitido realiza resta de cadenas de texto
print("Hola, mi nombre es" + 5) No se pueden realizar operaciones entre tipos de datos distinto, por ejemplo Strig + Integer
'''

#Se pueden concatener string e integer, si el dato númerico es convertido a string con la función str()
print("Mi edad es: " + str(33) + " Años")

#Se puede usar el simbolo de multiplicación para multiplicar un string por un número de tipo int. Pero fallara si es multiplicado por uno de tipo float, aúnque el float sea x.0
print("Alfredo " * 3)
print("Alfredo " * (5 - 1)) #Puede multiplicarse por el resultadod e una operación sencilla, pero si la operación es mas compleja, no hara nada

my_float_var = 2.5 * 2 # 2.5 x 2 = 5.0, entonces no debería ser posible el multiplicar ese resultado por una cadena de caracteres
print("HOLA " * int(my_float_var)) #Pero si la variable, la convertimos a entero con la función int(), entonces ya no sera my_float_var = 5.0, sino my_float_var = 5

#******************** OEPRADORES BOOLEANOS ********************
print("Mayor que: ",3 > 4)
print("Menor que: ",3 < 4)
print("Mayor o igual que: ",3 >= 4)
print("Menor o igual que: ",3 <= 4)
print("Identico que: ",3 == 4)
print("Diferente que: ",3 != 4)

#Es posible también usar los comparadores booleanos no solo con números, sino también con cadenas de texto, y la comparacíon la hace caracter a caracter y lo determina por el orden alfabético
print("Hola Mayor que Bola?:","Hola" > "Bola") #Ambas tiene 4 letras, pero la H es una letra más avanzada en el alfabeto, entonces se considera mayor, así que "Hola" > "Bola" = TRUE
print("hola Identico que HOLA?:","hola" == "HOLA") #Ambas son iguales, pero una minisculas y la otra en mayusculas, entonces "hola" == "HOLA" = FALSE
print("hOLA Identico que HOLA?:","hOLA" < "HOLA") #Ambas son iguales, pero la primera letra de una es minuscula, entonces Python detecta como mayor a las minusculas que mayusculas
print("Contando caracteres, Alfredo es mayor que Python? Alfredo tiene",len("Alfredo"),"letras y Python tiene",len("Python"),"letras, resultado:",len("Alfredo") > len("Python"))

#******************** OEPRADORES LÓGICOS ********************
print("***************** Tabla de verdad - Operador AND ******************")
print("True && True =",True and True)
print("True && False =",True and False)
print("False && True =",False and True)
print("False && False =",False and False)

print("***************** Tabla de verdad - Operador OR ******************")
print("True || True =",True or True)
print("True || False =",True or False)
print("False || True =",False or True)
print("False || False =",False or False)

print("***************** Tabla de verdad - Operador NOT AND ******************")
print("NOT (True && True) =",not(True and True))
print("NOT (True && False) =",not (True and False))
print("NOT (False && True) =",not (False and True))
print("NOT (False && False) =",not (False and False))

print("***************** Tabla de verdad - Operador NOT OR ******************")
print("NOT (True || True) =",not(True or True))
print("NOT (True || False) =",not (True or False))
print("NOT (False || True) =",not (False or True))
print("NOT (False || False) =",not (False or False))