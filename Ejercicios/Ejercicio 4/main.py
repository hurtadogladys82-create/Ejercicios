import paquetes.calculos as calculos
import paquetes.interfaz as interfaz

def ejecutar_calculadora():
    participantes = {}
    interfaz.mostrar_titulo()

    while True:
        print("\nOpciones: [1] Agregar persona | [2] Calcular total | [3] Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Validación de Nombre (solo letras y espacios)
            nombre = input("Nombre del amigo: ").strip()
            if not nombre.replace(" ", "").isalpha() or nombre == "":
                print("Error: El nombre solo debe contener letras.")
                continue
            
            # Validación de Monto (limpieza de $)
            monto_str = input(f"¿Cuánto pagó {nombre}?: ").strip().replace("$", "")
            try:
                monto = float(monto_str)
                participantes[nombre] = monto
                print(f"¡{nombre} agregado con éxito!")
            except ValueError:
                print("Error: El monto debe ser un número válido.")

        elif opcion == "2":
            try:
                # Realiza los cálculos
                total, promedio = calculos.obtener_promedio(participantes)
                balances = calculos.calcular_balances(participantes, promedio)
                
                # Muestra los resultados
                interfaz.mostrar_resultados(total, promedio, balances)
                
                #vuelve al inicio

            except ValueError as e:
                print(f"\nError: {e}")
            except ZeroDivisionError:
                print("\nError: No se puede dividir entre cero.")

        elif opcion == "3":
            print("Saliendo del programa... ¡Buen viaje!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_calculadora()