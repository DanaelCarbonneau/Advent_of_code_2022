#include<stdio.h>
#include<string.h>


char* nom_fichier = "input_10.txt";
int CRT[6][40];


void dessiner_pixel_CRT(int j, int reg_X){

    if ( (j >= reg_X -1 ) && (j <= reg_X+1)  ){
        printf("#");
    }
    else{
        printf(" ");
    }
}

void affichage_CRT(char* filename){
    //Ouverture du fichier
    FILE* f = fopen(filename,"r");
    
   

    //Simule le registre X
    int reg_X = 1;

    //on compte le nombre de cycles
    int compte_cycle = 0;

    //Buffers
    char buffer[256];
    char operation[256];

    //Indices de parcours sur le CRT    
    int i = 0;
    int j = 0;
    
    
    do{     //On lit chaque ligne

        fgets(buffer,256,f);
        int imm;

        //Cas où l'opération est une addition
        if (sscanf(buffer,"%s %d",operation,&imm) ==2){
            //On simule le passage d'un premier cycle
            compte_cycle+=1;
            
            //Après chaque cycle on dessine un nouveau caractère sur le CRT
            dessiner_pixel_CRT(j,reg_X);
            j+=1;
            if (j == 40) {
                j = 0;
                i+=1;
                printf("\n");
            }
           

            //Simulation du passage d'un cycle
            compte_cycle+=1;
            //Après chaque cycle on dessine un nouveau caractère sur le CRT
            dessiner_pixel_CRT(j,reg_X);
            j+=1;
            if (j == 40) {
                j = 0;
                i+=1;
                printf("\n");
            }


            reg_X +=imm;    //reg_X+= i aura bien pris deux cycles à se réaliser
        }
        else{
            //Autre cas : noop, qui prend un cycle en ne faisant rien d'autre
            compte_cycle+=1;

            //Après chaque cycle, on dessine un caractère sur le CRT
            dessiner_pixel_CRT(j,reg_X);
            j+=1;
            if (j == 40) {
                j = 0;
                i+=1;
                printf("\n");
            }

           
        }

    }while(strcmp(buffer,"~")!=0);

    fclose(f);

}






int main(){

    affichage_CRT(nom_fichier);

    return 0;
}