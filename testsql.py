import sqlite3

conn = sqlite3.connect("pelis.db")

conn.execute("CREATE TABLE Peliculas (id integer PRIMARY KEY AUTOINCREMENT , nombre text, duracion real)")
# sData = (3, "Tiburon", 2)

# cur = conn.cursor()

# cur.execute("SELECT * FROM Peliculas")

# rows = cur.fetchall()

# for i in rows:
#     print (i[1])
# # cur.execute("INSERT INTO PELICULAS (id,nombre,duracion) VALUES(?,?,?);", sData)

# # conn.commit()


conn.close()
