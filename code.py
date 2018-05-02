# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:07:57 2018

@author: johan
"""
from __future__ import division
#import random, time, toolkit
#import powerlaw as pl
import networkx as nx
import numpy as np
import math as m
import matplotlib.pyplot as plt

num_nodes = 100        # number of nodes in the network
nodes_conn = 8      

#initialize network
naka_net = nx.erdos_renyi_graph(num_nodes, float(nodes_conn) / float(num_nodes))

#create list of neighbors for each node
neighbor_list=list()
for line in nx.generate_adjlist(naka_net): 
    print(line)
    line=[int(s) for s in line.split(' ')]
    neighbor_list.append(line)
   
#matrix of nodes and information
info_list=np.zeros((100,3))

#first column: node IDs
info_list[:,0]=list(range(100))

#third column: block IDs, set all to 1
info_list[:,2]=1
    
"""
pseudo code for gossip
increment=[] 

def gossip():
"find nodes in state=1
"find neighbors for each node in state 1
for nodes[status]==1:
    if increment[node] < range_neighbors:
    "pick random neighbor
    "remove neighbor from neighbor_list
        if block[node]>block[neighbor]:
            "update neighbor block
            "neighbor block length +1
            "reset neighbors neighbor_list 
            "reset increment=0
    else node[]=0
    
 """
  
 def gossip():
     gossipers = info_list[:,0][info_list[:,1]==1] #nodes in state one
     gossipers = [int(i) for i in gossipers]
     listeners = [neighbor_list[i] for i in gossipers] #neighbors to those in state one
     
     #iterate thruohg all gossiping nodes
     for x in range(len(gossipers)):
         
         gossiper = gossipers[x] #index of the active node, that is gossipping 
         neighbors = listeners[x] #all its neighbors the active node has not yet gossiped to
         
       

    
