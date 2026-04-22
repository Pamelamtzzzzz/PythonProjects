API_KEY = "3c969dd7"   # sustituimos por la clave que recibimos

import httpx

API_KEY = "TU_CLAVE_AQUI"
URL_BASE = "http://www.omdbapi.com/"

# Hacemos la petición pasando los parámetros como un diccionario
parametros = {
    "apikey": API_KEY,
    "t": "Matrix"
}

respuesta = httpx.get(URL_BASE, params=parametros)

print(respuesta.status_code)   # 200 si todo bien
print(respuesta.text)           # la respuesta como texto (JSON sin parsear)


import httpx

API_KEY = "TU_CLAVE_AQUI"
URL_BASE = "http://www.omdbapi.com/"

parametros = {
    "apikey": API_KEY,
    "t": "Matrix"
}

respuesta = httpx.get(URL_BASE, params=parametros)

# El método .json() parsea el texto y devuelve un dict (o list, según el JSON)
datos = respuesta.json()

print(type(datos))   # <class 'dict'>
print(datos)

import httpx

API_KEY = "TU_CLAVE_AQUI"
URL_BASE = "http://www.omdbapi.com/"

parametros = {"apikey": API_KEY, "t": "Matrix"}

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

print(f"Título: {datos['Title']}")
print(f"Año: {datos['Year']}")
print(f"Director: {datos['Director']}")
print(f"Género: {datos['Genre']}")
print(f"Duración: {datos['Runtime']}")
print(f"Puntuación IMDb: {datos['imdbRating']}")
print(f"Sinopsis: {datos['Plot']}")

import httpx

API_KEY = "TU_CLAVE_AQUI"
URL_BASE = "http://www.omdbapi.com/"

parametros = {"apikey": API_KEY, "t": "Matrix"}

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

print(f"Título: {datos['Title']}")
print(f"Año: {datos['Year']}")
print(f"Director: {datos['Director']}")
print(f"Género: {datos['Genre']}")
print(f"Duración: {datos['Runtime']}")
print(f"Puntuación IMDb: {datos['imdbRating']}")
print(f"Sinopsis: {datos['Plot']}")

parametros = {"apikey": API_KEY, "t": "PeliculaQueNoExiste12345"}

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

print(respuesta.status_code)   # 200 (OK a nivel HTTP)
print(datos)

parametros = {"apikey": API_KEY, "t": "PeliculaQueNoExiste12345"}

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

if datos.get("Response") == "True":
    print(f"Título: {datos['Title']}")
    print(f"Año: {datos['Year']}")
else:
    print(f"Error: {datos.get('Error')}")


parametros = {"apikey": API_KEY, "i": "tt0133093"}   # ID de The Matrix

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

print(f"Por ID: {datos['Title']} ({datos['Year']})")

parametros = {"apikey": API_KEY, "s": "Matrix"}

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

print(datos)

parametros = {"apikey": API_KEY, "s": "Matrix"}

respuesta = httpx.get(URL_BASE, params=parametros)
datos = respuesta.json()

if datos.get("Response") == "True":
    print(f"Encontrados {datos['totalResults']} resultados (mostrando primera página):")
    for pelicula in datos["Search"]:
        print(f"  {pelicula['Year']} - {pelicula['Title']} (ID: {pelicula['imdbID']})")
else:
    print("No se han encontrado resultados")

import httpx

API_KEY = "TU_CLAVE_AQUI"
URL_BASE = "http://www.omdbapi.com/"


def buscar_pelicula_por_titulo(titulo):
    parametros = {"apikey": API_KEY, "t": titulo}
    respuesta = httpx.get(URL_BASE, params=parametros)
    datos = respuesta.json()

    if datos.get("Response") == "True":
        return datos
    else:
        return None


# Probamos la función
pelicula = buscar_pelicula_por_titulo("Inception")

if pelicula is not None:
    print(f"Título: {pelicula['Title']}")
    print(f"Año: {pelicula['Year']}")
    print(f"Director: {pelicula['Director']}")
    print(f"Puntuación: {pelicula['imdbRating']}")
else:
    print("Película no encontrada")

titulos = ["Inception", "The Godfather", "NoExistePelicula", "Pulp Fiction"]

for titulo in titulos:
    print(f"\n--- Buscando: {titulo} ---")
    pelicula = buscar_pelicula_por_titulo(titulo)

    if pelicula is not None:
        print(f"  {pelicula['Title']} ({pelicula['Year']}) - {pelicula['imdbRating']}")
    else:
        print(f"  No encontrada")

import httpx

# GET con parámetros
respuesta = httpx.get("https://api.ejemplo.com/endpoint", params={"k1": "v1", "k2": "v2"})

# Estado HTTP
respuesta.status_code   # 200, 404, 500...

# Cuerpo como texto
respuesta.text

# Cuerpo como diccionario (parseando JSON)
datos = respuesta.json()

# Doble nivel de comprobación en APIs tipo OMDb
if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos.get("Response") == "True":
        # usar datos
        pass