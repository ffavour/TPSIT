"""Nello slicing, si può specificare un terzo indice che stabilisce lo step o “passo”, cioè
il numero di elementi da saltare tra un carattere estratto e il successivo. Uno step di 2 significa
estrarre un carattere ogni 2 (uno sì, uno no), 3 significa uno ogni 3 (uno sì, due no), ecc.
 frutto = 'banana'
>>frutto[0:5:2]
'bnn'
Uno step di -1 fa scorrere all’indietro nella parola, per cui lo slicing [::-1] genera una stringa
scritta al contrario.
Usate questo costrutto per scrivere una variante di una sola riga della funzione palindromo
dell’Esercizio 6.3.
"""


def palindromo(parola):
    if parola[::-1] == parola:
        return True
    else:
        return False


def main():
    frutto = "banana"

    print(palindromo(frutto))


if __name__ == "__main__":
    main()
