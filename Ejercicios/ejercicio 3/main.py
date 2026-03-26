from criptografia.cesar import procesar_cesar
from criptografia.vigenere import procesar_vigenere

def pedir_numero():
    while True:
        try:
            valor = input("Ingrese el número de desplazamiento: ")

            return int(valor) # Si aqui se pone una letra, salta al except
        except ValueError:
            print("Error: Debes ingresar un numero entero. Intenta de nuevo.")

def menu():  
    while True:
        print("\nMenú de opciones:")
        print("1. César (Cifrar)\n2. César (Descifrar)\n3. Vigenère (Cifrar)\n4. Vigenère (Descifrar)\n5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("chao:)")
            break

        if opcion in ["1", "2", "3", "4"]:
            mensaje = input("Escribe el mensaje: ")
            
            if opcion in ["1", "2"]:
                num_clave = pedir_numero()
                modo = "cifrar" if opcion == "1" else "descifrar"
                print("Resultado:", procesar_cesar(mensaje, num_clave, modo))
            
            else:
                while True:
                    palabra_clave = input("Escribe la palabra clave: ")
                    if palabra_clave.isalpha(): break
                    print("Error: La clave debe ser solo letras.")
                
                modo = "cifrar" if opcion == "3" else "descifrar"
                print("Resultado:", procesar_vigenere(mensaje, palabra_clave, modo))
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()