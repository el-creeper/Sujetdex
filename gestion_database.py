import sqlite3

lien_db = "database.db"

## Connexion à la base de données
def connect_db():
    return sqlite3.connect(lien_db)

## Création de la table si elle n'existe pas
connexion = connect_db()
cursor = connexion.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS epreuves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    filiere TEXT NOT NULL,
    matiere TEXT NOT NULL,
    banque TEXT NOT NULL,
    nombre INTEGER NOT NULL
);
"""
)
connexion.commit()
connexion.close()

## Classe Epreuve avec gestion de la base
class Epreuve:
    def __init__(self, nom, filiere, matiere):
        self.nom = nom
        self.filiere = filiere
        self.nombre = 0
        self.matiere = matiere

        connexion = connect_db()
        cursor = connexion.cursor()

        # Vérifie si l'épreuve existe déjà en base
        cursor.execute("SELECT nombre FROM epreuves WHERE nom = ?", (self.nom,))
        result = cursor.fetchone()
        
        if result is None:
            # Insérer une nouvelle épreuve
            cursor.execute("INSERT INTO epreuves VALUES (?, ?, ?, ?)", (self.nom, self.filiere, self.matiere, self.nombre))
        else:
            # Charger le nombre d'occurrences depuis la base
            self.nombre = result[0]

        connexion.commit()
        connexion.close()

    def incr(self):
        """ Incrémente le nombre d'occurrences et met à jour la base de données """
        self.nombre += 1
        connexion = connect_db()
        cursor = connexion.cursor()
        cursor.execute("UPDATE epreuves SET nombre = ? WHERE nom = ?", (self.nombre, self.nom))
        connexion.commit()
        connexion.close()

    def modif_matiere(self, nv_nom):
        """ Modifie le nom de la matière et met à jour la base de données """
        self.matiere = nv_nom
        connexion = connect_db()
        cursor = connexion.cursor()
        cursor.execute("UPDATE epreuves SET matiere = ? WHERE nom = ?", (self.matiere, self.nom))
        connexion.commit()
        connexion.close()


    def __str__(self):
        return f"Epreuve : {self.nom} - {self.filiere} - {self.matiere} - {self.nombre}"

