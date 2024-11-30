from random import choice

def palabra():
    Palabras = ["Yucatan","Tangamandapio","Hello","Enderpearl","Corruptos"]
    return choice(Palabras).lower()

def guiones(separar):
    guiones = []
    for item in separar:
        guiones.append("_")
    return guiones

def validar_letra(palabra,guiones,vidas):
    
    tr1 = input("Dime tu letra: ".lower())
    while not tr1.isalpha():
        print("Tu letra  no es valida")
        tr1 = input("Dime tu letra: ")
    
    if tr1 in palabra:
        print(guiones)
        for i, letra in enumerate(palabra):
            if letra == tr1:
                guiones[i] = tr1
    else:
        print(guiones)
        lista.append(tr1)
        print(f"Lista de palabras incorrectas {lista}")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
    return guiones,vidas,lista

x = palabra()
y = guiones(x)
lista = []
vidas = 5

while "_" in y and vidas > 0:
    y,vidas,lista = validar_letra(x,y,vidas)
    print("".join(y))

if vidas == 0:
    print("Perdiste")
else:
    print("Ganaste")  

"""

"""