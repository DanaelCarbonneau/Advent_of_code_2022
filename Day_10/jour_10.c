#include<stdio.h>
#include<string.h>


char* nom_fichier = "input_10.txt";

int somme_longueur_signal(char* filename){
    //Ouverture du fichier
    FILE* f = fopen(filename,"r");

    //résultat
    int somme_longueurs = 0;

    //Simule le registre X
    int reg_X = 1;

    //on compte le nombre de cycles
    int compte_cycle = 0;

    //Buffers
    char buffer[256];
    char operation[256];

    
    
    do{     //On lit chaque ligne

        fgets(buffer,256,f);
        int imm;

        //Cas où l'opération est une addition
        if (sscanf(buffer,"%s %d",operation,&imm) ==2){
            //On simule le passage d'un premier cycle
            compte_cycle+=1;
            
            //Après chaque cycle on vérifie si on est sur une valeur de cycle à noter
            if ((compte_cycle -20)%40 == 0){
                somme_longueurs += reg_X*compte_cycle;
            }

            //Simulation du passage d'un cycle
            compte_cycle+=1;
            //printf("Là on a modifié la valeur du registre : %d\n",reg_X);
            //Après chaque cycle on vérifie si on est sur une valeur de cycle à noter
            if ((compte_cycle -20)%40 == 0){
                somme_longueurs += reg_X*compte_cycle;

            }

            reg_X +=imm;    //reg_X+= i aura bien pris deux cycles à se réaliser
        }
        else{
            //Autre cas : noop, qui prend un cycle en ne faisant rien d'autre
            compte_cycle+=1;

            //Après chaque cycle on vérifie si on est sur une valeur de cycle à noter
            if ((compte_cycle -20)%40 == 0){
                somme_longueurs += reg_X*compte_cycle;
            }
        }
    }while(strcmp(buffer,"~")!=0);

    fclose(f);

    return somme_longueurs;
}






int main(){

    printf("%d",somme_longueur_signal(nom_fichier));

    return 0;
}