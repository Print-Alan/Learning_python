#Metodo index()

mi_texto = "Esta es una prueba"
resutaldo1 = mi_texto[6] #El metodo index aqui indica que letra se encuentra en la 5 posicion. Se empieza a contar desde el 0
print(resutaldo1)

palabra = "ordenador"
resultado2 = palabra[4] #Lo mismo se encontraria la letra n
print(resultado2)

frase1 = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado3 = frase1.index("práctica") #Aqui le estamos pidiendo que nos diga en que indice se encuentra la pralabra: práctica
print(resultado3)

frase2 = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado4 = frase2.rindex("práctica") #El reverse index hace lo mismo pero empezando a buscar al contrario es decir desde el final
print(resultado4)

#Sub strings

frase3 = "Controlar la complejidad es la esencia de la programación"
resultado5 = frase3[0:9] #El metodo sub strings en este caso te dira que caracteres se encontraran desde el indice 1 hasta el 8. RECUERDA que el 9 no se cuenta tomara el numero anterior
print(resultado5)

frase4 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado6 = frase4[8::3] #Aqui le decimos que inicie en el caracter 7 hasta el final con un salto de 3 en 3
print(resultado6)

frase5 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado7 = frase5[::-1] #En este caso le pedimos que agrupe todos los caracteres al reves desde el final
print(resultado7)

#Metodos de String

frase6 = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase6[1].upper()) #En el metodo Upper le estamos diciendo que transforme el texto que contiene la variable frase pase a mayusculas

lista_palabras = ["La","legibilidad","cuenta."]
resultado8 = " ".join(lista_palabras) #El metodo join une las palabras que estan en una lista. En este caso con un espacio pero puede ser con cualquier caracter
print(resultado8)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado8 = frase.replace("difícil","fácil") #El metodo replace remplaza palabras por las que quieras despues de la coma
resultado9 = resultado8.replace("mala","buena")
print(resultado9)

#Propiedades de string

print("Repetición"*15) #En este caso el simbolo * multiplica 15 veces la palabra repeticion

x = ("""Tierra mojada
mis recuerdos de viaje,
entre las lluvias""") # Al poner 3 veces las comillas dobles te permite poder escribir texto en diferentes líneas.
print(x not in ("agua")) #No esta en (Not in) es una propiedad de tipo booleano que responde si es true or false. Tambien esta la propiedad (in) para verificar si se encuentra una palabra en tu texto

x = "lectroencefalografista."
print(len(x)) #Len te dice que tan largo es tu string

#Listas

mi_lista = ["1","hola","nop","1.5","8"] #Las listas se colocan entre corchetes y comillas