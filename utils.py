from sklearn import metrics

def NMI_evaluation(partition,ground_truth_file='./data/amazon_deup_new.txt'):

    # Load the ground truth community assignments
    ground_truth_labels = {}
    with open(ground_truth_file, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        community = i
        products = line.strip().split()
        for product in products:
            ground_truth_labels[int(product)] = community

    # Initialize dictionaries for storing predicted labels and filtered ground truth labels
    predicted_labels = {}
    final_GT_labels = {}

    # Iterate over each node and its corresponding community ID in the partition
    for node, community_id in partition.items():
        if node in ground_truth_labels:
            # Store the predicted label for the node
            predicted_labels[int(node)] = int(community_id)
            # Store the corresponding ground truth label for the node
            final_GT_labels[int(node)] = ground_truth_labels[int(node)]

    # Compute the NMI score
    nmi_score = metrics.normalized_mutual_info_score(list(final_GT_labels.values()), list(predicted_labels.values()))

    # Return the NMI score
    return nmi_score