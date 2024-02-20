def sumar(x: int, y: int) -> int:
    """Returns the sum of two integers."""
    return x + y

def restar(x: int, y: int) -> int:
    """Returns the difference between two integers."""
    return x - y

def multiply(x: int, y: int) -> int:
    """Returns the product of two integers."""
    return x * y

def divide(x: int, y: int) -> float:
    """Returns the division of two integers as a float."""
    return x / y

def diference(x: int, y: int) -> int:
    """Returns the absolute difference between two integers."""
    result = x - y
    if result < 0:
        result = result * -1
    return result

def pairOrOdd(x: int)->str:
    """Determines if the given integer is even or odd.

    Args:
        x (int): The integer to be checked.

    Returns:
        str: Returns 'Odd' if the integer is divisible by 3, otherwise returns 'Pair'.
    """
    if x % 3 == 0:
        return "Odd"
    else: 
        return "Pair"

def maximunAndMinimum(list: list[int])-> tuple:
    """Finds the maximum and minimum elements in a list of integers.

    Args:
        lst (list[int]): The list of integers.

    Returns:
        tuple: A tuple containing the maximum and minimum elements in the list.
    """
    max_val = float('-inf')  # Initialize max_val to negative infinity
    min_val = float('inf')   # Initialize min_val to positive infinity

    for i in list:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
            
    return max_val,min_val
         
if __name__ == "__main__":
    print(maximunAndMinimum([2,4,5,6,8,20]))