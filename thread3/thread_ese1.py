######################################
# Un processo produttore genera in modo casuale (anche con ripetizioni) numeri da 1 a 10 (inclusi) e
# li memorizza in un buffer condiviso che può contenere un solo numero alla volta. Due processi
# consumatori concorrenti tentano di acquisire tali numeri soltanto dopo la loro produzione.
# Uno dei due consumatori tenta di acquisire solo numeri da 1 a 5, l'altro solo numeri che vanno da 6 a 10.
# Quando lo prendono settano il buffer (variabile) a 0 (zero)
#####################################


from time import sleep
from threading import Thread, Lock
import random

mutex = Lock()  # creo il MUTEX
buffer = 0
continua = True  # per far ciclare il produttore n volte e la stessa variabile fa ciclare i consumatori


class Produttore(Thread):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global buffer
        global continua
        i = 0
        # while(1):
        while continua:
            mutex.acquire()
            if buffer == 0:
                buffer = random.randint(1, 10)
                print(f"Thread {self.id}: prodotto {buffer}")
                sleep(1)
                i += 1
                if i == 10:
                    continua = False
            mutex.release()  # rilascio MUTEX


class Consumatore(Thread):

    def __init__(self, id, valoremin, valoremax):
        Thread.__init__(self)
        self.id = id
        self.valoremin = valoremin
        self.valoremax = valoremax
        self.valore_raccolto = 0

    def run(self):
        global buffer
        global continua
        # while(1):
        while (continua):
            mutex.acquire()
            if (buffer >= self.valoremin and buffer <= self.valoremax):
                self.valore_raccolto += buffer
                print(f"Thread {self.id}: consumato {buffer} ed ho un totale di {self.valore_raccolto}")
                buffer = 0
                sleep(1)
            mutex.release()  # rilascio MUTEX


# creo 5 thread e li faccio partire
consumatore_1 = Consumatore("Cons_1", 1, 5)
consumatore_2 = Consumatore("Cons_2", 6, 10)
produttore = Produttore("Produttore")

produttore.start()
consumatore_1.start()
consumatore_2.start()

produttore.join()
consumatore_1.join()
consumatore_2.join()
