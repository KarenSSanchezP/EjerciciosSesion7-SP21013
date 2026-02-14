def num_divisores(n): 
    """Función que devuelve el número de divisores de un 
    número dado utilizando una función sum()"""
    return sum(1 for i in range(1, n+1) if n % i == 0)

print("Bienvenido. Ingrese los límites para generar la lista.")

lim_inf = int(input("Ingrese el límite inferior: "))
lim_sup = int(input("Ingrese el límite superior: "))
nums = list(range(lim_inf, lim_sup+1)) 

lista_mas_5_divs = list(filter(lambda x: num_divisores(x) > 5, nums))
print(f"Números con más de 5 divisores en la lista:\n{lista_mas_5_divs}")       