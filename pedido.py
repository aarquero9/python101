def pedido(pedido:dict,impuesto:int):
    """_summary_

    Args:
        pedido (dict): Pedido que tiene pizzas hamburguesas y patatas fritas
        impuesto (int): Numero de impuestos

    Returns:
        _type_: It returns the total cost for pizza, hamburgers, and fries as a tuple.
    
    General description:
    It calculates the total cost for pizza by multiplying the quantity of pizza by its unit value, then adding the tax for each pizza.
    It does the same calculation for hamburgers and fries.
    Finally, It returns the total cost for pizza, hamburgers, and fries as a tuple.
    """
    pizza = pedido["pizza"] ["cantidad"] * pedido["pizza"] ["valor"] + impuesto * pedido ["pizza"] ["cantidad"]
    hamburgesas = pedido["hamburgesas"] ["cantidad"] * pedido["hamburgesas"] ["valor"] + impuesto * pedido ["hamburgesas"] ["cantidad"]
    patatasFritas = pedido["patatasFritas"] ["cantidad"] * pedido["patatasFritas"] ["valor"] + impuesto * pedido ["patatasFritas"] ["cantidad"]
    return pizza,hamburgesas,patatasFritas

if __name__ == "__main__":
    pedio = { "pizza": {"cantidad": 2, "valor": 10 }, 
             "hamburgesas": {"cantidad": 10, "valor": 8 },
             "patatasFritas": {"cantidad": 4, "valor": 5 }}
    impuesto = 2
    pedio["hola"] = 20
    print(pedio)
    print(pedido(pedio,2))