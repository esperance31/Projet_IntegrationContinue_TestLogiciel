# Grille tarifaire des emvois de colis
def grille_tarifaire():
    print("__________Grille tarifaire__________ ")
    print("Colis de poids  inferieur à 1 kg   ----> 1000 FrCFA")
    print("Colis de poids  situé entre 1-5 kg ----> 2000 FrCFA")
    print("Colis de poids  superieur à 5 kg   ----> 3000 FrCFA")
    
    
def devis(poids, distance) :
    # la fonction prix suit un modele linéaire dependant du poids du colis et de la distance 
    w0 = 0
    w1 = 500
    w2 = 1000
    prix = w0 + poids*w1 + distance*w2
    return prix