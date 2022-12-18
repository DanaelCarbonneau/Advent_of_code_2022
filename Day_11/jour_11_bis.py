from pprint import*

# structure singe : Tuple (numéro, liste d'objets, type d'opération, nb opération, test_divisibilité, destination vrai, destination faux)


def tour_jeu(liste_singe,tab_inspection):
    """Fonction simulant un tour du jeu pour la liste de singes passée en paramètres"""
    mod = 1
    for singe in liste_singe :
        mod = mod * singe[4]
        
    
    for singe in liste_singe :

        while singe[1]!= []:
            obj_courant = singe[1].pop(0)
            if (singe[2]== '+'):
                obj_courant = obj_courant + singe[3]
            elif (singe[2]=='*'):
                obj_courant = obj_courant * singe[3]
            elif (singe[2]=='^'):
                obj_courant = obj_courant * obj_courant
            

            obj_courant = int(obj_courant%mod)


            if (obj_courant % singe[4] == 0) :
                liste_singe[singe[5]][1].append(obj_courant)
            else:
                liste_singe[singe[6]][1].append(obj_courant)
            
            tab_inspection[singe[0]] +=1
    
    return (liste_singe, tab_inspection)



def lire_input(filename):
    """Fonction renvoyant le tableau avec tous les singes pour le fichier filename"""
    with open(filename, 'r') as f:
        liste_singes = []
        fichier = f.read()
        liste_entrees = fichier.split("\n\n")
        i = 0
        for entree in liste_entrees:
            liste_objets = []
            lignes = entree.split("\n")


            l2 = lignes[1].split(": ")
            liste_obj = l2[1].split(", ")
            for obj in liste_obj:
                liste_objets.append(int(obj))

            l3 = lignes[2].split(" ")
            l4 = lignes[3].split(" ")
            l5 = lignes[4].split(" ")
            l6 = lignes[5].split(" ")

            if (l3[7] == "old"):
                singe = (i, liste_objets, '^', 2, int(l4[5]), int(l5[9]),int(l6[9]))
            
            else :
                singe = (i, liste_objets, l3[6], int(l3[7]), int(l4[5]), int(l5[9]),int(l6[9]))
            
            i+=1
            liste_singes.append(singe)
        return liste_singes





def main():
    s0 = (0,[79,98],'*',19,23,2,3)
    s1 = (1,[54, 65, 75, 74],'+',6,19,2,0)
    s2 = (2,[79, 60, 97],'^',2,13,1,3)
    s3 = (3,[74],'+',3,17,0,1)

    l = lire_input("input_11.txt")

    tab_inspection = [0 for i in range(len(l))]

    pprint(tab_inspection)


    for i in range (10000):
        (l,tab_inspection) = tour_jeu(l,tab_inspection)
    

    print("Résultats : ")
    pprint(tab_inspection)

    

    

if __name__ == '__main__':
	main()





