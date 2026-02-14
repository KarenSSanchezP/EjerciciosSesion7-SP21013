def voltear(pila, k):
    """
    Voltea los primeros k panqueques de la pila
    """
    pila[:k] = reversed(pila[:k])

def encontrar_indice_maximo(pila, n):
    """
    Encuenta el indice del elemento máximo en la pila
    """
    indice_maximo = 0
    for i in range(1, n):
        if pila[i] > pila[indice_maximo]:
            indice_maximo = i
    return indice_maximo

def ordenar_panqueque(pila):
    """
    Ordena la pila de panqueques por diámetro
    """
    volteos = []
    n = len(pila)
    
    for size in range(n, 1, -1):
        indice_maximo = encontrar_indice_maximo(pila, size)
        
        if indice_maximo != size - 1:
            if indice_maximo != 0:
                voltear(pila, indice_maximo + 1)
                volteos.append(indice_maximo)
            voltear(pila, size)
            volteos.append(size - 1)
    return pila, volteos

def main():
    try: 
        pila = [1, 5, 8, 3]
        print(f"Pila inicial: {pila}")
        
        pila_ordenada, sec_volteos = ordenar_panqueque(pila)
        print(f"Pila ordenada: {pila_ordenada}")
        print(f"Secuencia de volteos: {sec_volteos}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()