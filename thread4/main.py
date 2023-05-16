"""Progettare un’applicazione che implementi una camera blindata virtuale protetta da una password costituita da un
numero intero compreso tra 1 e 9999. La camera blindata viene attaccata da dei rapinatori che cercano di crackare la
password che protegge la camera blindata. I rapinatori sono due e cercano di crackare la password in modo
concorrente, il primo tentando tutti i numeri in modo crescente, il secondo provando con un numero alla volta in modo
decrescente. La camera blindata è controllata da una guardia che avrà bisogno di 10 secondi per raggiungere la camera
blindata. Se i rapinatori non avranno indovinato la password entro questo lasso di tempo saranno bloccati,
altrimenti, se uno dei rapinatori riuscirà ad indovinare la password prima che terminino i 10 secondi,
tutti i malviventi riusciranno a fuggire. Per ogni tentativo di crack della password i malviventi impiegheranno
almeno 5 millisecondi. Il poliziotto dovrà mostrare a video il suo nominativo e i secondi necessari per raggiungere
la camera blindata. Inoltre se arriverà prima di 10 secondi, riuscendo a catturare i malfattori, dovrà visualizzare
una frase appropriata alla situazione. Se uno dei rapinatori dovesse indovinare la password, dovrà mostrare il suo
nominativo e la password indovinata."""


import threading
import random
import time

password = 0  # numero compreso tra 1 e 9999
pwTrovata = False
guardiaArrivata = False
mutex = threading.Lock()


class RapinatoreCrescente(threading.Thread):
    def __int__(self):
        super().__init__()

    def run(self):
        global password
        global pwTrovata
        global guardiaArrivata

        i = 1
        while i < 10000 and guardiaArrivata is False and pwTrovata is False:
            pw = i
            # print(f"tentativo C {pw}")
            time.sleep(0.005)
            if pw == password:
                mutex.acquire()
                pwTrovata = True
                mutex.release()
                print(f"password trovata D {password}")
                break
            i += 1


class RapinatoreDecrescente(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        i = 9999
        global password
        global pwTrovata
        global guardiaArrivata

        while i > 0 and guardiaArrivata is False and pwTrovata is False:
            pw = i
            # print(f"tentativo D {pw}")
            time.sleep(0.005)
            if pw == password:
                print(f"password trovata D {password}")
                mutex.acquire()
                pwTrovata = True
                mutex.release()
                break
            i -= 1


class Guardia(threading.Thread):
    def __int__(self):
        super().__init__()

    def run(self):
        global pwTrovata
        global guardiaArrivata

        time.sleep(10)
        print("poliziotto ha raggiunto la camera blindata")
        guardiaArrivata = True

        if pwTrovata is False:
            print(f"BECCATI AHAHAHAHA")


def main():
    global password
    password = random.randint(1, 9999)
    # print(password)

    # istanzio gli oggetti
    r1 = RapinatoreCrescente()
    r2 = RapinatoreDecrescente(2)
    poliziotto = Guardia()

    # avvio thread
    r1.start()
    r2.start()
    poliziotto.start()

    print("aspetto la fine dei thread")
    print(threading.enumerate())

    # join dei thread
    r1.join()
    r2.join()
    poliziotto.join()

    print(f"la pw era {password}")


if __name__ == "__main__":
    main()
