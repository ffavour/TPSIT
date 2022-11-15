#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    char* name;
    struct node* next;  //con n minuscola pk la definizione di Node è nella riga successiva
}Node;

int main() {
    Node* lista;
    Node *temp;

    lista = (Node*)malloc(sizeof(Node));
    temp = (Node*)malloc(sizeof(Node));

    printf("inserisci il nome(1): ");
    fflush(stdin);
    scanf("%s", lista->name);
    printf("nome1: %s", lista->name);
    lista[0].next = NULL;

    printf("\ninserisci il nome(2): ");
    fflush(stdin);
    scanf("%s", temp->name);
    printf("nome2: %s ", temp->name);
    temp->next = NULL;
    lista->next = temp;  //operazione di link, concateniamo le strutture

    printf("\ninserisci il nome(3): ");
    fflush(stdin);
    scanf("%s", temp->name);
    printf("nome3: %s ", temp->name);
    temp->next = NULL;

    lista->next->next = temp;

    printf("\nlista concatenata1: %s", lista->next->name);
    printf("\nlista concatenata2: %s", lista->next->next->name);

    free(lista);
    free(temp);
    return 0;
}
