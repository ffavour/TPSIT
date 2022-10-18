#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*-Creare un file .csv con COGNOME, NOME, NASCITA (annomesegiorno in formato INT)
-scorrere il file con la funzione FGETS e STRTOK
-stampare in ordine DECRESCENTE (dal più grande al più piccolo)
 utilizzando i puntatori e allocazione dinamica (MALLOC)
 */

#define LUNG 1024 //max caratteri per riga
#define DIM 4 //max persone

typedef struct {
    int anno;
    int mese;
    int giorno;
}Nascita;

typedef struct {
    char* cognome;
    char* nome;
    Nascita n;
}Persone;

void letturaDaFile(Persone *p, char* riga){
    FILE *fp = fopen("..\\file.csv", "r");

    if(fp == NULL){
        printf("il file non esiste.\n");
    } else{
        int k = 0;

        p = (Persone*) malloc(DIM * sizeof (Persone));
        while (!feof(fp)){
            fgets(riga, LUNG, fp);

            (*(p + k)).cognome = strtok(riga, ",");
            (*(p + k)).nome = strtok(NULL, ",");
            (*(p + k)).n.anno = atoi(strtok(NULL, ","));
            (*(p + k)).n.mese = atoi(strtok(NULL, ","));
            (*(p + k)).n.giorno = atoi(strtok(NULL, ","));

            printf("\ncognome: %s\nnome: %s\ndata di nascita: %d-%d-%d\n", (*(p + k)).cognome, (*(p + k)).nome, (*(p + k)).n.anno,
                   (*(p + k)).n.mese, (*(p + k)).n.giorno);
            k++;
        }
    }

}

void scambio(Persone *x, Persone *y){
    Persone temp;

    *x = temp;
    *x = *y;
    *y = temp;
}

void bubbleSort(Persone *p, int dim){

    for(int k = 0; k < dim; k++){
        for(int j = k + 1; j < dim; j++){
            if((p + k)->n.anno < (p + j)->n.anno){
                scambio((p + k), (p + j));
            }
        }
    }
}


void visualizza(Persone *p, int dim){
    for(int k = 0; k < dim; k++){
        printf("\nnome: %s \ncognome: %s \ndata di nascita: %d-%d-%d\n\n", (*(p + k)).cognome, (*(p + k)).nome, (*(p + k)).n.anno,
               (*(p + k)).n.mese, (*(p + k)).n.giorno);
    }
}

int main() {
    //Persone *p;
    Persone p[DIM];
    char riga[LUNG];

    letturaDaFile(&p, &riga);
    bubbleSort(&p, DIM);
    visualizza(&p, DIM);
    //bubbleSort(&p, DIM);

    return 0;
}
