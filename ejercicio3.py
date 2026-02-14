def conteo_caracteres(cadena):
    """ Función que devuelve un diccionario con el conteo de 
    caracteres de una cadena de texto """
    conteo = {}
    for caracter in cadena:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    return conteo

cadena = input("Ingrese una cadena de texto: ")
resultado = conteo_caracteres(cadena)
print(f"El conteo de caracteres de la cadena '{cadena}' es: \n{resultado}")