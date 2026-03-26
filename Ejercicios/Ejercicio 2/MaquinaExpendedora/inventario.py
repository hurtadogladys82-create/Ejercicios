from MaquinaExpendedora.transacciones import ProductoAgotadoError

productos = {
    "A1": {"nombre": "Papas Fritas",
           "cantidad": 10,
           "precio": 1.50
           },
    "A2": {"nombre": "Galletas de Chocolate",
           "cantidad": 8,
           "precio": 1.25
           },
    "A3": {"nombre": "Gomitas de Frutas",
           "cantidad": 12,
           "precio": 1.00
           },
    "B1": {"nombre": "Coca-Cola 500ml",
           "cantidad": 15,
           "precio": 2.00
           },
    "B2": {"nombre": "Agua Mineral 500ml",
           "cantidad": 20,
           "precio": 1.00
           },
    "B3": {"nombre": "Té Frío Limón",
           "cantidad": 10,
           "precio": 1.75
           },
    "C1": {"nombre": "Maizoritos",
           "cantidad": 5,
           "precio": 0.85
           },
    "C2": {"nombre": "Maní Salado",
           "cantidad": 0,
           "precio": 1.10
           },
    "C3": {"nombre": "Nutella",
           "cantidad": 14,
           "precio": 1.50
           },
    "D1": {"nombre": "Jugo del Valle",
           "cantidad": 6,
           "precio": 1.80
           },
    "D2": {"nombre": "Gatorade",
           "cantidad": 9,
           "precio": 2.50
           },
    "D3": {"nombre": "Sándwich de Jamón",
           "cantidad": 4,
           "precio": 3.00
           }
}

def TomarProducto(codigo):
    productos[codigo]["cantidad"] -= 1
    print(f"Dispensando: {productos[codigo]['nombre']}")

def VerificarInventario(codigo):
    if codigo not in productos:
        print("No es válido. Introduzca un código válido.")
        return False
    
    if productos[codigo]["cantidad"] > 0:
        return True
    else:
        raise ProductoAgotadoError("Producto agotado. Lamentablemente no se encuentra en stock el producto")
pass