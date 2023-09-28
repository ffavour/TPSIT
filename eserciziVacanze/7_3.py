"""Scrivete una funzione di nome stima_pi che utilizzi questa formula per calcolare e restituire una
stima di π. Deve usare un ciclo while per calcolare gli elementi della sommatoria, fino a quando
l’ultimo termine è più piccolo di 1e-15 (che è la notazione di Python per 10−15). Controllate il
risultato confrontandolo con math.pi"""

import math


def stima_pi():
    k = 0
    termine = 1
    sommatoria = 0

    while abs(termine) > 1e-15:
        numeratore = math.factorial(4 * k) * (1103 + 26390 * k)
        denominatore = (math.factorial(k) ** 4) * (396 ** (4 * k))
        termine = numeratore / denominatore
        sommatoria += termine
        k += 1

    return 1 / ((2 * math.sqrt(2) / 9801) * sommatoria)


def main():
    approssimazioneStima_pi = stima_pi()
    differenza = abs(approssimazioneStima_pi - math.pi)
    print(f"risultato di stima_pi: {approssimazioneStima_pi}")
    print(f"risultato di math.pi: {math.pi}")
    print(f"differenza: {differenza}")


if __name__ == "__main__":
    main()
