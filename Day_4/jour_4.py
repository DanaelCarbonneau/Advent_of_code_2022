
#Partie 1

def overlap(ligne : str):
    """Fonction qui renvoie vrai s'il y a un overlap de tâches à la ligne passée en paramètres"""
    if (ligne == ""):
        return False
    l_ligne = ligne.split(',')

    s_intervalle_gauche  = l_ligne[0]
    s_intervalle_droite  = l_ligne[1]
    intervalle_gauche = s_intervalle_gauche.split('-')
    intervalle_droite = s_intervalle_droite.split('-')

    return  ( (int(intervalle_gauche[0] ) <= int(intervalle_droite[0])) and (int(intervalle_gauche[1]) >= int (intervalle_droite[1])) ) or  ( (int (intervalle_droite[0]) <= int(intervalle_gauche[0])) and (int (intervalle_droite[1]) >= int(intervalle_gauche[1])) )

def overlap_total(file_name : str):
    """Fonction qui renvoie le nombre d'overlaps de tâches dans le fichier dont le nom est passé en paramètres"""
    f = open(file_name)
    fichier = f.read()
    liste_ligne = fichier.split("\n")

    res = 0
    for ligne in liste_ligne:
        if(overlap(ligne)):
            res+=1    
    print(res)
    return res
    


def main():
    overlap_total("input_4.txt")


if __name__ == '__main__':
	main()


