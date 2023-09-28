"""Scrivete una funzione di nome eval_ciclo che chieda iterativamente all’utente di inserire un dato,
prenda il dato inserito e lo valuti con eval, infine visualizzi il risultato.
Deve continuare fino a quando l’utente non scrive 'fatto', e poi restituire il valore dell’ultima
espressione che ha valutato."""


def eval_ciclo():
    val = None
    while True:
        dato = input("inserire un dato (operazione numerica): ")
        if dato == 'fatto':
            break
        val = eval(dato)
        # print(val)
    return val


def main():
    print(eval_ciclo())


if __name__ == '__main__':
    main()
