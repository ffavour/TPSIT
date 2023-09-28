"""“L’altro giorno stavo guidando in autostrada e guardai il mio contachilometri. È a sei cifre, come la maggior
parte dei contachilometri, e mostra solo chilometri interi. Se la mia macchina, per esempio, avesse 300.000 km,
vedrei 3-0-0-0-0-0.” “Quello che vidi quel giorno era interessante. Notai che le ultime 4 cifre erano palindrome,
cioè si potevano leggere in modo identico sia da sinistra a destra che viceversa. Per esempio 5-4-4-5 è palindromo,
per cui il contachilometri avrebbe potuto essere 3-1-5-4-4-5” “Un chilometro dopo, gli ultimi 5 numeri erano
palindromi. Per esempio potrei aver letto 3-6-5-4-5-6. Un altro chilometro dopo, le 4 cifre di mezzo erano
palindrome. E tenetevi forte: un altro chilometro dopo tutte e 6 erano palindrome!” “La domanda è: quanto segnava il
contachilometri la prima volta che guardai?” Scrivete un programma in Python che controlli tutti i
numeri a sei cifre e visualizzi i numeri che soddisfano le condizioni sopra indicate. Soluzione: http: //
thinkpython2. com/ code/ cartalk2. py ."""


def ha_palindromo(numero):
    s = str(numero)
    return s == s[::-1]


def controlla(numero):
    return (ha_palindromo(numero) and
            ha_palindromo(numero + 1) and
            ha_palindromo(numero + 2) and
            ha_palindromo(numero + 3))


def controlla_tutti():
    numero = 100000
    while numero <= 999996:
        if controlla(numero):
            print(numero)
        numero += 1


def main():
    print('possibili chilometraggi:')
    controlla_tutti()


if __name__ == "__main__":
    main()
