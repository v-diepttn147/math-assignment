import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import pandas as pd
import numpy as np
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
import csv
import time
from ultis import NMI_evaluation

dataset_path = "data/amazon_ungraph_new.txt"
# Load the dataset
dataset = pd.read_csv(dataset_path, delimiter=' ', names=["from", "to", "characteristics"])

start = time.time()
# Create a graph object from the dataset
G = nx.from_pandas_edgelist(dataset, source="from", target="to")

print(G)

communities = girvan_newman(G)


f = open("result_girvan-newman.txt", "w")
f.write(f"Input file: {dataset_path}\n")
f.write(f"Graph specification: {G}\n\n")


num_com = 0
partition = {}
for com in next(communities):
    num_com += 1
    for i in com:
        partition[int(i)] = num_com
    f.write(f"Community {num_com}: {com}\n")

stop = time.time()


f.write(f"Runtime: {stop - start} s")

f.close()

print(f"Number of communities using Girvan-Newman: {num_com}")
print(f"Runtime: {stop - start} s")

print("="*20)
print("RUN EVALUATION")
print("NMI score: ",NMI_evaluation(partition))