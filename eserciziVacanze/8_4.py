"""Tutte le funzioni che seguono dovrebbero controllare se una stringa contiene almeno una lettera minuscola,
ma qualcuna di esse è sbagliata. Per ogni funzione, descrivete cosa fa in realtà (supponendo che il parametro sia una
stringa)."""


def una_minuscola1(s):
    for c in s:
        if c.islower():
            return True
    else:
        return False


def una_minuscola2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def una_minuscola3(s):
    for c in s:
        flag = c.islower()
    return flag


def una_minuscola4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def una_minuscola5(s):
    for c in s:
        if not c.islower():
            return False
    return True


def main():
    s = "FSSSSa"

    print(una_minuscola1(s))  # scorre la stringa come se fosse una lista, al primo carattere minuscolo ritorna true
    print(una_minuscola2(s))  # scorre la stringa come se fosse una lista, controlla che 'c' sia minuscolo
    print(una_minuscola3(s))  # scorre la stringa come se fosse una lista, al primo carattere minuscolo ritorna true
    print(una_minuscola4(s))  # scorre la stringa come se fosse una lista, al primo carattere minuscolo ritorna true
    print(una_minuscola5(s))  # scorre la stringa come se fosse una lista, al primo carattere minuscolo ritorna false


if __name__ == "__main__":
    main()
