

def priorite_element_intrus_ligne(ligne : str):
    """Retourne la priorité de l'élement intrus dans la ligne (se trouvant dans les deux compartiments)"""
    #On calcule l'indice de coupure de la ligne qui délimite les deux compartiments
    i:int = int(len(ligne) /2)

    compartiment_1 : str = ligne[:i]
    compartiment_2 : str = ligne[i:]

    for c in compartiment_1:
        ind_c_compartiment_2 : int = compartiment_2.find(c)
        if(ind_c_compartiment_2 != -1):
            
            if ord(c) <= 90 :
                return ord(c) - ord('A') + 27
            else :
                return ord(c) - ord('a') + 1
    return 0

def calcul_priorite(file_name : str):
    """Retourne la somme des priorités calculée pour le fichier donné en paramètres"""
    f = open(file_name)

    fichier = f.read()

    liste_ligne = fichier.split("\n")
    
    res = 0

    for ligne in liste_ligne:
        res += priorite_element_intrus_ligne(ligne)
    
    print(str(res))

    return res



def trouver_priorite_item_commun(ligne_1 : str,ligne_2 : str,ligne_3 : str):
    """Fonction retournant la priorité de l'élément commun aux trois lignes s'il existe et 0 sinon"""
    for c in ligne_1:
        ind_c_ligne_2 = ligne_2.find(c)
        if( ind_c_ligne_2 !=-1):
            ind_c_ligne_3 = ligne_3.find(c)
            if(ind_c_ligne_3 != -1):
                if ord(c) <= 90 :
                    return ord(c) - ord('A') + 27
                else :
                    return ord(c) - ord('a') + 1
    return 0

def somme_priorite_item_commun(file_name :str):
    """Fonction retourne la somme des priorités des items communs aux lignes prises trois par trois"""
    f = open(file_name)

    fichier = f.read()

    liste_ligne = fichier.split("\n")
    
    i : int = 2
    res = 0
    while i < len(liste_ligne):
        res += trouver_priorite_item_commun(liste_ligne[i-2], liste_ligne[i-1],liste_ligne[i])
        i+=3

    print(str(res))
    return res






def main():

    calcul_priorite("input_3")

    somme_priorite_item_commun("input_3")







if __name__ == '__main__':
	main()



