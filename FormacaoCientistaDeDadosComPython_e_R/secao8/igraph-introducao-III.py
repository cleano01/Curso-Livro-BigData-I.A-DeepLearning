from igraph import Configuration
from igraph import Graph
from igraph import plot

#configuracao para exebir o grafo
cfg = Configuration.instance()
cfg["apps.eog"] = "start"


grafo4 = Graph(directed = False)

grafo4.add_vertices(5)
grafo4.add_edges([(0,1), (1,2), (2,3), (3,4), 
                 (4,0), (0,2), (2,1)])

grafo4.add_vertex(5)
grafo4.add_vertex(6)

grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


#visualizar a matriz adjacente
#print(grafo4.get_adjacency())

#podemos pegas os dados da matriz
print(grafo4.get_adjacency()[0,])

#grafo4.get_adjacency()[0,1]  o ZERO(linha) UM(conluna)
print(grafo4.get_adjacency()[0,1])

#retorna as infomações dos vertices
'''for v in grafo4.vs:
    print(v)
'''


#plot(grafo4, bbox = (400, 400))



grafo5 = Graph(edges = [(0,1), (2,3), (0,2), (0,3)] , 
              #plot(grafo4, bbox = (400, 400))
directed= True)

grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo5.vs['peso'] = [40, 30, 30, 25]

'''for v in grafo5.vs:
    print(v)'''

#print(grafo5.vs[0])


grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo5.es['weight'] =[1, 2, 1, 3]

#percorrendo as arestas
for e in grafo5.es:
    print(e)
    

#print(grafo5.es[0])

grafo5.vs['type'] = ['Humano']

#nome do grafo
grafo5['name'] = 'Amizade'

print(grafo5)



#plot(grafo5, bbox = (400, 400))
