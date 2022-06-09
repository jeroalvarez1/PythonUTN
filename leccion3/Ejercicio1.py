#Ejer1
    #Escribir la siguientes expresion en forma de expresion algoritmina: (a3 * (b2 - 2ac))/2 b .Pedirle al usario que ingrese los valores y luego mostrarlos por pantalla
a = float(input("Ingrese el valor de 'a': "))
b = float(input("Ingrese el valor de 'b': "))
c = float(input("Ingrese el valor de 'c': "))
res = ((a ** 3) * ((b ** 2)-(2 * a * c))) / (2 * b)
print(f'El resultado es: {res}')