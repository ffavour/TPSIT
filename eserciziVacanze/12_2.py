"""1. Scrivete un programma che legga un elenco di parole da un file (vedi Paragrafo 9.1) e stampi
tutti gli insiemi di parole che sono tra loro anagrammabili.
Un esempio di come si può presentare il risultato:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Suggerimento: potete costruire un dizionario che faccia corrispondere un gruppo di lettere con
una lista di parole che si possono scrivere con quelle lettere. Il problema è: come rappresentare
il gruppo di lettere in modo che possano essere usate come chiave?
2. Modificate il programma in modo che stampi la lista di anagrammi più lunga per prima,
seguita dalla seconda più lunga, e così via.
3. Nel gioco da tavolo Scarabeo, fate un “en-plein” quando giocate tutte le sette lettere sul vostro
leggio formando, insieme a una lettera sul tavolo, una parola di otto lettere. Con quale gruppo
di 8 lettere si può fare un “en-plein” con maggior probabilità? Suggerimento: il gruppo dà
sette combinazioni.
Soluzione: http: // thinkpython2. com/ code/ anagram_ sets. py ."""


def leggiFile():
    file = open("file/words.txt", "r")
    parole = file.read()
    file.close()

    return parole.split()


def isAnagramma(parola1, parola2):
    return sorted(parola1) == sorted(parola2)


def trova_anagrammi(parole):
    anagrammi = []
    for i in range(len(parole)):
        for j in range(i + 1, len(parole)):
            if isAnagramma(parole[i], parole[j]):
                anagrammi.append((parole[i], parole[j]))
    return anagrammi


def stampa_anagrammi(anagrammi):
    if len(anagrammi) == 0:
        print("Nessun insieme di parole anagrammabili trovato.")
    else:
        print("Insiemi di parole anagrammabili trovati:")
        for coppia in anagrammi:
            print(coppia)


def main():
    parole = leggiFile()
    print(parole)

    paroleAnagrammi = trova_anagrammi(parole)
    stampa_anagrammi(paroleAnagrammi)


if __name__ == "__main__":
    main()
