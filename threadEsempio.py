from random import random
from time import sleep
from threading import Thread


class Task(Thread):
    def __int__(self, nome, temp):
        Thread.__init__(self)
        self.id = nome
        self.temp = temp

    def run(self):
        print(f"start thead {self.id}")
        sleep(self.temp)
        print(f"finish thread{self.id}")


class Task2(Thread):
    def __int__(self, id, temp):
        Thread.__init__(self)
        self.id = id
        self.temp = temp

    def run(self):
        for i in range(0, 21):
            print(i)


# creo 2 thread
t1 = Task(1, 3)
t2 = Task2(2, 3)

# inizializzo thread
t1.start()  # start == run
t2.start()

# aspetto tempo di attesa
t1.join()  # chiude thread
t2.join()
