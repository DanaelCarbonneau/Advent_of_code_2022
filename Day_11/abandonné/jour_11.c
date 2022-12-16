#include"structures.h"


int main(){
    singe** tab_singes = (singe**) malloc(4* sizeof(singe*));


    fifo* l = creer_file();

    c_fifo* c = creer_cellule(98);
    ajout_tete(l,c);
    c = creer_cellule(79);
    ajout_tete(l,c);

    tab_singes[0] = creer_singe(0,l,'*',19,23,2,3);


    fifo* l2 = creer_file();
    int val[4] = {54, 65, 75, 74};
    for (int i = 0 ; i < 4 ; i++){
        c = creer_cellule(val[i]);
        ajout_tete(l2,c);
    }
    tab_singes[1] = creer_singe(1,l2,'+',6,19,2,0);


    fifo* l3 = creer_file();
    int val_2[3] = {79, 60, 97};
    for (int i = 0 ; i < 3 ; i++){
        c = creer_cellule(val_2[i]);
        ajout_tete(l3,c);
    }
    tab_singes[2] = creer_singe(2,l3,'^',2,13,1,3);


    fifo* l4 = creer_file();
    c = creer_cellule(74);
    ajout_tete(l4,c);
    tab_singes[3] = creer_singe(3,l4,'+',3,17,0,1);

    for (int s = 0 ; s < 4 ; s++){
        afficher_singe(tab_singes[s]);
    }


    printf("\n=====Début du jeu=====\n");

    for (int i = 0 ; i < 20 ; i++){
        for (int s = 0 ; s < 4 ; s++){
             
            tour_singe(tab_singes[s],tab_singes);
        }
    }

    for (int s = 0 ; s < 4 ; s++){
        afficher_singe(tab_singes[s]);
    }

}