#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*-Creare un file .csv con COGNOME, NOME, NASCITA (annomesegiorno in formato INT)
-scorrere il file con la funzione FGETS e STRTOK
-stampare in ordine DECRESCENTE (dal più grande al più piccolo)
 utilizzando i puntatori e allocazione dinamica (MALLOC)
 */

#define LUNG 1024 //max caratteri per riga
#define DIM 10 //max persone

typedef struct {
    char* cognome;
    char* nome;
    int data;
}Persone;

int contaRighe(){
    FILE* fp;
    int righe = 0;
    char c[LUNG];
    char* riga = c;

    fp = fopen("..\\file.csv", "r");

    //test sulla corretta apertura del file
    if(fp != NULL){
        //scorro il file con FGETS
        while(fgets(riga, LUNG, fp))
        {
            righe++;
        }
    }else
        printf("Il file non esiste.\n");

    fclose(fp);

    return righe;
}

void letturaDaFile(Persone *p, int dim){
    FILE *fp = fopen("..\\file.csv", "r");
    char c[LUNG];
    char* riga = c;
    Persone* posizione = p;  //salva la posizione iniziale del puntatore

    if(fp == NULL){
        printf("il file non esiste.\n");
    } else{
        while (!feof(fp)){
            fgets(riga, LUNG, fp);

            p->cognome = strdup(strtok(riga, ","));
            p->nome = strdup(strtok(NULL, ","));
            p->data = atoi(strtok(NULL, ","));

            printf("\ncognome: %s\nnome: %s\ndata di nascita: %d\n", p->cognome, p->nome, p->data);
            p++;
        }
        p = posizione;

    }

}

void scambio(Persone *x, Persone *y){
    Persone temp;

    *x = temp;
    *x = *y;
    *y = temp;
}

void bubbleSort(Persone *p, int dim){
    Persone* posizione = p;

    for(int k = 0; k < dim; k++){
        for(int j = k + 1; j < dim; j++){
            if(p->data < (p + 1)->data){
                scambio(p, (p + 1));
            }
            p++;
        }
    }
    p = posizione;
}

void visualizza(Persone *p, int dim){
    Persone* posizione = p;

    for(p = posizione; p < posizione + dim; p++){
        printf("\nnome: %s \ncognome: %s \ndata di nascita: %d\n\n", p->cognome, p->nome, p->data);
    }
    p = posizione;
}



int main() {
    Persone *p;
    int righe;

    //conta le righe
    righe = contaRighe();
    //printf("le righe sono %d", righe);

    //crea vettore con malloc
    p = (Persone*)malloc(righe * sizeof (Persone));
    letturaDaFile(p, righe);

    //ordina e stampa
    bubbleSort(p, righe);
    printf("\npersone ordinate per data di nascita: \n\n");
    visualizza(p, righe);

    return 0;
}
