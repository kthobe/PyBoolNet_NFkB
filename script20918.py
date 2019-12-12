# PyBoolNet program to create an interaction graph from a boolnet file (e.g. exported from GINsim)
# To run it, go in pyboolnet conda environment and call it with python

import PyBoolNet
import FileExchange
import InteractionGraphs

Load = 1
IAgraph = 0
STGgraph = 0
Commitgraph =1

if Load == 1:
	# Load model from BoolNet file
	bnet_file = "/home/kthobe/Programs/PyBoolNet_NFkB/TNFLTbRmodel.bnet"

	# Create model in Primes format
	primes = FileExchange.bnet2primes(bnet_file)

if IAgraph ==1:
	# Build and format Interaction Graph
	igraph = PyBoolNet.InteractionGraphs.primes2igraph(primes)
	igraph.graph["rankdir"] = "TB"
	#InteractionGraphs.add_style_inputs(igraph)
	subgraphs =[(["TNFR","NEMO_IKK","IkBa", "RelA_p50c", "RelA_p50n"],{"label":"Canonical pathway"}),
		    (["LTbR","TRAF3", "NIK_IKKa", "p100p", "RelB_p52"],{"label":"Noncanonical pathway"})]
	InteractionGraphs.add_style_subgraphs(igraph,subgraphs)
	print(igraph.nodes())
	PyBoolNet.InteractionGraphs.igraph2image(igraph,"/home/kthobe/Programs/PyBoolNet_NFkB/TNF_LTbR2.pdf")

if STGgraph == 1:
	# Build and format STG and Commitment sets

	PyBoolNet.StateTransitionGraphs.create_image(primes, "asynchronous", "/home/kthobe/Programs/PyBoolNet_NFkB/stg.pdf")
	scc_graph = PyBoolNet.StateTransitionGraphs.stg2sccgraph(stg)
	PyBoolNet.StateTransitionGraphs.sccgraph2image(scc_graph, "/home/kthobe/Programs/PyBoolNet_NFkB/scc_graph.pdf")

if Commitgraph == 1:

	attrs = PyBoolNet.Attractors.compute_json(primes, "asynchronous")
	diag = PyBoolNet.Commitment.compute_diagram(attrs)
	PyBoolNet.Commitment.diagram2image(diag, "/home/kthobe/Programs/PyBoolNet_NFkB/commitment_diag.pdf")
