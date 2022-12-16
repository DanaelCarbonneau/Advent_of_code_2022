#include"structures.h"


int main(){
    singe** tab_singes = (singe**) malloc(8* sizeof(singe*));

    c_fifo* c;

    /*singe_0*/
    fifo* o0 = creer_file();
    int val0[6] = {52, 78, 79, 63, 51, 94};
    for (int i = 0 ; i < 6 ; i++){
        c = creer_cellule(val0[i]);
        ajout_tete(o0,c);
    }
    tab_singes[0] = creer_singe(0,o0,'*',13,5,1,6);
    
    /*singe_1*/
    fifo* o1 = creer_file();
    int val1[5] = {77, 94, 70, 83, 53};
    for (int i = 0 ; i < 5 ; i++){
        c = creer_cellule(val1[i]);
        ajout_tete(o1,c);
    }
    tab_singes[1] = creer_singe(1,o1,'+',3,7,5,3);

    /*singe_2*/
    fifo* o2 = creer_file();
    int val2[3] = {98, 50, 76};
    for (int i = 0 ; i < 3 ; i++){
        c = creer_cellule(val2[i]);
        ajout_tete(o2,c);
    }
    tab_singes[2] = creer_singe(2,o2,'^',2,13,0,6);

    /*singe_3*/
    fifo* o3 = creer_file();
    int val3[8] = {92, 91, 61, 75, 99, 63, 84, 69};
    for (int i = 0 ; i < 8 ; i++){
        c = creer_cellule(val3[i]);
        ajout_tete(o3,c);
    }
    tab_singes[3] = creer_singe(3,o3,'+',5,11,5,7);

    /*singe_4*/
    fifo* o4 = creer_file();
    int val4[4] = {51, 53, 83, 52};
    for (int i = 0 ; i < 4 ; i++){
        c = creer_cellule(val4[i]);
        ajout_tete(o4,c);
    }
    tab_singes[4] = creer_singe(4,o4,'+',7,3,2,0);

    /*singe_5*/
    fifo* o5 = creer_file();
    int val5[2] = { 76, 76};
    for (int i = 0 ; i < 4 ; i++){
        c = creer_cellule(val5[i]);
        ajout_tete(o5,c);
    }
    tab_singes[3] = creer_singe(5,o5,'+',4,2,4,7);


    /*singe_6 */
    fifo* o6 = creer_file();
    int val6[7] = { 75, 59, 93, 69, 76, 96, 65};
    for (int i = 0 ; i < 7; i++){
        c = creer_cellule(val6[i]);
        ajout_tete(o6 ,c);
    }

    tab_singes[6] = creer_singe(6,o6,'*',19,17,1,3);


    /*singe_7*/
    fifo* o7 = creer_file();
    int val7 [1 ] = { 89};
    for (int i = 0 ; i < 1; i++){
        c = creer_cellule(val7[i]);
        ajout_tete(o7,c);
    }

    tab_singes[7] = creer_singe(7,o7,'+',2,19,2,4);




    printf("\n=====Début du jeu=====\n");

    for (int i = 0 ; i < 20 ; i++){
        for (int s = 0 ; s < 8 ; s++){
             
            tour_singe(tab_singes[s],tab_singes);
        }
    }

    for (int s = 0 ; s < 4 ; s++){
        afficher_singe(tab_singes[s]);
    }

}