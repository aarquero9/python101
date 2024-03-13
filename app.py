from flask import Flask, request, render_template
import sqlite3
import json
class Producto:
    def __init__(self,id,nombre,imagen,valor):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.valor = valor
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Pitxar para ir a agur <a href='/agur'>AQUI</a>"


@app.route("/agur")
def agur():
    return "Pitxar para ir a HOME <a href='/'>AQUI</a>"


@app.route("/peliculas")
def peliculas():
    conn = sqlite3.connect("pelis.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Peliculas;")
    rows = cur.fetchall()
    conn.close()
    return json.dumps(rows)


@app.route("/especificPelicula")
def peliculaEspecifica():
    id = request.args.get("id")
    conn = sqlite3.connect("pelis.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Peliculas where id = ?;", (id,))
    rows = cur.fetchall()
    conn.close()
    return json.dumps(rows)


@app.route("/pagina1")
def pagina1():
    return app.send_static_file("pagina1.html")


@app.route("/pagina2")
def pagina2():
    return app.send_static_file("pagina2.html")


@app.route("/dinamic")
def dinamic():
    name = "Pedro"
    age = 27
    frutas = ["Manzana", "PERA", "Piña", "KIWI", "Fresa", "MANGO"]
    return render_template("injection1.html", name=name, age=age, frutas=frutas)

@app.route("/productos")
def productos():
    p1 = Producto(1, 'Raqueta', "https://tenistodo-tender.com/cdn/shop/products/babolat-falcon-naciagnieta_1024x1024.jpg?v=1649456468",1.5)
    p2 = Producto(2, 'Labadora', "https://i0.wp.com/cabauoportunitats.com/wp-content/uploads/2017/10/Rentadora-BEKO-59x56x85cm.jpg?fit=100%2C100&ssl=1", 20)
    p3 = Producto(2, 'Avion',"https://www.mundodeportivo.com/urbantecno/hero/2024/03/recreacion-del-proyecto-x-66a.jpg?width=1200&aspect_ratio=16:9", 25)
    print(p1)
    listap = [p1,p2,p3]
    return render_template("productos.html",listap = listap)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
