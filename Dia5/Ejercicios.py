#Ejercicio 1
def devolver_distintos(num1,num2,num3):
    suma = sum(num1,num2,num3)
    lista = [num1,num2,num3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
    
#Ejercicio 2
def elnombre(name):
    name = list(set(name))
    name.sort()
    return name
print(elnombre("entretenidoo"))

#Ejercicio 3
def  elnum(*args):
    for i in args:
        if args[i] == 0 and args[i- 1] == 0:
            return True
    return False

print(elnum(6,0,5,1,0,3,0,1))

#Ejercicio 4
def contar_primos(num):

    primos = [2]
    iteracion = 3

    if num < 2:
        return 0
    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)
contar_primos(11)
