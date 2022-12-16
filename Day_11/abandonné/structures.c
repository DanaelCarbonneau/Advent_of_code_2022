#include"structures.h"


/*Dans la fonction tour, il continue d'en retirer après la fin de la liste, voir
entre cette fonction et la fonction retrait tête.*/

c_fifo* creer_cellule(long long int n){
    c_fifo* cell = (c_fifo*) malloc(sizeof(c_fifo));

    cell->n = n;
    cell->precedent = NULL;
    cell->suivant = NULL;

    return cell;
}

fifo* creer_file(){
    fifo* file = (fifo*) malloc(sizeof(fifo));
    file->premier = NULL;
    file->dernier = NULL;
    return file;
}

fifo* ajout_tete(fifo* file, c_fifo* cellule){

    if (file->premier){
        cellule->suivant = file->premier;
        file->premier->precedent = cellule;
        file->premier = cellule;
    }
    else{
        file->premier = cellule;
        file->dernier = cellule;
    }
    return file;
}

c_fifo* retrait_tete(fifo* file){
    c_fifo* res = NULL;
    
    if(file->premier!=NULL){
        res = file->premier;
        
        file->premier = res->suivant;

        if (file->premier){
            file->premier->precedent = NULL;
        }
        if (res){
            res->suivant = NULL;
        }
    }
    afficher_fifo(file);
    return res;
}


fifo* ajout_queue(fifo* file, c_fifo* cellule){
    if(file->dernier){
        file->dernier->suivant = cellule;
        cellule->precedent = file->dernier;
        file->dernier = cellule;
    }   
    else{
        file->premier = cellule;
        file->dernier = cellule;
    }
    afficher_fifo(file);
    return file;
}

c_fifo* retrait_queue(fifo* file){
    c_fifo* res = NULL;
    if (file->dernier){
        if(file->dernier->n == file->premier->n){
            file->premier = NULL;
        }
        res = file->dernier;
        file->dernier = file->dernier->precedent;
        file->dernier->suivant = NULL;
        res->precedent = NULL;
    }
    return res;
}

void afficher_fifo(fifo* file){
    c_fifo* tmp = file->premier;
    while (tmp){
        printf("%lld -> ", tmp->n);
        tmp = tmp->suivant;
    }
    printf("\n");
}

void supprimer_fifo(fifo* file){
    c_fifo* tmp = file->premier;
    c_fifo* suiv;
    while (tmp){
        suiv = tmp->suivant;
        free(tmp);
        tmp = suiv;
    }
    free(file);   
}


singe* creer_singe(int num, fifo* objets, char type_ope, int nb_ope, int test_div, int dest_true, int dest_false){
    singe* res = (singe*) malloc(sizeof(singe));

    res->num = num;
    res->objets = objets;
    res->type_ope = type_ope;
    res->nb_ope = nb_ope;
    res->test_div = test_div;
    res->dest_true = dest_true;
    res->dest_false = dest_false;
    res->cpt_objts = 0;

    return res;
}

/*Fonction affichant toutes les informations d'un singe*/
void afficher_singe(singe* singe){
    printf("Singe %d\n",singe->num);
    printf("Liste d'objets : ");
    afficher_fifo(singe->objets);
    printf("Opération : new = old %c %d\n",singe->type_ope,singe->nb_ope);
    printf("Test : divisible par %d\n",singe->test_div);
    printf("\tSi vrai : jette au singe %d\n",singe->dest_true);
    printf("\tSi faux : jette au singe %d\n", singe->dest_false);
    printf("Il a manipulé %d objets\n",singe->cpt_objts);
    printf("\n");
}

/*Fonction permettant de libérer la mémoire allouée à un singe*/
void supprimer_singe(singe* singe){
    supprimer_fifo(singe->objets);
    free(singe);
}

/*Reproduit le tour effectué par le singe*/
void tour_singe(singe* s, singe** tab_singes){
    
    c_fifo* obj_manip;
    int i = 0;
    while(s->objets->premier){
        obj_manip = retrait_tete(s->objets);

        if (s->type_ope == '+'){
            obj_manip->n = obj_manip->n + s->nb_ope;
        }
        else if(s->type_ope == '*'){
            obj_manip->n = obj_manip->n * s->nb_ope;
        }
        else{
            obj_manip->n = obj_manip->n * obj_manip->n;
        }

        obj_manip->n = obj_manip->n / 3;
        
        if (obj_manip->n % s->test_div == 0){
            printf("Destination de l'objet : %d\n",s->dest_true);
            tab_singes[s->dest_true]->objets = ajout_tete(tab_singes[s->dest_true]->objets,obj_manip);
        }
        else{
            printf("Destination de l'objet : %d\n",s->dest_false);
            tab_singes[s->dest_false]->objets = ajout_tete(tab_singes[s->dest_false]->objets,obj_manip);
        }
        s->cpt_objts++;
        s->objets->premier;
        i++;
    }
}

