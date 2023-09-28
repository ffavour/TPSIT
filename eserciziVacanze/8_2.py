"""Esercizio 8.2. Esiste un metodo delle stringhe di nome count che è simile alla funzione del Paragrafo 8.7. Leggete
la documentazione del metodo e scrivete un’invocazione che conti il numero di a in 'banana'."""


def main():
    s = "banana"
    occorrenzeA = s.count("a")
    print(f"occorrenze di a in {s}: {occorrenzeA}")


if __name__ == "__main__":
    main()
