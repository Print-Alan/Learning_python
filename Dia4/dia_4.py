#operadores de comparacion

num1 = 36
num2 = 17
mi_bool = num1>=num2 #El operador de comparacion (>=) dice si num1 es mayor o igual a num2 lo cual es cierto es mayor
print(mi_bool)

num1 = 25**0.5 #le sacamos raiz cuadrada al 25 la cual es 5
num2 = 5
mi_bool = num1==num2 #comparamos si los valores de num1 y num2 son iguales (Lo cual es verdad  como es de tipo booleano contestara con un True) 
print(mi_bool)

num1 = 64 * 3
num2 = 24 * 8
mi_bool = num1 != num2
print(f"¿{num1} es diferente de {num2}?") #comparamos si los resultados de num1 y num2 son diferentes lo cual es (False) son iguales
print(mi_bool)

#Operadores logicos

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1>num2 and num1 < num3 #Verificamos si el valor de (num1) es mayor que (num2) (and) y menor que (num3)
print(mi_bool) #False (num1) es igual a (num2) no mayor, pero si es menor que (num3). Como una sentencia no se cumple cuenta como false

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3 #El operador (or) dice si (num1) es mayorque num2 o (num1) es menor que (num3)
print(mi_bool) #Lo cual solo se necesita cumplir una sentencia para que sea verdadero

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = "exito" and "tecnología" not in frase #El operador (and) los usamos para que se cumplan dos sentencias. (Not in) no estan en. 
print(mi_bool) #Le estamos diciendo si "exito" y "texnologia" no estan en frase lo cual es cierto (True)

#Control de flujo
#Segun se cumpla una condicion o no python ejecute un codigo o otro

num1 = int(input("Ingresa un número:")) #Pedimos numero
num2 = int(input("Ingresa otro número:")) #Pedimos numero

if num1 > num2: #Le decimos si (if) (num1) es mayor a (num2) imprime el siguiente codigo
    print(f"{num1} es mayor que {num2}")
elif num2 > num1: #Le dicimos si (elif) (num2) es mayor a (num1) imprime la sig linea
    print(f"{num2} es mayor que {num1}")
else: #Si no (else) se cumplen ninguna de las anteriores imprime la sig linea
    print("{num1} y {num2} son iguales")

edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia is True: #Si (if) su (edad) es mayor o igual a (18) y (tiene_licencia) (is) es (True) cierto imprime la sig linea
    print("Puedes conducir")
elif edad < 18 and not tiene_licencia is True: #Si (edad) es menor a 18 y (and) no (not) (tiene:licencia) es (is) (True) cierto imprime la sig linea
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else: # Si no se cumple ninguna imprime la el sig code
    print("No puedes conducir. Necesitas contar con una licencia")

habla_ingles = True
sabe_python = False

if habla_ingles is True and sabe_python is True: #Ya sabes lo que dice y se te olvida toma de nuevo la clase
    print("Cumples con los requisitos para postularte")
elif habla_ingles is False and sabe_python is False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles is False and sabe_python is True:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")

#Introduccion a Loops
#Los Loops son bucles que hace que algo se ejecute mas de una vez o que vuelva a sucerder una y otra vez. Por ejemplo el uso del loop en canciones.
#Tambien puedes hacer un loop que se repita una cantidad indefinida de veces hasta que se cumpla una condicion.
    #Por ejemplo el disparar en un juego que dispara hasta que se cumpla cierta condicion llamada balas igual a 0
#Elconcepto Iterable se relaciona con los loop, es decir que puedes iterar (repasar) sus elementos de 1 en 1, por ejemplo una lista que repasaria sus elemetos de 1 en 1

#Existen dos tipos de Loop: 1:Loop for (Los que se repiten una cantidad definida de iteraciones)   2:Loop while (Y los que se repiten una cantidad indefinida de veces (infinito))

#Loop for
Lista = ["a","b","c"]
for letra in Lista: #Por cada (For) (letra)letra es el nombre asignado a cada iteración en (in) Lista (Lista)
    print(letra) #Imprime las letras

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"] #Tenemos una lista con sus items
for alumnos in alumnos_clase:  #Por cada ((alumno)es el nombre asignado por cada item) en (in) el nombre de la lista (alumnos_clase)
    print(f"Hola {alumnos}") #Imprime hola + el nombre de cada alumno (alumnos)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] #Lista de numero
suma_numeros = 0 
for numero in lista_numeros: #Por cada (for) (numero) en (in) (lista_numeros)
    suma_numeros = suma_numeros + numero # 0 (suma_numeros) sera igual a 0 + cada (numero)
    print(suma_numeros) #imprime el resultado de cada numero sumado

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for num in lista_numeros: #Por cada integer (num) in (lista_numeros)
    if num % 2 == 0: #Si (if) (num) al modulo de 2 es igual a 0
        suma_pares = suma_pares + num #ejecuta suma pares + (num)
        print(suma_pares) #He imprime
    elif num % 2 == 1: #(elif) si no (num) al modulo de dos es igual a 1
        suma_impares = suma_impares + num #Ejecuta (suma_impares) + num
        print(suma_impares) #imprime

