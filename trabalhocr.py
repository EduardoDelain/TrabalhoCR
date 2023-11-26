import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Cria um grafo
Grafo = nx.Graph()
Subgrafo = nx.Graph()

#Adicionando nós
Grafo.add_node('inv1')
Grafo.add_node('inv2')
Grafo.add_node('inv3')
Grafo.add_node('inf1')
Grafo.add_node('inf2')
Grafo.add_node('inf3')
Grafo.add_node('inf4')
Grafo.add_node('inf5')
Grafo.add_node('pot1')
Grafo.add_node('pot2')
Grafo.add_node('pot3')
Grafo.add_node('pot4')
Grafo.add_node('pot5')
Grafo.add_node('pot6')

#Adiciona enlaces(arestas)
Grafo.add_edge('inv1', 'inv2')
Grafo.add_edge('inv1', 'inv3')
Grafo.add_edge('inv3', 'inf5')
Grafo.add_edge('inv2', 'inf1')
Grafo.add_edge('inv3', 'inf2')
Grafo.add_edge('inf1', 'inf3')
Grafo.add_edge('inf1', 'inf4')
Grafo.add_edge('inf3', 'inf4')
Grafo.add_edge('pot2', 'pot6')
Grafo.add_edge('pot1', 'pot3')
Grafo.add_edge('pot1', 'pot4')
Grafo.add_edge('inf3', 'pot1')
Grafo.add_edge('inf4', 'pot1')
Grafo.add_edge('inf2', 'pot2')
Grafo.add_edge('inf2', 'pot5')
Grafo.add_edge('inf5', 'pot6')
Grafo.add_edge('pot5', 'pot4')


#Nomeando os nós
center_node = 'inv1'
node_two = 'inv2'
node_tree = 'inv3'
node_four = 'inf1'
node_five = 'inf2'
node_six = 'inf3'
node_seven = 'inf4'
node_eight = 'inf5'
node_nine = 'pot1'
node_ten = 'pot2'
node_eleven = 'pot3'
node_twelve = 'pot4'
node_thirdteen = 'pot5'
node_fourteen = 'pot6'

#Criando a estrutura de desing do grafo
edge_nodes = set(Grafo) - {center_node}
pos_grafo = nx.circular_layout(Grafo.subgraph(edge_nodes))
pos_subgrafo = nx.circular_layout(Grafo.subgraph(edge_nodes))

#Posicionamento de cada nó para melhor entendimento
pos_grafo[center_node] = np.array([-5, 0])
pos_grafo[node_two] = np.array([-4, 0.5])
pos_grafo[node_tree] = np.array([-4, -0.5])
pos_grafo[node_four] = np.array([-2, 1])
pos_grafo[node_five] = np.array([-2, 0])
pos_grafo[node_six] = np.array([-1, 1.5])
pos_grafo[node_seven] = np.array([-1, 0.5])
pos_grafo[node_eight] = np.array([-2, -1])
pos_grafo[node_nine] = np.array([0, 1])
pos_grafo[node_ten] = np.array([0, -0.25])
pos_grafo[node_eleven] = np.array([1, 1.5])
pos_grafo[node_twelve] = np.array([1, 0.5])
pos_grafo[node_thirdteen] = np.array([0, 0.25])
pos_grafo[node_fourteen] = np.array([2, -0.25])

#Plotando o grafo
plt.figure(2)
nx.draw_networkx(Grafo, pos_grafo, with_labels=True)
plt.show()

#Calculando o agrupamento para cada nó
print(nx.clustering(Grafo)) 

#Calculando o algoritmo de dijkstra para o topo da piramide
print(nx.shortest_path(Grafo, source='inv1', weight="weight", method='dijkstra'))
