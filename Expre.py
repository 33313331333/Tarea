##
# 01 - Expresiones regulares
#

"""
Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda.
Se utilizan para la búsqueda de cadenas de texto, validacion de datos, etc.

¿Por qué aprender Regex?

Busqueda avanzada 

Validación de datos. Asegurarse que los datos que ingresa el ususario como el email, telefono, etc., son correctos.

Extracción de información. Permite obtener y aprovechar datos especificos de un texto, como nombres, fechas o direcciones.

Manipulación de texto. Extraer, reemplazar y modificar partes de la cadena de texto facilmente. 

"""

#1. Importar el modulo de expresiones regulares "re"
import re

#2. Crear un patron, que es una cadena de texto
# que describe lo que queremos encontrar.
pattern = "Hola"

#3. El texto donde queremos buscar
text = "Hola mundo"

#4. usar la funcion de búsqueda de "re"
result = re.search(pattern, text)

if result:
    print("He encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el patron
print(result.group())

# .start() devuelve la posicion inicial de la conincidencia 
print(result.start())

# .end() devuelve la posicion final de la coincidencia
print(result.end())

# Ejercicio 1
# Encuentra la primera ocurrencia de la palbra "IA" en el siguiente texto e indica en que posicion empieza y termina
# la coincidencia 

pattern = "IA"
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede fallar con las regex para ir con cuidado"
result = re.search(pattern, text)

if result:
    print(f"He encontrado el patrón en el texto en la posicion {result.start()} y termina en la posicion {result.end()}")
else:
    print("No he encontrado el patrón en el texto")

#------------------------------------------------------------------------------------------------------------

# Encontrar todas las coincidencias de un patron 
# .findall() Devulve una lista con todas la coincidencias

text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(matches)
print(len(matches))

# .finditer() Devuelve un iterador que contiene todos los resultados de la busqueda

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

### Modificadores 

# los modificadores son opciones que se pueden agregar a un patron para cambiar 
# su comportamiento

#re. IGNORECASE: Ignora las mayusculas y minusculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala.Viva la Ia"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

print(found)
###
# 02 - Metacarcteres 
# los metacaracteres son simbolos especiales con significados especificos en las expresiones generales
###

import re

#1. El punto (.)
# coincidir con cualquier caracter excepto una nueva linea

text = "El granjero salio de su casa con sus compañeros de caza para ir al bosque."
pattern = "ca.a"
found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No se ha encontrado el patron")
#Como uswar la barra invertida para anular el significado especial de un simbolo
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

#2.  \d: conincide con cualquier digito (0-9)

text = "Mi numero de telefono es 0984734678"
pattern = r"\d{10}"
found = re.findall(pattern, text)
print(found)

#3.  \w: coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "Hotorrinolaringologo_80"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

#4. \s Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)

text = "Hola mundo \n ¿como estas?\t"
pattern = r"\s"
found = re.findall(pattern, text)
print(found)

#5. ^: Coincide con el principio de una cadena
username = "423_Leonel122"
pattern = r"^\w"
valid = re.search(pattern, username)
if valid:
    print("El nombre de usuario es valido")
else:
    print("El numero de usario no es valido")

phone = "+52 767 108 5853"
pattern = r"^\+\d{1,3}"
valid = re.search(pattern, phone)
if valid:
    print("El telefono es valido")
else:
    print("El telefono no es valido")

# $: coincide con el final de una cadena 

text = "Hola mundo mundial"
pattern = r"mundo$"
valid = re.search(pattern, text)
if valid:
    print("La cadena es valido")
else:
    print("La cadena no es valido")

#Ejercicio: Valida un correo que sea del IT de Cd. Altamirano

#Ejercicio. Tenemos una lista de archivos que necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf leonel.webp secret.txt"

# 7. \b. Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"
valid = re.findall(pattern, text)
print(valid)

# |: coincidir con una accion u otra
frutas = "platano, piña, manzana, aguacate, pera, uva, durazno"
pattern = r"uva|p..a|\b\w{7}\b"
valid = re.findall(pattern, frutas)
print(valid)


#Ejercicios de Evaluacion

#Ejercicio: Valida un correo que sea del IT de Cd. Altamirano
correo = "L24930010@cdaltamirano.tecnm.mx"
pattern = r"^L\d{8}@cdaltamirano\.tecnm\.mx$"
valid = re.search(pattern, correo)
if valid:
    print("El correo es validado")
else:
    print("El correo es invalido")


#Ejercicio 2: Tenemos una lista de archivos que necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf leonel.webp secret.txt"
pattern = r"\b\w{1,100}\.txt\b"
valid = re.findall(pattern, files)
if valid:
    print("Ficheros txt.", (valid))
else:
    print("No hay ficheros txt")

#Ejercicio 3: Convinaciones de patrones
objetos = "Papel, Lápiz, Borrador, Pizarra, Computadora, Proyector, Pizarra digital, Pizarrón"
pattern = r"P\w{1,20}|\b\w{1,20}\b"
valid = re.findall(pattern, objetos)
print(valid)

