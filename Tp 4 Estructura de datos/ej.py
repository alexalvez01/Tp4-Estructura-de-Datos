pokemones=[
    {
        "numero": 1,
        "nombre": "Bulbasaur",
        "nivel": 5,
        "tipo": ["Planta", "Veneno"]
    },
    {
        "numero": 4,
        "nombre": "Charmander",
        "nivel": 5,
        "tipo": ["Fuego"]
    },
    {
        "numero": 7,
        "nombre": "Squirtle",
        "nivel": 5,
        "tipo": ["Agua"]
    },
    {
        "numero": 25,
        "nombre": "Pikachu",
        "nivel": 5,
        "tipo": ["Eléctrico"]
    },
    {
        "numero": 39,
        "nombre": "Jigglypuff",
        "nivel": 10,
        "tipo": ["Normal", "Hada"]
    },
    {
        "numero": 52,
        "nombre": "Meowth",
        "nivel": 12,
        "tipo": ["Normal"]
    },
    {
        "numero": 94,
        "nombre": "Gengar",
        "nivel": 25,
        "tipo": ["Fantasma", "Veneno"]
    },
    {
        "numero": 133,
        "nombre": "Eevee",
        "nivel": 7,
        "tipo": ["Normal"]
    },
    {
        "numero": 150,
        "nombre": "Mewtwo",
        "nivel": 70,
        "tipo": ["Psíquico"]
    },
    {
        "numero": 151,
        "nombre": "Mew",
        "nivel": 50,
        "tipo": ["Psíquico"]
    }

]

def hash_tipo(dato):
    return dato["tipo"]
def hash_digito(dato):
    return str(dato["numero"])[-1]
def hash_nivel(dato):
    return dato["nivel"] // 10

tabla_por_tipo={}
tabla_por_numero={}
tabla_por_nivel={}

def agregar_pokemon(pokemon):
   
    clave_tipo = hash_tipo(pokemon)
    for tipo in clave_tipo:
        if tipo not in tabla_por_tipo:
            tabla_por_tipo[tipo] = []
        tabla_por_tipo[tipo].append(pokemon)
    
    
    clave_digito = hash_digito(pokemon)
    if clave_digito not in tabla_por_numero:
        tabla_por_numero[clave_digito] = []
    tabla_por_numero[clave_digito].append(pokemon)
    
    
    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_por_nivel:
        tabla_por_nivel[clave_nivel] = []
    tabla_por_nivel[clave_nivel].append(pokemon)


for pokemon in pokemones:
    agregar_pokemon(pokemon)
    
    
def pokemones_por_ultimo_digito(digitos):
    resultado = []
    for digito in digitos:
        resultado.extend(tabla_por_numero.get(digito, []))
    return resultado
def pokemones_por_multiplos(multiples):
    resultado = []
    for pokemon in pokemones:
        for multiple in multiples:
            if pokemon["nivel"] % multiple == 0:
                resultado.append(pokemon)
                break
    return resultado
def pokemones_por_tipo(tipos):
    resultado = []
    for tipo in tipos:
        resultado.extend(tabla_por_tipo.get(tipo, []))
    return resultado

nuevo_pokemon = {
    "numero": 200,
    "nombre": "Steelix",
    "nivel": 40,
    "tipo": ["Acero", "Tierra"]
}

agregar_pokemon(nuevo_pokemon)

print("Pokémon cuyos números terminan en 3, 7 y 9:")
resultados_ultimo_digito = pokemones_por_ultimo_digito(['3', '7', '9'])
for pokemon in resultados_ultimo_digito:
    print(pokemon["nombre"])

print("\nPokémon cuyos niveles son múltiplos de 2, 5 y 10:")
resultados_multiplos = pokemones_por_multiplos([2, 5, 10])
for pokemon in resultados_multiplos:
    print(pokemon["nombre"])

print("\nPokémon de los tipos Acero, Fuego, Eléctrico, Hielo:")
resultados_tipo = pokemones_por_tipo(["Acero", "Fuego", "Eléctrico", "Hielo"])
for pokemon in resultados_tipo:
    print(pokemon["nombre"])