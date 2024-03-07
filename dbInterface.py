import sqlite3

accion = ""
conn = sqlite3.connect("pelis.db")
print("Bienvenidos a mi DB tienes estas opciones disponibles:")


def showAll():
    cur = conn.cursor()

    cur.execute("SELECT * FROM Peliculas")

    rows = cur.fetchall()

    for i in rows:
        print("=========================")
        print(f"ID = {i[0]}")
        print(f"Title = {i[1]}")
        print(f"Duration = {i[2]}h")
        print("=========================")


while accion != "q":
    match accion:
        case "1":
            name = input("Whats the name of your film? ")
            duration = float(input("And the duration? "))
            filmData = (name, duration)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO PELICULAS (nombre,duracion) VALUES(?,?);", filmData
            )
            conn.commit()
            accion = ""
        case "2":
            showAll()
            accion = ""
            pass
        case "3":
            selection = int(input("Which one will you like to see?"))
            cur = conn.cursor()

            cur.execute("SELECT * FROM Peliculas WHERE id = ?;", (selection,))

            rows = cur.fetchall()
            print("=========================")
            print(f"ID = {rows[0][0]}")
            print(f"Title = {rows[0][1]}")
            print(f"Duration = {rows[0][2]}h")
            print("=========================")
            accion = ""
            pass
        case "4":
            showAll()
            selection = int(input("Which one will you like to update? "))
            name = input("Whats the name of your film? ")
            duration = float(input("And the duration? "))
            filmData = (name, duration, selection)
            cur = conn.cursor()
            cur.execute(
                "UPDATE PELICULAS SET nombre = ?, duracion = ?  WHERE id = ?;",
                filmData,
            )
            conn.commit()
            accion = ""
            pass
        case "5":
            showAll()
            selection = int(input("Which one will you delete? "))
            cur = conn.cursor()
            cur.execute("DELETE FROM PELICULAS WHERE id = ?;", (selection,))
            accion = ""
            pass
        case _:
            print("1--->Create")
            print("2--->See all data")
            print("3--->See one entry")
            print("4--->Update")
            print("5--->Delete")
            print("q--->For exiting")
            accion = input("Que quieres hacer?")

print("Adios y gracias!")
conn.close()
