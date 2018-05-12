# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:26:15 2018

@author: johan
"""

import matplotlib.pyplot as plt



# Nodes = 1000
###############################################################################
# Connections = 3

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Nodes = 1000, Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/3 Conns/numconsensus3.png', bbox_inches='tight')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Nodes = 1000, Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/3 Conns/orphans3.png', bbox_inches='tight')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Nodes = 1000, Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/3 Conns/totalblocks3.png', bbox_inches='tight')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Nodes = 1000, Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/3 Conns/ratio3.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# Onchain Blocks")
plt.title("Nodes = 1000, Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/3 Conns/onchain3.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Nodes = 1000, Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/3 Conns/avgtime3.png', bbox_inches='tight')
plt.show()


###############################################################################
# Connections = 64

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Nodes = 1000, Connections = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/64 Conns/numconsensus64.png', bbox_inches='tight')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Nodes = 1000, Connections = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/64 Conns/orphans64.png', bbox_inches='tight')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Nodes = 1000, Connections = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/64 Conns/totalblocks64.png', bbox_inches='tight')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Nodes = 1000, Connections = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/64 Conns/ratio64.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# Onchain Blocks")
plt.title("Nodes = 1000, Connections = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/64 Conns/onchain64.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Nodes = 1000, Connections = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/64 Conns/avgtime64.png', bbox_inches='tight')
plt.show()

###############################################################################
# Connections = 8

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Nodes = 1000, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/8 Conns/numconsensus8.png', bbox_inches='tight')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Nodes = 1000, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/8 Conns/orphans8.png', bbox_inches='tight')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Nodes = 1000, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/8 Conns/totalblocks8.png', bbox_inches='tight')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Nodes = 1000, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/8 Conns/ratio8.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# Onchain Blocks")
plt.title("Nodes = 1000, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/8 Conns/onchain8.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Nodes = 1000, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/8 Conns/avgtime8.png', bbox_inches='tight')
plt.show()


###############################################################################
# Nodes = 100 
###############################################################################
# Connections = 8

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Nodes = 100, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/100 Nodes, 8 Conns/numconsensus100.png', bbox_inches='tight')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Nodes = 100, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/100 Nodes, 8 Conns/orphans100.png', bbox_inches='tight')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Nodes = 100, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/100 Nodes, 8 Conns/totalblocks100.png', bbox_inches='tight')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Nodes = 100, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/100 Nodes, 8 Conns/ratio100.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# Onchain Blocks")
plt.title("Nodes = 100, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/100 Nodes, 8 Conns/onchain100.png', bbox_inches='tight')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Nodes = 100, Connections = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='upper left', bbox_to_anchor=(1,1), shadow=True, title="Dilution rate")
plt.savefig('C:/Users/johan/Documents/GitHub/blockchain/100 Nodes, 8 Conns/avgtime100.png', bbox_inches='tight')
plt.show()