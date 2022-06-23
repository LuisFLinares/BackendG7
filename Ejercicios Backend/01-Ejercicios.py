# ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
# for numero in range(5):
#     print(numero, end="")


# EJERCICIO 1
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
altura = int(input("Ingrese la altura del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))

for h in range (1,altura +1):
    for w in range (1,ancho +1):
        print('*',end="")
    print("")

# EJERCICIO 2
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
thickness = int(input('Ingrese el grosor: '))

heigh = thickness + 2*(thickness-1)
row = thickness
space= thickness-1 #3

for i in range(1,heigh+1): 
    if(i < thickness):
        print(" "*space,end="")
        for j in range(row):
            print("*",end="")
        row+=2
        space-=1
    if(i >=thickness and i<= (thickness+ thickness-1 )):
        for j in range(row):
            print("*",end="")
        space=0        
    if(i >(thickness+ thickness-1 )):
        row-=2
        space+=1
        print(" "*space,end="")
        for j in range(row):
            print("*",end="")        
    print()

# EJERCICIO 3
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *
n= int(input("tamaño del triangulo: "))
triangulo = n


for i in range(n,0,-1):
    for j in range(0,i,1):
        print("*",end="")
      
    print()

# EJERCICIO 4
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12


# EJERCICIO 5
# si el texto de ingreso es:
texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]
# Hacer el codigo para ello


# EJERCICIO 6
# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'


# EJERCICIO 7
# dado los siguientes numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1