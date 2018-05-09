# -*- coding: utf-8 -*-
"""
Agent-Based Model of Bitcoin/Blockchain networks

Created on Tue Apr 24 14:07:57 2018

@authors: Johanna Croton, Nikolaj Bauer, Sebastian Haelg

"""
# Import packages
from __future__ import division
import random
import numpy as np
import copy
from copy import deepcopy

# Set random seed
random.seed(100)

# Set order parameters
network_delay = 10  # lambda^-1
num_nodes = 100     # number of nodes in the network
nodes_conn = 8      # maximum number of connections    
dilusion_rate = 0.9 # percentage of NON-miners
expo_scale = 0.096  # parameter for exponential distribution of computational power   


###############################################################################
# Define Functions  
###############################################################################  

def random_graph(n, k):
    """
    Function to initialize the network
    """
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
  
    
def consensus():
    """
    Creates a vector of each node's last block element, 
    then checks if all elements of the vector are equal.
    If returns true, then the network has reached consensus.
    """
    
    a = [last_block[i][-1] for i in range(num_nodes)]
    return(len(set(a)) <=1)


def delay_time(L, n):
    """
    Creates an array of delay times, i.e. the time it will take a node to gossip to one neighbor, 
    to two neighbors, ect. such that the time intervall between the gossiping events follows a 
    poisson distribution.    
    """  
    epsilon = np.random.poisson(L, n+1)
    delay=list()
    delay.append(epsilon[0])
    for e in range(n-1):
        delay.append(delay[e] + epsilon[e + 1])
    return(delay)
    
        
def new_block(lucky, num):  
    """
    Creates a new block when called for "lucky" miner node using its parent block (blockID) and
    the current block number. 
    """
    # Set variables that are changed within the function to global scope
    global last_block
    global info_list
    global neighbors
    global delay_list
    global list_blockIDs
    
    # Create the block
    block_ID = copy.copy(last_block[lucky])  # copy parent block from lucky miner
    block_ID.append(num)                     # add current block number parent block
    print(block_ID)                          
    list_blockIDs.append(block_ID)           # record each new block to global scope
    last_block[lucky] = copy.copy(block_ID)  # add the new block to lucky's chain
    
    # Update lucky's info
    info_list[lucky, 1] = 1                                                     # set lucky's state to "gossiping"
    neighbors[lucky] = copy.copy(neighbor_list[lucky])                          # reset neighbors to gossip new block to (all)
    delay_list[lucky] = delay_time(network_delay, len(neighbor_list[lucky]))    # reset the delay times
    delay_list[lucky] = [x+t for x in delay_list[lucky]]


def gossiping():
    """
    One round of gossiping for all nodes that are in state 1. 
    """
    
    # Set variables that are changed within the function to global scope
    global delay_list
    global neighbor_list
    global neighbors
    global last_block
    global info_list
    global last_block
    
    # Iterate throuhg all gossiping nodes
    for gossiper in gossipers:
         listeners = neighbors[gossiper]        # find listeners, i.e. neighbors that the node has not its gossiped current block to yet
         if len(listeners) == 0 :               # if there are no more neighbors to gossip to
             info_list[gossiper,1] = 0          # gossiper stops gossiping, set state to 0     
         elif delay_list[gossiper][0] < t :     # if there are listeners to gossip to and time is > than the node's delay_time
             choose = random.randrange(0,len(listeners)) 
             listener = listeners[choose]       # choose a random listener to gossip to  
             del neighbors[gossiper][choose]    # remove the listener from the neighbors that can still be gossiped to
             del delay_list[gossiper][0]        # next entry will be the time it takes to gossip to two nodes
             
             # Compare gossiper and listener's chain lengths
             if len(last_block[gossiper]) > len(last_block[listener]) :      # listener's chain is shorter
                 last_block[listener] = copy.copy(last_block[gossiper])      # listener adopts gossiper's chain
                 info_list[listener][1] = 1                                  # update listener's state to gossiper
                 neighbors[listener] = copy.copy(neighbor_list[listener])    # reset neighbors to gossip new block to (all)
                 delay_list[listener] = delay_time(network_delay, len(neighbor_list[listener])) 
                 delay_list[listener] = [x+t for x in delay_list[listener]]  # reset the delay times
             elif len(last_block[gossiper]) == len(last_block[listener]):    # if both chains are equally long
                  if (last_block[gossiper][-1] > last_block[listener][-1]):  # last element in gossiper's chain is bigger (older) than the listener's
                      last_block[listener] = copy.copy(last_block[gossiper]) # listener adopts gossiper's chain
                        

###############################################################################
#Initialize Variables
###############################################################################                      
    

