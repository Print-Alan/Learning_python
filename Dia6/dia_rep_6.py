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

mi_archivo = open("texto.txt")
print(mi_archivo.readline())
mi_archivo.close()

mi_archivo = open("texto.txt")
l_por_l = mi_archivo.readline()
l_por_l = mi_archivo.readline()
print(l_por_l)
mi_archivo.close()
