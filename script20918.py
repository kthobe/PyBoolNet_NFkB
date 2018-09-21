# PyBoolNet program to create an interaction graph from a boolnet file (e.g. exported from GINsim)

import PyBoolNet
import FileExchange
import InteractionGraphs 

primes = FileExchange.bnet2primes("/home/kthobe/mdcstg1/PyBoolNet/TNFLTbRmodel.bnet")

igraph = PyBoolNet.InteractionGraphs.primes2igraph(primes)

PyBoolNet.InteractionGraphs.igraph2image(igraph,"/home/kthobe/Programs/TNF_LTbR2.pdf")

