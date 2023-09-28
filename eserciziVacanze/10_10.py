""". Per controllare se una parola è contenuta in un elenco, è possibile usare l’operatore
in, ma è un metodo lento, perché ricerca le parole seguendo il loro ordine.
Dato che le parole sono in ordine alfabetico, possiamo accelerare l’operazione con una ricerca binaria
(o per bisezione), che è un po’ come cercare una parola nel vocabolario. Partite nel mezzo e controllate
se la parola che cercate viene prima o dopo la parola di metà elenco. Se prima, cercherete nella prima
metà nello stesso modo, se dopo, cercherete nella seconda metà.
Ad ogni passaggio, dimezzate lo spazio di ricerca. Se l’elenco ha 113.809 parole, ci vorranno circa
17 passaggi per trovare la parola o concludere che non c’è.
Scrivete una funzione di nome bisezione che richieda una lista ordinata e un valore da ricercare,
e restituisca True se la parola fa parte della lista, o False se non è presente.
Oppure, potete leggere la documentazione del modulo bisect e usare quello! Soluzione: http:
// thinkpython2. com/ code/ inlist. py ."""

import bisect


def leggiFile():
    file = open("file/words.txt", "r")
    parole = file.read()
    file.close()

    return parole.split()


def ricercaBinaria(lista, elemento):
    lista.sort()
    indice = bisect.bisect_left(lista, elemento)
    if indice < len(lista) and lista[indice] == elemento:
        return True
    return False


def main():
    print(ricercaBinaria([1, 3, 4, 5, 7, 9], 5))

    parole = leggiFile()
    print(parole)

    pUtente = input("inserire parola da cercare: ")

    if ricercaBinaria(parole, pUtente):
        print(f"{pUtente} è presente nell'elenco")
    else:
        print(f"{pUtente} non è presente nell'elenco")


if __name__ == "__main__":
    main()
