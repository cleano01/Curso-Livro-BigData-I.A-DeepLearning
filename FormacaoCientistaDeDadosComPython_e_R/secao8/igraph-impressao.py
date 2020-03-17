from igraph import Configuration
from igraph import Graph
from igraph import plot

#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"


grafo5 = Graph(edges = [(0,1), (2,3), (0,2), (0,3)] , 
directed= True)

grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo5.vs['peso'] = [40, 30, 30, 25]

grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo5.es['weight'] =[1, 2, 1, 3]

#print das arestas
for v in grafo5.vs:
    print(v)

#print vertices
for e in grafo5.es:
    print(e)

grafo5.vs['cor'] = ['blue', 'red', 'yellow', 'green']


#edge_curverd = deixa curva do grafo
#vertex_shape = muda de os vertices para formato de quadrado
plot(grafo5, bbox =(300,300),
    vertex_size = grafo5.vs['peso'],
    edge_width = grafo5.es['weight'],
    vertex_color = grafo5.vs['cor'],
    edge_curverd = 0.4,
    vertex_shape = 'square')
