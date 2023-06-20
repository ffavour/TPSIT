"""
Progettare un programma in grado di gestire un parcheggio con un numero di 12 posti.
Nel parcheggio potranno entrare delle macchine (creare tra 5 e 12 auto con random) e
ogni macchina si fermerà per un tempo random (tra 1 e 5). SI PRECISA: le auto non dovranno
aspettare il tempo delle altre macchine parcheggiate prima di entrare.
Stampare all'ingresso e all'uscita delle auto il numero dei posti liberi in modo corretto.
Esempio stampe: "Entra auto 3 - posti liberi x su 12" , "Esce auto 2 - posti liberi y su 12"
"""
from threading import Thread, Lock
import random
import time

mutex = Lock()
postiDisponibili = 12
continua = True
pieno = False


class Parcheggio(Thread):
    def __init__(self, auto):
        Thread.__init__(self)

        self.id = id
        self.id = id
        self.auto = auto

    def run(self):
        global postiDisponibili
        global continua
        global mutex
        global pieno

        i = 0
        while continua:
            self.auto[i].run()
            mutex.acquire()
            if postiDisponibili == 0:
                print(f"il parcheggio è pieno")
                pieno = True
            elif self.auto[i].parcheggiata is True:

                mutex.release()  # rilascio MUTEX

            i += 1


class Automobile(Thread):
    def __init__(self, id):
        Thread.__init__(self)

        self.id = id
        self.parcheggiata = False

    def run(self):
        global continua

        if pieno is False:
            print(f"auto {self.id} entra nel parcheggio")
            self.parcheggiata = True

        time.sleep(random.randint(1, 5))
        print(f"auto {self.id} esce dal parcheggio")
        self.parcheggiata = False


def main():

    listaAuto = []

    # carico una lista con le auto
    for i in range(0, 10):
        auto = Automobile(i)
        listaAuto.append(auto)

    parcheggio = Parcheggio(listaAuto)
    parcheggio.run()

    # join dei thread
    parcheggio.join()
    for elementi in listaAuto:
        elementi.join()


if __name__ == "__main__":
    main()
