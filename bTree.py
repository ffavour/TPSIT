import random


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        pass

    def printTree(self, level=0):
        if self.left is not None:
            self.left.printTree(level + 1)

        print(f"Livello {level} -> {self.key}")

        if self.right is not None:
            self.right.printTree(level + 1)

    def insertNode(self, key):
        if self.key is not None:
            if key > self.key:  # chiave maggiore (destra)
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insertNode(key)

            elif key < self.key:  # chiave minore (minore)
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insertNode(key)
        else:
            self.key = key

    def findNode(self, key):
        if key > self.key:
            # andiamo a destra
            if (self.right == None):
                return f"Nodo {key} non trovato"
            return self.right.findNode(key)
        elif key < self.key:
            # andiamo a sinistra
            if (self.left == None):
                return f"Nodo {key} non trovato"
            return self.left.findNode(key)
        else:
            return f"Nodo {key} trovato"

    def height(self):
        if self.left is None:
            heightL = 0
        else:
            heightL = self.left.height() #ricorsione per capire altezza

        if self.right is None:
            heightR = 0
        else:
            heightR = self.right.height()

        #controlla dove l'h è maggiore
        if heightL > heightR:
            return heightL + 1
        else:
            return heightR + 1


    def eBilanciato(self):
        pass


def printTree(root):
    printTree(root.left)
    if root is not None:
        printTree(root.key)
    printTree(root.right)


def buildBTree(nodes):
    """
    nodes deve contenere valori ordinati in ordine crescente
    """

    l = len(nodes)  # lunghezza della lista

    if l == 0:
        return None

    # nodes.sort()  #riordina la lista

    m = l // 2  # trovo indice punto medio della lista
    # print(f"nodo di mezzo: {nodes[m]}")
    root = Node(nodes[m])  # creo nodo root
    root.left = buildBTree(nodes[0:m])
    root.right = buildBTree(nodes[m + 1:])

    return root


def altezzaAlbero(root):
    pass


def main():
    lista_key = list(range(0, 40, 5))
    random.shuffle(lista_key)
    lista_key.sort()
    print(lista_key)

    #crea e stampa albero bilanciato
    albero = buildBTree(lista_key)
    albero.printTree()
    print(f"l'altezza dell'albero è {albero.height() - 1}") #-1 per togliere il root

    albero.altezza = 5 #python permette di aggiungere attributi o metodi a caso

    #crea albero partendo da una lista di chiavi
    """albero = Node(lista_key[0])
    for key in lista_key[1:]:  # dal secondo elemento (cicla su elemento)
        albero.insertNode(key)

    albero.printTree()
    print(albero.findNode(2))"""


if __name__ == "__main__":
    main()
