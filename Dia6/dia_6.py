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


#mi_archivo = open("texto.txt")
print(mi_archivo.read()) #Lee el archivo completo y imprime
mi_archivo.close

#mi_archivo = open("texto.txt")
print(mi_archivo.readline()) #Lee la primera linea e imprime
mi_archivo.close

#mi_archivo = open("texto.txt")
mi_archivo.readline() #Lee la primera linea
print(mi_archivo.readline()) #Lee la segunda linea e imprime
mi_archivo.close


#Crear y escribir archivos

#Vamos a modificar los archivos desde python
#mi_archivo = open("archivo.txt","r") (Read) Leer es modo por defecto
#mi_archivo = open("archivo.txt","w") (Write) Escribir recetea todo el contenido del archivo 
#mi_archivo = open("archivo.txt","a") (append) Se posiona el cursor al final para escribir

archivo = open("prueba.txt","w")
archivo.write("Soy el nuevo texto\n")

archivo = open("prueba.txt","a")
archivo.write("Bienvenidos")
archivo.close()

archivo = open("mi_archivo.txt","w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()

#archivo = open("mi_archivo","a")
archivo = open("mi_archivo.txt","a")
#archivo.write("Log de erorres\nAcciones por el usuario\nNuevo inicio de sesión")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("registro.txt","a") 
for i in registro_ultima_sesion: #Por cada item en la lista
    archivo.writelines(i + "\t") #Al archivo le escribriras en varias lineas el item y una tabulacion
archivo.close()
archivo = open("registro.txt")
print(archivo.read())
archivo.close()

#Directorios
#Al abrir un archivo python lo busca en la carpeta donde esta guardado el programa que utilizas
#De la sig manera podemos abrir archivos que se encuentran en otra parte
import os #Importamos os (operative system) que nos da las herramientas para interactuar con el directorio

ruta = os.chdir("C:\\Users\\SSD\\Desktop") #Especificamos la ruta del archivo en el chdir (change directory)
archivo2 = open("otro_archivo.txt")        #Abrimos el archivo
print(archivo2.read())                     #Imprimimos
archivo2.close()

#ruta1 = os.makedirs("C:\\Users\\SSD\\Desktop\\Otra")   Makedirs crea directorios colocando la ruta y el nombre del archivo

ruta2 = "C:\\Users\\SSD\\Desktop\\Ilearn-py\\Dia6\\prueba.txt"
elemento = os.path.basename(ruta2) #Pedimos el nombre de base de nuestra ruta
elemento = os.path.dirname(ruta2)   #Pedimos el nombre completo de la ruta
elemento = os.path.split(ruta2)     #Nos da ambos
print(elemento)

#os.rmdir("C:\\Users\\SSD\\Desktop\\Otra") #Rmdir Elimina los directorios

from pathlib import Path

carpta = Path("C:/Users/SSD/Desktop") / "otro_archivo.txt" #Path hace que cualquier sistema windows o Mac lo pueda entender
mi_archivo1 = open(carpta)
print(mi_archivo1.read())
mi_archivo1.close()

#pathlib
#Nos permite manipular rutas de archivos de forma rapida

from pathlib import Path, PureWindowsPath #PureWindowsPath nos transforma cualquier ruta a una ruta de windows

carpeta = Path("C:/Users/SSD/Desktop/otro_archivo.txt")

ruta_windows = PureWindowsPath(carpeta) #Nos transforma la ruta a una ruta windows
print(ruta_windows)

print(carpeta.read_text()) #El objeto de Path nos permite leer de forma más sencilla usando .read_text(). Sin abrir y cerrar achivos
print(carpeta.name) #Nos da el nombre del archivo
print(carpeta.suffix) #Nos dice de que tipo es .txt, etc
print(carpeta.stem) #Nos da el nombre del archivo sin decir el tipo

if not carpta.exists(): #El metodo exist nos dice si existe devolviendo un booleano
    print("Este archivo no existe")
else:
    print("Si existe")

#Path
#Representa una ruta de un alrchivo
#Te sirve por ejemplo:
#-Crear o mover archivos
#-Enumerar archivos
#-Crear rutas basadas en strings. mi_ruta = Path("Carpeta","Archivo","Documento","Doc.txt")     De esa manera
from pathlib import Path

base = Path.home() #Te da una ruta absouta
guia = Path(base,"Barcelona","Sagrada_Familia.txt") #Teda la ruta obsoluta + la creada
guiaadd = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
guia2 = guiaadd.with_name("La_Pedrera.txt") #Sustituye el ultimo string de un Path
print(base)
print(guia)
print(guiaadd.parent) #Es una propiedad que devuelve el antecesor de un archivo
print(guiaadd.parent.parent) #Mientras más parents pongas tu retrocedera en el arbol de directorios
print(guia2)

guia_Europa = Path(Path.home(),"Europa")

for txt in Path(guia_Europa).glob("**/*.txt"):
    print(txt)

guia3 = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia3.relative_to(Path("Europa")) #Relative_to() Elimina del inicio de una ruta el segmento que corresponde a otra ruta base especificada.
en_españa = guia3.relative_to(Path("Europa","España")) #De españa en adelante
print(en_europa)
print(en_españa)
