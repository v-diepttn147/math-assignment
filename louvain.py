import community
import networkx as nx
import pandas as pd

if __name__ == "__main__":

    dataset_path = "data/amazon_ungraph_new.txt"
    
    # Load the dataset
    dataset = pd.read_csv(dataset_path, delimiter=' ', names=["from", "to", "characteristics"])

    # Create a graph object from the dataset
    graph = nx.from_pandas_edgelist(dataset, source="from", target="to")
    
    # Apply the Louvain algorithm
    partition = community.best_partition(graph)

    # Print the identified communities
    for node, community_id in partition.items():
        print(f"Node {node} belongs to community {community_id}")