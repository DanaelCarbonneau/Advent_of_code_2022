#Dictionnaire associant chaque coup à son score
points_coup = {"X": 1, "Y":2, "Z" : 3}

#Dictionnaire associant chaque coup de l'adversaire le coup qui nous fait perdre

fait_perdre = {"A":"Z","B": "X","C" : "Y"}

ex_aequo = {"A":"X", "B":"Y", "C" : "Z"}

def calcul_score_ligne(ligne :str):
    """ str -> int
    Fonction qui calcule le score résultatnt de la ligne passée en paramètres"""
    res : int = points_coup[ligne[2]]

    if(ex_aequo[ligne[0]] == ligne[2]):                   #cas ex aequo
        res+= 3
        return res
    elif not(fait_perdre[ligne[0]]== ligne[2]): #cas où on gagne
        res += 6
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
    print("Résultat = " + str(calcul_score_total("input_2.txt")))


if __name__ == '__main__':
	main()


