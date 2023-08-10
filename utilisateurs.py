import sqlite3
import verifier
import re

# Création de la table des utilisateurs dans la base de données
def create_table_utilisateurs():
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS utilisateur
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nom_utilisateur TEXT NOT NULL,
                  password TEXT NOT NULL,
                  email TEXT NOT NULL,
                  numero INTEGER NOT NULL)''')
    conn.commit()
    conn.close()
    
# Inscription d'un nouvel utilisateur
def enregistrement_utilisateurs(nom_utilisateur, email, password, numero):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()

    # Vérifier si l'utilisateur existe déjà
    c.execute("SELECT * FROM utilisateur WHERE nom_utilisateur=?", (nom_utilisateur,))
    if c.fetchone():
        print("L'utilisateur existe déjà. changer de nom d'utilisateur")
        conn.close()
        return 

    # Crypter le mot de passe avant de le stocker
    #hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insérer l'utilisateur dans la base de données
    c.execute("INSERT INTO utilisateur (nom_utilisateur, email, password, numero) VALUES (?, ?, ?, ?)",
              (nom_utilisateur, email, password, numero))
    conn.commit()
    conn.close()