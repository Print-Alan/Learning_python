from random import choice

def palabra():
    Palabras = ["Yucatan","Tangamandapio","Hello","Enderpearl","Corruptos"]
    return choice(Palabras)

def guiones(separar):
    guiones = []
    for item in separar:
        guiones.append("_")
    return guiones

def pedir_letra(enunciado,guiones,vidas):
    x = input("Dime tu letra a elegir: ")
    if x  in enunciado:
        print("Tu letra si está")
        for i, letra in enumerate(enunciado):
            if letra == x:
                guiones[i] = x
    else:
        print("Tu letra no está")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
    return guiones,vidas 


palabra_seleccionada = palabra()
guiones_seleccionados = guiones(palabra_seleccionada)
vidas = 5

while "_" in guiones_seleccionados and vidas > 0: 
    guiones_seleccionados,vidas = pedir_letra(palabra_seleccionada, guiones_seleccionados,vidas) 
    print(''.join(guiones_seleccionados))

if vidas == 0:
    print("Perdiste")
else:
    print("Ganaste")    