def mostrar_titulo():
    print("\n" + "="*35)
    print("  CALCULADORA DE GASTOS DE VIAJE GRUPAL")
    print("="*35)

def mostrar_resultados(total, promedio, balances):
    print("\n" + "-"*35)
    print(f"Gasto Total: {total:.2f}$")
    print(f"Monto por Persona: {promedio:.2f}$")
    print("-"*35)
    print("Estado de cuentas:")
    
    for nombre, balance in balances.items():
        if balance > 0:
            print(f" > {nombre}: Recibe {balance:.2f}$")
        elif balance < 0:
            print(f" > {nombre}: Debe poner {abs(balance):.2f}$")
        else:
            print(f" > {nombre}: Está al día.")
    print("-"*35)