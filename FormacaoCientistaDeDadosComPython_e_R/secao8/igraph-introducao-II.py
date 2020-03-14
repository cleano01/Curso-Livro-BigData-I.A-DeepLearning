from igraph import Configuration
from igraph import Graph
from igraph import plot

#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"

#edges = arestas
#direct = TRUE  estamos informando que o grafo sera direcionado
grafo1 = Graph(edges = [(0,1), (2,2), (2,3), (3,0)],
             directed = True)

grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)


#direct = TRUE  estamos informando que o grafo NAO sera  direcionado
grafo2 = Graph(edges = [(0,1), (2,2), (2,3), (3,0)],
             directed = False)
print(grafo2)


#direct = False  estamos informando que o grafo NAO sera  direcionado
grafo3 = Graph(directed = False)

#add_vertices adciona vertice no grafo
grafo3.add_vertices(10)

#add_vertex(16) = estamos falando que queremos adicionar o vertice 16
grafo3.add_vertex(16)

#dd_edges() = adicona arestas
grafo3.add_edges([(0,1), (2,2), (2,3), (3,0)])

'''print(grafo3)
plot(grafo3, bbox =(300, 300))'''



grafo4 = Graph(directed = False)

grafo4.add_vertices(5)
grafo4.add_edges([(0,1), (1,2), (2,3), (3,4), 
                 (4,0), (0,2), (2,1)])

grafo4.add_vertex(5)
grafo4.add_vertex(6)

grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plot(grafo4, bbox = (400, 400))




    
