def devolver_distintos(num1,num2,num3):
    suma = sum(num1,num2,num3)
    if suma > 15:
        return max(suma)
    elif suma < 10:
        return min(suma)
    else:
        return suma/len(suma)