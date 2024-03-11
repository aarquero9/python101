from dataclasses import dataclass
import sqlite3


@dataclass
class Peliculas:
    id: int
    nombre: str
    duracion: float

listaPelis = []
conn = sqlite3.connect("pelis.db")
filmData = Peliculas(-1, "test recover id", 1.4)

cur = conn.cursor()
cur.execute(
    "INSERT INTO PELICULAS (nombre,duracion) VALUES(?,?);",
    (filmData.nombre, filmData.duracion),
)

conn.commit()
cur.execute("SELECT * FROM Peliculas WHERE nombre = ?;", (filmData.nombre,))

rows = cur.fetchall()
filmData.id = rows[0][0]
listaPelis.append(filmData)
print(filmData)
conn.close()
