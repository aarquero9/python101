def adult(age: int)-> bool:
    """_summary_

    Args:
        age (int): User age

    Returns:
        bool: Adult true minor False
    """
    if age >= 18:
        return True
    else: 
        return False
    

print(adult(18))