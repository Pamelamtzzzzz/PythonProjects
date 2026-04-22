ventas = [
    {"titulo": "El nombre del viento", "autor": "Patrick Rothfuss", "precio": 22.50, "unidades": 45, "categoria": "fantasia"},
    {"titulo": "Sapiens", "autor": "Yuval Noah Harari", "precio": 19.90, "unidades": 120, "categoria": "ensayo"},
    {"titulo": "1984", "autor": "George Orwell", "precio": 12.00, "unidades": 80, "categoria": "ficcion"},
    {"titulo": "La chica del tren", "autor": "Paula Hawkins", "precio": 15.50, "unidades": 30, "categoria": "ficcion"},
    {"titulo": "Breves respuestas", "autor": "Stephen Hawking", "precio": 18.00, "unidades": 60, "categoria": "ensayo"},
    {"titulo": "Dune", "autor": "Frank Herbert", "precio": 24.00, "unidades": 90, "categoria": "fantasia"},
    {"titulo": "El cuento de la criada", "autor": "Margaret Atwood", "precio": 16.50, "unidades": 55, "categoria": "ficcion"},
    {"titulo": "Homo Deus", "autor": "Yuval Noah Harari", "precio": 21.00, "unidades": 40, "categoria": "ensayo"},
    {"titulo": "El Hobbit", "autor": "J.R.R. Tolkien", "precio": 14.00, "unidades": 150, "categoria": "fantasia"},
    {"titulo": "Pequeñas grandes cosas", "autor": "Jodi Picoult", "precio": 17.50, "unidades": 25, "categoria": "ficcion"},
]

#lista de titulos
lista_titulos = list(map(lambda libro: libro["titulo"],ventas))
print(lista_titulos)

#libros baratos
libros_baratos = list(filter(lambda libro: libro["precio"]<=16,ventas))
print(libros_baratos)

#libros caros
libros_caros = filter(lambda libro: libro["precio"]> 20,ventas)
transformando_titulos = list(map(lambda libro: libro["titulo"], libros_caros))
print(transformando_titulos)

#libros ordenados 
libros_ordenados = sorted(ventas, key=lambda libro: libro["precio"], reverse= True)
imprimir_lista = map(lambda libro: libro["titulo"], libros_ordenados)
print(list(imprimir_lista))

#Top 3 libros vendidos 
top_tres = sorted(ventas, key=lambda libro: libro["unidades"], reverse = True)
imprimir_top = list(map(lambda libro: libro["titulo"], top_tres))
imprimir_toptres = print(imprimir_top[:3])