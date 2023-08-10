import sqlite3

# Connexion d'un utilisateur
def login(nom_utilisateur, password):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    

    # Rechercher l'utilisateur dans la base de données
    c.execute("SELECT * FROM utilisateur WHERE nom_utilisateur=?", (nom_utilisateur,))
    user = c.fetchone()

    if not user:
        print("L'utilisateur n'existe pas.")
        conn.close()
        return False

    # Vérifier le mot de passe
    if password :
        # if bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8'))
        print("Connexion réussie ! Bienvenue, ", user[1])
        conn.close()
        return True
    else:
        print("Mot de passe incorrect.")
        conn.close()
        return False