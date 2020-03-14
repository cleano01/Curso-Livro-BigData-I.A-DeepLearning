from igraph import Configuration
from igraph import Graph
from igraph import plot


'''
Em caso de duvida de instalacao dos pacotes =  
https://github.com/cleano01/Curso-Livro-BigData-I.A-DeepLearning/commit/7513ff5e442b37aec8f2dbfb5dbb15d660f9cba6
'''

#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"

#edges = arestas
#direct = TRUE  estamos informando que o grafo sera direcionado
grafo1 = Graph(edges = [(0,1), (1,2), (2,3), (3,0)],
             directed = True)

#vcount() = informa quantos vertices temos
grafo1.vs['label'] = range(grafo1.vcount())
#print(grafo1)
#plot(grafo1, bbox= (300, 300))




#edges = arestas
#direct = TRUE  estamos informando que o grafo sera direcionado
grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(0,3),
              (3,2),(2,1),(1,0)], 
              directed = True)

#vcount() = informa quantos vertices temos
grafo2.vs['label'] = range(grafo2.vcount())
#print(grafo2)
#plot(grafo2, bbox= (300, 300))


#edges = arestas
#direct = TRUE  estamos informando que o grafo sera direcionado
grafo3 = Graph(edges = [(0,1), (1,2), (2,3), (3,0), (1,1)],
             directed = True)

#vcount() = informa quantos vertices temos
grafo3.vs['label'] = range(grafo3.vcount())
#print(grafo3)
#plot(grafo3, bbox= (300, 300))


#edges = arestas
#direct = TRUE  estamos informando que o grafo sera direcionado
grafo4 = Graph(edges = [(0,1), (1,2), (2,3), (3,0), (1,1)],
             directed = True)

grafo4.add_vertex(5)

#vcount() = informa quantos vertices temos
grafo4.vs['label'] = range(grafo4.vcount())
print(grafo4)
plot(grafo4, bbox= (300, 300))
