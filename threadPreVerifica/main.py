import threading

saldo = 100
mutex = threading.Lock()


class Deposita(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global saldo  # rende la var globale saldo modificabile
        for _ in range(10000000):
            mutex.acquire()
            saldo = saldo + 10  # questa è l'area creitica => la risorsa viene acceduta da + thread
            mutex.release()  # mutex "blocca" la risorsa temporaneamente, il codice ora è thread-safe


class Preleva(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global saldo  # rende la var globale saldo modificabile
        for _ in range(10000000):
            mutex.acquire()
            saldo = saldo - 10
            mutex.release()


def main():
    # istanze oggetti thread
    alice = Deposita()
    bob = Preleva()

    # esecuzione thrread
    alice.start()
    bob.start()

    print("aspetto la fine dei thread")
    print(threading.enumerate())

    # join thread
    alice.join()
    bob.join()

    print(f"il saldo è {saldo}")


if __name__ == "__main__":
    main()
