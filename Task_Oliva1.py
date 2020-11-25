# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:40:41 2020

@author: gaiad
"""

import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt 
from networkx import betweenness_centrality
from networkx import eigenvector_centrality
from networkx import degree_centrality
from networkx import closeness_centrality


#funzioncina ad hoc per plottare un grafo
def show_graph(adjacency_matrix,filename):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500)
    plt.savefig(filename)
    plt.show()

n=100 #numero di nodi
p=0.15 #probabilità


A=np.zeros([n,n])
i=1
for i in range(n):
        j=i+1
        for j in range(n):
            num=np.random.rand(1)
            if num<p:
                 A[i][j]=1
                 A[j][i]=1
                 
show_graph(A,"grafo.png")
G=nx.Graph(A)
bc=list(betweenness_centrality(G))
ec=list(eigenvector_centrality(G))
dc=list(degree_centrality(G))
cc=closeness_centrality(G)

dc1=[]
ec1=[]
bc1=[]
cc1=[]
#normalizzo 
for i in range(len(dc)):
    dc1.append(dc[i]/max(dc))
    ec1.append(ec[i]/max(ec))
    cc1.append(cc[i]/max(cc))
    bc1.append(bc[i]/max(bc))

dc1_color = [dc1[i] for i in range(len(dc1))]
ec1_color = [ec1[i] for i in range(len(ec1))]
bc1_color = [bc1[i] for i in range(len(bc1))]
cc1_color = [cc1[i] for i in range(len(cc1))]

plt.figure(figsize=(6, 4))

plt.subplot(2, 2, 1)
nx.draw(G,pos=None,with_labels=False,node_size=100,node_color=dc1_color,width=0.05)


plt.subplot(2, 2, 2)
nx.draw(G,pos=None,with_labels=False,node_size=100,node_color=ec1_color,width=0.05)

plt.subplot(2, 2, 3)
nx.draw(G,pos=None,with_labels=False,node_size=100,node_color=bc1_color,width=0.05)

plt.subplot(2, 2, 4)
nx.draw(G,pos=None,with_labels=False,node_size=100,node_color=cc1_color,width=0.05)

plt.savefig("centrality.png")