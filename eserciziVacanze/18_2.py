"""Scrivete un metodo per Mazzo di nome dai_mani che prenda come parametri il
numero di mani e il numero di carte da dare a ciascuna mano, e crei il numero stabilito di oggetti
Mano, distribuisca il numero prefissato di carte a ogni mano e restituisca una lista delle Mani."""


class Mano:
    def __init__(self):
        self.carte = None


class Mazzo:
    def __init__(self):
        pass

    def dai_mani(self, nMani, nCarte):
        mani = []
        for _ in range(nMani):
            mano = Mano()
            mano.carte = nCarte
            mani.append(mano)
        return mani


def main():
    pass


if __name__ == "__main__":
    main()
