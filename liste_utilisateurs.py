import sqlite3

# Liste des utilisateurs
def liste_utilisateur ():
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()

    c.execute("SELECT * FROM utilisateur ")
    
    utilisateurs = c.fetchall()

    print("Liste des utilisateurs :")
    for utilisateur in utilisateurs:
        print(f"ID : {utilisateur[0]}")
        print(f"Nom d'utilisateur : {utilisateur[1]}")
        print(f"Adresse e-mail : {utilisateur[3]}")
        print(f"Numero : {utilisateur[4]}")
        print()

    conn.close()