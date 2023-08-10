import re

def check_input(input_string):
    # Expression régulière pour vérifier si l'input contient uniquement des lettres (minuscules ou majuscules)
    regex_pattern = r"^[A-Za-z]+$"

    if re.match(regex_pattern, input_string):
        print("L'input est valide.")
    else:
        print("L'input n'est pas valide. Il doit contenir uniquement des lettres (minuscules ou majuscules).")
        
        
def check_mdp(password):
    # Au moins 6 caractères, au moins une lettre minuscule, au moins une lettre majuscule, au moins un chiffre
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$"

    if re.match(regex, password):
        return True
    else:
        return False
    
    
def check_email(email):
    # Format d'une adresse mail: suite de lettre ou de chiffre + @ nom de domaine+ . com, net, etc
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(regex, email):
        return True
    else:
        return False

def check_number(entree):
    # Suite de 8 numbre pour le numero
    regex = r"^\d{8}$"

    if re.match(regex, entree):
        return True
    else:
        return False


