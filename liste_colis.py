import sqlite3

# Liste des colis
def liste_colis( ):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()

    c.execute("SELECT * FROM colis ")
    
    colis = c.fetchall()

    print("Liste des colis en base :")
    for coli in colis:
        print(f"ID : {coli[0]}")
        print(f"Nom du client : {coli[1]}")
        print(f"Adresse  : {coli[2]}")
        print(f"Poids du colis  : {coli[3]}")
        print(f"Numero : {coli[4]}")
        print(f"Commentaire  : {coli[5]}")
        print()

    conn.close()