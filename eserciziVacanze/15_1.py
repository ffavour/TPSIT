"""Scrivete una definizione di classe di nome Cerchio, avente gli attributi centro e
raggio, dove centro è un oggetto Punto e raggio è un numero.
Istanziate un oggetto Cerchio che rappresenti un cerchio con il centro nel punto (150, 100) e di
raggio 75.
Scrivete una funzione di nome punto_nel_cerchio, che prenda un Cerchio e un Punto e
restituisca True se il punto giace dentro il cerchio, circonferenza compresa.
Scrivete una funzione di nome rett_nel_cerchio, che prenda un Cerchio e un Rettangolo e
restituisca True se il rettangolo giace interamente all’interno del cerchio, circonferenza compresa.
Scrivete una funzione di nome rett_cerchio_sovrapp, che prenda un Cerchio e un Rettangolo
e restituisca True se almeno uno degli angoli del Rettangolo ricade all’interno del cerchio. Oppure,
più difficile, se una qualunque porzione del Rettangolo ricade all’interno del cerchio.
Soluzione: http: // thinkpython2. com/ code/ Circle. py ."""

import math


class Cerchio:
    def __init__(self, centro, raggio):
        self.centro = centro
        self.raggio = raggio


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rettangolo:
    def __init__(self, angolo_sup_sx, larghezza, altezza):
        self.angolo_sup_sx = angolo_sup_sx
        self.larghezza = larghezza
        self.altezza = altezza


def punto_nel_cerchio(cerchio, punto):
    distanza = math.sqrt((punto.x - cerchio.centro.x) ** 2 + (punto.y - cerchio.centro.y) ** 2)
    if distanza <= cerchio.raggio:
        return True
    return False


def rett_nel_cerchio(cerchio, rettangolo):
    angolo_sup_dx = Punto(rettangolo.angolo_sup_sx.x + rettangolo.larghezza, rettangolo.angolo_sup_sx.y)
    angolo_inf_sx = Punto(rettangolo.angolo_sup_sx.x, rettangolo.angolo_sup_sx.y - rettangolo.altezza)
    angolo_inf_dx = Punto(angolo_sup_dx.x, angolo_inf_sx.y)

    if punto_nel_cerchio(cerchio, rettangolo.angolo_sup_sx) and punto_nel_cerchio(cerchio,
                                                                                  angolo_sup_dx) and punto_nel_cerchio(
            cerchio, angolo_inf_sx) and punto_nel_cerchio(cerchio, angolo_inf_dx):
        return True
    return False


def rett_cerchio_sovrapp(cerchio, rettangolo):
    angolo_sup_dx = Punto(rettangolo.angolo_sup_sx.x + rettangolo.larghezza, rettangolo.angolo_sup_sx.y)
    angolo_inf_sx = Punto(rettangolo.angolo_sup_sx.x, rettangolo.angolo_sup_sx.y - rettangolo.altezza)
    angolo_inf_dx = Punto(angolo_sup_dx.x, angolo_inf_sx.y)

    if punto_nel_cerchio(cerchio, rettangolo.angolo_sup_sx) or punto_nel_cerchio(cerchio,
                                                                                 angolo_sup_dx) or punto_nel_cerchio(
            cerchio, angolo_inf_sx) or punto_nel_cerchio(cerchio, angolo_inf_dx):
        return True
    return False


def main():
    centro = Punto(150, 100)

    cerchio = Cerchio(centro, 75)

    punto = Punto(170, 120)
    if punto_nel_cerchio(cerchio, punto):
        print("Il punto si trova all'interno del cerchio")
    else:
        print("Il punto non si trova all'interno del cerchio")

    rettangolo = Rettangolo(Punto(130, 80), 50, 40)
    if rett_nel_cerchio(cerchio, rettangolo):
        print("Il rettangolo si trova interamente all'interno del cerchio")
    else:
        print("Il rettangolo non si trova interamente all'interno del cerchio")

    if rett_cerchio_sovrapp(cerchio, rettangolo):
        print("Il rettangolo si sovrappone al cerchio")
    else:
        print("Il rettangolo non si sovrappone al cerchio")


if __name__ == "__main__":
    main()
