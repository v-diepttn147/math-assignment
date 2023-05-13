from community import community_louvain
import networkx as nx
import pandas as pd
from utils import NMI_evaluation

if __name__ == "__main__":

    dataset_path = "data/amazon_ungraph_new.txt"
    
    # Load the dataset
    dataset = pd.read_csv(dataset_path, delimiter=' ', names=["from", "to", "characteristics"])

    # Create a graph object from the dataset
    graph = nx.from_pandas_edgelist(dataset, source="from", target="to")
    
    # Apply the Louvain algorithm
    partition = community_louvain.best_partition(graph)

    # Print the identified communities
    for node, community_id in partition.items():
        print(f"Node {node} belongs to community {community_id}")

    print("="*20)
    print("RUN EVALpip UATION")
    print("NMI score: ",NMI_evaluation(partition))