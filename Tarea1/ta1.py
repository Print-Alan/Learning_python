from random import randint
def lanzar_dados():
    dado1 = 1
    dado2 = 6
    excepcion = 0
    return dado1, dado2, excepcion

def evaluar_jugada(dado1, dado2, excepcion):
    suma_dados = dado1 + dado2
    if excepcion == 1:
        print("La suma de tus datos es excelente por excepción")
    else:
        if suma_dados <= 6:
            return f"La suma de tus dados es {suma_dados}. Lamentable"
        elif suma_dados > 6 and suma_dados < 10:
            # elif 6 < suma_dados < 10:
            return f"La suma de tus dados es {suma_dados}. Tienes buenas chances" 
        else: return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

resultado1, resultado2, excepcion = lanzar_dados()
mensaje = evaluar_jugada(resultado1, resultado2,excepcion)
print(mensaje)