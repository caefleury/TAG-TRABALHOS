Após estudar e analisar o Capítulo 7 (Components, Communities and Cliques), deve-se resolver e enviar (códigos e respostas) aos exercícios, do item 7.5.2 (Data exercises): 4, 5, 6, 7, 8, 9, 10, 11, 12 e 13.

Exercícios:

4. Determine the connected components of this network and reduce the network to its largest connected component.

5. Use the Louvain algorithm to determine a vertex partition/community structure with optimal modularity in this network.

6. Compare the modularity of the Louvain community structure with that of the ground truth department structure.

7. Visualize the graph color-coded by the Louvain community, and then visualize the graph separately color-coded by the ground truth department. Compare the visualizations. Can you describe any of the Louvain communities in terms of departments?

8. Create a dataframe containing the community and department for each vertex. Manipulate this dataframe to show the percentage of individuals from each department in each community. Try to visualize this using a heatmap or other style of visualization and try to use this to describe the communities in terms of departments.

9. Find the largest clique size in the graph. How many such largest cliques are there? What do you think a clique represents in this context?

10. Try to visualize the members of these cliques in the context of the entire graph. What can you conclude?

Extension: These questions require the use of the Leiden community detection algorithm, which you may recall from earlier in this chapter is guaranteed to find a partition which at least matches the modularity of a Louvain partition, and can often improve it. If you are a Python programmer, the Leiden algorithm is easily used from the cdlib package. If you are an R programmer, you will need to use the leiden package, which uses a Python implementation of the algorithm inside R. You may need to be familiar with the reticulate package73 to ensure that an appropriate Python environment is available inside your R session.

11. Use the Leiden community detection algorithm to find a vertex partition with optimal modularity. How many communities does the Leiden algorithm detect?

12. Compare the Leiden partition modularity to the Louvain partition modularity.

13. Try to use visualization or data exploration methods to determine the main differences between the Leiden and Louvain partitions.
