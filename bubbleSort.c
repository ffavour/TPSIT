#include <stdio.h>
#include <stdlib.h>

/*Compito per il 10 ottobre: procedere all'ordinamento di un array di interi utilizzando l'algoritmo
 * di bubble sort senza l'utilizzo di partentesi quadre (ad esclusione della dichiarazione dell'array)
 * author: Favour Osasere*/

#define DIM 5

void caricaVett(int *vett, int dim){
    for(int k = 0; k < dim; k++){
        printf("inserire un numero: ");
        scanf("%d", &(*(vett + k)));
    }
}

void visVett(int *v, int dim){
    for(int k = 0; k < dim; k++){
        printf("%d ", *(v + k));
    }
}

void bubbleSort(int *v, int dim){
    int temp;

    for(int k = 0; k < dim; k++){
        for(int j = k + 1; j < dim; j++){
            if(*(v + k) > *(v + j)){
                temp = *(v + k);
                *(v + k) = *(v + j);
                *(v + j) = temp;
            }
        }

    }
}

int main() {

    int vett[DIM];
    int *v = vett;

    caricaVett(v, DIM);
    visVett(v, DIM);
    printf("\nvettore ordinato\n");
    bubbleSort(v, DIM);
    visVett(v, DIM);

    return 0;
}
