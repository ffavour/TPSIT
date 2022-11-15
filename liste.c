/*crea  una  lista e la  stampa*/

//osasere favour


#include  <stdio.h>
#include  <stdlib.h>

typedef struct node {
    int valore;
    struct node *next;
} Node;

void stampa(Node *lista){
    Node *l;
    l = lista;  //l è una variabile di appoggio
    printf("numeri  inseriti: \n");
    while (l != NULL) {
        printf("%d - %p \n", l->valore, l->next);
        l = l->next;  //al puntatore viene assegnato valore di l->next, se è null finisce il ciclo
    }
    printf("\n");
}
int lunghezza(Node *lista){
    int cont;
    Node *l;
    l = lista;
    while (l != NULL){
        l = l->next;
        cont++;
    }

    return cont;
}

int main() {
    int n;
    int contN = 0;
    Node *lista;
    Node *l;
    lista = NULL;

    do {
        printf("Inserisci  un  naturale o  -1 per  terminare\n");
        scanf("%d", &n);

        if (n >= 0) {
            if (lista == NULL) /*  prima  iterazione  */
            {
                lista = (Node *) malloc(sizeof(Node));
                l = lista; //puntatore d'appogggio l che punta a lista
            } else /*  iterazioni  successive  */
            {
                l->next = (Node *) malloc(sizeof(Node));
                l = l->next;
            }
            l->valore = n;
            l->next = NULL;
        }
    } while (n >= 0);

    stampa(lista);

    //conta elementi in lista
    contN = lunghezza(lista);
    printf("\nci sono %d elementi", contN);



    return 0;
}
