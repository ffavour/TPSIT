"""Progettare un’applicazione che implementi una camera blindata virtuale protetta da una password costituita da un numero intero compreso tra 1 e 9999. La camera blindata viene attaccata da dei rapinatori che cercano di crackare la password che protegge la camera blindata. I rapinatori sono due e cercano di crackare la password in modo concorrente, il primo tentando tutti i numeri in modo crescente, il secondo provando con un numero alla volta in modo decrescente.
La camera blindata è controllata da una guardia che avrà bisogno di 10 secondi per raggiungere la camera blindata. Se i rapinatori non avranno indovinato la password entro questo lasso di tempo saranno bloccati, altrimenti, se uno dei rapinatori riuscirà ad indovinare la password prima che terminino i 10 secondi, tutti i malviventi riusciranno a fuggire.
Per ogni tentativo di crack della password i malviventi impiegheranno almeno 5 millisecondi.
Il poliziotto dovrà mostrare a video il suo nominativo e i secondi necessari per raggiungere la camera blindata. Inoltre se arriverà prima di 10 secondi, riuscendo a catturare i malfattori, dovrà visualizzare una frase appropriata alla situazione.
Se uno dei rapinatori dovesse indovinare la password, dovrà mostrare il suo nominativo e la password indovinata."""

import threading

def main():
    pass


if __name__ == "__main__":
    main()