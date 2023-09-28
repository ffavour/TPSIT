"""Scrivete una funzione di nome disegna_rett che prenda un oggetto Turtle e un
Rettangolo e usi la Tartaruga per disegnare il Rettangolo. Vedere il Capitolo 4 per esempi di uso
degli oggetti Turtle.
Scrivete una funzione di nome disegna_cerchio che prenda un oggetto Turtle e un Cerchio, e
disegni il Cerchio.
Soluzione: http: // thinkpython2. com/ code/ draw. py ."""

import turtle

import turtle
import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rettangolo:
    def __init__(self, angolo_sup_sx, larghezza, altezza):
        self.angolo_sup_sx = angolo_sup_sx
        self.larghezza = larghezza
        self.altezza = altezza


class Cerchio:
    def __init__(self, centro, raggio):
        self.centro = centro
        self.raggio = raggio


def disegna_rett(t, rettangolo):
    t.penup()
    t.goto(rettangolo.angolo_sup_sx.x, rettangolo.angolo_sup_sx.y)
    t.pendown()
    t.setheading(0)
    t.forward(rettangolo.larghezza)
    t.right(90)
    t.forward(rettangolo.altezza)
    t.right(90)
    t.forward(rettangolo.larghezza)
    t.right(90)
    t.forward(rettangolo.altezza)
    # funzione a effetti collaterali


def disegna_cerchio(t, cerchio):
    t.penup()
    t.goto(cerchio.centro.x, cerchio.centro.y - cerchio.raggio)
    t.pendown()
    t.setheading(0)
    circonferenza = 2 * math.pi * cerchio.raggio
    lato = circonferenza / 360
    for _ in range(360):
        t.forward(lato)
        t.right(1)


def main():
    t = turtle.Turtle()

    rettangolo = Rettangolo(Punto(0, 0), 200, 100)
    disegna_rett(t, rettangolo)

    cerchio = Cerchio(Punto(100, -100), 75)
    disegna_cerchio(t, cerchio)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
