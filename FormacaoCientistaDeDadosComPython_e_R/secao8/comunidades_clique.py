from igraph import Configuration
from igraph import Graph
from igraph import plot
import igraph
import numpy as np

#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"


grafo = igraph.load('Grafo.graphml')
#print(grafo)

#plot(grafo, 
#    bbox = (300, 300))


comunidades = grafo.clusters()
print(comunidades)

#relacionmento entre comunidades
c = comunidades.membership
print(c)

#plot(grafo, vertex_color = comunidades.membership)


print('#######')

grafo2 = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                       directed = True)
grafo2.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo2.es['weight'] = [2,1,2,1,2,1,3,1]

comunidades2 = grafo2.clusters()
print(comunidades2)

c2 = comunidades2.membership
print(c2)

#fazendo grupo com dendograma
dendograma = grafo2.community_edge_betweenness()
print(dendograma)

#retrona a quantidade de grupos
grupos_dendograma = dendograma.optimal_count
print(grupos_dendograma)

comunidades3 = dendograma.as_clustering()
print(comunidades3)

print(comunidades3.membership)

#plot(grafo2, vertex_color = comunidades3.membership)
cores = comunidades3.membership
cores = np.array(cores)

cores = cores * 100

#plot(grafo2,bbox = (300,300) ,vertex_color = cores)

#cliques
cli = grafo.as_undirected().cliques(min =4)
print(cli)

#numero de cliques
print(len(cli))
