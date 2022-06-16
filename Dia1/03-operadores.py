# Operadores Aritmeticos 

edad_juan = 40
edad_maria = 34

# SUMA
print(edad_juan + edad_maria)

# RESTA
print(edad_juan - edad_maria)

# MULTIPLICACION
print(edad_juan * edad_maria)

# DIVISION 
print(edad_juan / edad_maria)

# MODULO
print(edad_juan % edad_maria)

# COCIENTE
print(edad_juan // edad_maria)

# POTENCIA 
print(edad_juan ** 1 )

# En el caso de los String 
# cuando hacemos una sumatoria en los String se hara una concatenacion
mes = 'Junio'
temporada = 'Invierno'
print(mes + temporada)
# y si hacemos uso de la multiplicacion hara que se repita N cantidad de veces 
print(mes * 5)

# -----------------------------------------------------------------------------------

# Operadores Comporacion 
edad_Luis = 15
edad_martha = 30

# > Mayor que
print(edad_Luis > edad_martha)

# < Menor que 
print(edad_Luis < edad_martha)

# == igual que 
print(edad_Luis == edad_martha)

# != Diferente que 
print(edad_Luis >= edad_martha)

# >= Mayor o igual que 
print(edad_Luis >= edad_martha)

# <= menos o igual que 
print(edad_Luis <= edad_martha)

# Operadores Logicos
edad_luis = 15
edad_martha = 30 
# and Y > basta con una de las dos codiciones sea F para que todo sea F
print(edad_luis > 18 and edad_luis > edad_martha)

#or O > basta con que una sea V para que todo sea V
print(edad_luis > 18 or edad_luis > edad_martha)
# not NO >invierte el resultado
print(not edad_luis > 50)


# Ejercicios
edad_eduardo= 18
edad_renato = 26
edad_laura = 35


# Como saber si eduardo es mayor de edad
print(edad_eduardo >= 18)

# Como saber si eduardo es mayor que laura
print(edad_eduardo >  edad_laura)

# Como saber si renato es menor que laura pero mayor que eduardo
print(edad_renato < edad_laura and edad_renato > edad_eduardo)

# como saber si laura puede ser mayor que renato o menor que eduardo
print(edad_laura > edad_renato  or edad_laura < edad_eduardo)

# Operadores de Asignacion
# = Asignacion 
edad = 50

# += incremento
edad += 1 #edad++

#-= decremento 
edad -= 1 #edad--

# *= multiplicador
edad *= 1 

# /= division
edad /= 2 