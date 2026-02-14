def contar_vocales(palabra):
    """
    Función que devuelve el número de vocales de una palabra
    utilizando una función sum().
    """
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)

palabras = ["Michael", "Jackson", "Tyler", "Joseph", "Josh", "Dun", "Gaga"]
dicc_vocales = dict(map(lambda p: (p, contar_vocales(p)), palabras))

print(f"Lista: {palabras}\n"
    f"Número de vocales por palabra:\n{dicc_vocales}")