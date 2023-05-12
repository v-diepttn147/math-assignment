import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
import csv
import timeit

start = timeit.default_timer()

input_file = "amazon_ungraph_new_sorted.txt"
with open(input_file, "r") as read_obj:
    csv_reader = csv.reader(read_obj, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    list_of_rows = [[int(row[0]), int(row[1])] for row in csv_reader if row]

G = nx.Graph()
G.add_edges_from(list_of_rows)

print(G)

communities = girvan_newman(G)

f = open("result_girvan-newman.txt", "w")
f.write(f"Input file: {input_file}\n")
f.write(f"Graph specification: {G}\n\n")

num_com = 0
for com in next(communities):
    num_com += 1
    f.write(f"Community {num_com}: {com}\n")

stop = timeit.default_timer()

f.write(f"Runtime: {stop - start} s")

f.close()

print(f"Number of communities using Girvan-Newman: {num_com}")
print(f"Runtime: {stop - start} s")
