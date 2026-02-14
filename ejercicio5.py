def torres_hanoi(n, desde, hasta, aux):
    """ Función recursiva que realiza el algoritmo de
    Torres de Hanói para n discos """
    if n == 0: # Caso base: No hay discos
        print("No hay discos")
        return 0
    elif n == 1: # Caso base: Solo hay 1 disco
        print(f"Mover el disco {n} de la varilla {desde} a la varilla {hasta}")
        return 1
    else: # Caso recursivo: Hay n discos
        pasos = 0 # Variable auxiliar para contar los pasos
        # Movemos n-1 discos de 'desde' a 'aux'
        pasos += torres_hanoi(n-1, desde, aux, hasta)
        # Movemos el disco n (el grande) de 'desde' a 'hasta'
        print(f"Mover el disco {n} de la varilla {desde} a la varilla {hasta}")
        pasos += 1
        # Movemos n-1 discos de 'aux' a 'hasta'
        pasos += torres_hanoi(n-1, aux, hasta, desde)
        return pasos # Retornamos el número de pasos

try: 
    n = int(input("Ingrese el numero de discos: "))
    if 0 <= n <= 20:
        total_pasos = 2 ** n - 1
        print(f"Para n = {n}, se realizarán {total_pasos} pasos en total. Los pasos son los siguientes:")
        torres_hanoi(n, 1, 3, 2)
    else:
        print(f"El valor debe estar entre 0 y 20")
except ValueError:
    print(f"Ingrese un numero valido")