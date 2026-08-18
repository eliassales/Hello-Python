### Strings ###

my_string = "Mi valor string"
my_other_string = 'Mi otro valor'
my_new_line_string = "Este es un string \n con salto de linea" # string con un salto de linea
my_tab_string = "Este es un string \t con salto de linea" # string con tabulacion

print(my_string)
print(my_other_string)
print(my_new_line_string)
print(my_tab_string)

### Operaciones ###

# para calcular longitud
print(len(my_string))
print(len(my_other_string))

# concatenar strings
print(my_string + " " + my_other_string)

# escapar string
my_scape_string = "'\\tEste es un String \\n escapado" # una \ antes de los caracteres especiales los escapa, es decir \n con \\n.
print(my_scape_string)

# formatear
name="Elias"
lastname="Apellido"
age=39

my_format_string = f"Mi nombre es {name} {lastname} y mi edad es {age} años" # esta es por inferencia, y desde mi punto las mas legible y mejor
print(my_format_string)
my_format_string = "Mi nombre es %s %s y mi edad es %d años" %(name, lastname, age) # permite formatear con tipo de dato, por ej sin age pasamos un string da un error.
print(my_format_string)
my_format_string = "Mi nombre es {} {} y mi edad es {} años".format(name, lastname, age) # otra forma de inferencia menos directa
print(my_format_string)

# desempaquetado de caracteres
language = "Python"
#a, b = language # da error porque no coinciden las variables creadas con los caracteres que tiene Python
a, b, c, d, e, f = language #aca no da error porque coincide la cantidad de caractere
print(a)
print(f)

# division
language_slice = language[1:3] 
print(language_slice) # muestra yt
language_slice = language[1:] 
print(language_slice) # omite el 1 en este caso y muestra el resto: ython
language_slice = language[-2] 
print(language_slice) # muestra la 'o' porque arranca del final al principio
language_slice = language[::-1] 
print(language_slice) # muestra al reves la cadena: nohtyP
language_slice = language[0:6:2] 
print(language_slice) # muestra Pto

language = "python es un Lenguaje"
# capitalize
print(language.capitalize()) # mayuscula primer caracter cadena

# upper
print(language.upper()) # en mayuscula todo

# lower
print(language.lower()) # en minuscula todo

# count
print(language.count("n")) # cuantas veces esta el caracter "n"

# isnumercic
print(language.isnumeric()) # comprueba si la variable tiene un valor numerico
print("3".isnumeric())

# isupper
print(language.isupper()) #comprueba si todos los caracteres estan en mayusculas
print(language.lower().isupper())
print(language.upper().isupper())

# title
print(language.title()) # pone en mayuscula el primer caracter de cada palabra

# starswith
print(language.startswith("py")) # permite verificar si empieza con los caracteres indicados
print(language.startswith("Py")) # false, porque p minuscula no es lo mismo que p en mayuscula

