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
