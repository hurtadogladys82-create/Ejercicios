def obtener_promedio(participantes):
    """Calcula el total y el promedio por persona."""
    cantidad = len(participantes)

    # Manejo de error
    if cantidad == 0:
        raise ValueError("No hay participantes")

    total_gastado = sum(participantes.values())
    promedio = total_gastado / cantidad
    return total_gastado, promedio

def calcular_balances(participantes, promedio):
    """Calcula cuánto debe poner o recibir cada uno."""
    balances = {}
    for nombre, pago in participantes.items():
        balances[nombre] = pago - promedio
    return balances