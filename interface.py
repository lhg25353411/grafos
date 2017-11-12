from tkinter import *
import networkx as nx
from matriz import in_mat as mat
#import dijkstra-algorithm as dj
from kruskal import Algoritimo_kruskal as kr
from prim_graph import Graph as prim
import dijkstraalgorithm 




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
        self.inserirElemento["text"] = "Insere Elem Matriz"
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
        
        self.matrizLabel = Label(self.matrizContainer, text="Elementos da matriz: ", font=self.fontePadrao)
        self.matrizLabel.pack(side=TOP)

        self.matriz = Entry(self.matrizContainer)
        self.matriz["width"] = 30
        self.matriz["font"] = self.fontePadrao
        self.matriz.pack(side=BOTTOM)
        
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
        self.p.graph = self.m.get_matriz_adj()

        self.m.mat_clear()

        self.p.primMST()
        
        
        self.m.mat_clear()  
        
    #Método chama Kruskal
    def chamaKruskal(self):
        self.mensagem["text"] = ("O escolhido foi Kruskal!")
        
        mst = self.k.kruskal(self.G)
        print(mst.edges)
        print(self.k.peso(mst))
        
        self.m.mat_clear()  
    #Método chama Dijkstra
    def chamaDijkstra(self) :
        H = nx.DiGraph(self.G)
        v1 = int(input("Digite o vertice de oferta: "))
        v2 = int(input("Digite o vertice de demanda: "))
        print(dijkstraalgorithm.dijkstra(H,v1,v2))
        """
        self.mensagem["text"] = ("O escolhido foi Dijkstra!")
        
        n = int(input("Digite o vértice fonte: "))
        try:
            fonte = int(n)
        except():
            pass    
        
        if fonte in self.G:
            print(fonte)
            custos = dijkstra(self.G,fonte) #lembrar da importação correta
            print("Distâncias do ",fonte,"para todos os outros vértices:\n",custos)
        else:
            print("Não existe nenhum vértice com essa definição")

        self.m.mat_clear()
        """
    #Método chama Geracao dos Grafos
    def chamaGerar(self):
        self.mensagem["text"] = ("O escolhido foi gerar automaticamente!")
        """
        É necessário obter a matriz automaticamente bem como obter a matriz de adj que será usada no algoritmo de prim
        """
        #G contém um grafo gerado automáticamente
        self.m = mat()
        self.m.random_g()
        self.G = self.m.to_graph()
        self.list_adj = self.m.get_matriz_adj()
        

    #Método chama Insercao de Vértice do Grafo por Matrix
    def chamaInserirVert(self):
        """
        global vertices
        vertices = int(self.vertice.get())
        """
        self.m = mat()
        self.m.to_mat()
        self.G = m.to_graph()
        self.list_adj = m.get_matriz_adj()
        
        """FUNCAO CORRIGIDA PARA INSERIR VERTICES"""
        
        self.vertices = int(self.vertice.get())
        self.mensagem["text"] = ("O escolhido foi inserir manualmente!")
        self.mx = []
        self.elemento_atual = 0
        self.msg_matriz["text"] = ("Insira", self.vertices**2, "elementos!")

        for vertice in range(self.vertices):
            self.mx.extend([[None] * self.vertices])

        print(self.mx)
        
    
    #Método chama Insercao da Matriz
    def chamaInserirMatriz(self):
        mx = []
        m = mat()
        m.to_mat()
        G = m.to_graph
        
        """FUNCAO CORRIGIDA PARA INSERIR MATRIZ"""
        elemento = int(self.matriz.get())
        self.mx[self.elemento_atual // self.vertices][self.elemento_atual % self.vertices] = elemento
        self.elemento_atual += 1

        print(self.mx)
            
root = Tk()
root.geometry('800x600')
Application(root)
root.mainloop()