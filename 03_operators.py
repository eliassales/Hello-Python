### Operadores ###

### Operadores numericos ###
print("Suma:", 3 + 4)
print("Resta:", 3 - 4)
print("Multiplicacion:", 3 * 4)
print("Division:", 14 / 3)
print("Modulo:", 14 % 3)
print("Floor Division:", 14 // 3) # redondea para abajo al entero mas cercano
print("Exponente:", 2 ** 3)

# Operadores con cadenas
print("Hola " + "Python " + "¿Que tal?") # concatenar cadenas de texto
#print("Hola" - "Python") # da error por operando no soportado
#print("Hola" + 5) # da error por mezclar tipos de datos
print("Hola " + str(5)) # aca al convertirlo a string no hay problema

# el multiplo debe ser un valor entero, porque sino da error
print("Gol " * 3) # multiplica la cadena por el valor correspondiente
print("Gol " * (2 ** 3)) # multiplica la cadena por el valor correspondiente

### Operadores de Comparacion ###
print("Mayor:", 3 > 4)
print("Menor:", 3 < 4)
print("Mayor igual:", 3 >= 4)
print("Menor igual:", 3 <= 4)
print("Igual:", 3 == 4)
print("Distinto:", 3 != 4)

# para todos los casos lo que se compara es un orden alfabetico por ASCII
print("Mayor:", "Hola" > "Pyton")
print("Menor:", "Hola" < "Pyton")
print("Mayor igual:", "Hola" >= "Pyton") # false
print("Mayor igual:", "Hola" >= "Bola") # true
print("Mayor igual:", "Hola" >= "Sola") # false
print("Menor igual:", "Hola" <= "Pyton")
print("Igual:", "Hola" == "Pyton")
print("Distinto:", "Hola" != "Pyton")

### Operadores Logicos ###
print(3 > 4 and "Hola" > "Pyton") 
print(5 > 4 and "Hola" < "Pyton") # con 'and' ambos true para true, el resto false
print(3 > 4 or "Hola" > "Pyton") # con 'or' ambos false para false, el resto true
print(3 > 4 or "Hola" < "Pyton")
print(3 < 4)
print(not(3 < 4)) # con 'not' se invierte el valor, true pasa a false y viceversa

