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

#Loop while
#Los loop while se repiten mientras (while) se cumpla un condicion.
#Por ejemplo en un juego que cuando el jugador muere puede revivir mientras tiene una cantidad de vidas mayor a 0
#Debes tener cuidado, por que si no estableces expresamente de que deje de cumplirse la condicion por ejecurse infinitamente

numero = 10
while numero >= 0: #Mientras (while) 10 (numero) sea mayor a (0)
    print(numero) #Imprime desde el 10
    numero = numero - 1 #Iras restando a (numero) -1 hasta llegar a cero

numero = 50
while numero >= 0: #Mientras numero sea mayor o igual a 0 imprime
    if numero % 5 == 0: #si el numero es modulo de 5 y igual a 0
        print(numero) #imprime numero
        numero -=1    #numero -1 hasta llegar a 0
    else:             #Si no ejecuta el sig code
        numero -=1    #Le vas restando a num 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,-6,-6,-4,-3]
for num in lista_numeros: #(for) Por cada (num) (in) (lista_numeros)
    if num <=0:  #Si (if) (num) es menor o igual a (0)
        continue #Excluyelo, pasa de este
    print(num)   #imprime

#Rango (Range)
#Es una fucion que te permite establecer un rango de caracteres o items sin la necesdad de crear listas o variables multiples veces

mi_lista = list(range(2500,2586)) #Lista (list) con un Rango (range) de 2500 a 2585 numeros 
print(mi_lista) 

mi_lista = list(range(3,301,3)) #Creamos una lista con un rango del 3 al 300 la cual esta formada por multiplos de 3
print(mi_lista)

suma_cuadrados =0
for num in range(1,16): #Por (for) cada (num) (in) (range 1,15)
    suma_cuadrados += num ** 2 #Haras una suma de num elevado a la 2
    print(suma_cuadrados)

#Enumerador
#Enumerate sirve para acceder a los indices de una colecccion mas facilmente

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"] #Lista
for numero, nombre in enumerate(lista_nombres): #Por cada (numero), (nombre) en (in) (enumerate: Es una funcion que hace mas facil acceder a los indices) que contendra (lista_nombres)
    print(f'{nombre} se encuentra en el índice {numero}') #imprime (nombre) se ecuentra en el indice (numero)

lista_indices = [] #Creamos una lista
for num,nom in list(enumerate("Python")): #Por cada num,nom in list(enumera("Python"))
    lista_indices.append((num,nom)) #Añade a lista de indices num, nom
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,name in enumerate(lista_nombres): #Por cada (for) numero de indice (indice), valor (name) en (in) enumerado (enumerate) (lista_nombres)
    if name.startswith("M"): #si (if) (name) inicia (.startswith("M")) con M 
        print(indice) #imprime el numero del indice

#Zip
#Zip combina dos o mas listas entrelazando sus elementos en tuples

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
x = list(zip(capitales,paises)) #Guarda e x una (list) que una dos o mas listas (zip) : (capitales y paises)
for capi,pais in x: #Por cada (for) capital(capi), pais (pais) en (in) x
    print(f"La capital de {pais} es {capi}")

marcas = ["Gucci","Sait lorean","Hermes","All-Nasar"]
productos = ["Osito gominola","Botas","Oro","Al bicho siuuuu"]
mi_zip = zip(marcas,productos) #Creamos un objeto zip formado por listas

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
numeros = list(zip(espaniol,portugues,ingles)) #Lo mismo que el primer ejercicio de Zip
print(numeros)

#Min y Max 
#Sirve para detectar los valores mas altos y mas bajos en una coleccion (Desordenada o ordenada) funciona con: valores numericos y alfabeticos

