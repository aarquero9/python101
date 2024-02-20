def isCapital(word: str) -> bool:
    """Checks if the first letter of a word is capitalized.

    Args:
        word (str): The input word.

    Returns:
        bool: True if the first letter of the word is capitalized, otherwise False.
    """
    if word[0].isupper():
        return True
    else:
        return False

def largestWord(text: str) -> str:
    """Finds the largest word in the given text.

    Args:
        text (str): The input text containing words.

    Returns:
        str: The largest word found in the text.
    """
    words = text.split(" ")
    
    max_length_word = ""
    for word in words:
        if len(max_length_word) < len(word):
            max_length_word = word
    return max_length_word

def countMayus(text: str)-> int:
    """Counts the number of uppercase letters in the given text.

    Args:
        text (str): The input text.

    Returns:
        int: The number of uppercase letters in the text.
    """
    numberOfMayus = 0
    
    for i in text:
        if i.isupper():
            numberOfMayus += 1
    return numberOfMayus

print(countMayus("El Lorem Ipsum fue concebido como un texto de relleno, formateado de una cierta manera para permitir la presentación de elementos gráficos en documentos, sin necesidad de una copia formal. El uso de Lorem Ipsum permite a los diseñadores reunir los diseños y la forma del contenido antes de que el contenido se haya creado, dando al diseño y al proceso de producción más libertad."))