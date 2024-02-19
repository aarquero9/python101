
def pedido(pedido,impuesto):
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