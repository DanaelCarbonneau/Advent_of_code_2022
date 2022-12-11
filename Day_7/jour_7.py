from pprint import*

#Fonctionne mais ne fait pas l'arbre

def compte_taille(fichier):
    pile_path = []
    liste_res = []

    for ligne in fichier :
        
        if ligne[0] == "$":
            if ligne[1] == "cd":
                if ligne[2] == "..":

                    retrait = pile_path.pop()
                    liste_res.append([retrait[0],retrait[1]])
                    
                else :
                    pile_path.append([ligne[2],0])
                    
        else : 
            if ligne[0] != "dir" : 
                for dir in pile_path :
                    dir[1] += int(ligne[0])

    
    for dir in pile_path :
        liste_res.append(dir)
        if (dir[0]=="/"):
            pere = (dir)

    return (liste_res,pere)


def calculer_cout_inf(borne : int, liste_tailles):
    """Calcule la somme des tailles des dossiers dont le coût est inférieur à la borne."""
    somme : int = 0
    for taille in liste_tailles : 
        if taille[1] <= borne:
            somme+= taille[1]
    return somme 


def calculer_plus_petit_taille_sup(borne : int, liste_tailles):
    """Retourne le nom du plus petit répertoire dont la taille dépasse la borne supérieure"""
    taille_min_sup_borne = -1

    for dir in liste_tailles : 
        if dir[1] >= borne :
            if(taille_min_sup_borne == -1):
                taille_min_sup_borne = dir[1]
            else :
                if dir[1] < taille_min_sup_borne :
                    taille_min_sup_borne = dir[1]
    
    return taille_min_sup_borne

def calculer_taille_necessaire(espace_total, espace_necessaire, pere) :
    """Calcule l'espace qu'il faut nécessairement supprimer"""
    return espace_necessaire -  (espace_total - pere[1] )

    

def main():
    filename = input("Filename ?")
    with open(filename, 'r') as f:
        fichier = f.read()
        liste_ligne = fichier.split("\n")
        liste_instructions = []

        for ligne in liste_ligne:
            liste_instructions.append(ligne.split(" "))

        liste_plus_pere = compte_taille(liste_instructions)
        pprint(liste_plus_pere[0])


        
        print(str(calculer_cout_inf(100000,liste_plus_pere[0])))

        espace_a_suppr = calculer_taille_necessaire(70000000,30000000,liste_plus_pere[1])

        print(str(calculer_plus_petit_taille_sup(espace_a_suppr,liste_plus_pere[0])))




if __name__ == '__main__':
	main()

