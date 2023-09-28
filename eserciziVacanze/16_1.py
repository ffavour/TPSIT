"""Scrivete una funzione di nome moltiplica_tempo che accetti un oggetto Tempo e un numero, e restituisca un nuovo
oggetto Tempo che contiene il prodotto del Tempo iniziale per il numero. Usate poi moltiplica_tempo per scrivere una
funzione che prenda un oggetto Tempo che rappresenta il tempo finale di una gara, e un numero che rappresenta la
distanza percorsa, e restituisca un oggetto Tempo che rappresenta la media di gara (tempo al chilometro)"""


class Tempo:
    def __init__(self, tempo):
        self.tempo = tempo


def moltiplica_tempo(tempo, numero):
    nuovoTempo = tempo.tempo * numero
    return Tempo(nuovoTempo)


def mediaGara(tempoFin, distanza):
    tempoChilometro = moltiplica_tempo(tempoFin, 1 / distanza)
    return tempoChilometro


def main():
    t1 = Tempo(4)
    t2 = moltiplica_tempo(t1, 5)
    print(t2.tempo)

    t3 = mediaGara(t2, 30)
    print(t3.tempo)


if __name__ == "__main__":
    main()
