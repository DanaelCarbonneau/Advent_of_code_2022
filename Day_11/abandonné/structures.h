#ifndef STRUCTURES_H
#define STRUCTURES_H

#include<stdio.h>
#include<stdlib.h>

typedef struct _c_fifo{
    long long int n;           //Représente le niveau d'inquiétude dans notre problème
    struct _c_fifo* precedent;
    struct _c_fifo* suivant;
} c_fifo;

typedef struct _fifo{
    c_fifo* premier;
    c_fifo* dernier;
}fifo;


/*Fonction permettant de créer une cellule de la file d'attente*/
c_fifo* creer_cellule(long long int n);

/*Fonction permettant de créer une file vide*/
fifo* creer_file();


/*Fonction permettant d'ajouter la cellule en tête de al file*/
fifo* ajout_tete(fifo* file, c_fifo* cellule);

/*Fonction permettant de retirer le premier élément de la file*/
c_fifo* retrait_tete(fifo* file);

/*Fonction permettant de retirer le dernier élément de la file*/
c_fifo* retrait_queue(fifo* file);

/*Fonction permettant d'ajouter la cellule en queue de la file*/
fifo* ajout_queue(fifo* file, c_fifo* cellule);

/*Fonction permettant d'afficher la file passée en paramètres*/
void afficher_fifo(fifo* file);

/*Fonction permettant de libérer la mémoire allouée à une file*/
void supprimer_fifo(fifo* file);


typedef struct _singe{
    int num ;           //Numéro du singe
    fifo* objets;       //Objets que le singe a en sa possession
    char type_ope;      //type d'opération effectuée
    int  nb_ope;        //Nombre avec lequel s'effectue l'opération
    int test_div;       //Nombre avec lequel le test de divisibilité s'effectue

    int dest_true;      //Numéro du singe destination si le test est vrai
    int dest_false;     //Numéro du singe destination si le test est faux
    int cpt_objts ;      //Compte le nombre d'objets manipulés par un singe
}singe;

/*Créé un singe avec toutes ses informations*/
singe* creer_singe(int num, fifo* objets, char type_ope, int nb_ope, int test_div, int dest_true, int dest_false);

/*Fonction affichant toutes les informations d'un singe*/
void afficher_singe(singe* singe);

/*Fonction permettant de libérer la mémoire allouée à un singe*/
void supprimer_singe(singe* singe);

/*Reproduit le tour effectué par le singe*/
void tour_singe(singe* s, singe ** tab_singes);





#endif
