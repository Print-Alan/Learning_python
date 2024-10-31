#Metodo index()

mi_texto = "Esta es una prueba"
resutaldo1 = mi_texto[6] #El metodo index aqui indica que letra se encuentra en la 5 posicion. Se empieza a contar desde el 0
print(resutaldo1)

palabra = "ordenador"
resultado2 = palabra[4] #Lo mismo se encontraria la letra n
print(resultado2)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado3 = frase.index("práctica") #Aqui le estamos pidiendo que nos diga en que indice se encuentra la pralabra: práctica
print(resultado3)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado4 = frase.rindex("práctica") #El reverse index hace lo mismo pero empezando a buscar al contrario es decir desde el final
print(resultado4)

#Sub strings

frase = "Controlar la complejidad es la esencia de la programación"
resultado5 = frase[0:9] #El metodo sub strings en este caso te dira que caracteres se encontraran desde el indice 1 hasta el 8. RECUERDA que el 9 no se cuenta tomara el numero anterior
print(resultado5)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado6 = frase[8::3] #Aqui le decimos que inicie en el caracter 7 hasta el final con un salto de 3 en 3
print(resultado6)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado7 = frase[::-1] #En este caso le pedimos que agrupe todos los caracteres al reves desde el final
print(resultado7)

