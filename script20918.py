# PyBoolNet program to create an interaction graph from a boolnet file (e.g. exported from GINsim)
# To run it, go in pyboolnet conda environment and call it with python

import PyBoolNet
import FileExchange
import InteractionGraphs 


bnet_file = "/home/kthobe/Programs/PyBoolNet_NFkB/TNFLTbRmodel.bnet"

primes = FileExchange.bnet2primes(bnet_file)

igraph = PyBoolNet.InteractionGraphs.primes2igraph(primes)
igraph.graph["rankdir"] = "TB"
#InteractionGraphs.add_style_inputs(igraph)
subgraphs =[(["TNFR","NEMO_IKK","IkBa", "RelA_p50c", "RelA_p50n"],{"label":"Canonical pathway"}),
	    (["LTbR","TRAF3", "NIK_IKKa", "p100p", "RelB_p52"],{"label":"Noncanonical pathway"})]
InteractionGraphs.add_style_subgraphs(igraph,subgraphs)
print(igraph.nodes())



PyBoolNet.InteractionGraphs.igraph2image(igraph,"/home/kthobe/Programs/PyBoolNet_NFkB/TNF_LTbR2.pdf")

