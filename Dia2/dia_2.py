#Tipos de datos

#string (str) es una cadena de texto, por ejemplo: "hola","%&#/"," ","123". Lo que este dentro de las comillas sera tratado como texto
#interger (int) tipo de dato que es un numero entero, por ejemplo: 150,140,10,-15,0
#floating(float) tipo de dato que guarda numeros decimal, por ejemplo: 1.25,25.0,500.50,-95.1
#listas(list)["sal",1,-3,4.5,"Marte",0] Una coleccion ordenada de objetos
#diccionarios (dic) {'color':'rojo','arte':'cine'} Son pares de palabras agrupados primero por la clave y despues el valor separados por una coma
#tuples(tuple) ('lun','mar','mie','jue','vie') Son similares a las listas, pero con la diferencia de que no pueden modificarse
#sets(set) {'a','b','c','d','e'} Es un conjunto de elementos ordenados unicos e irrepetibles
#booleanos (bool) True, False Es un dato que solo puede tener dos valores true, false. Para saber si una condicion se cumple

#Variables

nombre = "Juan"
edad = 15

nombre = "Julia "
apellido = "Roberts"
nombrecompleto = nombre + apellido
print(nombrecompleto)

curso = "Python"
print("Estás tomando un curso de" + " " + curso )

edad = input("Dime tu edad ") #Input transforma los valores dados a strings
print("Tu edad es: " + edad)

num_enter = 5
print(type(num_enter))

num_decimal = 1.5
print(type(num_decimal))

num1 = 7.5
num2 = 2.5
sum = int(num1 + num2)
print(type(sum) )

#Conversiones

mi_valor = 1 
otro_valor = 2
sum = int(mi_valor + otro_valor)
print(sum)

num1 = int(7.5)
print(type(num1))

num2 = float(10)
print(type(num2))

num1 = "7.5"
num2 = "10"
print((float(num1)) + (float(num2)))

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}") #Format (f) realizara una tarea asignada entre { }

puntos_nuevos = 350
puntos_totales = 1225
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_totales)) #Esta es otra manera de escribir Format, la clasica

puntos_anteriores = 875
puntos_nuevos = 350
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos")

x = 874
y = 27
print(f"{x//y}") #La doble barra indica que es una divicion al piso es dice que eliminara los numeros despues de punto decimal

print(f"{456 % 33}") # El operador Modulo (%) Te da como resultado el sobrante de la divicion es decir cuantas veces entra 33 en 456 = 13, pero sobran 27
#sirve para determinar si un número es par o impar, o para ciclos y repetición en estructuras de datos.

print(f"{783**0.5}") #El operador Raiz cuadrada (**0.5) El resultado da un numero que al ser multiplicadp por sí mismo da el valor que se le asigno en este caso 783

print(round(10 / 3,2)) #El metodo Round redondea al numero decimal mas cercano y que sea par esto si se usa un .5. La coma despues de la operación le puedes idicar cuantos decimales quiers que muestre

valor = 10.676767
print(round(valor)) #El metodo Round redondea al numero decimal mas cercano

print(round(5**0.5,4)) #Aqui le estamos diciendo que eleve al cuadrado y que muestre el resultado con 4 decimales

