#Metodos,ayuda y documentacion
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

#isdisjoint
#Se utiliza para determinar si dos conjuntos son disjuntos, es decir, si no tienen elementos en común. Devuelve True si no tienen elementos en común y False en caso contrario.
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv) #Verifica si en los dos sets no hay conjuntos iguales: si no hay te dara:True. Si hay conjuntos iguales:False
print(conjuntos_aislados)


#Funciones
#Los metodos son funciones que fueron desarrolladas por los creadores de python y incorporadas a los objetos
#Pero tambien podemos crear metodos propios, para que no tengamos que escribir el codigo entero

#Crear funciones
#Para crear funciones se necesita de una sintaxis precisa
#Para es se usa : 
#Def mi_funcion ():
"""Esta funcion se encarga
    de esto y esto"""
    #(Codigo)
#Ejemplo:
def saludo_hola ():
    """
    Esta funcion sirve para saludar
    """
    print("hola")
saludo_hola() #Ejecuta la funcion saludo_hola

def saludar(): #Define la funcion (def) (saludar)
    print("¡Hola mundo!") #Que cada que se invoque imprima el code
saludar() #Invocar saludar()

def bienvenida1(name1):
    print(f"¡Bienvenido {name1}!")
nombre_persona1 = "Jose"

def cuadrado(un_numero):
    print(un_numero **2) #Playing to be something more than gods
un_numero = 5


#Return
#Lo que hace es devolver el resultado de la funcion y puedes almacenarlo en una variable
def ejem(nombre):
    return "Hola "+ nombre #Return te devuelve el valor y lo puedes almacenar en una variable

def multi(num1,num2):
    total = num1 * num2 #Return lo guarda para que puedas trabajar despues 
    return  total #Lo que se suele hacer es almacenarla en una variable

def potencia(num1,ex):
    resu = num1 ** ex
    return resu
num1 = 5
ex = 2

def usd_a_eur(dolares):
    conversi = dolares * 0.90
    print(f"Tienes {conversi} euros") #No se suele usar el (print) en los return
    return conversi #Guardo (conversi)
dolares = 1 
usd_a_eur(dolares) #Invocamos usd_a_eur

def invertir_palabra(palabra):
    inver = palabra[::-1].upper()
    print(inver)
    return inver
palabra ="Curso"
invertir_palabra(palabra)


#Funciones dinamicas

#Ejemplo:
def check_3_cifras(numero):
    return numero in range(100,1001)
resultado1 = check_3_cifras(65)
print(resultado1)

#otro un poco mas complejo
def rango_3_cifras(lista):
    for n in lista:
        if n in range(100,1001):
            return True
        else:
            pass
    return False

resultado2 = rango_3_cifras([555,99,6000])
print(resultado2)

lista_numeros = [3,5,6,-50,-500] #Definimos una lista de numeros
def todos_positivos(lista_numeros): #Creamos la funcion (todos_positivos) que trabaja con (lista_numeros)
    for numero in lista_numeros: #Le decimos que por cada numero in lista_numeros
        if numero < 0:           #Si numero es menor a 0
            return False         #Devuelve False
    else:                        #De lo contrario
        return True              #Devuelve True

