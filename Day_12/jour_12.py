from pprint import*

from collections import deque

def dijkstra(graph, vertex):
    queue = deque([vertex])
    distance = {vertex: 0}
    while queue:
        t = queue.popleft()
        print("On visite le sommet " + str(t))
        for voisin in graph[t]:
                queue.append(voisin)
                nouvelle_distance = distance[t] + graph[t][voisin]
                if(voisin not in distance or nouvelle_distance < distance[voisin]):
                    distance[voisin] = nouvelle_distance
                    print("Met à jour le sommet " + str(voisin) + " avec la distance : " + str(nouvelle_distance))
                    
    return distance

#Liste d'ajacence du graphe
graph = {'A':{'B':15,'C':4},'B':{'E':5},'C':{'E':11,'D':2},'D':{'E':3},'E':{}}
distance = dijkstra(graph,'A')
print("Distances" + str(distance))



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
                print("i = " + str(i) + "len(liste_ligne) = " + str(len(liste_ligne)))
                if (i+1 < len(liste_ligne)) and (liste_ligne[i][j] == liste_ligne[i+1][j] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i+1][j])):
                    liste_adj[cpt_sommets].append(cpt_sommets + len(liste_ligne))

                if j+1 < len(liste_ligne[i]) and (liste_ligne[i][j] == liste_ligne[i][j+1] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i][j+1])):
                    liste_adj[cpt_sommets].append(cpt_sommets + 1)
                
                if i > 0 and (liste_ligne[i][j] == liste_ligne[i-1][j] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i-1][j])):
                    liste_adj[cpt_sommets].append(cpt_sommets - len(liste_ligne))
                
                if j > 0 and (liste_ligne[i][j] == liste_ligne[i][j-1] or ord(liste_ligne[i][j])+1 == ord(liste_ligne[i][j-1])):
                    liste_adj[cpt_sommets].append(cpt_sommets - 1)


                if liste_ligne[i][j] == 'E':
                    place_dest = cpt_sommets
                cpt_sommets+=1
                j+=1

            cpt_ligne +=1
            i+=1

        return (liste_adj, place_dest)


        

def main():
    (graphe, place_dest) = recuperer_graphe()
    d_graphe = {}

    for s in graphe :
        voisins = {}
        for voisin in s :
            print(voisin)
            voisin[voisin] = 1
        

    pprint(d_graphe)
    



if __name__ == '__main__':
	main()
