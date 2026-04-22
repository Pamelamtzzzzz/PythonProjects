#Parte 1: ITERACIONES
#############################################
# Todo esto son iterables
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
diccionario = {"a": 1, "b": 2}
cadena = "hola"
rango = range(5)

# Todos soportan for
for x in lista:
    print(x)

for caracter in cadena:
    print(caracter)


numeros = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numeros))        # 8    número de elementos
print(sum(numeros))        # 31   suma total
print(max(numeros))        # 9    máximo
print(min(numeros))        # 1    mínimo
print(sorted(numeros))     # [1, 1, 2, 3, 4, 5, 6, 9]  copia ordenada

# Las mismas funciones sobre una tupla
print(sum((10, 20, 30)))   # 60

# O sobre un conjunto
print(max({5, 2, 8}))      # 8

r = range(1_000_000)

print(type(r))        # <class 'range'>
print(len(r))         # 1000000   sí, tiene longitud
print(r[0])           # 0         sí, soporta índice
print(sum(r))         # 499999500000

# Para verlo como lista explícita, lo convertimos
pequenos = list(range(5))
print(pequenos)       # [0, 1, 2, 3, 4]

nombres = ["Ana", "Luis", "María"]

# enumerate
for i, nombre in enumerate(nombres):
    print(f"{i}: {nombre}")

# zip
edades = [30, 25, 40]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Los podemos convertir a lista si queremos verlos "todos de golpe"
print(list(enumerate(nombres)))   # [(0, 'Ana'), (1, 'Luis'), (2, 'María')]
print(list(zip(nombres, edades))) # [('Ana', 30), ('Luis', 25), ('María', 40)]

#######################################################################################

#PARTE 2: LAMBDAS

###########################################################################################
# Versión normal
def doblar(x):
    return x * 2

print(doblar(5))    # 10


# Versión lambda equivalente
doblar_lambda = lambda x: x * 2

print(doblar_lambda(5))    # 10

# Dos parámetros
sumar = lambda a, b: a + b
print(sumar(3, 4))    # 7

# Sin parámetros
saludo = lambda: "Hola"
print(saludo())       # Hola

# MAL: no aporta nada frente a def normal
calcular = lambda precio, iva: precio * (1 + iva / 100) if iva > 0 else precio
# BIEN: pasamos una lambda porque es trivial y de un solo uso
precios = [100, 200, 300]
con_iva = list(map(lambda p: p * 1.21, precios))

numeros = [1, 2, 3, 4, 5]

# map devuelve un iterable perezoso, lo convertimos a lista para verlo
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)          # [2, 4, 6, 8, 10]

# Otro ejemplo: pasar cadenas a mayúsculas
nombres = ["ana", "luis", "maría"]
mayus = list(map(lambda s: s.upper(), nombres))
print(mayus)           # ['ANA', 'LUIS', 'MARÍA']

# Calcular la longitud de cada cadena
longitudes = list(map(lambda s: len(s), nombres))
print(longitudes)      # [3, 4, 5]


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solo los pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)           # [2, 4, 6, 8, 10]

# Solo los mayores que 5
grandes = list(filter(lambda x: x > 5, numeros))
print(grandes)         # [6, 7, 8, 9, 10]

# Filtrar nombres que empiezan por vocal
nombres = ["ana", "luis", "maría", "carlos", "elena"]
vocales = {"a", "e", "i", "o", "u"}
por_vocal = list(filter(lambda n: n[0] in vocales, nombres))
print(por_vocal)       # ['ana', 'elena']



palabras = ["pera", "manzana", "uva", "sandía"]

# Orden alfabético (por defecto)
print(sorted(palabras))
# ['manzana', 'pera', 'sandía', 'uva']

# Ordenar por LONGITUD
print(sorted(palabras, key=lambda p: len(p)))
# ['uva', 'pera', 'sandía', 'manzana']

# Ordenar por longitud descendente
print(sorted(palabras, key=lambda p: len(p), reverse=True))
# ['manzana', 'sandía', 'pera', 'uva']

#Ordenación por campo cuando los elementos son estructurados:

# Lista de tuplas (nombre, edad, salario)
empleados = [
    ("Ana", 30, 35000),
    ("Luis", 25, 28000),
    ("María", 40, 42000),
    ("Carlos", 28, 31000),
]

# Ordenar por edad (índice 1 de la tupla)
por_edad = sorted(empleados, key=lambda e: e[1])
print(por_edad)

# Ordenar por salario descendente
por_salario = sorted(empleados, key=lambda e: e[2], reverse=True)
print(por_salario)

#Ordenación de diccionarios por un campo:

empleados = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "María", "edad": 40},
]

# Por edad
por_edad = sorted(empleados, key=lambda e: e["edad"])
print(por_edad)

# Por nombre alfabético
por_nombre = sorted(empleados, key=lambda e: e["nombre"])
print(por_nombre)

#Max y Min tambien aceptan key
empleados = [
    ("Ana", 30, 35000),
    ("Luis", 25, 28000),
    ("María", 40, 42000),
    ("Carlos", 28, 31000),
]

# El empleado con MAYOR salario
mejor_pagado = max(empleados, key=lambda e: e[2])
print(mejor_pagado)      # ('María', 40, 42000)

# El más joven
mas_joven = min(empleados, key=lambda e: e[1])
print(mas_joven)         # ('Luis', 25, 28000)

# La palabra más larga de una lista
palabras = ["pera", "manzana", "uva", "sandía"]
print(max(palabras, key=lambda p: len(p)))   # manzana

#ENCADENAR OPERACIONES 
empleados = [
    {"nombre": "Ana", "depto": "Ventas", "salario": 35000},
    {"nombre": "Luis", "depto": "IT", "salario": 28000},
    {"nombre": "María", "depto": "IT", "salario": 42000},
    {"nombre": "Carlos", "depto": "Ventas", "salario": 31000},
    {"nombre": "Elena", "depto": "IT", "salario": 55000},
]

# Paso 1: filtrar los de IT
it = filter(lambda e: e["depto"] == "IT", empleados)

# Paso 2: ordenar por salario descendente
it_ordenados = sorted(it, key=lambda e: e["salario"], reverse=True)

# Resultado
for empleado in it_ordenados:
    print(f"{empleado['nombre']}: {empleado['salario']}€")


#ATAJOS UTILES:

from operator import itemgetter

empleados = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
]

# Estas dos líneas son equivalentes
por_edad_lambda = sorted(empleados, key=lambda e: e["edad"])
por_edad_getter = sorted(empleados, key=itemgetter("edad"))

print(por_edad_lambda == por_edad_getter)   # True

#CHULETA
# Iterables :: cualquier cosa que acepte for
for x in iterable: ...

# Funciones que aceptan iterables
len(iterable)
sum(iterable)
max(iterable)
min(iterable)
sorted(iterable)
list(iterable)        # convertir a lista

# Lambdas
lambda: expresion                  # sin parámetros
lambda x: expresion                # un parámetro
lambda a, b: expresion             # varios parámetros

# Combinación iterable + lambda
map(funcion, iterable)             # transformar cada elemento
filter(funcion, iterable)          # seleccionar elementos
sorted(iterable, key=funcion)      # ordenar por criterio
sorted(iterable, key=funcion, reverse=True)
max(iterable, key=funcion)         # máximo según criterio
min(iterable, key=funcion)         # mínimo según criterio

# Convertir el resultado perezoso a lista
list(map(lambda x: x * 2, numeros))
list(filter(lambda x: x > 0, numeros))