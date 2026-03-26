class ProductoAgotadoError(Exception): pass
class SaldoInsuficienteError(Exception): pass
class DenominacionInvalidaError(Exception): pass

cajaMaquina = {
    100.0: {"cantidad": 5},
    50.0: {"cantidad": 5},
    20.0: {"cantidad": 10},
    5.0: {"cantidad": 20},
    1.0: {"cantidad": 50},
    0.50: {"cantidad": 50},
    0.25: {"cantidad": 50},
    0.10: {"cantidad": 50},
    0.05: {"cantidad": 50},
    0.01: {"cantidad": 50}
}

ValoresPermitidos = [0.01, 0.05, 0.10, 0.25, 0.50, 1, 5, 20, 50, 100]
def ValidarMoneda(valor):
    if valor not in ValoresPermitidos:
        raise DenominacionInvalidaError(f"La moneda por {valor}, no es aceptada.")
    return True

def CalcularVuelto(pago, precio):
    if pago < precio:
        raise SaldoInsuficienteError(f"Saldo insuficiente. Falta: {precio-pago}$")

    VueltoNecesario = round(pago - precio, 2)
    if VueltoNecesario == 0:
        return {}

    vueltoAEntregar = {}
    CajaTemporar = {k: v["cantidad"] for k, v in cajaMaquina.items()}
    resto = VueltoNecesario

    for denominacion in sorted(CajaTemporar.keys(), reverse=True):
        while resto >= denominacion and CajaTemporar[denominacion] > 0:
            resto = round(resto - denominacion, 2)
            CajaTemporar[denominacion] -= 1
            vueltoAEntregar[denominacion] = vueltoAEntregar.get(denominacion, 0) + 1

    if resto > 0:
        raise Exception("Error interno: La máquina no tiene sencillo suficiente para dar el vuelto.")

    for denom, cant in vueltoAEntregar.items():
        cajaMaquina[denom]["cantidad"] -= cant

    return vueltoAEntregar