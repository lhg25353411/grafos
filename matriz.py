import networkx as nx

class to_mat():
    
    list = [] #lista de lista da matriz
    quant_vert

    #captura uma matriz de adjacencia do usuario    
    def in_mat(self):
        self.quant_vert = input("Digite a quantidade de vertices: ")
        print("Digite a matriz de adjacencia: ")
        for x in range(0,int(quant_vert)):
            n = input()
            m = n.split(" ")
            self.list.append(m)
       """ 
        for x in range(0,int(quant_vert)):
            m = list[x]
            for y in range(0,int(quant_vert)):
                if y == int(quant_vert)-1:
                    print(m[y]+"\n")
                else:
                    print(m[y]+" ")
        """    
    #transforma a matriz em um grafo
    def to_graph_(self):
        G = nx.Graph(int(self.quant_vert))
        for x in range(0,int(self.quant_vert)):
            m = list[x]
            for y in range(0,int(self.quant_vert)):
                if x <= y:
                    if int(m[y]) > 0:
                        G.add_edge(x, y, {'weight':int(m[y]))}
        return G                            
            