#Dictionnaire associant chaque coup à son score
points_coup = {"A": 1, "B":2, "C" : 3}

#Dictionnaire associant à chaque coup de l'adversaire le coup qui nous fait perdre

fait_perdre = {"A":"C","B": "A","C" : "B"}

#Dictionnaire associant à chaque coup de l'adversaire le coup nous faisant gagner
fait_gagner = {"A" : "B", "B" : "C", "C" : "A"}

#Dictionnaire associant chaque situation avec la partie du score sur la victoire obtenu
situation = {"X": 0, "Y": 3 , "Z": 6}

def calcul_score_ligne(ligne :str):
    """ str -> int
    Fonction qui calcule le score résultatnt de la ligne passée en paramètres"""
    res : int = situation[ligne[2]]             #Calcul du nombre de points de la situation

    #On calcule quelle coup il fallait jouer
    if(ligne[2]== 'X'):
        res += points_coup[fait_perdre[ligne[0]]]
    elif (ligne[2]== 'Y'):
        res += points_coup[ligne[0]]
    else :
        res += points_coup[fait_gagner[ligne[0]]]


    return res


def calcul_score_total(nom_fichier : str):
    """str -> int
    Fonction calculant le score total du déroulement présenté dans le fichier dont le nom est passé en paramètres"""
    res : int = 0

    f = open(nom_fichier)

    i = f.read()

    liste_ligne : list[str] = i.split("\n")

    for ligne in liste_ligne :
        if(len(ligne)==3):
            res += calcul_score_ligne(ligne)
    
    return res

def main():
    print("Résultat = " + str(calcul_score_total("input_2_bis.txt")))


if __name__ == '__main__':
	main()


