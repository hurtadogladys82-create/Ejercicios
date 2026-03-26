import MaquinaExpendedora.inventario
from MaquinaExpendedora.transacciones import (
    ValidarMoneda, 
    CalcularVuelto, 
    ProductoAgotadoError, 
    SaldoInsuficienteError, 
    DenominacionInvalidaError
)
import MaquinaExpendedora.inventario as inventario

def menuPrincipal():
        print("================================================")
        print("           Máquina Expendedora Agry")
        print("================================================")
        print("Catálogo:")
        for codigo, info in MaquinaExpendedora.inventario.productos.items():
            estado = info['cantidad'] if info ['cantidad'] > 0 else "AGOTADO"
            print (f"[{codigo}] {info['nombre']} - ${info['precio']} | Stock: {estado}")
        print("================================================")


def ejecutar():
    while True:
        menuPrincipal()
        dineroBandeja = 0.0

        try:
            codigo = input("Ingrese código del producto (o 'VOLVER' para cancelar): ").upper()
            if codigo == "VOLVER":
                continue

            if not MaquinaExpendedora.inventario.VerificarInventario(codigo):
                continue

            producto = MaquinaExpendedora.inventario.productos[codigo]
            precio = producto["precio"]

            print(f"Has seleccionado: {producto['nombre']}. Precio: ${precio}")

            monto_str = input(f"Ingrese el pago total (Monedas/Billetes permitidos): ")
            dineroBandeja = float(monto_str)

            ValidarMoneda(dineroBandeja)

            vuelto = CalcularVuelto(dineroBandeja, precio)

            MaquinaExpendedora.inventario.TomarProducto(codigo)

            if vuelto:
                print(f"Entregando vuelto de: ${dineroBandeja - precio:.2f}")
                for moneda, cant in vuelto.items():
                    print(f" -> {cant} de ${moneda}")
            else:
                print("Pago exacto, sin vuelto.")

            print("¡Gracias por su compra!")
            dineroBandeja = 0.0

        except ProductoAgotadoError as e:
            print(f"\n[ERROR]: {e}")
        except SaldoInsuficienteError as e:
            print(f"\n[ERROR DE PAGO]: {e}")
        except DenominacionInvalidaError as e:
            print(f"\n[ERROR DE MONEDA]: {e}")
        except ValueError:
            print("\n[ERROR]: Formato de pago incorrecto. Use números.")
        except Exception as e:
            print(f"\n[SISTEMA]: {e}")
        finally:
            if dineroBandeja > 0:
                print(f"\n[DEVOLUCIÓN]: Retirando sus ${dineroBandeja:.2f} de la bandeja...")
                dineroBandeja = 0.0

        while True:
            opcion = input("\n1) Volver a comprar\n2) Salir\nSeleccione: ")
            if opcion == '1':
                break
            elif opcion == '2':
                print("Apagando máquina...")
                return
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    ejecutar()