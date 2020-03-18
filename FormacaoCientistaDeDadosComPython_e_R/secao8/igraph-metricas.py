from igraph import Configuration
from igraph import Graph
from igraph import plot
import igraph
#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"

grafo = igraph.load('Grafo.graphml')

#plot(grafo, bbox = (400, 400))


#grau de entrada e saida
grau_entrada_saida = grafo.degree(type = 'all')
print(grau_entrada_saida)

#grau de entrada 
grau_entrada = grafo.degree(type = 'in')
print(grau_entrada)


#grau de saida 
grau_saida = grafo.degree(type = 'out')
print(grau_saida)



#pessoas mais influentes
grau = grafo.degree(type = 'in')
#plot(grafo, vertex_size = grau)

#maior distancia entre os vertices
print(grafo.diameter(directed = True))


#retorna os vertices com maior distancia no grafo
print(grafo.get_diameter())

#retorna os vizinhos
print(grafo.neighborhood())


grafo2 = grafo

print(grafo.isomorphic(grafo2))