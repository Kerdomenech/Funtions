# lista
tallas = [34, 36, 38, 40, 42]

# funciones implementando el algoritmo de busqueda
def buscar_talla(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2 
        
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
            
    return -1  # Si no hay la talla , devuelve -1

continuar = "si"

while continuar == "si":
    talla_buscada = int (input("\n¿Qué talla buscas? "))
    resultado = buscar_talla(tallas, talla_buscada)

    if resultado != -1:
        print(f" Talla encontrada en la posición: {resultado}")
    else:
        print("Talla no disponible")
    
    # el ciclo continua o no
    continuar = input("¿Quieres buscar otra talla? (si/no): ")

print("¡Gracias!")