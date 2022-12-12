from pprint import*

#REVOIR LA GESTION DES COINS ET DU SUIVI PAR LA QUEUE (ne considère pas qu'elle puisse bouger en diagonale)
#la tête suit le bon chemin !


def ecart(tete,queue):
    """Fonction qui retourne vrai s'il y a un écart nécessitant déplacement entre la tête et la queue"""
    return tete[0] - queue[0] > 1 or tete[0] - queue[0] < -1 or tete[1]-queue[1] > 1 or tete[1] - queue[1] < -1

def rapproche(coord_q, coord_t):
    if coord_q :
        return a -1
    else:

def avancer_selon_instruction(tete,queue, instruction):
    """Retourne le couple de couples de coordonnées (tete, queue)  après l'instruction passée en paramètres"""


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
    

    x_q = queue[0]
    y_q = queue[1]
    if ecart(tete,queue):
        if tete[0] != queue[0]:
            x_q = rapproche(queue[0], tete[0])
        if tete[1] != queue[1]:
            y_q = rapproche(queue[1], tete[1])
    
    queue = (x_q,y_q)
    print("Position finale: ")
    print( tete)
    print(queue)

    return (tete,queue)


def suivre_instructions(liste_instructions):
    
    tete = (0,0)
    queue = (0,0)
    ens_position_queue = set()

    for instruction in liste_instructions :
        for i in range (int(instruction[1])):
            (t,q) = avancer_selon_instruction(tete,queue,instruction[0])
            tete = t
            queue = q

            ens_position_queue.add(queue)
            draw(tete,queue)
    return ens_position_queue


def draw(tete, queue):
    for x in range(0,5):
        ligne = ""
        for y in range(0,6):
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
        pprint(res)


        print("Nombre de positions prises par T :" + str(len(res)))




if __name__ == '__main__':
	main()


    

    
    
    
        

