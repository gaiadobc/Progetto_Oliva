# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:59:49 2020

@author: gaiad
"""
import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt 
from networkx import erdos_renyi_graph
from networkx import watts_strogatz_graph
from networkx import barabasi_albert_graph
from networkx import degree_centrality

plt.figure(figsize=(12, 10))
    
#Creo rete ERDOS-RENYI
G=erdos_renyi_graph(50, 0.15, seed=None, directed=False)  #true=grafo diretto
plt.subplot(3, 2, 1)
nx.draw(G,node_size=10)

#Creo rete WATTS-STROGATZ (small-world)
G1=watts_strogatz_graph(50, 10, 0.15, seed=None)   #nodi,connessini vicini(grado),prob
plt.subplot(3, 2, 3)
nx.draw(G1,node_size=10)

#Creo rete BARABASI-ALBERT (scale free)
G2=barabasi_albert_graph(50, 2, seed=None)
plt.subplot(3, 2, 5)
nx.draw(G2,node_size=10)



plt.subplot(3, 2, 6)
dc=list(degree_centrality(G1))
dc1=[]
for i in range(len(dc)):
    dc1.append(dc[i]/max(dc))
dc1_color = [dc1[i] for i in range(len(dc1))]
nx.draw(G2,pos=None,with_labels=False,node_size=100,node_color=dc1_color,width=1)

plt.subplot(3, 2, 4)
dc=list(degree_centrality(G1))
dc1=[]
for i in range(len(dc)):
    dc1.append(dc[i]/max(dc))
dc1_color = [dc1[i] for i in range(len(dc1))]
nx.draw(G1,pos=None,with_labels=False,node_size=100,node_color=dc1_color,width=1)


plt.subplot(3, 2, 2)
dc=list(degree_centrality(G))
dc1=[]
for i in range(len(dc)):
    dc1.append(dc[i]/max(dc))
dc1_color = [dc1[i] for i in range(len(dc1))]
nx.draw(G,pos=None,with_labels=False,node_size=100,node_color=dc1_color,width=1)

plt.savefig("Tipi_di_rete.png")
