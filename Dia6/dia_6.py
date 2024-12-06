# Abrir y manipular archivos
# Manipular archivos de python inplica las E/S (Entrada y Salida de datos) o en ingles que lo encontrarias como I/O (input y output)
"""
Podemos hacer las siguientes opciones en archivos .txt de texto:
Abrir : open()
Leer : read()
Escribir : write()
Cerrar : close()
"""
mi_archivo = open("prueba.txt") #Abre el archivo de texto
print(mi_archivo.read()) #Lee el archivo y lo imprime
mi_archivo.close #Cierra el archivo para guardar espacio en memoria, buenas practicas


print(mi_archivo.readline()) #Lee la primera linea del archivo y la imprime
mi_archivo.close #Cierra el archivo

#
mi_archivo = open("texto.txt")
print(mi_archivo.read()) #Lee el archivo completo y imprime
mi_archivo.close

mi_archivo = open("texto.txt")
print(mi_archivo.readline()) #Lee la primera linea e imprime
mi_archivo.close

mi_archivo = open("texto.txt")
mi_archivo.readline() #Lee la primera linea
print(mi_archivo.readline()) #Lee la segunda linea e imprime
mi_archivo.close

