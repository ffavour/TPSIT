"""Questo esercizio è un aneddoto monitorio su uno degli errori più comuni e difficili
da trovare in Python. Scrivete una definizione di una classe di nome Canguro con i metodi seguenti:
1. Un metodo __init__ che inizializza un attributo di nome contenuto_tasca ad una lista
vuota.
2. Un metodo di nome intasca che prende un oggetto di qualsiasi tipo e lo inserisce in
contenuto_tasca.
3. Un metodo __str__ che restituisce una stringa di rappresentazione dell’oggetto Canguro e
dei contenuti della tasca.
Provate il codice creando due oggetti Canguro, assegnandoli a variabili di nome can e guro, e
aggiungendo poi guro al contenuto della tasca di can.
Scaricate http: // thinkpython2. com/ code/ BadKangaroo. py . Contiene una soluzione al
problema precedente, ma con un grande e serio errore. Trovatelo e sistematelo.
Se vi bloccate, potete scaricare http: // thinkpython2. com/ code/ GoodKangaroo. py , che
spiega il problema e illustra una soluzione."""


class Canguro:
    def __init__(self):
        self.contenuto_tasca = []

    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        s = ""
        for elemento in self.contenuto_tasca:
            s += str(elemento) + " - "
        return s


def main():
    can = Canguro()
    guro = Canguro
    can.intasca(guro)



if __name__ == "__main__":
    main()