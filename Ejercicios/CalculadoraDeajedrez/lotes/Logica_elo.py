class JugadorNoEncontradoError(Exception):
    pass
jugadores_db = {} # Diccionario para almacenar jugadores y sus puntos Elo
historial_partidas = []  # Lista para almacenar el historial de partidas
def calcular_nuevo_elo(jugador_a, jugador_b, resultado_a):
    k = 32  # Factor de ajuste, comúnmente utilizado en el sistema de Elo
    probabilidad_a = 1 / (1 + 10 ** ((jugador_b - jugador_a) / 400)) # Formula Expectativa
    ajuste = k * (resultado_a - probabilidad_a) # Retornamos cuánto se debe sumar o restar
    return round(ajuste)

def procesar_lote(lote_de_partidas):

    for i, linea in enumerate(lote_de_partidas, 1):
        try:
            # Separamos por el carácter solicitado '|'
            partes = [p.strip() for p in linea.split('|')]
            if len(partes) != 3:
                raise ValueError("Formato incorrecto. Debe ser: JugadorA | JugadorB | Resultado")

            j_a, j_b, res_str = partes

            # Buscador de registros en memoria
            if j_a not in jugadores_db or j_b not in jugadores_db:
                raise JugadorNoEncontradoError(f"Jugador '{j_a}' o '{j_b}' no existe.")

            # Manejo de resultado (1, 0, o 1/2)
            res_a = 0.5 if res_str == "1/2" else float(res_str)

            # Aplicar cambio
            cambio = calcular_nuevo_elo(jugadores_db[j_a], jugadores_db[j_b], res_a)
            jugadores_db[j_a] += cambio
            jugadores_db[j_b] -= cambio
            
            historial_partidas.append(linea)  # Guardar en historial
            print(f"  > Partida {i}: {j_a} vs {j_b} [PROCESADA]")

        except Exception as e:
            # Requerimiento: Registrar error pero continuar con el resto
            print(f"  > Error en línea {i}: {e}") # Asegúrate de cerrar con 'e}')
