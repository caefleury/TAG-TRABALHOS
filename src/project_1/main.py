import onadata as ona
import pandas as pd
import networkx as nx
from cdlib import algorithms, evaluation
import matplotlib.pyplot as plt

# dados
edge_list = pd.read_csv('src/project_1/data/email_edgelist.csv')
vertices_list = pd.read_csv('src/project_1/data/email_vertices.csv')


email_edgelist_graph = nx.from_pandas_edgelist(edge_list,
                                               source='from',
                                               target='to',
                                               create_using=nx.Graph())


# Exercício 4
print("\033[1;32m" + "<----- Exercício 4 ----->" + "\033[0m")
connected_components = list(nx.connected_components(email_edgelist_graph))
largest_connected_component = max(connected_components, key=len)
print("Maior componente conectado: Muito grande para visualizar no terminal! ")

# Exercício 5
print("\033[1;32m" + "<----- Exercício 5 ----->" + "\033[0m")
louvain_communities = nx.community.louvain_communities(email_edgelist_graph)
louvian_commmunity_modularity = nx.community.modularity(
    email_edgelist_graph, louvain_communities)
print("Modularidade:", louvian_commmunity_modularity)

# Exercício 6
print("\033[1;32m" + "<----- Exercício 6 ----->" + "\033[0m")
# criar dicionario de vertices com departamentos
departments = vertices_list.set_index('id')['dept'].to_dict()
dept_communities = dict()
for vertice, dept in departments.items():
    # maiores vertices
    if vertice in email_edgelist_graph:
        if dept not in dept_communities:
            dept_communities[dept] = set()

        dept_communities[dept].add(vertice)

dept_communities = list(dept_communities.values())
dept_modularity = nx.community.modularity(
    email_edgelist_graph, dept_communities)

print(
    f"Modularidade das comunidades Louvain {louvian_commmunity_modularity:.3f}")
print(f"Modularidades com a estrutura de departamentos: {dept_modularity:.3f}")

# Exercício 7
print("\033[1;32m" + "<----- Exercício 7 ----->" + "\033[0m")
# departments = vertices_list.set_index('id')['dept'].to_dict()
# nx.draw(email_edgelist_graph,labels=departments, with_labels=True,
#         node_color='orange', node_size=800, width=4, edge_cmap=plt.cm.Blues)
# plt.show()

# print("")

# nx.draw(communities, with_labels=True, nnode_color='orange',
#          node_size=800, width=4, edge_cmap=plt.cm.Blues)
# plt.show()

# Exercício 8
print("\033[1;32m" + "<----- Exercício 8 ----->" + "\033[0m")

# Exercício 9
print("\033[1;32m" + "<----- Exercício 9 ----->" + "\033[0m")
cliques = list(nx.find_cliques(email_edgelist_graph))
maximal_cliques = sorted(cliques, key=len)

print("Tamanho do maior clique:", maximal_cliques[0])

num_largest_cliques = 0
for clique in cliques:
    if len(clique) == len(maximal_cliques[0]):
        num_largest_cliques += 1
print("Quantidade de cliques do mesmo tamanho do maior:",
      num_largest_cliques)  # Only one
print("O clique maximal nesse contexto é a maior rede de indivíduos(vertices)...")
print("conectados entre si se comunicando por meio do email(arestas).")

# Exercício 10
print("\033[1;32m" + "<----- Exercício 10 ----->" + "\033[0m")
cliques = list(nx.find_cliques(email_edgelist_graph))
maximal_cliques = sorted(cliques, key=len)
# nx.draw(cliques, with_labels=True, node_color='orange', node_size=500, width=2, edge_cmap=plt.cm.Blues)
# plt.show()
print("Cliques isolados estão desconectados da rede maior")
print("O tamanho dos cliques em relação ao grafo total indica a coesão geral da rede.")
print("Cliques grandes em um grafo esparso são mais significativos.")

# Exercício 11
print("\033[1;32m" + "<----- Exercício 11 ----->" + "\033[0m")
leiden_communities = algorithms.leiden(email_edgelist_graph)
leiden_communities_number = len(leiden_communities.communities)
print(f"Comunidades Leiden: {leiden_communities_number}")

# Exercício 12
print("\033[1;32m" + "<----- Exercício 12 ----->" + "\033[0m")
modularity_louvain = nx.community.modularity(
    email_edgelist_graph, louvain_communities)
modularity_leiden = evaluation.modularity_density(
    email_edgelist_graph, leiden_communities).score

print(f"Modularidade do Louvain: {modularity_louvain:.3f}")
print(f"Modularidade do Leiden: {modularity_leiden}")

print("\033[1;32m" + "Exercícios -> 4, 5, 6, 10, 11, 12" + "\033[0m")
