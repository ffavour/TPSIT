import random
import time

n = 100
l = [random.uniform(0.,1.) for _ in range(n)]
#print(l)

start_time = time.time()  #avvio cronometro
maximum = l[0]

for element in l:
    if element > maximum:
        maximum = element

end_time = time.time()

print(f"il valore massimo e' {maximum}")

print(f"durata dell'algoritmo: {end_time - start_time}")