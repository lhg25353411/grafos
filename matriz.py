import networkx as nx
from random import randint

class in_mat():

    
    def __init__(self):
        self.quant_vert = 0 
        self.matriz = [] #matriz de adj
    
    #recebe a matriz de adjacencia do usuario e passa para o objeto matriz
    def to_mat(self):
        self.quant_vert = int(input("Digite a quantidade de vertices: "))
        print("Digite a matriz de adjacencia: ")
        for x in range(0,self.quant_vert):
            n = input()
            m = list(map(int, n.split(" ")))
            self.matriz.append(m)

        for i in range(0,len(self.matriz)):
            [int(elem) for elem in self.matriz[i]]   
            
    #transforma a matriz em um grafo da blibioteca networkx
    def to_graph(self):
        G = nx.Graph()
        #adiciona ao grafico a quantidade de vertices em quant_vert
        for z in range(0,int(self.quant_vert)):
            G.add_node(z)
            
        for x in range(0,int(self.quant_vert)):
            for y in range(0,int(self.quant_vert)):
                if x <= y:
                    if int(self.matriz[x][y]) > 0:
                        n = int(self.matriz[x][y])
                        G.add_edge (x,y,weight = n)
                        
        #self.matriz.clear()
        
        return G

    #Gera aleatoriamente um grafo a partir de um numero de vertices
    #essa função ja atribui o grafo a G e retorna-o, não sendo necessa´rio chamar a função to_graph
    def random_g(self): 
        #n é o numero de vertices
        n = int(input("Digite a quantidade de vertices para gerar um grafo: "))
        G = nx.connected_watts_strogatz_graph(n,randint(int(n/2),n-1),0.5,100,randint(1,100))
        
        # a é uma lista contendo as arestas do grafo
        a = G.edges()
        
        #matriz de adj do grafo
        self.matriz = []
        for i in range(n):
            self.matriz.append([0]*n)
        
        #plotagem do peso gerado aletoriamente na matriz
        for v1,v2 in a:
            n = randint(1,50)
            self.matriz[v1][v2] = n
            self.matriz[v2][v1] = n
            #atribuição do peso no grafo
            G.edges[v1,v2]['weight']=n
            
        self.quant_vert = G.number_of_nodes()
        
        #G.edges[v1,v2]['weight']=n
        return G
    #Função que retorna a matriz de adjacência do grafo gerado automaticamente
    def get_matriz_adj(self):
        return self.matriz
    
    #Função que reinicia para os valores iniciais //Necessario?
    def mat_clear(self):
        self.quant_vert = 0 
        self.matriz = []
    
    #função que gera um grafo completo    
    def graph_comp(self):
        v = int(input("Digite a quantidade de vertices para gerar um grafo completo: "))
        G = nx.complete_graph(v)
        
        self.quant_vert = G.number_of_nodes()
        
        a = G.edges()
        
        self.matriz = []
        for i in range(v):
            self.matriz.append([0]*v)
            
        for v1,v2 in a:
            n = randint(1,50)
            self.matriz[v1][v2] = n
            self.matriz[v2][v1] = n
            #atribuição do peso no grafo
            G.edges[v1,v2]['weight']=n
        
        return G
            
            
        
        
        
        """
        self.quant_vert = randint(1,self.max_vert)
        list_aux = []
        #n = randint(1,self.quant_vert)
        for x in range(0,self.quant_vert):
            for y in range(0,self.quant_vert):
                list_aux.append(randint(0,self.max_arest))
            print(list_aux)    
            self.matriz.append(list_aux)
            list_aux.clear()
            """
       
        
                
        
                                
            
