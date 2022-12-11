from pprint import*

#Ne fonctionne pas si deux dossiers ont le même nom à cause de la table de hachage


#Dictionnaire_arborescence {nom_dossier : (taille_fichiers, liste_fils)}
Dictionnaire_arborescence = {}
Dictionnaire_taille = {}

Dictionnaire_collisions = {}

def remplir_Dictionnaire_arborescence (fichier):
    """Créé l'arborescence correspondant au fichier en remplissant le dictionnaire en variable globale"""
    pile_path = ["/"]

    for ligne in fichier : 
        if ligne[0] == "$":
            if ligne[1] == "cd" : 
                if ligne[2] == "..":
                    pile_path.pop()

                else:
                    pile_path.append(ligne[2])
                    Dictionnaire_arborescence[pile_path[-1]] = (0,[])
        else : 
            if ligne[0] == "dir":
                Dictionnaire_arborescence[pile_path[-1]][1].append(ligne[1])
            else :
                Dictionnaire_arborescence[pile_path[-1]] = (Dictionnaire_arborescence[pile_path[-1]][0] + int(ligne[0]), Dictionnaire_arborescence[pile_path[-1]][1])
    return Dictionnaire_arborescence

def calculer_taille_dictionnaire(cle):
    """Calcule récursivement la taille du dossier et la note dans le dictionnaire de la taille"""
    if Dictionnaire_arborescence[cle][1] == []:
        Dictionnaire_taille[cle] = Dictionnaire_arborescence[cle][0]
        
    else : 
        taille = Dictionnaire_arborescence[cle][0]
        for fils in Dictionnaire_arborescence[cle][1]:
            taille+= calculer_taille_dictionnaire(fils)
        Dictionnaire_taille[cle] = taille
    
    return Dictionnaire_taille[cle]

def calculer_cout_inf(borne : int):
    """Calcule la somme des tailles des dossiers dont le coût est inférieur à la borne."""
    somme : int = 0
    for cle in Dictionnaire_taille : 
        if Dictionnaire_taille[cle] <= borne:
            somme+= Dictionnaire_taille[cle]
    return somme 

def main():
    filename = input("Filename ?")
    with open(filename, 'r') as f:
        fichier = f.read()
        liste_ligne = fichier.split("\n")
        liste_instructions = []

        for ligne in liste_ligne:
            liste_instructions.append(ligne.split(" "))

        remplir_Dictionnaire_arborescence(liste_instructions)

        calculer_taille_dictionnaire("/")

        pprint(Dictionnaire_arborescence)

        print(str(calculer_cout_inf(100000)))

      

if __name__ == '__main__':
	main()












