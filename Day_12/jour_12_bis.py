
from pprint import*

def trouver_sommet_minimum(sommets_ouverts:dict) : 
    key_min = -1

    for key in sommets_ouverts.keys() : 
        if key_min == -1 or key_min > key or key == 0:
            key_min = key
    
    return key_min


def passage_autorise(a,b):

    if b == 'E' :
        return a == 'z' or a == 'y'
    

    if a == 'S' :
        return b == 'a' or b == 'b'

    return ord(b) <= ord(a)+1

def voisins(matrice,x):
    res = []

    if x[0] > 0 :
        if passage_autorise(matrice[x[0]-1][x[1]], matrice[x[0]][x[1]]):
            res.append((x[0]-1,x[1]))
        
    
    if x[0] < len(matrice)-1 :
        if passage_autorise(matrice[x[0]+1][x[1]], matrice[x[0]][x[1]]):
            res.append((x[0]+1,x[1]))
        
    

    if x[1] > 0:
        if passage_autorise(matrice[x[0]][x[1]-1], matrice[x[0]][x[1]]):
            res.append((x[0],x[1]-1))
        
    if x[1] < len(matrice[0])-1:
        if passage_autorise(matrice[x[0]][x[1]+1], matrice[x[0]][x[1]]):
            res.append((x[0],x[1]+1))
    
    return res
    

   
def dijkstra_matrice(matrice, coord_depart, coord_dest):
    """retourne le plus court chemin par l'algorithme de dijkstra entre le sommet (0,0) et 
    le sommet de coordonnées doord_dest"""

    sommets_ouverts = {0:[coord_dest]}
    

    distances = []
    for i in range(len(matrice)):
        l_distances = []
        for  j in range (len(matrice[0])):
            l_distances.append(-1)
        distances.append(l_distances)
    distances[coord_dest[0]][coord_dest[1]] = 0
    visites = []

    for i in range(len(matrice)):
        l_visites = []
        for  j in range (len(matrice[0])):
            l_visites.append(0)
        visites.append(l_visites)
    

    for i in range(len(matrice)*len(matrice[0])+1):
        d_min = trouver_sommet_minimum(sommets_ouverts)

        if d_min == -1 :
            print("sortie anticipée")
            return distances[0][0]
        
        x = sommets_ouverts[d_min].pop(0)
        liste_voisins = voisins(matrice,x)


        for v in liste_voisins :

            if (distances[v[0]][v[1]] == -1) :
                distances[v[0]][v[1]] = distances[x[0]][x[1]] + 1
            
            if (distances[v[0]][v[1]] > distances[x[0]][x[1]] + 1) :
                distances[v[0]][v[1]] = distances[x[0]][x[1]] + 1 

            if visites[v[0]][v[1]] == 0 : 

                if distances[v[0]][v[1]] in sommets_ouverts.keys() :
                    
                    sommets_ouverts[distances[v[0]][v[1]]].append(v)
                else :
                    sommets_ouverts[distances[v[0]][v[1]]] = [v]

        visites[x[0]][x[1]] = 1

        if sommets_ouverts[d_min]== []:
            sommets_ouverts.pop(d_min)

    pprint(distances)
    return distances[coord_depart[0]][coord_depart[1]]



def recuperer_graphe():
    filename = input("Filename ?")
    with open(filename, 'r') as f:
        fichier = f.read()
        liste_ligne = fichier.split("\n")
        i = 0
        for ligne in liste_ligne :
            j = 0
            for c in ligne :
                if c == 'S':
                    depart = (i,j)
                elif c == 'E':
                    arrivee = (i,j)
                j+=1
            i+=1
        return (liste_ligne,depart,arrivee)


def main():
    (matrice, depart, arrivee) = recuperer_graphe()

    
    print(dijkstra_matrice(matrice,depart,arrivee))




if __name__ == '__main__':
	main()


    


