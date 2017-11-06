
class PriorityQueue:

    def __init__(self):
        self.fila = [0]
        self.tamanho = 0

    def find_min(self):
        if self.tamanho != 0:
            return self.fila[1]

    def remove_min(self):
        minimo = self.find_min()
        self.fila[1] = self.fila[self.tamanho]
        self.tamanho = self.tamanho-1
        self.fix_down(1)
        return minimo

    def insert(self, elemento):
        self.fila.append(elemento)
        self.tamanho = self.tamanho+1
        self.fix_up(self.tamanho)

    def increase_key(self, indice, valor):
        self.fila[indice] = valor
        self.fix_up(indice)

    def decrease_key(self, indice, valor):
        self.fila[indice] = valor
        self.fix_down(indice)

    def __contains__(self, elemento):
        for pair in self.fila:
            if pair == elemento:
                return True
        return False

   #Heap Algorithms

    def fix_down(self, i):

        while 2*i <= self.tamanho:
            f = 2*i
            if f < self.tamanho and self.fila[f] > self.fila[f+1]:
                f = f+1
            if self.fila[i] <= self.fila[f]:
                i = self.tamanho
            else:
                aux = self.fila[f]
                self.fila[f] = self.fila[i]
                self.fila[i] = aux
                i = f

    def build_min_heap(self, lista):
        self.fila = [0]
        self.tamanho = len(lista)
        for i in lista:
            self.fila.append(i)

        i = len(lista)//2
        while i >= 1:
            self.fix_down(i)
            i -= 1

    def fix_up(self, i):
        while i >= 2 and self.fila[i//2] > self.fila[i]:
            aux = self.fila[i//2]
            self.fila[i//2] = self.fila[i]
            self.fila[i] = aux
            i = i//2
