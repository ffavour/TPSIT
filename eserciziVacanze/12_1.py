""". Scrivete una funzione di nome piu_frequente che riceva una stringa e stampi le
lettere in ordine di frequenza decrescente. Trovate delle frasi di esempio in diverse lingue e osservate
come varia la frequenza delle lettere. Confrontate i vostri risultati con le tabelle del sito http:
// en. wikipedia. org/ wiki/ Letter_ frequencies . Soluzione: http: // thinkpython2.
com/ code/ most_ frequent. py ."""


def piu_frequente(stringa):
    frequenze = {}

    for lettera in stringa:
        if lettera in frequenze:
            frequenze[lettera] += 1
        else:
            frequenze[lettera] = 1

    return frequenze


def main():
    s = "abbbeeaaaayy"
    n = piu_frequente(s)
    print(n)


if __name__ == "__main__":
    main()
