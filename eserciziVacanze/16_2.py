"""Il modulo datetime fornisce l’oggetto time, simile all’oggetto Tempo di questo
capitolo, ma che contiene un ricco insieme di metodi e operatori. Leggetene la documentazione sul
sito http: // docs. python. org/ 3/ library/ datetime. html .
1. Usate il modulo datetime per scrivere un programma che ricavi la data odierna e visualizzi
il giorno della settimana.
2. Scrivete un programma che riceva una data di nascita come input e visualizzi l’età dell’utente
e il numero di giorni, ore, minuti e secondi che mancano al prossimo compleanno.
3. Date due persone nate in giorni diversi, esiste un giorno in cui uno ha un’età doppia dell’altro.
Questo è il loro “Giorno del Doppio”. Scrivete un programma che prenda due date di nascita
e calcoli quando si verifica il “Giorno del Doppio”.
4. Un po’ più difficile: scrivetene una versione più generale che calcoli il giorno in cui una
persona ha n volte l’età di un’altra.
Soluzione: http: // thinkpython2. com/ code/ double. py"""

import datetime


def dataEGiorno():
    dataOggi = datetime.date.today()
    data_formattata = dataOggi.strftime("%d/%m/%Y")

    indexGiorno = dataOggi.weekday()
    listaGiorni = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
    giornoSettimana = listaGiorni[indexGiorno]

    return data_formattata, giornoSettimana


def calcoloEtaEProxCompleanno(dataNascita):
    dataNascita = datetime.datetime.strptime(dataNascita, "%d/%m/%Y").date()
    # print(dataNascita)

    dataOggi = datetime.date.today()
    # print(dataOggi)
    eta = dataOggi.year - dataNascita.year

    if dataOggi.month < dataNascita.month or (
            dataOggi.month == dataNascita.month and dataOggi.day < dataNascita.day):
        eta -= 1

    prossimoCompleanno = datetime.date(dataOggi.year, dataNascita.month, dataNascita.day)
    differenza = prossimoCompleanno - dataOggi
    print(differenza)

    return eta, differenza


def main():
    data, giorno = dataEGiorno()

    print("data di oggi:", data)
    print("giorno della settimana:", giorno)

    dataNascita = input("inserire la data di nascita (gg/mm/aaaa): ")
    eta, diff = calcoloEtaEProxCompleanno(dataNascita)
    print(eta, diff)


if __name__ == "__main__":
    main()

# Stampa la data odierna e il giorno della settimana
