numberOfEmployees = {
    "Google": 25000,
    "Microsoft": 30000,
    "Apple": 20000,
    "Amazon": 35000,
    "Facebook": 28000
}

userPassword = {
    "usuario1": "contraseña123",
    "usuario2": "clave456",
    "nombreusuario": "miclave789",
    "john_doe": "password",
    "user123": "securepass"
}

def checkNumberOfEmployees(eleccion: str) -> str:
    """Returns the number of employees based on the chosen option.

    Args:
        eleccion (str): The selected option for which the number of employees is requested.

    Returns:
        str: The number of employees corresponding to the chosen option.
    """
    return numberOfEmployees[eleccion]

def login(username: str, password: str) -> bool:
    """
    Checks if the provided username and password are valid.

    Args:
        username (str): The username to be checked.
        password (str): The password associated with the username.

    Returns:
        bool: True if the username and password are valid, otherwise False.
    """      
    if username in userPassword and userPassword[username] == password:
        return True
    else: return False

#MAINNNN-----------------------------------
print(checkNumberOfEmployees("Google"))

username = input("Dame el usuario ")
password = input("Dame el password ")

print(login(username,password))