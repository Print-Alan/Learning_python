#Metodos
# Los metodos son funciones pertenecientes a los objetos que permiten manipularlos, analizarlos o ejecutar acciones
#Por ejemplo "Hola".lower(), "Hola".index()
"""
La documentación oficial de
Python (o Biblioteca Estándar de Python), que contiene toda la
información necesaria : https://docs.python.org/es/3.13/library/index.html
Esa informacion te servira para trabajar con metodos que esten saliendo o que nadie te ha enseñado
"""
#lstrip
#Lo que hace es eliminar los caracteres de izquierda a derecha hasta que encuentre un carácter que no esté en la lista.
x = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
y = x.lstrip(",:_#") #Los caracteres se van a eliminar, se detendra hasta que encuentre un caracter que no este en la lista
print(y)

#insert
#Se utiliza para insertar un elemento en una lista en una posición específica. Este método es muy útil cuando necesitas agregar un elemento en un lugar específico de tu lista sin reemplazar ningún otro elemento.
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
n = frutas.insert(3,"naranja") #primero se coloca la posicion y despues tu item
print(frutas)

