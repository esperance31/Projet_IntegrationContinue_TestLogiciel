import re

def check_input(input_string):
    # Expression régulière pour vérifier si l'input contient uniquement des lettres (minuscules ou majuscules)
    regex_pattern = r"^[A-Za-z]+$"

    if re.match(regex_pattern, input_string):
        print("L'input est valide.")
    else:
        print("L'input n'est pas valide. Il doit contenir uniquement des lettres (minuscules ou majuscules).")

if __name__ == "__main__":
    user_input = input("Entrez votre input : ")
    check_input(user_input)