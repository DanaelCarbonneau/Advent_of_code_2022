from pprint import*

#UTILISER DIKJSTRA



def recuperer_graphe():
    filename = input("Filename ?")
    with open(filename, 'r') as f:
        fichier = f.read()
        liste_ligne = fichier.split("\n")

        liste_adj = []
        i = 0
        cpt_sommets = 0
        cpt_ligne = 0
        while i < len(liste_ligne) :
            j = 0
            while j < len(liste_ligne[i]):
                liste_adj.append([])
                if i+1 < len(liste_ligne) and (liste_ligne[i][j] == liste_ligne[i+1][j] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i+1][j])):
                    liste_adj[cpt_sommets].append(cpt_sommets + len(liste_ligne))

                if j+1 < len(liste_ligne[i]) and (liste_ligne[i][j] == liste_ligne[i][j+1] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i][j+1])):
                    liste_adj[cpt_sommets].append(cpt_sommets + 1)
                
                if i > 0 and (liste_ligne[i][j] == liste_ligne[i-1][j] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i-1][j])):
                    liste_adj[cpt_sommets].append(cpt_sommets - len(liste_ligne))
                
                if j > 0 and (liste_ligne[i][j] == liste_ligne[i][j-1] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i][j-1])):
                    liste_adj[cpt_sommets].append(cpt_sommets - 1)

                cpt_sommets+=1
                j+=1

            cpt_ligne +=1
            i+=1

        return liste_adj


        

def main():
    graphe = recuperer_graphe()
    pprint(graphe)
    



if __name__ == '__main__':
	main()
