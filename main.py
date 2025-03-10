# funcion para determinar si una palabra es palindromo o no

def palindromo(palabra):
    # ahora usare la docstring para hacer test sobre la documentacion
    """
    La funcion palindromo recibe una palabra y determina si es palindromo o no

    Args:
        palabra (str): palabra a evaluar

    Returns:
        bool: True si es palindromo, False si no lo es

    Examples:
        >>> palindromo("ana")
        True
        >>> palindromo("hola")
        False
    
    """
    # primero normalizamos la palabra
    palabra = palabra.lower()
    # luego reemplazamos los espacios en blanco por nada o mejor dicho se quitan
    palabra = palabra.replace(" ", "")
    # ahora comparamos la palabra original con la palabra invertida
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    if palindromo(palabra):
        print("La palabra es palindromo")
    else:
        print("La palabra no es palindromo")