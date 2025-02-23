# %%
import numpy as np
import pandas as pd
from collections import Counter

# %%
#Decision Trees
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features #No. of features we want to select from our df 
        self.root = None

#Training
#When we call fit: 
#   we check that #features is not more than actual #features
#   Call grow_tree 
#   Grow tree checks the best feature. At first checks the stopping criteria and then calls best split 
#   Best split calls Information Gain
#   Information Gain calls Entropy and split
#   Split is run = tells what the left and the right trees are 
#   Inforamtion Gain passed back to best split, and best split is passed back to grow-tree
#Then create child nodes in iteration 

    def fit(self, X, y): 
        self.classes_, y = np.unique(y, return_inverse=True) #Convert y to non-negative integers 
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_feats = X.shape # Total no. of samples and features
        n_labels = len(np.unique(y))
        
        #Check the stopping criteria
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
        
        feat_idxs = np.random.choice(n_feats, self.n_features, replace=False) #For unique features (No duplicated)

        #Find the best split
        best_feature, best_thresh = self._best_split(X, y, feat_idxs)

        #Create child nodes
        left_idxs, right_idxs = self._split(X.iloc[:, best_feature], best_thresh)
        left = self._grow_tree(X.loc[left_idxs], y[left_idxs], depth+1)
        right = self._grow_tree(X.loc[right_idxs], y[right_idxs], depth+1)
        return Node(best_feature, best_thresh, left, right)


    def _best_split(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_threshold = None, None

        for feat_idx in feat_idxs:
            X_column = X.iloc[:, feat_idx]
            thresholds = np.unique(X_column)

            for thr in thresholds:
                #Calculate the information gain
                gain = self._information_gain(y, X_column, thr)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = thr
        
        return split_idx, split_threshold
        

    def _information_gain(self, y, X_column, threshold):
        #Parent entropy
        parent_entropy = self._entropy(y)

        #Create children
        left_idxs, right_idxs = self._split(X_column, threshold)

        if len(left_idxs) == 0 or len(right_idxs) == 0: 
            return 0
        
        #Calculate weighted entropy of children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r 

        #Calculate the Information Gain
        information_gain = parent_entropy - child_entropy
        return information_gain

    def _split(self, X_column, split_thresh):
        left_idxs = X_column <= split_thresh 
        right_idxs = X_column > split_thresh 
        return left_idxs, right_idxs

    def _entropy(self, y):
        hist = np.bincount(y.astype(int))
        ps = hist / len(y) # p(X) = #x/n
        return -np.sum([p * np.log2(p) for p in ps if p>0])

    def _most_common_label(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value 

    
    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        elif hasattr(X, 'values'):
            X = X.values
        
        if X.ndim == 1:
            X = X.reshape(1, -1) #Ensure X is a 2D array

        predictions = []
        for x in X:
            prediction = self._traverse_tree(x, self.root)
            predictions.append(prediction)

        return np.array(predictions)

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        
        if not isinstance(x, np.ndarray): #Ensure x is numpy array
            x = np.array(x)
        
        if node.feature >= len(x):
            raise ValueError(f'Feature index {node.feature} is out of range for input with {len(x)} features')

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)


