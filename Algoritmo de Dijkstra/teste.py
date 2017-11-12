import random
import networkx as nx
import dijkstraalgorithm as djk
import time
import matplotlib.pyplot as plt

lista_vertices=list()
lista_media_tempo= list()

for n in range(0,5000, 5):
    print(n)
    G = nx.gn_graph(n)
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,100)
    soma=0.
    for i in range(1, 11):
        start= time.time()
        djk.dijkstra(G, list(G.nodes())[0], G.number_of_nodes()-1)
        tempo = time.time() - start
        soma=soma+tempo;
    lista_vertices.append(n)
    lista_media_tempo.append(soma/10)

plt.plot(lista_vertices, lista_media_tempo)
plt.axis([0, 5000, 0, max(lista_media_tempo) * 2])
plt.ylabel('Tempo de execução (Segundos)')
plt.xlabel('Número de Vértices')
plt.title("Desempenho Algoritmo de Dijkstra")
plt.show()