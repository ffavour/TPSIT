def somma(a, b):
    return a + b


def main():
    print(somma)    #somma è un oggetto
    somma.descrizione = "la funzione calcola la somma"
    x = somma(3, 5)
    print(x)
    print(somma.descrizione)


if __name__ == "__main__":
    main()
