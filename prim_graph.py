import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [] #inicializa a matriz de adjacencia vazia
 
    # Funcao para imprimir a arvore geradora minima
    def printMST(self, parent):
        print("\nArestas \tPeso")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
 
    #Funcao para encontrar o vertice com distancia minima
    def minKey(self, key, mstSet): 
        # Inicializa com valor minimo
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Funcao que constroi e imprimi a arvore geradora minima para um grafo
    # usando uma matriz de adjacencia
    def primMST(self):
 
        #O valor usado para escolher o peso de aresta minimo para o corte
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array para armazenar a arvore geradora minima
        key[0] = 0   # O primeiro vertice eh zero
        mstSet = [False] * self.V
 
        parent[0] = -1  # O primeiro no eh sempre a raiz
 
        for cout in range(self.V):
 
            # Escolhe o vertice de distancia minima do conjunto de vertices ainda nao percorridos
            u = self.minKey(key, mstSet)
 
            # Coloca o vertice da distancia minima na arvore geradora minima
            mstSet[u] = True
 
            # Atualiza o valor dos vertices adjacentes escolhido somente se a
            # distancia atual for maior que a nova distancia e o vertice nao
            # estiver na arvore geradora minima
            for v in range(self.V):
                # o graph[u][v] nao eh zero apenas para vertices adjacentes
                # mstSet[v] eh falso para vertices ainda nao incluidos na arvore geradora minima
                # atualiza a key somente se o graph[u][v] for menor que a key[v]
                if(self.graph[u][v] > 0 and mstSet[v] == False and
                   key[v] > self.graph[u][v]):
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.printMST(parent)

# entrada do numero de vertices
vertices = int(input("Insira a quantidade de vertices do grafo: "))
g  = Graph(vertices) # g eh objeto grafo e guarda o numero de vertices no construtor

# preenche a matriz de adjacencia com entrada do usuario
for i in range(vertices):
    tmp = []
    for j in range(vertices):
        element = int(input("Digite o elemento da posicao {0}-{1}: ".format(i,j)))
        tmp.append(element)
        
    g.graph.append(tmp[:])
 
g.primMST();
 