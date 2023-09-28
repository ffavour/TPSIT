"""Esercizio 7.1. Copiate il ciclo del Paragrafo 7.5 e incapsulatelo in una funzione di nome mia_radq
che prenda a come parametro, scelga un valore appropriato di x, e restituisca una stima del valore
della radice quadrata di a.Quale verifica, scrivete una funzione di nome test_radq che stampi una tabella come questa:

a   mia_radq(a)   math.sqrt(a)  diff
-   ----------    ------------  ----
1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0           2.0           0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0           3.0           0.0

La prima colonna è un numero, a; la seconda è la radice quadrata di a calcolata con mia_radq; la
terza è la radice quadrata calcolata con math.sqrt; la quarta è il valore assoluto della differenza trale due stime
"""
import math


def mia_radq(x):
    a = x
    while True:
        # print(f"x = {x}")
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def trovaLughezzaMax(riga):
    l = []
    for elemento in riga:
        l.append(len(str(elemento)))
    maxL = max(l)
    return maxL


def aggiungiSpazi(riga, lunghezza):
    rigaNuova = []

    for elemento in riga:
        while len(str(elemento)) < lunghezza:
            elemento += " "
        rigaNuova.append(elemento)
    return rigaNuova


def stampaTabella(x, miaRQ, lMath, diff):

    for k in range(9):
        print(x[k], miaRQ[k], lMath[k], diff[k])


def creaTabella(datiTabella):
    intestazioneColonne = ["a", "mia_radq(a)", "math.sqrt(a)", "diff"]
    trattini = []

    # crea trattini per intestazione
    for elemento in intestazioneColonne:
        nTrattini = len(elemento)
        t = "-" * nTrattini
        trattini.append(t)

    # aggiunge intestazione e trattini
    for k in range(len(datiTabella)):
        datiTabella[k].insert(0, intestazioneColonne[k])
        datiTabella[k].insert(1, trattini[k])

    # trova la lunghezza max per ogni riga
    lunghezzeMax = []
    for k in range(len(datiTabella)):
        lMax = trovaLughezzaMax(datiTabella[k])
        lunghezzeMax.append(lMax)

    # rende ogni riga della stessa lunghezza
    for k in range(len(lunghezzeMax)):
        datiTabella[k] = aggiungiSpazi(datiTabella[k], lunghezzeMax[k])

    return datiTabella

def test_radq():
    valori_x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    listaMia_radq = []
    listaMath = []
    listaDiff = []

    datiTabella = []

    for x in valori_x:
        radq_mia = mia_radq(x)
        listaMia_radq.append(str(radq_mia))

        radq_math = math.sqrt(x)
        listaMath.append(str(radq_math))

        diff = abs(radq_mia - radq_math)
        listaDiff.append(str(diff))

    datiTabella.append(valori_x)
    datiTabella.append(listaMia_radq)
    datiTabella.append(listaMath)
    datiTabella.append(listaDiff)

    tabellaNuova = creaTabella(datiTabella)
    stampaTabella(tabellaNuova[0], tabellaNuova[1], tabellaNuova[2], tabellaNuova[3])


def main():
    radiceQ = mia_radq(4)
    print(f"radice quadrata: {radiceQ}")

    test_radq()


if __name__ == '__main__':
    main()
