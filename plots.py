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
plt.title("Num. Nodes = 1000; Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Num. Nodes = 1000; Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Num. Nodes = 1000; Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Num. Nodes = 1000; Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# of Onchain Blocks")
plt.title("Num. Nodes = 1000; Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Num. Nodes = 1000; Connections = 3")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults[i]]) for i in range(len(fullresults))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()



##################################################
# Connections = 64

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Num. Nodes = 1000; Connection = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Num. Nodes = 1000; Connection = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Num. Nodes = 1000; Connection = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Num. Nodes = 1000; Connection = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# of Onchain Blocks")
plt.title("Num. Nodes = 1000; Connection = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Num. Nodes = 1000; Connection = 64")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults000[i]]) for i in range(len(fullresults000))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()


##################################################
# Connections = 8

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Num. Nodes = 1000; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Num. Nodes = 1000; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Num. Nodes = 1000; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Num. Nodes = 1000; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# of Onchain Blocks")
plt.title("Num. Nodes = 1000; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Num. Nodes = 1000; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults001[i]]) for i in range(len(fullresults001))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:26:15 2018

@author: johan
"""

import matplotlib.pyplot as plt


###############################################################################
# Nodes = 100
###############################################################################
###############################################################################
# Connections = 8

# Number of Consensus
plt.xlabel("Network Delays")
plt.ylabel("# Consenus Reached")
plt.title("Num. Nodes = 100; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[5] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of orphaned blocks
plt.xlabel("Network Delays")
plt.ylabel("# Orphaned Blocks")
plt.title("Num. Nodes = 100; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[0] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Number of total blocks
plt.xlabel("Network Delays")
plt.ylabel("# Total Blocks")
plt.title("Num. Nodes = 100; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[1] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Ratio
plt.xlabel("Network Delays")
plt.ylabel("Orphaned Blocks / Total Blocks")
plt.title("Num. Nodes = 100; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[2] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Onchain Blocks
plt.xlabel("Network Delays")
plt.ylabel("# of Onchain Blocks")
plt.title("Num. Nodes = 100; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[3] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()

# Time until Consensus
plt.xlabel("Network Delays")
plt.ylabel("Average Time until Consensus")
plt.title("Num. Nodes = 100; Connection = 8")
plt.xscale("log")
[plt.plot(network_delays, [column[4] for column in fullresults002[i]]) for i in range(len(fullresults002))]
plt.legend([round(i, 2) for i in dilusion_rates], loc='lower right')
plt.show()