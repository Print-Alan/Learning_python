from random import randint
x = input("Dime tu nombre: ")
print(f"Bueno {x} he pensado en un numero del 1 al 100 tienes 8 intentos para advinarlo")
aleatorio = randint(1,101)
for chance in range(1,9):
    if chance >= 1:
        chance -=1
        adivinar = int(input("Adivina: "))
        if adivinar < 1 or adivinar > 100:
            print("Elegiste un numero que no esta permitido ")
        elif adivinar < aleatorio:
            print("Tu respuesta es incorrecta, has elegido un numero menor al del programa ")
        elif adivinar > aleatorio:
            print("Tu respuesta es incorrecta, has elegido un numero mayor al del programa ")
        elif adivinar == aleatorio:
            print(f"Has ganado en {chance} intentos")
            break
if adivinar != aleatorio:
    print(f"Has perdido el numero secreto era {aleatorio}")