#Manera 1
menor = min(58,96,72,64,35) #El minimo de esta serie de numeros guardalo en menor
mayor = max(58,96,72,64,35) #El maximo de esta serie de numeros guardalo en mayor
print(menor,mayor) 
#Manera 2
lista = [58,96,72,64,35]
print(max(lista)) #impreime el maximo de la siguente lista
print(f"El menor es {min(lista)} y el mayor es {max(lista)}") #Otra manera es esta
#Manera 3
nombres = ["juan","pablo","alicia","carlos"]
print(min(nombres)) #Imprime el caracter que va primero en el abecedario de la lista nombres(Min y max:Buscan primero en las mayusculas y despues en las minusculas)
nombre1 = "carlOs" #Busca primero en las mayusculas y despues en las minsculas. Si quieres que busque la letra sin confusiones utiliza e metodo .lower()
print(min(nombre1.lower())) #asi transformara el dato a minuscula y podras ubicarlo mejor 
#Manera 4
dic = {"c1":45,"c2":11} #Diccionario
print(min(dic)) #En los diccionarios imprime la clave menor
print(min(dic.values())) #Si quieres el valor utiliza el metodo .values()


lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros) #el valor maximo de lista de numeros guandalo en valor_maximo
print(valor_maximo)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros) #El valor maximo restale el valor minimo y guardo el la variable rango
print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values()) #El valor minimo del diccionario 
ultimo_nombre =max(diccionario_edades) #La clave mayor del diccionario
print(edad_minima)
print(ultimo_nombre.lower()) #imprime la clave mayor minuscula de el diccionario

#Random
#El metodo randint(): Sirve para generar numeros enteros aleatorios
#randint() pertenece a una libreria llamada Random y para importar el metodo se usa: from (random) import (randint), (desde (libreria) importa (metodo))
#Si vas importar muchos elementos de una misma libreria remplaza el metodo por un asterisco: from (random) import *

#randint
from random import randint # De (from) la libreria (random) importa (randint). Al importar librerias es importante que tu archivo .py no tenga el mismo nombre de las librerias que vas a importar
aleatorio = randint(1,50) #Una vez importada la libreria random int (randint) del 1 al 50, escogera un numero random
print(aleatorio)
#uniform
from random import * #Con el (*) estamos inportando todos los contenidos de la libreria random
aleatorio1 = round(uniform(1,5),1) #Uniform da un numero aleatorio de tipo float. Con el metodo (round) redondeamos es cantidad y añade 1 numero decimal (float)
print(aleatorio1)
#Random
#Ya importamos los contenidos de la libreria en la linea anterior
aleatorio2 = random() #Te devuelve el tipo de dato float del 0 al 1
print(aleatorio2)
#Choice
colores = ["azul","rojo","verde","amarillo"]
aleatorio3 =choice(colores) #Choice te elige un elemento aleatoria en la lista de colores
print(aleatorio3)
#shuffle
numeros1 = list(range(5,51,5))
shuffle(numeros1) #Hace una mezcla aleatoria de tu lista. El metodo shuffle no se puede almacenar en una lista, ni tampoco con strings
print(numeros1)

from random import randint
aleatorio = randint(1,10) #random interger del 1 to 10
print(aleatorio)

from random import random
aleatorio = round(random(),1) #numero decimal del cero al uno con un decimal
print(aleatorio)

from random import choice
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres) #Elige un nombre al azar de la lista nombres
print(sorteo)

#Comprensión de listas
#Es una manera dinamica de construir listas. Si tienes que construir una lista atraves de un loop que pasa varias veces por un append, te ayudara

#Manera comun
palabra3 = "python"
lista1 = []
for letra in palabra3: #Por cada letra en palabra3
    lista1.append(letra) #En una lista agrega cada letra
print(letra)

#manera de comprension
palabra3 = "python"
lista1 = [letra for letra in palabra3] #Manera de comprension
print(letra)

lista2 = [n for n in range(0,21,2) if n * 2 > 10]
print(lista2)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [num**2 for num in valores] #Numero elevado al cuadrado por cada num in valores
print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [num for num in valores if num % 2 == 0] #Si solo vas a ocupar (if) esta es la manera de usarlo
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(num - 32) * (5/9) for num in temperatura_fahrenheit] #Siuuuuu
print(grados_celsius)

