x = input("Ingresa tu texto: ")
y = x.lower()
lista = len(y)
letra1 = y[0]
letra2 = y[-1]
linvertidas = y[::-1]
pit = "Python"
low =pit.lower() in y

a = input("\nIngresa 1 letras de tu eleccion: ")
ra = a.lower()
letra_a = y.count(ra)

b = input("\nIngresa 1 letras de tu eleccion: ")
rb = b.lower()
letra_b = y.count(rb)

c = input("\nIngresa 1 letras de tu eleccion: ")
rc = c.lower()
letra_c = y.count(rc)

print(f"\nHay un total de palabra en tu texto de {lista}")
print(f"\nTu primera letra es {letra1} y tu ultima letra es {letra2}")
print(f"\npalabras invertidas {linvertidas}\n\nPython esta en tu texto: {low}")
print(f"\ntu letra {a} aparece {letra_a} veces\ntu letra {b} aparece {letra_b} veces\ntu letra {c} aparece {letra_c} veces")