for trial in range(1, 20):
                      
    # Initialize the network
    network = random_graph(num_nodes, nodes_conn)   # call network function
    neighbor_list=network[1]                        # create list of each node's neighbors                 
    
    # Create empty matrix of nodes and information
    info_list=np.zeros((num_nodes,3))               # 1:node IDs 2:status 3:mining probabilities
    info_list[:,0]=list(range(num_nodes))           # update column 1: node IDs
    
    # Make block IDs for the current block in each node's chain
    last_block =[[(0)] for i in range(num_nodes)]
    
    # Counter of new blocks in order of creation
    block_num = 1
                        
    # Create a random first block with ID 1
    new = random.randrange(0, num_nodes) # choose a random node 
    info_list[new,1] = 1                 # change random node's state to gossiping
    last_block[new] = [0,1]              # Record block ID to node's chain
    
    # Create a list to keep track the block creation sequence
    list_blockIDs = list()          # intialize empty list
    list_blockIDs.append([0])       # add block 0 (all nodes start out with)
    list_blockIDs.append([0, 1])    # add block 1 (was manually inserted)
    
    # Endow each node with computational power = number of trials it needs to solve cryptographic problem
    comp_power = np.random.exponential(expo_scale, int(num_nodes*(1-dilusion_rate))) # computing power for fraction of nodes that are miners (non-mining nodes are 0)
    miners = random.sample(range(num_nodes), int(num_nodes*(1-dilusion_rate)))       # choose random miners
    info_list[miners,2] = comp_power                                                 # update info list column 3 for miners
    probability_dt = (info_list[:,2]/sum(info_list[:,2]))/100                        # probability that a specific node mines a new block (node's comp. power / sum of all node's comp. power)
    probability = copy.copy(probability_dt)                                          # variable that will be used below
        
    # Calculate network delays for all nodes
    delay_list = list()                                         # initialize empty list
    for i in range(num_nodes):                                  # for each node add delay times to its list
       add = delay_time(network_delay, len(neighbor_list[i]))
       delay_list.append(add)
    
    # Find the gossipers
    gossipers = info_list[:,0][info_list[:,1]==1] # find nodes in state one
    gossipers = [int(i) for i in gossipers]       # convert to integrals 
    
    # Create copy of the neighbor list to keep track of which nodes have been gossiped to for a specific block
    neighbors = copy.copy(neighbor_list) # create copy for deleting and adding listeners to
    #neighbors = [neighbor_list[i] for i in gossipers] #neighbors to those nodes in state one
    
    # Variable to check whether a new consensus has been reached
    cons = np.zeros((1,2))
    consensus_times = [] 
    
    # Time and gossiping round begin at zero
    t=0 

    
         
###############################################################################
# Run the code
###############################################################################    


    
            
    while t <10000 :
    
        gossiping() # one round of gossip
        
        gossiping_round = gossiping_round + 1 # increment number of rounds
        # print("gossiping round number:")
        # print(gossiping_round)
        
        
        # Block creation, keeping in mind that for all non-miners probability=0
        for i in range(num_nodes):              # iterate through all nodes
            lottery = random.uniform(0.0, 1.0)  # generate random number
            if lottery > probability[i]:        # node does not mine a new block
                probability[i] = (1-probability[i]) * probability[i]  # probability of finding block next round goes up 
            else:                               # node mines a new block
                block_num = block_num + 1       # increment block number
                new_block(i, block_num)         # function creates a new block; current node is "lucky"
                probability[i] = probability_dt[i] # reset miner's probability
               # print("new block mined by")     # output: which miner got lucky
               # print(i)
                
        # Check for consensus in the network    
        cons[0,0] = copy.copy(cons[0,1]) # first column is previous consensus status
        cons[0,1] = consensus()          # update second column with current consensus status
        if cons[0,0] != cons[0,1]:       # consensus status has changed
            if cons[0,1] == True:        # if network is in consensus
                print("consensus reached after t =") 
                print(t)
                consensus_times.append(t) # record times that consensus was reached
           
        # Update information for next round            
        t=t+1                                         # increment time
        gossipers = info_list[:,0][info_list[:,1]==1] # find nodes in state one
        gossipers = [int(i) for i in gossipers]       # convert to integrals 
         
    
    # Record results     
    chain_len = [len(last_block[i]) for i in range(num_nodes)]  # find the main (longest) chain(s)
    longest_chain_index = chain_len.index(max(chain_len))       # record the index (if multiple chains are equally long, chooses one) 
    longest_chain = copy.copy(last_block[longest_chain_index])  # longest chain's block
    check_block = list(range(longest_chain[-1]+1))              # create a comparison chain with no gaps
    orphans = list(set(check_block) - set(longest_chain))       # compare longest chain with comparison chain, missing blocks are orphans
    num_orphans = len(orphans)                                  # record number of orphaned blocks
    num_total = block_num                                       # record total number of blocks mined
    num_onchain = len(longest_chain)                            # record total number of blocks on the main chain
    num_consensus = len(consensus_times)                        # record number of times consensus was reached
    
    ratio = num_orphans/num_total
    print("Trial")
    print(trial)
    print(num_orphans)

    orphanedblocks.append(num_orphans)
    
    

  
