### Variables ###

# Se debe respetar el formato 'snake case' (todo minuscula y guiones bajos)

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Permite mostrar diferentes datos en una sola sentencia
print(my_string_variable, my_int_variable, my_bool_variable)
print("El valor de int es:", my_int_variable)

my_int_var = 8
print(my_int_var)
my_int_to_str_var = str(my_int_var) # sirve para convertir un valor numerico a string
print(my_int_to_str_var)
print(type(my_int_to_str_var))

# Algunas funciones del sistema
print(len(my_string_variable)) # cuenta los caracteres de la cadena

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, lastname, age, use_glases = "Elias", "Sales", 39, True
print("Mi nombre es:", name, "Mi apellido es:", lastname, "Tengo la edad de:", age, "Uso lentes:", use_glases)

# Input para poder ingresar valores a variables
"""
name = input("Cual es tu nombre?: ")
print("Nombre:", name)
"""

# Forzamos el tipo de dato con ": str"
address: str = "Mi dirección"
#address = 32 # Esto da un error en el interprete, pero en tiempo de ejecucion cambia el valor de address de str a int
print(address)
print(type(address))
