from pprint import*

def est_visible(tableau, i,j, n,m,val):
    visibilite = [False,False,False,False]
    for k in range(i) : 
        if val <= tableau[k][j]:
            visibilite[0] = True
    
    for k in range(i+1,n):
        if val <= tableau[k][j]:
            visibilite[1] = True
    
    for k in range(j):
        if val <= tableau[i][k]:
            visibilite[2] = True
    
    for k in range(j+1,m):
        if val <= tableau[i][k]:
            visibilite[3] = True
    
    return visibilite[0] and visibilite[1] and visibilite[2] and visibilite[3]


def compte_arbres_visibles(tableau, n, m):
    """Compte le nombre d'arbres visibles dans le tableau de dimensions n * m"""
    cpt : int = 0
    for i in range(n):
        for j in range(m):
            if not est_visible(tableau,i,j,n,m,tableau[i][j]):
                cpt+=1
    
    return cpt



def visibilite_de_l_arbre(tableau, i,j, n,m,val):
    visibilite = [0,0,0,0]

    k = i
    while k>1 and val <= tableau[k][j]:             #boucle décroissante (on remonte)
        if val == tableau[i][k]:
            visibilite[0]+=1
            break
        visibilite[0] +=1
        k = k-1
    
    k = i+1
    while k < n-1 and val <= tableau[k][j]:          #boucle croissante (on descend)
        if val == tableau[i][k]:
            visibilite[1]+=1
            break
        visibilite[1] +=1
        k +=1
    
    k = j
    while k > 1 and val <= tableau[i][k]:                   #boucle décroissante (on va à gauche)
        if val == tableau[i][k]:
            visibilite[2]+=1
            break
        visibilite[2] +=1
        k = k-1
    
    k = j+1
    while k < m-1 and  val <= tableau[i][k]:        #boucle croissante (on va à droite)
        if val == tableau[i][k]:
            visibilite[3]+=1
            break
        visibilite[3] +=1
        k+=1
    
    return visibilite[0] * visibilite[1] * visibilite[2] * visibilite[3]


def trouve_arbre_meilleure_vue(tableau, n, m):
    """retourne l'arbre maximisant la qualité de la vue (en nombre d'arbres)"""
    max : int = -1
    
    for i in range(n):
        for j in range(m):
            vis = visibilite_de_l_arbre(tableau,i,j,n,m, tableau[i][j])
            if max < vis:
                max = vis
    
    return max


def main():
    
    with open("input_8.txt", 'r') as f:
        fichier = f.read()
        liste_ligne_s = fichier.split("\n")
        
        liste_ligne = []

        for ligne in liste_ligne_s :
            liste_elt = []
            for chiffre in ligne : 
                liste_elt.append(int(chiffre))
            liste_ligne.append(liste_elt)

        print(compte_arbres_visibles(liste_ligne,99,99))
        print(trouve_arbre_meilleure_vue(liste_ligne,99,99))
        
if __name__ == '__main__':
	main()

