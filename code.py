# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:07:57 2018

@author: johan
"""
from __future__ import division
import random
#import powerlaw as pl
import networkx as nx
import numpy as np
import math as m
import matplotlib.pyplot as plt


random.seed(100)

#order parameters
network_delay = 10   #lambda
discovery = []      #expected time between block discoveries
num_nodes = 100        # number of nodes in the network
nodes_conn = 8      

"""
#initialize network
naka_net = nx.erdos_renyi_graph(num_nodes, float(nodes_conn) / float(num_nodes))

#create list of neighbors for each node
neighbor_list=list()
for line in nx.generate_adjlist(naka_net): 
    print(line)
    line=[int(s) for s in line.split(' ')]
    neighbor_list.append(line)
    
for i in range(len(neighbor_list)):  #remove the node ID from the neighbor-list
    del neighbor_list[i][0]
 """

def random_graph(n, k):
    # A function that creates a random graph, by Martin Ritchie
    # 08/06/2016. This funciton is a revision of my first 
    # attempt in python to code the Erdos-Renyi random graph
    # algortihtm. The code now include an adjacency list and
    # edge list as ouput in addtion to the adjacency matrix. 
    # ------------------- Inputs --------------------------
    # N: number of nodes.
    # k: desired average degree.
    # ------------------- Outputs -------------------------
    # A: adjacency matrix (line 16 for sparse).
    # A_list: adjacency list.
    # edge_list: list of edges. 
   # import ipdb
    # ipdb.set_trace()
    # A = lil_matrix((n, n), dtype=np.int8)
    A_list = [[] for i in range(n)] 
    edge_list = []
    p = 1 - (float(k) / (n - 1))
    A = np.random.random((n, n))
    A *= np.tri(*A.shape)
    np.fill_diagonal(A, 0)
    
    edge = A>p 
    A[edge] = 1
    no_edge = A <= p 
    A[no_edge] = 0  # All low values set to 0
    A = np.add(A, A.transpose())

    for i in range(n):
        for j in range(i-1):
            if A[i, j] > 0: 
                A_list[i] = A_list[i] + [j]
                A_list[j] = A_list[j] + [i]
                edge_list.append((i,j))
                edge_list.append((j,i))
    return (A, A_list, edge_list) 
  
    

def delay_time(L, n):
    """
    create an array of time it will take to gossip to one neighbor, to two neighbors,
    ect. such that the time intervall between the gossiping events follows a 
    poisson distribution
    """
    
    
    epsilon = np.random.poisson(L, n)
    
    delay=list()
    delay.append(epsilon[0])
    
    for e in range(n-1):

        delay.append(delay[e] + epsilon[e+1])
    return(delay)
        
    
    
    
def gossiping():
    
     #iterate throuhg all gossiping nodes
        for gossiper in gossipers:
            

             listeners = neighbors[gossiper] #all the neighbors the active node has not yet gossiped to
             
             if len(listeners) == 0 :    #if there are no more neighbors to gossip to
                 info_list[gossiper,1] = 0
                 
             elif delay_list[gossiper][0] < t :  #time is > than the delay for the next gossip round
                
                 choose = random.randrange(0,len(listeners)) #choose a random node to gossip to
                 listener = listeners[choose]
                 del neighbors[gossiper][choose] #remove the neighbor
                 del delay_list[gossiper][0] #next entry will be the time it takes to gossip to two nodes
                 
                 if info_list[gossiper][2] > info_list[listener][2] : #compare chains (block-ID)
                     
                     info_list[listener][2] = info_list[gossiper][2] #adopt gossipers Chain
                     info_list[listener][1] = 1 #change the state
                     neighbors[listener] = neighbor_list[listener] #start gossiping to all neighbors again
                      #need to update the listeners delay times (newly started gossiping)
                     delay_list[listener] = delay_time(network_delay, len(neighbor_list[listener]))
                     delay_list[listener] = [x+t for x in delay_list[listener]]
       
                        
#initialize the network
network = random_graph(num_nodes, nodes_conn)
neighbor_list=network[1]                    


                        
#matrix of nodes and information
info_list=np.zeros((num_nodes,3))

#first column: node IDs
info_list[:,0]=list(range(100))

#third column: block IDs, set all to 1
info_list[:,2]=1
  
    
#calculating network delays for all nodes
delay_list = list()
for i in range(num_nodes):
   add = delay_time(network_delay, len(neighbor_list[i]))
   delay_list.append(add)


gossipers = info_list[:,0][info_list[:,1]==1] #nodes in state one
gossipers = [int(i) for i in gossipers]
neighbors = neighbor_list #we will delete and add the neighbors from this list
#neighbors = [neighbor_list[i] for i in gossipers] #neighbors to those nodes in state one
t=0 
 
    
while len(gossipers) > 0 :

    gossiping()


    t=t+1
    gossipers = info_list[:,0][info_list[:,1]==1] #nodes in state one
    gossipers = [int(i) for i in gossipers]

print("Consensus reached after t =")
print(t)    
 
       

    
