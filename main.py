import sqlite3


import utilisateurs
import colis
import payements
import liste_utilisateurs
import liste_colis
import grille_tarifaire
import login
import verifier

#import bcrypt


# ... Demander à l'utilisateur s'il veut s'inscrire ou se connecter 
choix = int(input( "Bienvenue à vous, Voullez vous vous inscrire ou vous connecter? "
                "Taper 1 si vous avez pas de compte et 2 pour vous connecter à un compte : "))

if choix == 1 : 
    
    utilisateurs.create_table_utilisateurs()
    print("Entrez les informations relatives de l'utilisateur :")
    nom_utilisateur = input("Nom d'utilisateur : ")
    email = input("Adresse e-mail : ")
    password = input("Mot de passe : ")
    numero = input("Numero : ")

    inscription = utilisateurs.enregistrement_utilisateurs(nom_utilisateur, email, password, numero)
    

elif choix == 2 :
    
    print("Entrer les informations de connexion : ")
    nom_utilisateur = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    
    log = login.login(nom_utilisateur, password)
    if log == True :
        print("----------Affichage du menu----------")
        print("1. Ajouter un colis")
        print("2. Voir la grille tarifaire")
        print("3. AJouter un payement")
        print("4. Afficher la liste des utilisateurs")
        print("5. Afficher la liste des colis")
        print("6. Avoir un dévis")
        
        tache = int(input("Entrer le choix de la transaction : "))
        if tache == 1 :
            colis.create_table_colis()
            print("Entrez les informations relatives au colis :")
            nom_client = input("Nom d'utilisateur : ")
            adresse = input("Entrer la localisation : ")
            poids = input("Entrer le poids du colis en kilogramme : ")
            numero = input("Numero du destinataire: ")
            commentaire = input("Renseigner des détails du colis: ")
            nouveau_colis = colis.enregistrement_colis(nom_client, adresse, poids, numero, commentaire)
            '''if nouveau_colis == True :
                print("Nouveau colis enregistré avec succès")
            else :
                print("Echec d'enregistrement") '''
                
        elif tache == 2 :
            grille_tarifaire.grille_tarifaire()
            
            
        elif tache == 3 :
            payements.create_table_payements()
            print("Entrez les informations relatives au payement :")
            nom_client = input("Nom d'utilisateur : ")
            id_colis = input("Entrer l'identifiant du colis : ")
            code_transaction = input("Entrer le code de la transaction Orange ou Moov Money : ")
            payements.enregistrement_payement(nom_client, id_colis, code_transaction)
            
        elif tache == 4 :
            liste_utilisateurs.liste_utilisateur()
            
        elif tache == 5 :
            liste_colis.liste_colis()
            
        elif tache == 6 :
            print("Ici vous pouvez voir le prix de notre livraison en renseignant le poids et la distance à faire")
            poids = int(input("Poids en kg : "))
            dist = int(input("Distance à parcourir : "))
            grille_tarifaire.devis(poids, dist)
            
            
    

