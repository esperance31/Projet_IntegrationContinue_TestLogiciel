import sqlite3

# Création de la table des colis dans la base de données
def create_table_colis():
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS colis
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nom_client TEXT NOT NULL,
                  adresse TEXT NOT NULL,
                  poids_colis TEXT NOT NULL,
                  numero INTEGER NOT NULL,
                  commentaire TEXT)''')
    conn.commit()
    conn.close()
    
# Inscription d'un nouveau colis
def enregistrement_colis(nom_client, adresse, poids_colis, numero, commentaire):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()

    # Insérer le colis dans la base de données
    c.execute("INSERT INTO colis (nom_client, adresse, poids_colis, numero, commentaire) VALUES (?, ?, ?, ?, ?)",
              (nom_client, adresse, poids_colis, numero, commentaire))
    conn.commit()
    conn.close()