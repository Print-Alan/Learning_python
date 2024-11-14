#Ejercicio 1
def devolver_distintos(num1,num2,num3):
    suma = sum(num1,num2,num3)
    if suma > 15:
        return max(suma)
    elif suma < 10:
        return min(suma)
    else:
        return suma/len(suma)
    

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