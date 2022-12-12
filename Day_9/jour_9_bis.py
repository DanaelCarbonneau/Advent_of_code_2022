from pprint import*


def ecart(tete,queue):
    """Fonction qui retourne vrai s'il y a un écart nécessitant déplacement entre la tête et la queue"""
    return tete[0] - queue[0] > 1 or tete[0] - queue[0] < -1 or tete[1]-queue[1] > 1 or tete[1] - queue[1] < -1

def rapproche(coord_q, coord_t):
    if coord_q > coord_t:
        return coord_q -1
    else:
        return coord_q +1

def avancer_selon_instruction(tete, instruction):
    """Retourne la position de la tête après l'instruction"""


    if instruction == "U" :
        x_t = tete[0]+1
        y_t = tete[1]
        tete = (x_t,y_t)
        
    if instruction == "D" :
        x_t = tete[0]-1
        y_t = tete[1]
        tete = (x_t,y_t)
        
    
    if instruction == "L" :
        x_t = tete[0]
        y_t = tete[1]-1
        tete = (x_t,y_t)
        
    
    if instruction == "R" :
        x_t = tete[0]
        y_t = tete[1]+1
        tete = (x_t,y_t)
    


    return tete

def suivre_instructions(liste_instructions):
    tab_coordonnées = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0), (0,0)]
    ens_position_queue = set()

    for instruction in liste_instructions :
        for i in range (int(instruction[1])):
            tete = avancer_selon_instruction(tab_coordonnées[0],instruction[0])
            tab_coordonnées[0] = tete
            for j in range (len(tab_coordonnées)-1):

                x_suiv = tab_coordonnées[j+1][0]
                y_suiv = tab_coordonnées[j+1][1]

                if ecart(tab_coordonnées[j], tab_coordonnées[j+1]):

                    if tab_coordonnées[j][0]!= tab_coordonnées[j+1][0]:
                        x_suiv = rapproche(tab_coordonnées[j+1][0],tab_coordonnées[j][0])
                    
                    if tab_coordonnées[j][1] != tab_coordonnées[j+1][1]:
                        y_suiv = rapproche(tab_coordonnées[j+1][1],tab_coordonnées[j][1])
                    
                tab_coordonnées[j+1] = (x_suiv,y_suiv)

            print(tab_coordonnées) 
            ens_position_queue.add(tab_coordonnées[-1])

            #draw(tab_coordonnées[0],tab_coordonnées[-1])
    return ens_position_queue


def draw(tete, queue):
    for x in range(0,50):
        ligne = ""
        for y in range(0,60):
            if x == tete[0] and y == tete[1]:
                ligne+= "H"
            elif x == queue[0] and y == queue[1]:
                ligne+="T"
            else:
                ligne+="."
        print(ligne)
    print("\n")


def main():
    filename = input("Filename ?")
    with open(filename, 'r') as f:
        fichier = f.read()
        liste_ligne = fichier.split("\n")
        liste_instructions = []

        for ligne in liste_ligne:
            liste_instructions.append(ligne.split(" "))

        res = suivre_instructions(liste_instructions)
        


        print("Nombre de positions prises par T :" + str(len(res)))




if __name__ == '__main__':
	main()


    

    
    
    
        

