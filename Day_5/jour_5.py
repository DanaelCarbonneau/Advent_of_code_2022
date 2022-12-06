def instruction_une_ligne(tab_pile, s_ligne : str):
    """Fonction qui applique l'opération de la ligne passée en paramètre au tableau de piles représentant notre situation"""
    
    ligne = s_ligne.split()
    if (ligne != []) : 
        nb_depl = int(ligne[1])
    else :
        nb_depl = 0
    for i in range ( nb_depl ) :
        elt = tab_pile[ int(ligne[3]) -1 ].pop()
        tab_pile[ int(ligne[5])-1].append(elt)
    
    return tab_pile

def instruction_une_ligne_2(tab_pile, s_ligne : str):
    """Fonction qui applique l'opération de la ligne passée en paramètres en ajoutant les présupposés de la partie 2"""
    ligne = s_ligne.split()

    if (ligne != []) : 
        nb_depl = int(ligne[1])
    else :
        nb_depl = 0
    
    pile_ligne = []
    for i in range ( nb_depl ) :
        elt = tab_pile[ int(ligne[3]) -1 ].pop()
        pile_ligne.append(elt)

    for i in range (nb_depl):
        elt = pile_ligne.pop()
        tab_pile[ int(ligne[5])-1].append(elt)
    
    return tab_pile



def toutes_les_instructions(tab_pile, instructions : str):
    """Fonction qui applique toutes les instructions de la chaîne instructions au tableau de piles représentant notre situation"""
    l_instuctions = instructions.split("\n")

    for ins in l_instuctions : 
        tab_pile = instruction_une_ligne(tab_pile,ins)
    
    return tab_pile


def toutes_les_instructions_2(tab_pile, instructions : str):
    """Fonction qui applique toutes les instructions de la chaîne instructions au tableau de piles représentant notre situation"""
    l_instuctions = instructions.split("\n")

    for ins in l_instuctions : 
        tab_pile = instruction_une_ligne_2(tab_pile,ins)
    return tab_pile

def initialiser_piles_instructions(filename : str):
    """Fonction qui initialise la pile manuellement et les instructions à partir du fichier"""

    with open(filename, 'r') as f:
        fichier = f.read()
        deux_parties = fichier.split("\n\n")
        
        tab_piles = [[], [], [], [], [], [], [], [], [] ]
        tab_piles[0] = ['R','G','J','B','T','V','Z']
        tab_piles[1] = ['J','R','V','L']
        tab_piles[2] = ['F','Q','S']
        tab_piles[3] = ['Z','H','N','L','F','V','Q','G']
        tab_piles[4] = ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W']
        tab_piles[5] = ['S', 'W', 'T', 'C', 'H', 'F']
        tab_piles[6] = ['D','Z','C','V','F','N','J']
        tab_piles[7] = ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q']
        tab_piles[8] = [ 'J', 'B', 'Q','V','P']

        print(tab_piles)
        instructions = deux_parties[1]

        return (tab_piles,instructions)




def main():

    (tab_piles, instructions) = initialiser_piles_instructions("input_5.txt")

    #tab_piles = toutes_les_instructions(tab_piles,instructions)

    tab_piles = toutes_les_instructions_2(tab_piles,instructions)
    print(tab_piles)

    res = ""

    for pile in tab_piles:
        res += pile.pop()
    
    print(res)
    

if __name__ == '__main__':
	main()

