import lotes.Logica_elo as elo
def menu(calculadora_ajedrez = None):
    while True:
        
        print("\n" + "="*30)
        print("Bienvenido a la Calculadora de Ajedrez")
        print("="*30)
        print("1. Ingresar jugadores del torneo")
        print("2. Ingresar lote de partidas")
        print("3. Historial de Partidas")
        print("4. Salir")
    
        opcion = input("Seleccione una opción: ")
    
        continuar = True
        match opcion:
            case "1":
                print("\n--- Registro de Jugadores ---")
                nombres = input("Ingrese los nombres de los jugadores separados por comas: ")
                for nombre in nombres.split(","):
                    n = nombre.strip().title()
                    if n:
                    # VALIDACIÓN: Evitar sobrescribir si ya existe
                     if n in elo.jugadores_db:
                        print(f"⚠ El jugador '{n}' ya está registrado.")
                     else:
                        elo.jugadores_db[n] = 1200
                        print(f" '{n}' registrado (1200 pts).")
            
            case "2":
                #Verificacion de Datos vacios
                if not elo.jugadores_db:
                 print("\n ERROR: No hay jugadores en el sistema.")
                 print("Primero debe registrarlos en la Opción 1.")
                 continue  # Volver al menú para registrar jugadores
                else:
                 print("\n--- Modo Lote (Ejemplo: A | B | 1) ---")
                 print("Escriba 'FIN' para procesar el lote.")
                 lote_temporal = []
                
                # Bucle de Datos
                while True:
                    print("=" * 20)
                    j1 = input("Nombre del Jugador 1: ").strip().title()
                    if not j1: break 
                        
                    j2 = input("Nombre del Jugador 2: ").strip().title()
                    res = input("Resultado (1 = Gana J1, 0 = Gana J2, 0.5 o 1/2 = Empate): ").strip()
                    
                    linea_automatica = f"{j1} | {j2} | {res}"
                    lote_temporal.append(linea_automatica)
                    print(" Partida anotada.")
                        
                if lote_temporal:        
                 print("\n--- Procesando resultados del lote ---")
                for i, linea in enumerate(lote_temporal, 1):
                     try:
                       partes = [p.strip() for p in linea.split('|')]
                       if len(partes) != 3: 
                             raise ValueError("Formato incorrecto. Debe ser: JugadorA | JugadorB | Resultado")

                       j_a, j_b, res_str = partes
                       if j_a not in elo.jugadores_db or j_b not in elo.jugadores_db:
                             raise elo.JugadorNoEncontradoError(f"Jugador '{j_a}' o '{j_b}' no existe.")
                         
                       res_val = 0.5 if res_str == "1/2" else float(res_str)
                       ajuste = elo.calcular_nuevo_elo(elo.jugadores_db[j_a], elo.jugadores_db[j_b], res_val)
                         
                       elo.jugadores_db[j_a] += ajuste
                       elo.jugadores_db[j_b] -= ajuste
                       print(f" ✔ Partida {i} OK.")
                     except Exception as e:
                        print(f" Error en partida {i}: {e}")
                else:
                    print("\nNo se ingresaron partidas")
            
            case "3":
                
                if not elo.jugadores_db:
                    print("\n la base de datos esta vacia.")
                    continue 
                
                
                print("\n1. Ver Ranking General")
                print("2. Buscar historial de un jugador")
                sub_opcion = input("Seleccione: ")   
                  
                if sub_opcion == "1":
                     print("\n--- Ranking General ---")
                     ranking = sorted(elo.jugadores_db.items(), key=lambda x: x[1], reverse=True)
                     for n, p in ranking:
                        print(f"• {n.ljust(15)} | {round(p)} pts")
                        
                elif sub_opcion == "2":
                     busqueda = input("Ingrese el nombre del jugador: ").strip().title()
                     print(f"\n=== partida encontrada para {busqueda} ===")
                     encontrado = False
                     
                     for partida in elo.historial_partidas:
                        if busqueda in partida:
                           print( f" >> {partida}" )
                           encontrado = True
                if not encontrado:
                        print(f"No se encontraron partidas para '{busqueda}'.")

            case "4" :
                print("\nSaliendo de la aplicación. ¡Hasta luego!")
                return
            case _:
                print("\nOpción no válida. Por favor, seleccione una opción del 1 al 4.")
                
if __name__ == "__main__":
     menu()