from igraph import Configuration
from igraph import Graph
from igraph import plot
import igraph
#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"


grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                       directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]


#es = acessa as arestas
#plot(grafo, bbox = (300,300), 
#edge_label = grafo.es['weight'])

#vamos descubir a menor rora de A até H

#output = 'vpath' vai fazer o calculo/visitas dos vertices
caminho_vertice = grafo.get_shortest_paths(0,7, 
                  output = 'vpath')
print(caminho_vertice)



#output = 'epath' vai fazer o calculo/visitas das arestas
caminho_aresta = grafo.get_shortest_paths(0,7, 
                output = 'epath')
print(caminho_aresta)


caminho_aresta_id = []
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)


caminho_nome_vertices = []
for n in caminho_vertice[0]:
    print(grafo.vs[n]['label'])
    caminho_nome_vertices.append(grafo.vs[n]['label'])


for v in grafo.vs:
    if v['label'] in caminho_nome_vertices:
        v['color'] = 'green'
    else:
        v['color'] = 'gray'

#plot(grafo, bbox = (300,300), 
#edge_label = grafo.es['weight'])

for e in grafo.es:
    if e.index in caminho_aresta_id:
        e['color'] = 'green'

    else:
        e['color'] = 'gray'


plot(grafo, bbox = (300,300), 
edge_label = grafo.es['weight'])