""""
Esta es la forma de documentar en python
"""

"""
alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Proporcione el ancho del rectangulo: "))

area = alto * ancho

perimetro = (alto * ancho) * 2

print("El perimetro es: ", perimetro)
print("El area es: ", area)
"""
"""
miVariable = 10
print(miVariable)

#Operadores de reasignacion
miVariable = miVariable + 1
print(miVariable)

#Sintaxis mas resumida
miVariable += 1
print(miVariable)

#miVariable = miVariable - 2
miVariable -= 2
print(miVariable)

#miVariable = miVariable * 3
miVariable *= 3
print(miVariable)

#miVariable = miVariable / 2
miVariable /= 2
print(miVariable)

#operadores de comparacion

d = 4
b= 2
resultado = d == b #comprobamos si son iguales
print(resultado)

resultado = d != b #comprobamos si son iguales
print(resultado)

resultado = d > b #comprobamos si son iguales
print(resultado)

resultado = d < b #comprobamos si son iguales
print(resultado)

resultado = d <= b #comprobamos si son iguales
print(resultado)

resultado = d >= b #comprobamos si son iguales
print(resultado)"""
# ejercico numero para o impar
""""
numero = int(input("Ingrese un numero: "))
#f significa format. Sirve para cambiarle el formato al valor entre {} una vez resulto.
print(f"El residuo de la division es: {numero % 2}")
if numero % 2 == 0:
    print(f"El numero {numero} ingresado es PAR")
else:
    print(f"El numero {numero} ingresado es IMPAR")
"""
'''
edadAdulto = 18
edad = int(input("Ingrese su edad: "))
print(f"Su edad es {edad}")
if edad >= edadAdulto:
    print(f"Su edad es {edad}, usted ES mayor de edad")
else:
    print(f"Su edad es {edad}, usted NO ES mayor de edad")
'''
# Ejercicio valor dentro del rango
'''
valor = int(input("Ingrese un valor: "))
valorMin = 0
valorMax = 5
resultado = valorMin <= valor and valorMax >= valor
if resultado:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")
'''
'''
#Ejercio con el operador or, not
vacaciones = False
diaDescanso = True

if not(vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene tarabajo que hacer")
'''
# Ejercicio rango
'''
edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)
if veinte or treinta:
    if treinta:
        print("La edad está dentro del rango de los (30´0) años")
    elif veinte:
        print("La edad está dentro del rango de los (20´0) años")
else:
    print("La edad no está dentro del rango de los (20´0) a (30´0) años")
'''
'''
edad = int(input("Ingrese la edad: "))

if (20 <= edad < 30) or (30 <= edad < 40):
    print("Estas dentro del rango de los 20 o 30 años")
else:
    print("no estas dentro del rango de los 20 o 30 años")
'''
# El mayor de dos numero
# numero1 = int(input("Digite el valor para el numero1: "))
# numero2 = int(input("Digite el valor para el numero2: "))
'''
if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
elif numero1 < numero2:
    print(f"El numero mayor es: {numero2}")
elif numero1 == numero2:
    print("Los numeros son iguales")
'''


class TiendaLibro:
    def __init__(self, nombre, idLibro, precio, envio):  # constructor
        self.nombre = nombre  # self. esta haciendo la variable publica
        self.idLibro = idLibro
        self.precio = precio
        self.envio = envio

    def operacionesValores(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.idLibro}")
        print(f"Precio: ${self.precio}")
        if self.envio == 0:
            print(f"El envio es gratuito")
        else:
            print(f"El coste del envio es: ${self.envio}")


nombreEnter = input("Ingrese el nombre del libro: ")
idEnter = input("Ingrese el id del libro: ")
precio = float(input("Ingrese el precio del libro: "))
envio = float(input("Ingrese el precio del envio del libro: "))

llamarClase = TiendaLibro(nombreEnter, idEnter, precio, envio)

llamarClase.operacionesValores()