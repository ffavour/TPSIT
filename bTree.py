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
            if key > self.key:  # chiave maggiore
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insertNode(key)

            elif key < self.key:  # chiave minore
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insertNode(key)
        else:
            self.key = key

    def findNode(self, key):
        if key > self.key:
            #andiamo a destra
            if(self.right == None):
                return f"Nodo {key} non trovato"
            return self.right.findNode(key)
        elif key < self.key:
            #andiamo a sinistra
            if (self.left == None):
                return f"Nodo {key} non trovato"
            return self.left.findNode(key)
        else:
            return f"Nodo {key} trovato"

    def altezza(self, root):
        h = 0
        if root is None:
            return 0
        else:
            pass


    def eBilanciato(self):
        pass



def printTree(root):
    printTree(root.left)
    if root is not None:
        printTree(root.key)
    printTree(root.right)

def creaAlberoBilanciato():
    pass


def main():
    lista_key = list(range(0, 40, 5))
    random.shuffle(lista_key)
    print(lista_key)

    albero = Node(lista_key[0])
    for key in lista_key[1:]:  # dal secondo elemento (cicla su elemento)
        albero.insertNode(key)

    albero.printTree()
    print(albero.findNode(2))


if __name__ == "__main__":
    main()
