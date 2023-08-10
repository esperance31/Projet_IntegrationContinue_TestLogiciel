import sqlite3

# Création de la table des payements dans la base de données
def create_table_payements():
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS payement
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nom_client TEXT NOT NULL,
                  id_colis INTEGER NOT NULL,
                  code_transaction TEXT NOT NULL)''')
    conn.commit()
    conn.close()
    
# Inscription d'un nouveau payement
def enregistrement_payement(nom_client, id_colis, code_transaction):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()

    # Insérer le colis dans la base de données
    c.execute("INSERT INTO payement (nom_client, id_colis, code_transaction) VALUES (?, ?, ?)",
              (nom_client, id_colis, code_transaction))
    conn.commit()
    conn.close()