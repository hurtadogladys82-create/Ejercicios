def procesar_cesar(texto, clave, modo):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ""
    
    # Si vamos a descifrar, restamos la clave en lugar de sumarla
    if modo == "descifrar":
        clave = -clave

    for letra in texto:
        es_mayuscula = letra.isupper()
        letra_min = letra.lower()

        if letra_min in alfabeto:
            posicion_actual = alfabeto.find(letra_min)
            # Aplicamos el movimiento y el "reloj" de 27 letras
            nueva_posicion = (posicion_actual + clave) % 27
            nueva_letra = alfabeto[nueva_posicion]
            
            resultado += nueva_letra.upper() if es_mayuscula else nueva_letra
        else:
            resultado += letra # Si no es letra (espacio, número), se queda igual
    return resultado
