# Creation des classes pour la base de donnees
print(f"Chargement de {__file__}")

import sqlite3

lien_db = "database.db"
connexion = sqlite3.connect(lien_db)

## Connexion a la base de donnee
def connect_db():
    connexion = sqlite3.connect(lien_db)
    return connexion

## class Epreuve 
cursor = connexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS epreuves (nom TEXT, filiere TEXT, nombre INTEGER)")
connexion.commit()    

class Epreuve:
    def __init__(self, nom, filiere):
        self.nom = nom
        self.filiere = filiere
        self.nombre = 0
        connexion = connect_db()
        cursor = connexion.cursor()
        cursor.execute("INSERT INTO epreuves VALUES (?, ?, ?)", (self.nom, self.filiere, self.nombre))
        connexion.commit()

    def incr(self):
        self.nombre += 1


