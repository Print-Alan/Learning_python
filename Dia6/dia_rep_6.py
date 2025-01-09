#Abrir y manipular archivos
mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea.rstrip()) #.rstrip() Elimina el salto de linea
una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()

#mi_archivo = open("texto.txt")
#print(mi_archivo.read())
#mi_archivo.close()

#mi_archivo = open("texto.txt")
#print(mi_archivo.readline())
#mi_archivo.close()

#mi_archivo = open("texto.txt")
#l_por_l = mi_archivo.readline()
#l_por_l = mi_archivo.readline()
#print(l_por_l)
#mi_archivo.close()

#Crear y escribir archivos

mi_archivo = open("prueba.txt","w")
mi_archivo.write("Soy el nuevo texto")
mi_archivo.close()

mi_archivo = open("mi_archivo.txt","w")
mi_archivo.write("Nuevo texto")
mi_archivo.close()
mi_archivo =open("mi_archivo.txt")
print(mi_archivo.read())
mi_archivo.close()

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()

archivo = open("registro.txt","a")
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for p in registro_ultima_sesion:
    archivo.writelines(p +"\t")
archivo.close()

archivo = open("registro.txt")
print(archivo.read())
archivo.close()

#Directorios

import os

ruta = os.getcwd() #Ruta con la que trabajamos
print(ruta)

ruta2 = os.chdir("C:\\Users\\SSD\\Desktop\\Ilearn-py\\Dia6") #cambiar a esta ruta 
print(ruta2)