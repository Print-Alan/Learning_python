#Abrir y manipular archivos
mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea.rstrip()) #.rstrip() Elimina el salto de linea
una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()

mi_archivo = open("texto.txt")
print(mi_archivo.read())
mi_archivo.close()