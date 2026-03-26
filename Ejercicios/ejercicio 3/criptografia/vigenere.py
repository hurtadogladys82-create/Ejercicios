def procesar_vigenere(texto, clave_palabra, modo):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ""
    clave_palabra = clave_palabra.lower()
    indice_clave = 0

    for letra in texto:
        es_mayuscula = letra.isupper()
        letra_min = letra.lower()

        if letra_min in alfabeto:
            posicion_texto = alfabeto.find(letra_min)
            # Buscamos cuánto vale la letra de la clave que toca usar
            letra_de_clave = clave_palabra[indice_clave % len(clave_palabra)]
            posicion_clave = alfabeto.find(letra_de_clave)

            if modo == "cifrar":
                nueva_posicion = (posicion_texto + posicion_clave) % 27
            else:
                nueva_posicion = (posicion_texto - posicion_clave) % 27

            nueva_letra = alfabeto[nueva_posicion]
            resultado += nueva_letra.upper() if es_mayuscula else nueva_letra
            
            indice_clave += 1 # Solo avanzamos la clave si usamos una letra
        else:
            resultado += letra
    return resultado