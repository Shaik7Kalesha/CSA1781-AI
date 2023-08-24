# Define a simple dataset
# Each row: [feature_1, feature_2, label]
dataset = [
    [2.0, 3.5, 0],
    [3.0, 4.0, 0],
    [1.5, 2.5, 1],
    [4.5, 5.0, 1]
]

# Define a Decision Tree Node class
class DecisionTreeNode:
    def __init__(self, feature_idx=None, threshold=None, left=None, right=None, label=None):
        self.feature_idx = feature_idx  # Index of the feature to split on
        self.threshold = threshold      # Threshold value to split on
        self.left = left                # Left subtree
        self.right = right              # Right subtree
        self.label = label              # Class label (if leaf node)

# Define a function to calculate Gini impurity
def gini_impurity(labels):
    label_counts = {}
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1
    total_samples = len(labels)
    gini = 1.0
    for count in label_counts.values():
        gini -= (count / total_samples) ** 2
    return gini

# Define a function to find the best split for a dataset
def find_best_split(dataset):
    best_gini = float('inf')
    best_feature_idx = None
    best_threshold = None
    
    num_features = len(dataset[0]) - 1
    for feature_idx in range(num_features):
        feature_values = [row[feature_idx] for row in dataset]
        thresholds = list(set(feature_values))
        
        for threshold in thresholds:
            left_indices = [i for i, val in enumerate(feature_values) if val <= threshold]
            right_indices = [i for i, val in enumerate(feature_values) if val > threshold]
            
            left_labels = [dataset[i][-1] for i in left_indices]
            right_labels = [dataset[i][-1] for i in right_indices]
            
            if left_labels and right_labels:
                gini_left = gini_impurity(left_labels)
                gini_right = gini_impurity(right_labels)
                weighted_gini = (len(left_labels) / len(dataset)) * gini_left + (len(right_labels) / len(dataset)) * gini_right
                
                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_feature_idx = feature_idx
                    best_threshold = threshold
    
    return best_feature_idx, best_threshold

# Define a recursive function to build the Decision Tree
def build_decision_tree(dataset):
    labels = [row[-1] for row in dataset]
    
    # If all labels are the same, return a leaf node
    if len(set(labels)) == 1:
        return DecisionTreeNode(label=labels[0])
    
    # If no features left or dataset is small, return a leaf node with the majority class
    if len(dataset[0]) == 1 or len(dataset) < 2:
        label_counts = {}
        for label in labels:
            label_counts[label] = label_counts.get(label, 0) + 1
        majority_label = max(label_counts, key=label_counts.get)
        return DecisionTreeNode(label=majority_label)
    
    best_feature_idx, best_threshold = find_best_split(dataset)
    
    if best_feature_idx is None or best_threshold is None:
        label_counts = {}
        for label in labels:
            label_counts[label] = label_counts.get(label, 0) + 1
        majority_label = max(label_counts, key=label_counts.get)
        return DecisionTreeNode(label=majority_label)
    
    left_indices = [i for i, val in enumerate([row[best_feature_idx] for row in dataset]) if val <= best_threshold]
    right_indices = [i for i, val in enumerate([row[best_feature_idx] for row in dataset]) if val > best_threshold]
    
    left_subtree = build_decision_tree([dataset[i] for i in left_indices])
    right_subtree = build_decision_tree([dataset[i] for i in right_indices])
    
    return DecisionTreeNode(feature_idx=best_feature_idx, threshold=best_threshold,
                            left=left_subtree, right=right_subtree)

# Define a function to make predictions using the Decision Tree
def predict_sample(tree, sample):
    if tree.label is not None:
        return tree.label
    
    if sample[tree.feature_idx] <= tree.threshold:
        return predict_sample(tree.left, sample)
    else:
        return predict_sample(tree.right, sample)

# Build the Decision Tree
tree = build_decision_tree(dataset)

# Sample test data
test_samples = [
    [2.5, 3.7],
    [1.0, 2.0],
    [4.0, 4.5]
]

# Make predictions
for sample in test_samples:
    predicted_label = predict_sample(tree, sample)
    print(f"Sample {sample}: Predicted Label {predicted_label}")
