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

lista_numeros = [1,50,500,5000,750]
def suma_menores(lista_numeros): #definimos una funcion que opera con lista_numeros
    suma = 0
    for numero in lista_numeros: #Por cada numero en lista
        if numero > 0 and numero < 1000: #Si numero es mayor a 0 y menor a 1000
            suma += numero              #Suma los numeros
            print(suma)                 #He imprime
        else:                           #Si no entra en los parametros del if
            pass                        #Pasa de ese numero
    return suma                         #Y regresa a suma
suma_menores(lista_numeros)             #Invcamos a suma_menores

lista_numeros = [1,50,502,5000,755,600,33,61]
def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
            print(f"Cantidad de números pares: {cantidad}")
        else:
            pass
    return cantidad
cantidad_pares(lista_numeros)

#Ejemplo de funcion:
precios_cafe = [("capichino",1.5),("Expreso",1.2)]

def cafeo_mas_caro(precios_cafe):
    precio_mayor = 0
    cafe_nombre = ""
    for cafe,precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_nombre = cafe
        else: pass
    return (cafe_nombre,precio_mayor)
print(cafeo_mas_caro(precios_cafe))
cafeo_mas_caro(precios_cafe)

#Interaccion de funciones
#muchas funciones interactuando entre si, unsando su resultad como parametro diferente

from random import shuffle
#Lista inicial
palitos = ["-","--","---","----"]

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedirle intento
def probar_suerte():
    intento = []
    while intento not in ["1","2","3",]:
        intento = input("Elige un numero del 1 al 3: ")

    return int(intento)

#Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te a tocado {lista[intento]}")
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

#
from random import randint
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        # elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances" 
    else: return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
resultado1, resultado2 = lanzar_dados()
mensaje = evaluar_jugada(resultado1, resultado2)
print(mensaje)

lista_numeros = [1,2,15,7,2,8] #creamos una lista

def reducir_lista(lista): #Creamos una funcion que opere con lista
    lista = list(set(lista)) #A la lista la a transformar en un set para eliminar los duplicados y luego a lista
    lista.sort()             #A la lista la va a ordenar de menor a mayor
    lista.pop(-1)            #Eliminara el numero que se encuntre al final (mayor)
    return lista             #Regrese lista
    
def promedio(lista):         #Creamos la funcion promedio que opere con lista
    calcular_promedio = sum(lista)/len(lista)   #Sumara todos los valores de lista y los dividira por el cuantos sean
    return calcular_promedio

from random import choice #De la biblioteca (random) importa (Choice)
lista_numeros = [1,2,3,4,5,6,7] #Lista de num

def lanzar_moneda ():       #Creamos la funcion (lanzar_monedas())
    moneda_mia = ["Cruz","Cara"]    #Creamos una lista dentro de lanzar_monedas()
    return choice(moneda_mia)       #Elige un valor de moneda mia y regresalo

def probar_suerte(Rmoneda,listaNum):    #Crreamos la funcion probar_suerte(Rmoneda,listNum) Que opera con 2 valores
    if Rmoneda == "Cara":               #Si Rmoneda es igual a Cara
        print("La lista se autodestruirá")  #Imprime esto
        listaNum.clear() #Elimina la lista
        return listaNum  #Regresa la lista vacia
    
    else:                               #Si no se cumple lo anterior
        print("La lista fue salvada")   #Imprime esto
        return listaNum                 #Y regresa la lista

Resultado_moneda=lanzar_moneda()        #El resultado de lanzar_moneda() guardalo en Resultado_moneda
peru = probar_suerte(Resultado_moneda,lista_numeros)    #Probar_suerte() Operara con el Resultado_moneda y la lista_numeros
print(Resultado_moneda,peru) #Imprime ambos

#Argumentos indefenidos (*args)
#*Args (Arguments) Te permite definir funciones cuyo numero de argumentos sea variable
#Ejemplo:
def suma(*args): #*Args es god
    return sum(args)

print(suma(5,6,4))


def suma_cuadrados(*args):
    suma = 0
    for item in args:
        item = item**2
        suma += item
    return suma
print(suma_cuadrados(1,2,3))

def suma_absolutos(*args):
    suma = 0
    for item in args:
        suma += abs(item) #La funcion abs() convierte todos los valores negativos en positivos
    return suma
print(suma_absolutos(1,2,3,-1))

def numeros_persona(nombre,*args_num):
    suma_numeros = 0
    for num in args_num:
        suma_numeros += num
    return f"{nombre}, la suma de tus números es {suma_numeros}"
print(numeros_persona("Alan",1,2,3))

#Argumentos indefinidos(**kwargs)
#key word arguments Funcionaa con diccionarios para pasar valores y que haga algo con ese codigo
#Ejemplo:
def suma (**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
print(suma(x=3, y=5, z=2))

def cantidad_atributos(**kwargs):
    return len(kwargs)      #len te dira cuantas claves hay en tu dicconario
    
kwarg = {'color_ojos': 'azules', 'color_pelo':'rubio'} 
cantidad_atributos(**kwarg)

dic = {'color_ojos':'azules','color_pelo':'rubio'}
def lista_atributos(**keywords):
    return list(keywords.values()) #Values te dira los valores de cada clave y en forma de lista
    
print(lista_atributos(**dic))

def describir_persona(nombre,**kwargs):
    descripcion = f"Características de {nombre}:\n"
    for nombre_argumento,valor_argumento in kwargs.items():
        descripcion += f"{nombre_argumento}: {valor_argumento}\n"
    descripcion = descripcion.rstrip('\n') #Eliminamos el ultimo salto de linea
    return descripcion
    
nombre = "tomás"
Características = {"Color_ojos": "azules", "color_pelo": "rubio"}
resultado = describir_persona(nombre,**Características)
print(resultado)

