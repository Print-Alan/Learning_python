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