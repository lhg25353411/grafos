
from tkinter import *
import networkx as nx
from matriz import in_mat as mat
#import dijkstra-algorithm as dj
from kruskal import Algoritimo_kruskal as kr
from prim_graph import Graph as prim
import dijkstraalgorithm
import matplotlib.pyplot as plt




class Application:
    def __init__(self, master=None):
        self.G = nx.Graph()
        self.m = mat() #classe da matriz
        self.list_adj = [] #matriz de adj
        self.k = kr()
        self.p = prim()
        
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
                
        self.titulo = Label(self.primeiroContainer, text="PROGRAMA DE GRAFOS")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
                
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.titulo = Label(self.segundoContainer, text="Escolha o algoritmo desejado:")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.space = Frame(master)
        self.space["padx"] = 20
        self.space.pack()
        
        self.space = Label(self.space, text="", font=self.fontePadrao)
        self.space.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.prim = Button(self.terceiroContainer)
        self.prim["text"] = "Prim"
        self.prim["font"] = ("Calibri", "8")
        self.prim["width"] = 12
        self.prim["command"] = self.chamaPrim
        self.prim.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()
        
        self.kruskal = Button(self.quartoContainer)
        self.kruskal["text"] = "Kruskal"
        self.kruskal["font"] = ("Calibri", "8")
        self.kruskal["width"] = 12
        self.kruskal["command"] = self.chamaKruskal
        self.kruskal.pack()
        
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()
        
        self.dijkstra = Button(self.quintoContainer)
        self.dijkstra["text"] = "Dijkstra"
        self.dijkstra["font"] = ("Calibri", "8")
        self.dijkstra["width"] = 12
        self.dijkstra["command"] = self.chamaDijkstra
        self.dijkstra.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()
                
        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 10
        self.setimoContainer.pack()
                
        self.titulo = Label(self.setimoContainer, text="Você quer gerar grafos automáticos ou inserir manualmente?")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.space1 = Frame(master)
        self.space1["padx"] = 20
        self.space1.pack()
        
        self.space1 = Label(self.space1, text="", font=self.fontePadrao)
        self.space1.pack()
        
        self.oitavoContainer = Frame(master)
        self.oitavoContainer["padx"] = 20
        self.oitavoContainer.pack()
        
        self.gerar = Button(self.oitavoContainer)
        self.gerar["text"] = "Gerar"
        self.gerar["font"] = ("Calibri", "8")
        self.gerar["width"] = 12
        self.gerar["command"] = self.chamaGerar
        self.gerar.pack()
               
        self.space2 = Frame(master)
        self.space2["padx"] = 20
        self.space2.pack()
        
        self.space2 = Label(self.space2, text="", font=self.fontePadrao)
        self.space2.pack()
        
        self.verticeContainer = Frame(master)
        self.verticeContainer["padx"] = 20
        self.verticeContainer.pack()
        
        
        #######################
        
        self.dijk_v_fonteContainer = Frame(master)
        self.dijk_v_fonteContainer["padx"] = 20
        self.dijk_v_fonteContainer.pack()

        #####################
        
        self.dijk_v_destinoContainer = Frame(master)
        self.dijk_v_destinoContainer["padx"] = 20
        self.dijk_v_destinoContainer.pack()
        
        ######################
        
        self.space3 = Frame(master)
        self.space3["padx"] = 20
        self.space3.pack()
        
        self.space3 = Label(self.space3, text="", font=self.fontePadrao)
        self.space3.pack()
        
        self.inserirContainer = Frame(master)
        self.inserirContainer["padx"] = 20
        self.inserirContainer.pack()
        
        self.inserir = Button(self.inserirContainer)
        self.inserir["text"] = "Salva Nº Vértices"
        self.inserir["font"] = ("Calibri", "8")
        self.inserir["width"] = 12
        self.inserir["command"] = self.chamaInserirVert
        self.inserir.pack()
        
        self.space4 = Frame(master)
        self.space4["padx"] = 20
        self.space4.pack()
        
        self.space4 = Label(self.space4, text="", font=self.fontePadrao)
        self.space4.pack()
        
        self.matrizContainer = Frame(master)
        self.matrizContainer["padx"] = 20
        self.matrizContainer.pack()
        
        self.space5 = Frame(master)
        self.space5["padx"] = 20
        self.space5.pack()
        
        self.space5 = Label(self.space5, text="", font=self.fontePadrao)
        self.space5.pack()
        
        self.inserirEContainer = Frame(master)
        self.inserirEContainer["padx"] = 20
        self.inserirEContainer.pack()
        
        self.inserirElemento = Button(self.inserirEContainer)
        self.inserirElemento["text"] = "Abrir Arquivo"
        self.inserirElemento["font"] = ("Calibri", "8")
        self.inserirElemento["width"] = 12
        self.inserirElemento["command"] = self.chamaInserirMatriz
        self.inserirElemento.pack()
        
        self.space6 = Frame(master)
        self.space6["padx"] = 20
        self.space6.pack()
        
        self.space6 = Label(self.space6, text="", font=self.fontePadrao)
        self.space6.pack()
        
        self.verticeLabel = Label(self.verticeContainer,text="N° de vértices: ", font=self.fontePadrao)
        self.verticeLabel.pack(side=TOP)

        self.vertice = Entry(self.verticeContainer)
        self.vertice["width"] = 30
        self.vertice["font"] = self.fontePadrao
        self.vertice.pack(side=BOTTOM)

        
        ###############################
        self.dijk_v_fonteLabel = Label(self.dijk_v_fonteContainer,text="Dijkstra - Vertice Fonte: ", font=self.fontePadrao)
        self.dijk_v_fonteLabel.pack(side=TOP)

        self.dijk_v_fonte = Entry(self.dijk_v_fonteContainer)
        self.dijk_v_fonte["width"] = 30
        self.dijk_v_fonte["font"] = self.fontePadrao
        self.dijk_v_fonte.pack(side=BOTTOM)
        
      
        ##########################
        self.dijk_v_destinoLabel = Label(self.dijk_v_destinoContainer,text="Dijkstra - Vertice Destino: ", font=self.fontePadrao)
        self.dijk_v_destinoLabel.pack(side=TOP)

        self.dijk_v_destino = Entry(self.dijk_v_fonteContainer)
        self.dijk_v_destino["width"] = 30
        self.dijk_v_destino["font"] = self.fontePadrao
        self.dijk_v_destino.pack(side=BOTTOM)
        ##########################
        
        
        self.mzContainer = Frame(master)
        self.mzContainer["padx"] = 20
        self.mzContainer.pack()
        
        self.msg_matriz = Label(self.mzContainer, text="", font=self.fontePadrao)
        self.msg_matriz.pack()
        """
        self.G = nx.Graph()
        self.m = mat()
        self.list_adj = []
        """
    
    #Método chama Prim
    def chamaPrim(self):
        self.mensagem["text"] = ("O escolhido foi Prim!")
        self.p.V = self.G.number_of_nodes()
        self.p.graph = self.list_adj

        #self.m.mat_clear()

        self.G = self.p.primMST()
        
        
        #.m.mat_clear()  
        #teste
        
        dict= []
        for (u, v, wt) in self.G.edges.data('weight'):
            dict.append({(u,v) : wt})
            
        print(dict)    
        
        plt.figure(figsize=(8,8))
        nx.draw(self.G,node_size=5,alpha=1,node_color="white", edge_color = "#1880C7", with_labels=True,font_size=15)
        plt.axis('equal')
        plt.savefig('circular_tree.png')
        plt.show()

        
    #Método chama Kruskal
    def chamaKruskal(self):
        self.mensagem["text"] = ("O escolhido foi Kruskal!")
        
        mst = self.k.kruskal(self.G)
        print(mst.edges)
        print(self.k.peso(mst))
        
        dict = []
        
        for (u, v, wt) in mst.edges.data('weight'):
            dict.append({(u,v) : wt})
            
        print(dict) 
        
        plt.figure(figsize=(8,8))
        nx.draw(mst,node_size=5,alpha=1,node_color="white", edge_color = "#1880C7", with_labels=True,font_size=15)        
        plt.axis('equal')
        plt.savefig('circular_tree.png')
        plt.show()

        
        #self.m.mat_clear()
        
    #Método chama Dijkstra
    def chamaDijkstra(self) :
        H = nx.DiGraph(self.G)
        v1 = int(self.dijk_v_destino.get())
        v2 = int(self.dijk_v_fonte.get())
        caminho_minimo = dijkstraalgorithm.dijkstra(H,v1,v2)
        print(caminho_minimo)
        g = nx.Graph(caminho_minimo[:len(caminho_minimo):-1])
        for i in range(0, len(caminho_minimo) - 2):
            g.add_edge(caminho_minimo[i], caminho_minimo[i + 1])
        nx.draw(g, with_labels=True)
        plt.title("Peso do Camínho Mínimo: " + str(caminho_minimo[len(caminho_minimo) - 1]))
        self.mensagem["text"] = "Peso do Camínho Mínimo: " + str(caminho_minimo[len(caminho_minimo) - 1]['peso'])
        plt.show()
        # dict = []
        #
        # for (u, v, wt) in H.edges.data('weight'):
        #     dict.append({(u,v) : wt})
        #
        # print(dict)
        #
        # plt.figure(figsize=(8,8))
        # nx.draw(H,node_size=5,alpha=1,node_color="white", edge_color = "#1880C7", with_labels=True,arrows=True,font_size=15)
        # plt.axis('equal')
        # plt.savefig('circular_tree.png')
        # plt.show()
        
        
        
      
    #Método chama Geracao dos Grafos
    def chamaGerar(self):
        self.mensagem["text"] = ("O escolhido foi gerar automaticamente!")
        """
        É necessário obter a matriz automaticamente bem como obter a matriz de adj que será usada no algoritmo de prim
        """
        
        #G contém um grafo gerado automáticamente
        self.m.random_g()
        self.G = self.m.to_graph()
        self.list_adj = self.m.get_matriz_adj()
        
        dict = []
        
        for (u, v, wt) in self.G.edges.data('weight'):
            dict.append({(u,v) : wt})
            
        print(dict) 
        
        plt.figure(figsize=(8,8))
        nx.draw(self.G,node_size=5,alpha=1,node_color="white", edge_color = "#1880C7", with_labels=True,font_size=15)
        plt.axis('equal')
        plt.savefig('circular_tree.png')
        plt.show()

    #Método chama Insercao de Vértice do Grafo por Matrix
    def chamaInserirVert(self):

        self.mensagem["text"] = ("Número de vértices definido: ")
  
        """
        global vertices
        vertices = int(self.vertice.get())
        """
        
        #limpar os atributos da classe para reutilização
        self.G.clear()
        self.m.mat_clear()
        
        #conseguir o valor digitado pelo usuario no campo "Nº de vértices"
        #print(self.vertice.get())
        self.m.quant_vert = int(self.vertice.get())
        print(self.m.quant_vert)
    
    #Método chama Insercao da Matriz
    def chamaInserirMatriz(self):
        
        #A matriz agora sera lida de um arquivo
        ref_arq_mat = open("matriz_adj.txt",'r')
        
        for linha in ref_arq_mat:
            valores = linha.split()
            self.m.matriz.append(valores)    
            
        #trasnforma caracter da lista em int
        for i in range(0,len(self.m.matriz)):
            self.m.matriz[i]=[int(elem) for elem in self.m.matriz[i]]  

        ref_arq_mat.close()
        
        #self.m.to_mat()
        
        print(self.m.matriz)
        
        self.G = self.m.to_graph()
        self.list_adj = self.m.get_matriz_adj()
        
        dict = []
        
        for (u, v, wt) in self.G.edges.data('weight'):
            dict.append({(u,v) : wt})
            
        print(dict) 
        
        plt.figure(figsize=(8,8))
        nx.draw(self.G,node_size=5,alpha=1,node_color="white", edge_color = "#1880C7", with_labels=True,font_size=15)
        plt.axis('equal')
        plt.savefig('circular_tree.png')
        plt.show()
        
            
root = Tk()
root.geometry('800x600')
Application(root)

root.mainloop()