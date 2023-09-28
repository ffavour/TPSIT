"""Un cifrario di Cesare è un metodo di criptazione debole che consiste nel “ruotare”
ogni lettera di una parola di un dato numero di posti seguendo la sequenza alfabetica, ricominciando
da capo quando necessario. Ad esempio ’A’ ruotata di 3 posti diventa ’D’, ’Z’ ruotata di 1 posto
diventa ’A’.
Per ruotare una parola, si ruota ciascuna delle sue lettere dello stesso numero di posti prefissato.
Per esempio, “cheer” ruotata di 7 dà “jolly” e “melon” ruotata di -10 dà “cubed”. Nel film 2001:
Odissea nello Spazio, il computer di bordo si chiama HAL, che non è altro che IBM ruotato di -1.
Scrivete una funzione di nome ruota_parola che richieda una stringa e un intero come parametri,
e che restituisca una nuova stringa che contiene le lettere della stringa di partenza ruotate della
quantità indicata.
Potete usare le funzioni predefinite ord, che converte un carattere in un codice numerico, e chr,
che converte i codici numerici in caratteri. Le lettere sono codificate con il loro numero di ordine
alfabetico, per esempio:
>> ord('c') - ord('a')
2
Dato che 'c' è la “2-esima” lettera dell’alfabeto. Ma attenzione: i codici numerici delle lettere
maiuscole sono diversi.
Su Internet, talvolta, vengono codificate in ROT13 (un cifrario di Cesare con rotazione 13) delle
barzellette potenzialmente offensive. Se non siete suscettibili, cercatene qualcuna e decodificatela.
Soluzione: http: // thinkpython2. com/ code/ rotate. py ."""


def ruota_parola(parola, pos):
    parolaFinale = ""

    for lettera in parola:
        if lettera.isupper():
            codice_iniziale = ord("A")
            codice_finale = ord("Z")
        else:
            codice_iniziale = ord("a")
            codice_finale = ord("z")

        codice_lettera = ord(lettera)
        nuovo_codice = codice_lettera + pos

        if nuovo_codice < codice_iniziale:
            if lettera == "a" and pos < 0:
                nuovo_codice = codice_finale + (nuovo_codice - codice_iniziale + 1)
            elif lettera == "A" and pos < 0:
                nuovo_codice = codice_finale + (nuovo_codice - codice_iniziale + 1)
            else:
                nuovo_codice = codice_finale - (codice_iniziale - nuovo_codice + 1)
        elif nuovo_codice > codice_finale:
            nuovo_codice = codice_iniziale + (nuovo_codice - codice_finale - 1)

        parolaFinale += chr(nuovo_codice)

    return parolaFinale


def main():
    parola = input("inserire una parola/frase: ")
    numeroRotazione = int(input("inserire di quanto vuoi ruotare la parola: "))

    output = ruota_parola(parola, numeroRotazione)
    print(f"risultato: {output}")


if __name__ == "__main__":
    main()
