# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
# programme devra calculer x^n, ou n est le nombre fourni par l’utilisateur, sans utiliser de
# fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach
# ni ... boucle. Seulement de la récursivité.

def puissance(n):
    x=2
    if n == 0:
        return 1
    else:
        return x * puissance(n-1)

# demander à l'utilisateur de renseigner un nombre entier

n = int(input("Entrez un nombre entier (pour la puissance): "))
print(puissance(n))


