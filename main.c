#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*Creare un programma in linguaggio C che legga il file vgsales.csv e lo importi in un array di strutture.
Ogni riga contiene i campi separati da virgole, per cui può essere comodo creare una funzione split
che dalla riga letta ritorni la struttura valorizzata.*/

#define NGIOCHI 16599 //numero di giochi
#define DIM 1024      //caratteri per riga

typedef char Stringa[DIM];

typedef struct{
    int rank;
    char* name;
    char* platform;
    int year;
    char* genre;
    char* publisher;
    float NASales;
    float EUSales;
    float JPSales;
    float otherSales;
    float globalSales;
}Videogioco;


int main()
{
    Videogioco *v;
    Stringa riga;

    v = (Videogioco*)malloc(NGIOCHI * sizeof (Videogioco));

    FILE *fp;
    fp = fopen("..\\vgsales.csv", "r");

    //controlla se file esiste
    if(fp == NULL){
        printf("il file non esiste.\n");
    }else{
        int k = 0;

        while (!feof(fp)){
            fgets(riga, DIM, fp);
            //conto lunghezza riga e creo array della 1 riga con malloc
            //dopo 1° giro faccio realloc

            (*(v + k)).rank = atoi(strtok(riga, ","));
            (*(v + k)).name = strtok(NULL, ",");
            (*(v + k)).platform = strtok(NULL, ",");
            (*(v + k)).year = atoi(strtok(NULL, ","));
            (*(v + k)).genre = strtok(NULL, ",");
            (*(v + k)).publisher = strtok(NULL, ",");
            (*(v + k)).NASales = atof(strtok(NULL, ","));
            (*(v + k)).EUSales = atof(strtok(NULL, ","));
            (*(v + k)).JPSales = atof(strtok(NULL, ","));
            (*(v + k)).otherSales = atof(strtok(NULL, ","));
            (*(v + k)).globalSales = atof(strtok(NULL, ","));

            printf("\n %d, %s, %s, %d, %s, %s, %.2f, %.2f, %.2f, %.2f, %.2f \n", (*(v + k)).rank, (*(v + k)).name, (*(v + k)).platform, (*(v + k)).year,
                   (*(v + k)).genre, (*(v + k)).publisher, (*(v + k)).NASales, (*(v + k)).EUSales, (*(v + k)).JPSales, (*(v + k)).otherSales, (*(v + k)).globalSales);

            k++;

        }

    }

    free(v);
    fclose(fp);
    return 0;
}
