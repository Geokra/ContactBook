import sqlite3
from contact import contact
import sys

conn = sqlite3.connect("database.db")

work = True

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            first text,
            last text,
            email text,
            age text
            )
            """)

while work == True:
    
    a = input("K = Kontakt suchen // E = Eintrag verfassen // U = Kontakt updaten // L = Kontakt löschen: ")

    # Erstellen eines neuen Eintrages
    if a == "E":
        first = input("Geben Sie den Vornamen ein: ")
        last = input("Geben Sie den Nachnamen ein: ")
        age = input("Geben Sie das Alter ein: ")
        email_ = input("Geben Sie die Email ein: ")

        con = contact(first, last, age, email_)

        c.execute("INSERT INTO contact VALUES (:first, :last, :age, :email)", {'first': con.first, 'last': con.last, 'email': con.email_, 'age': con.age})

        conn.commit()
        conn.close
      
    # Suchen eines existierenden Eintrages
    if a == "K":
        b = input("Suchen Per Vorname = A, Nachname = B, Alter = C, Email = D: ")
        if b == "A":
            d = input("Eingabe Vorname: ")
            c.execute("SELECT * FROM contact WHERE first=:first", {'first': d})
            print(c.fetchall())
        if b == "B":
            d = input("Eingabe Nachname: ")
            c.execute("SELECT * FROM contact WHERE last=:last", {'last': d})
            print(c.fetchall())
        if b == "C":
            d = input("Eingabe Alter: ")
            c.execute("SELECT * FROM contact WHERE age=:age", {'age': d})
            print(c.fetchall())
        if b == "D":
            d = input("Eingabe Email: ")
            c.execute("SELECT * FROM contact WHERE email=:email", {'email': d})
            print(c.fetchall())

        conn.commit()
        conn.close

    # Aktualisieren eines Eintrages
    if a == "U":
        b = input("Wählen Sie den Kontakt aus den Aktualisieren wollen (Email eingeben): ")
        c.execute("SELECT * FROM contact WHERE email=:email", {'email': b})
        print(c.fetchall())
        ä = input("Ist das die Person die Sie aktualisieren wollen? J/N ")
        if ä == "J":
            ü = input("Geben Sie ein was Sie aktualisisieren wollen Vorname(V), Nachname(N), Alter(A), Email(E) ")
            if ü == "V":
                ö = input("Geben Sie den neuen Vornamen ein: ")
                conn.execute("UPDATE contact set first=:first", {'first': ö})
                print(c.fetchall())
            if ü == "N":
                ö = input("Geben Sie den neuen Nachnamen ein: ")
                conn.execute("UPDATE contact set last=:last", {'last': ö})
                print(c.fetchall())
            if ü == "A":
                ö = input("Geben Sie das neue Alter ein: ")
                conn.execute("UPDATE contact set age=:age", {'age': ö})
                print(c.fetchall())
            if ü == "E":
                ö = input("Geben Sie die neue Email ein: ")
                conn.execute("UPDATE contact set email=:email", {'email': ö})
                print(c.fetchall())

        conn.commit()

    # Löschen eines Eintrages
    if a == "L":
        b = input("Wählen Sie den Kontakt aus den Sie löschen wollen (Email eingeben): ")
        c.execute("SELECT * FROM contact WHERE email=:email", {'email': b})
        print(c.fetchall())
        ö = input("Ist der Kontakt den Sie löschen möchten? J/N: ")
        if ö == "J":
            ä = input("Kontakt löschen? J/N: ")
            if ä == "J":
                print(f"Kontakt {c.fetchall()} wurde gelöscht")
                c.execute("DELETE from contact where email = :email", {'email': b}) 
                

    x = input("Weiter machen? J/N: ")
    if x == "N":
        work == False
        sys.exit()
       
    
    # TODO: ID adden um Einträge zu kategorisieren 
    #       ID -> Um Einträge zu löschen
    #       ID -> Um Einträge zu aktualisieren
    #       ID Funktionalität hinzufügen