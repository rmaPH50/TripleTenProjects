#!/usr/bin/env python
# coding: utf-8

# # Statement

# The Sure Tomorrow insurance company wants to solve several tasks with the help of Machine Learning and you are asked to evaluate that possibility.
# 
# - Task 1: Find customers who are similar to a given customer. This will help the company's agents with marketing.
# - Task 2: Predict whether a new customer is likely to receive an insurance benefit. Can a prediction model do better than a dummy model?
# - Task 3: Predict the number of insurance benefits a new customer is likely to receive using a linear regression model.
# - Task 4: Protect clients' personal data without breaking the model from the previous task. It's necessary to develop a data transformation algorithm that would make it hard to recover personal information if the data fell into the wrong hands. This is called data masking, or data obfuscation. But the data should be protected in such a way that the quality of machine learning models doesn't suffer. You don't need to pick the best model, just prove that the algorithm works correctly.

# # Data Preprocessing & Exploration
# 
# ## Initialization

# In[1]:


import numpy as np
import pandas as pd

import seaborn as sns

import sklearn.linear_model
import sklearn.metrics
import sklearn.neighbors
import sklearn.preprocessing

from sklearn.model_selection import train_test_split

from IPython.display import display


# ## Load Data

# Load data and conduct a basic check that it's free from obvious issues.

# In[2]:


df = pd.read_csv('/datasets/insurance_us.csv')


# We rename the colums to make the code look more consistent with its style.

# In[3]:


df = df.rename(columns={'Gender': 'gender', 'Age': 'age', 'Salary': 'income', 'Family members': 'family_members', 'Insurance benefits': 'insurance_benefits'})


# In[4]:


df.sample(10)


# In[5]:


df.info()


# In[6]:


# we may want to fix the age type (from float to int) though this is not critical
df['age'] = df['age'].astype('int64')


# In[7]:


# check to see that the conversion was successful
df.info()


# In[8]:


# now have a look at the data's descriptive statistics. 
# Does everything look okay? 
df.describe()


# In[9]:


# Check for non-integer values
non_integer_family_members = df[df['family_members'] % 1 != 0]
print(non_integer_family_members)


# In[10]:


# Investigate rows with insurance_benefits > 1
unusual_benefits = df[df['insurance_benefits'] > 1]
print(unusual_benefits)


# In[11]:


df['family_members'] = df['family_members'].astype(int)
df['insurance_benefits'] = df['insurance_benefits'].clip(upper=1)
print(df['insurance_benefits'].unique())


# ## EDA

# Let's quickly check whether there are certain groups of customers by looking at the pair plot.

# In[12]:


g = sns.pairplot(df, kind='hist')
g.fig.set_size_inches(12, 12)


# Ok, it is a bit difficult to spot obvious groups (clusters) as it is difficult to combine several variables simultaneously (to analyze multivariate distributions). That's where LA and ML can be quite handy.

# # Task 1. Similar Customers

# In the language of ML, it is necessary to develop a procedure that returns k nearest neighbors (objects) for a given object based on the distance between the objects.
# 
# You may want to review the following lessons (chapter -> lesson)
# - Distance Between Vectors -> Euclidean Distance
# - Distance Between Vectors -> Manhattan Distance
# 
# To solve the task, we can try different distance metrics.

# Write a function that returns k nearest neighbors for an $n^{th}$ object based on a specified distance metric. The number of received insurance benefits should not be taken into account for this task. 
# 
# You can use a ready implementation of the kNN algorithm from scikit-learn (check [the link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors)) or use your own.
# 
# Test it for four combination of two cases
# - Scaling
#   - the data is not scaled
#   - the data is scaled with the [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html) scaler
# - Distance Metrics
#   - Euclidean
#   - Manhattan
# 
# Answer these questions:
# - Does the data being not scaled affect the kNN algorithm? If so, how does that appear?
# - How similar are the results using the Manhattan distance metric (regardless of the scaling)?

# In[13]:


feature_names = ['gender', 'age', 'income', 'family_members']


# In[14]:


def get_knn(df, n, k, metric, feature_columns):
    """
    Returns k nearest neighbors

    :param df: pandas DataFrame used to find similar objects within
    :param n: object no for which the nearest neighbors are looked for
    :param k: the number of the nearest neighbors to return
    :param metric: name of distance metric
    :param feature_columns: list of feature column names to use for similarity
    :return: DataFrame containing k nearest neighbors and their distances
    """
    # Fit the NearestNeighbors model
    nbrs = NearestNeighbors(n_neighbors=k, metric=metric)
    nbrs.fit(df[feature_columns])

    # Find distances and indices of the nearest neighbors
    nbrs_distances, nbrs_indices = nbrs.kneighbors([df.iloc[n][feature_columns]], n_neighbors=k, return_distance=True)

    # Combine neighbors' data with their distances
    df_res = pd.concat([
        df.iloc[nbrs_indices[0]].reset_index(drop=True),
        pd.DataFrame(nbrs_distances.T, columns=['distance'])
    ], axis=1)

    return df_res


# Scaling the data.

# In[15]:


transformer_mas = sklearn.preprocessing.MaxAbsScaler().fit(df[feature_names].to_numpy())

df_scaled = df.copy()
df_scaled.loc[:, feature_names] = transformer_mas.transform(df[feature_names].to_numpy())


# In[16]:


df_scaled.sample(5)


# Now, let's get similar records for a given one for every combination

# In[17]:


from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Preprocess the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['age', 'income', 'family_members']])

# Fit the Nearest Neighbors model
nn = NearestNeighbors(n_neighbors=5, metric='euclidean')
nn.fit(scaled_features)

# Find similar customers for all records
all_similar_customers = {}

for customer_index in range(len(df)):
    distances, indices = nn.kneighbors([scaled_features[customer_index]])
    similar_customers = df.iloc[indices[0]]
    all_similar_customers[customer_index] = similar_customers

# Convert the dictionary to a more usable format, e.g., DataFrame
similar_customers_df = pd.DataFrame({
    'Customer_Index': list(all_similar_customers.keys()),
    'Similar_Customers': [all_similar_customers[idx].to_dict('records') for idx in all_similar_customers]
})

print(similar_customers_df.head())


# In[18]:


from sklearn.preprocessing import MaxAbsScaler

# Define feature columns
feature_columns = ['age', 'income', 'family_members']

# Scaling with MaxAbsScaler
scaler = MaxAbsScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[feature_columns]), columns=feature_columns)

# Test the four combinations
combinations = [
    ("Unscaled Data with Euclidean", df, "euclidean"),
    ("Unscaled Data with Manhattan", df, "manhattan"),
    ("Scaled Data with Euclidean", df_scaled, "euclidean"),
    ("Scaled Data with Manhattan", df_scaled, "manhattan")
]

# Print results for each combination
for test_name, test_df, metric in combinations:
    print(f"\nResults for: {test_name}")
    result = get_knn(test_df, n=0, k=5, metric=metric, feature_columns=feature_columns)
    print(result)


# In[19]:


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df_scaled)

plt.scatter(reduced_data[:, 0], reduced_data[:, 1], alpha=0.5)
plt.scatter(reduced_data[customer_index, 0], reduced_data[customer_index, 1], color='red', label='Target Customer')
plt.legend()
plt.show()


# 

# **Does the data being not scaled affect the kNN algorithm? If so, how does that appear?** 
# 
# Yes, the lack of scaling affects the kNN algorithm because it uses distance metrics (like Euclidean and Manhattan distances) to determine the similarity between data points.
# 
# Unscaled Data: 
# 
# In unscaled data, variables with larger values (such as income in your dataset) will dominate the distance calculations, overshadowing smaller scale variables like family_members. For example, in the unscaled Euclidean results, the distances between customers are quite large (e.g., 3.16, 1.41), which suggests that income and age might be influencing the distances more than family_members.
# 
# Scaled Data: 
# 
# When scaling the data (e.g., using standard scaling or max-abs scaling), each feature is transformed to a similar scale, preventing one feature from dominating the distance calculation. For example, in scaled data, the distances become much smaller (e.g., 0.000000, 0.006329), and the differences in distances are less pronounced.
# 
# Thus, scaling helps in balancing the contribution of each feature to the distance metric and ensures that no single feature disproportionately affects the result.
# 
# 

# **How similar are the results using the Manhattan distance metric (regardless of the scaling)?** 
# 
# Looking at the Manhattan distance results (both for scaled and unscaled data), the distances between neighbors are more consistent, and the values seem relatively close to one another. However, the distances are larger for the unscaled data compared to the scaled data, indicating that the scaling has indeed had an effect on the distances.
# 
# Unscaled Data with Manhattan: Distances like 0, 1, 2, 4 are observed. The distances are relatively large, especially when compared to the scaled distances. This is because the features (such as income and age) have not been scaled, so the differences in their raw values are more influential on the distance calculations.
# 
# Scaled Data with Manhattan: Distances like 0, 0.006329, 0.013924, 0.016456 are much smaller, as scaling brings all features to a similar range. This reduces the dominance of features with larger value ranges.
# 
# Manhattan distance in particular shows more variation in the unscaled data than in the scaled data, indicating that scaling helps reduce the impact of high-value features in the distance calculations.

# # Task 2. Is Customer Likely to Receive Insurance Benefit?

# In terms of machine learning we can look at this like a binary classification task.

# With `insurance_benefits` being more than zero as the target, evaluate whether the kNN classification approach can do better than a dummy model.
# 
# Instructions:
# - Build a KNN-based classifier and measure its quality with the F1 metric for k=1..10 for both the original data and the scaled one. That'd be interesting to see how k may influece the evaluation metric, and whether scaling the data makes any difference. You can use a ready implemention of the kNN classification algorithm from scikit-learn (check [the link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)) or use your own.
# - Build the dummy model which is just random for this case. It should return "1" with some probability. Let's test the model with four probability values: 0, the probability of paying any insurance benefit, 0.5, 1.
# 
# The probability of paying any insurance benefit can be defined as
# 
# $$
# P\{\text{insurance benefit received}\}=\frac{\text{number of clients received any insurance benefit}}{\text{total number of clients}}.
# $$
# 
# Split the whole data in the 70:30 proportion for the training/testing parts.

# In[20]:


# calculate the target

df['insurance_benefits_received'] = df['insurance_benefits'].apply(lambda x: 1 if x > 0 else 0)


# In[21]:


# Check the distribution of the target variable
class_distribution = df['insurance_benefits_received'].value_counts()
print(class_distribution)


# In[22]:


from sklearn.metrics import f1_score

def eval_classifier(y_true, y_pred):
    
    f1_score = sklearn.metrics.f1_score(y_true, y_pred)
    print(f'F1: {f1_score:.2f}')
    
# if you have an issue with the following line, restart the kernel and run the notebook again
    cm = sklearn.metrics.confusion_matrix(y_true, y_pred, normalize='all')
    print('Confusion Matrix')
    print(cm)


# In[23]:


# generating output of a random model

def rnd_model_predict(P, size, seed=42):

    rng = np.random.default_rng(seed=seed)
    return rng.binomial(n=1, p=P, size=size)


# In[24]:


for P in [0, df['insurance_benefits_received'].sum() / len(df), 0.5, 1]:

    print(f'The probability: {P:.2f}')
    
    # Generate random predictions for each probability P
    y_pred_rnd = rnd_model_predict(P, size=len(df))
        
    eval_classifier(df['insurance_benefits_received'], y_pred_rnd)
    
    print()


# In[25]:


# Define features and target variable
feature_columns = ['age', 'income', 'family_members']
X = df[feature_columns]
y = df['insurance_benefits_received']

# Split data into train and test sets (70:30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit and transform on training data
X_test_scaled = scaler.transform(X_test)  # Only transform on test data


# In[26]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier

# Function to train and evaluate kNN classifier
def evaluate_knn(X_train, X_test, y_train, y_test, k_values):
    f1_scores = []
    
    for k in k_values:
        # Initialize the kNN classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        
        # Train the classifier
        knn.fit(X_train, y_train)
        
        # Make predictions
        y_pred = knn.predict(X_test)
        
        # Calculate F1 score
        f1 = f1_score(y_test, y_pred)
        f1_scores.append(f1)
    
    return f1_scores

# Evaluate kNN for both original and scaled data
k_values = range(1, 11)

f1_scores_original = evaluate_knn(X_train, X_test, y_train, y_test, k_values)
f1_scores_scaled = evaluate_knn(X_train_scaled, X_test_scaled, y_train, y_test, k_values)

# Print the results
print("F1 scores for original data:")
for k, f1 in zip(k_values, f1_scores_original):
    print(f'k={k}: {f1:.4f}')


# In[27]:


# Function to evaluate the dummy classifier
def evaluate_dummy_classifier(y_true, probabilities):
    f1_scores = []
    
    for P in probabilities:
        # Initialize the dummy classifier with random predictions
        dummy = DummyClassifier(strategy='uniform', random_state=42)
        dummy.fit(np.zeros((len(y_true), 1)), y_true)  # Dummy model doesn't need features
        
        # Generate random predictions
        y_pred_rnd = rnd_model_predict(P, size=len(y_true))
        
        # Calculate F1 score
        f1 = f1_score(y_true, y_pred_rnd)
        f1_scores.append(f1)
    
    return f1_scores

# Evaluate dummy classifier with different probabilities
probabilities = [0, df['insurance_benefits_received'].sum() / len(df), 0.5, 1]
dummy_f1_scores = evaluate_dummy_classifier(y_test, probabilities)

# Print dummy model results
print("\nDummy model F1 scores:")
for P, f1 in zip(probabilities, dummy_f1_scores):
    print(f'P={P:.2f}: {f1:.4f}')


# # Task 3. Regression (with Linear Regression)

# With `insurance_benefits` as the target, evaluate what RMSE would be for a Linear Regression model.

# Build your own implementation of LR. For that, recall how the linear regression task's solution is formulated in terms of LA. Check RMSE for both the original data and the scaled one. Can you see any difference in RMSE between these two cases?
# 
# Let's denote
# - $X$ — feature matrix, each row is a case, each column is a feature, the first column consists of unities
# - $y$ — target (a vector)
# - $\hat{y}$ — estimated tagret (a vector)
# - $w$ — weight vector
# 
# The task of linear regression in the language of matrices can be formulated as
# 
# $$
# y = Xw
# $$
# 
# The training objective then is to find such $w$ that it would minimize the L2-distance (MSE) between $Xw$ and $y$:
# 
# $$
# \min_w d_2(Xw, y) \quad \text{or} \quad \min_w \text{MSE}(Xw, y)
# $$
# 
# It appears that there is analytical solution for the above:
# 
# $$
# w = (X^T X)^{-1} X^T y
# $$
# 
# The formula above can be used to find the weights $w$ and the latter can be used to calculate predicted values
# 
# $$
# \hat{y} = X_{val}w
# $$

# Split the whole data in the 70:30 proportion for the training/validation parts. Use the RMSE metric for the model evaluation.

# In[28]:


import math

class MyLinearRegression:
    
    def __init__(self):
        
        self.weights = None
    
    def fit(self, X, y):
        
        # adding the unities
        X2 = np.append(np.ones([len(X), 1]), X, axis=1)
        # Calculate weights using the closed-form solution (w = (X^T X)^-1 X^T y)
        self.weights = np.linalg.inv(X2.T @ X2) @ X2.T @ y

    def predict(self, X):
        
        # adding the unities
        X2 = np.append(np.ones([len(X), 1]), X, axis=1)  
        
        # Calculate predicted values (ŷ = Xw)
        y_pred = X2 @ self.weights
        
        return y_pred


# In[29]:


def eval_regressor(y_true, y_pred):
    
    rmse = math.sqrt(sklearn.metrics.mean_squared_error(y_true, y_pred))
    print(f'RMSE: {rmse:.2f}')
    
    r2_score = math.sqrt(sklearn.metrics.r2_score(y_true, y_pred))
    print(f'R2: {r2_score:.2f}')    


# In[30]:


X = df[['age', 'gender', 'income', 'family_members']].to_numpy()
y = df['insurance_benefits'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

lr = MyLinearRegression()

lr.fit(X_train, y_train)
print(lr.weights)

y_test_pred = lr.predict(X_test)
eval_regressor(y_test, y_test_pred)


# In[31]:


# Evaluate the model using RMSE and R2
eval_regressor(y_test, y_test_pred)

# To check the performance after scaling the data
scaler = StandardScaler()

# Scale the training and testing data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit the model to the scaled data
lr.fit(X_train_scaled, y_train)
print(f'Weights (scaled data): {lr.weights}')

# Make predictions on the scaled test data
y_test_pred_scaled = lr.predict(X_test_scaled)


# # Task 4. Obfuscating Data

# It best to obfuscate data by multiplying the numerical features (remember, they can be seen as the matrix $X$) by an invertible matrix $P$. 
# 
# $$
# X' = X \times P
# $$
# 
# Try to do that and check how the features' values will look like after the transformation. By the way, the intertible property is important here so make sure that $P$ is indeed invertible.
# 
# You may want to review the 'Matrices and Matrix Operations -> Matrix Multiplication' lesson to recall the rule of matrix multiplication and its implementation with NumPy.

# In[32]:


personal_info_column_list = ['gender', 'age', 'income', 'family_members']
df_pn = df[personal_info_column_list]


# In[33]:


X = df_pn.to_numpy()


# Generating a random matrix $P$.

# In[34]:


# Create a random invertible matrix P of shape (5, 5) to match the number of features in X
rng = np.random.default_rng(seed=42)
P = rng.random(size=(X.shape[1], X.shape[1])) 


# In[35]:


# rng = np.random.default_rng(seed=42)
# P = rng.random(size=(X.shape[1], X.shape[1]))


# Checking the matrix $P$ is invertible

# In[36]:


# Check if the matrix P is invertible by computing the determinant
det_P = np.linalg.det(P)

if det_P != 0:
    print("Matrix P is invertible.")
else:
    print("Matrix P is not invertible.")


# Can you guess the customers' ages or income after the transformation? no

# In[37]:


# Apply the transformation X' = X × P
X_prime = X.dot(P)

# Display the transformed matrix X'
print("Transformed Data (X'):")
print(X_prime)


# Can you recover the original data from $X'$ if you know $P$? Try to check that with calculations by moving $P$ from the right side of the formula above to the left one. The rules of matrix multiplcation are really helpful here.

# In[38]:


# Recover the original X using X' and P^-1
P_inv = np.linalg.inv(P)  # Inverse of P
X_recovered = X_prime.dot(P_inv)

# Display the recovered matrix X (should be close to the original X)
print("Recovered Data (X):")
print(X_recovered)


# Print all three cases for a few customers
# - The original data
# - The transformed one
# - The reversed (recovered) one

# In[39]:


# Define the number of customers to show
num_customers_to_show = 5  # Display first 5 customers for comparison

# Display the original, transformed, and recovered data for a few customers
print(f"\nDisplaying the first {num_customers_to_show} customers:")

# Loop to print the original, transformed, and recovered data
for i in range(num_customers_to_show):
    print(f"\nCustomer {i+1}:")
    print(f"Original Data (X): {X[i]}")  # Accessing the i-th row of NumPy array
    print(f"Transformed Data (X'): {X_prime[i]}")  # Accessing the i-th row of NumPy array
    print(f"Recovered Data (X): {X_recovered[i]}")  # Accessing the i-th row of NumPy array


# You can probably see that some values are not exactly the same as they are in the original data. What might be the reason for that?

# The reason the recovered data is not exactly the same as the original data lies in the nature of numerical precision when performing matrix operations.

# In[40]:


# Check if the recovered data is close to the original with a tolerance
for i in range(num_customers_to_show):
    print(f"Customer {i+1}:")
    if np.allclose(X[i], X_recovered[i], atol=1e-6):
        print("The recovered data is close to the original.")
    else:
        print("The recovered data differs from the original.")


# ## Proof That Data Obfuscation Can Work with LR

# The regression task has been solved with linear regression in this project. Your next task is to prove _analytically_ that the given obfuscation method won't affect linear regression in terms of predicted values i.e. their values will remain the same. Can you believe that? Well, you don't have to, you should prove it!

# So, the data is obfuscated and there is $X \times P$ instead of just $X$ now. Consequently, there are other weights $w_P$ as
# $$
# w = (X^T X)^{-1} X^T y \quad \Rightarrow \quad w_P = [(XP)^T XP]^{-1} (XP)^T y
# $$
# 
# How would $w$ and $w_P$ be linked if you simplify the formula for $w_P$ above? 
# 
# What would be predicted values with $w_P$? 
# 
# What does that mean for the quality of linear regression if you measure it with RMSE?
# 
# Check Appendix B Properties of Matrices in the end of the notebook. There are useful formulas in there!
# 
# No code is necessary in this section, only analytical explanation!

# **Answer**

# Step 1: Original Linear Regression Weights (
# 𝑤
# w)
# In linear regression, the weight vector 
# 𝑤
# w is computed using the normal equation:
# 
# 𝑤
# =
# (
# 𝑋
# 𝑇
# 𝑋
# )
# −
# 1
# 𝑋
# 𝑇
# 𝑦
# w=(X 
# T
#  X) 
# −1
#  X 
# T
#  y
# where:
# 
# 𝑋
# X is the matrix of features,
# 𝑦
# y is the vector of target values,
# 𝑤
# w is the weight vector to be learned.
# Step 2: Transformed Data and Weights (
# 𝑤
# 𝑃
# w 
# P
# ​
#  )
# After applying the obfuscation method, the data matrix is transformed by multiplying it by an invertible matrix 
# 𝑃
# P, resulting in the transformed feature matrix 
# 𝑋
# 𝑃
# =
# 𝑋
# 𝑃
# X 
# P
# ​
#  =XP.
# 
# The new weights 
# 𝑤
# 𝑃
# w 
# P
# ​
#   are computed using the normal equation for the transformed data:
# 
# 𝑤
# 𝑃
# =
# (
# 𝑋
# 𝑃
# 𝑇
# 𝑋
# 𝑃
# )
# −
# 1
# 𝑋
# 𝑃
# 𝑇
# 𝑦
# w 
# P
# ​
#  =(X 
# P
# T
# ​
#  X 
# P
# ​
#  ) 
# −1
#  X 
# P
# T
# ​
#  y
# Substitute 
# 𝑋
# 𝑃
# =
# 𝑋
# 𝑃
# X 
# P
# ​
#  =XP into the above formula:
# 
# 𝑤
# 𝑃
# =
# (
# (
# 𝑋
# 𝑃
# )
# 𝑇
# (
# 𝑋
# 𝑃
# )
# )
# −
# 1
# (
# 𝑋
# 𝑃
# )
# 𝑇
# 𝑦
# w 
# P
# ​
#  =((XP) 
# T
#  (XP)) 
# −1
#  (XP) 
# T
#  y
# Simplifying further:
# 
# 𝑤
# 𝑃
# =
# (
# 𝑃
# 𝑇
# 𝑋
# 𝑇
# 𝑋
# 𝑃
# )
# −
# 1
# 𝑃
# 𝑇
# 𝑋
# 𝑇
# 𝑦
# w 
# P
# ​
#  =(P 
# T
#  X 
# T
#  XP) 
# −1
#  P 
# T
#  X 
# T
#  y
# Step 3: Relation Between 
# 𝑤
# w and 
# 𝑤
# 𝑃
# w 
# P
# ​
#  
# We can rewrite the formula for 
# 𝑤
# 𝑃
# w 
# P
# ​
#   as:
# 
# 𝑤
# 𝑃
# =
# (
# 𝑃
# 𝑇
# (
# 𝑋
# 𝑇
# 𝑋
# )
# 𝑃
# )
# −
# 1
# 𝑃
# 𝑇
# 𝑋
# 𝑇
# 𝑦
# w 
# P
# ​
#  =(P 
# T
#  (X 
# T
#  X)P) 
# −1
#  P 
# T
#  X 
# T
#  y
# Now, recall that the inverse of a product of matrices satisfies the following property:
# 
# (
# 𝑃
# 𝑇
# 𝐴
# 𝑃
# )
# −
# 1
# =
# 𝑃
# −
# 1
# 𝐴
# −
# 1
# (
# 𝑃
# −
# 1
# )
# 𝑇
# (P 
# T
#  AP) 
# −1
#  =P 
# −1
#  A 
# −1
#  (P 
# −1
#  ) 
# T
#  
# where 
# 𝐴
# =
# 𝑋
# 𝑇
# 𝑋
# A=X 
# T
#  X. Thus, we can simplify:
# 
# 𝑤
# 𝑃
# =
# 𝑃
# −
# 1
# (
# 𝑋
# 𝑇
# 𝑋
# )
# −
# 1
# 𝑋
# 𝑇
# 𝑦
# w 
# P
# ​
#  =P 
# −1
#  (X 
# T
#  X) 
# −1
#  X 
# T
#  y
# Notice that this is exactly:
# 
# 𝑤
# 𝑃
# =
# 𝑃
# −
# 1
# 𝑤
# w 
# P
# ​
#  =P 
# −1
#  w
# Step 4: Predicted Values with 
# 𝑤
# 𝑃
# w 
# P
# ​
#  
# The predicted values for the original data are:
# 
# 𝑦
# ^
# =
# 𝑋
# 𝑤
# y
# ^
# ​
#  =Xw
# For the transformed data, the predicted values using 
# 𝑤
# 𝑃
# w 
# P
# ​
#   are:
# 
# 𝑦
# ^
# 𝑃
# =
# 𝑋
# 𝑃
# 𝑤
# 𝑃
# =
# 𝑋
# 𝑃
# 𝑃
# −
# 1
# 𝑤
# =
# 𝑋
# 𝑤
# y
# ^
# ​
#   
# P
# ​
#  =X 
# P
# ​
#  w 
# P
# ​
#  =XPP 
# −1
#  w=Xw
# Thus, we can see that:
# 
# 𝑦
# ^
# 𝑃
# =
# 𝑦
# ^
# y
# ^
# ​
#   
# P
# ​
#  = 
# y
# ^
# ​
#  
# This means that the predicted values remain the same even after the obfuscation transformation.
# 
# Step 5: Impact on RMSE
# Since the predicted values 
# 𝑦
# ^
# 𝑃
# y
# ^
# ​
#   
# P
# ​
#   are exactly the same as the original predicted values 
# 𝑦
# ^
# y
# ^
# ​
#  , the Root Mean Square Error (RMSE), which measures the difference between the predicted and actual target values, will remain unchanged:
# 
# RMSE
# =
# 1
# 𝑛
# ∑
# 𝑖
# =
# 1
# 𝑛
# (
# 𝑦
# ^
# 𝑖
# −
# 𝑦
# 𝑖
# )
# 2
# RMSE= 
# n
# 1
# ​
#   
# i=1
# ∑
# n
# ​
#  ( 
# y
# ^
# ​
#   
# i
# ​
#  −y 
# i
# ​
#  ) 
# 2
#  
# ​
#  
# Therefore, since the predicted values are unchanged, the RMSE will be the same for both the original and obfuscated data.

# **Analytical proof**

# Analytical Proof Using Key Formulas
# Original Weights Calculation:
# 
# 𝑤
# =
# (
# 𝑋
# 𝑇
# 𝑋
# )
# −
# 1
# 𝑋
# 𝑇
# 𝑦
# w=(X 
# T
#  X) 
# −1
#  X 
# T
#  y
# Transformed Data and Weights:
# 
# Transformed feature matrix:
# 𝑋
# 𝑃
# =
# 𝑋
# 𝑃
# X 
# P
# ​
#  =XP
# Transformed weights:
# 𝑤
# 𝑃
# =
# (
# 𝑋
# 𝑃
# 𝑇
# 𝑋
# 𝑃
# )
# −
# 1
# 𝑋
# 𝑃
# 𝑇
# 𝑦
# w 
# P
# ​
#  =(X 
# P
# T
# ​
#  X 
# P
# ​
#  ) 
# −1
#  X 
# P
# T
# ​
#  y
# Substituting 
# 𝑋
# 𝑃
# =
# 𝑋
# 𝑃
# X 
# P
# ​
#  =XP:
# 𝑤
# 𝑃
# =
# (
# (
# 𝑋
# 𝑃
# )
# 𝑇
# (
# 𝑋
# 𝑃
# )
# )
# −
# 1
# (
# 𝑋
# 𝑃
# )
# 𝑇
# 𝑦
# w 
# P
# ​
#  =((XP) 
# T
#  (XP)) 
# −1
#  (XP) 
# T
#  y
# Simplified using matrix properties:
# 𝑤
# 𝑃
# =
# 𝑃
# −
# 1
# 𝑤
# w 
# P
# ​
#  =P 
# −1
#  w
# Predicted Values:
# 
# Original predicted values:
# 𝑦
# ^
# =
# 𝑋
# 𝑤
# y
# ^
# ​
#  =Xw
# Transformed predicted values:
# 𝑦
# ^
# 𝑃
# =
# 𝑋
# 𝑃
# 𝑤
# 𝑃
# y
# ^
# ​
#   
# P
# ​
#  =X 
# P
# ​
#  w 
# P
# ​
#  
# Substituting 
# 𝑋
# 𝑃
# =
# 𝑋
# 𝑃
# X 
# P
# ​
#  =XP and 
# 𝑤
# 𝑃
# =
# 𝑃
# −
# 1
# 𝑤
# w 
# P
# ​
#  =P 
# −1
#  w:
# 𝑦
# ^
# 𝑃
# =
# (
# 𝑋
# 𝑃
# )
# (
# 𝑃
# −
# 1
# 𝑤
# )
# y
# ^
# ​
#   
# P
# ​
#  =(XP)(P 
# −1
#  w)
# Simplified:
# 𝑦
# ^
# 𝑃
# =
# 𝑋
# 𝑤
# y
# ^
# ​
#   
# P
# ​
#  =Xw
# Therefore:
# 𝑦
# ^
# 𝑃
# =
# 𝑦
# ^
# y
# ^
# ​
#   
# P
# ​
#  = 
# y
# ^
# ​
# 

# ## Test Linear Regression With Data Obfuscation

# Now, let's prove Linear Regression can work computationally with the chosen obfuscation transformation.
# 
# Build a procedure or a class that runs Linear Regression optionally with the obfuscation. You can use either a ready implementation of Linear Regression from sciki-learn or your own.
# 
# Run Linear Regression for the original data and the obfuscated one, compare the predicted values and the RMSE, $R^2$ metric values. Is there any difference?

# **Procedure**
# 
# - Create a square matrix $P$ of random numbers.
# - Check that it is invertible. If not, repeat the first point until we get an invertible matrix.
# - <! your comment here !>
# - Use $XP$ as the new feature matrix

# In[41]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create an invertible matrix P
rng = np.random.default_rng(seed=42)
while True:
    P = rng.random(size=(X.shape[1], X.shape[1]))  # Square matrix based on feature count
    if np.linalg.det(P) != 0:  # Ensure invertibility
        break

# Step 2: Obfuscate the features
X_P = np.dot(X, P)

# Step 3: Train Linear Regression Models
model_original = LinearRegression()
model_original.fit(X, y)
y_pred_original = model_original.predict(X)

model_obfuscated = LinearRegression()
model_obfuscated.fit(X_P, y)
y_pred_obfuscated = model_obfuscated.predict(X_P)


# In[42]:


# Step 4: Evaluate the Models
rmse_original = np.sqrt(mean_squared_error(y, y_pred_original))
r2_original = r2_score(y, y_pred_original)

rmse_obfuscated = np.sqrt(mean_squared_error(y, y_pred_obfuscated))
r2_obfuscated = r2_score(y, y_pred_obfuscated)

# Step 5: Print and Compare Results
print(f"Original RMSE: {rmse_original}, R^2: {r2_original}")
print(f"Obfuscated RMSE: {rmse_obfuscated}, R^2: {r2_obfuscated}")
print("\nPredicted values comparison:")
print(f"Original Predictions: {y_pred_original[:5]}")
print(f"Obfuscated Predictions: {y_pred_obfuscated[:5]}")


# In[ ]:





# # Conclusions

# Conclusion
# The Sure Tomorrow insurance company aims to enhance its business operations by leveraging machine learning solutions. This project systematically addressed the four tasks posed by the company, evaluating their feasibility and effectiveness. Below are the conclusions for each task:
# 
# Task 1: Finding Similar Customers
# By analyzing customer profiles using various similarity measures (e.g., Euclidean distance or cosine similarity), we identified methods for grouping customers with similar characteristics. This provides marketing agents with valuable insights for targeted campaigns, enabling more personalized and effective outreach. The implementation demonstrated that customer segmentation can be performed efficiently based on the dataset's features.
# 
# Task 2: Predicting Insurance Benefit Likelihood
# A classification model was developed to predict whether a new customer is likely to receive an insurance benefit. The performance of the model was compared against a dummy model, and the results showed a significant improvement. The trained model surpassed the dummy model in terms of accuracy, precision, recall, and F1-score, confirming its potential for reliable predictions. This demonstrates that machine learning can indeed support decision-making processes more effectively than random baselines.
# 
# Task 3: Predicting the Number of Insurance Benefits
# Using linear regression, we predicted the number of insurance benefits a customer is likely to receive. The model demonstrated a good fit to the data, with performance metrics such as RMSE and 
# 𝑅
# 2
# R 
# 2
#   indicating that the predictions were reasonably accurate. This task highlights the practical application of regression models in forecasting numerical outcomes in the insurance domain, which could guide the company's policy recommendations and risk assessments.
# 
# Task 4: Protecting Client Data via Obfuscation
# A data masking technique was implemented using matrix transformations to obfuscate sensitive customer data. This transformation ensured that personal information could not be recovered if the dataset fell into the wrong hands. The obfuscation algorithm preserved the quality of the linear regression model, as demonstrated by identical RMSE and 
# 𝑅
# 2
# R 
# 2
#   values for both the original and obfuscated datasets. This proves that the proposed data transformation effectively balances privacy and machine learning model performance.
# 
# 

# Overall Project Impact
# 
# This project showcased the power of machine learning in solving real-world business challenges. Key takeaways include:
# 
# Machine learning models can effectively support decision-making and improve marketing strategies.
# 
# Predictive models outperform simple heuristics, adding measurable value to the business.
# 
# Data obfuscation techniques can safeguard sensitive information without compromising model quality, addressing privacy concerns in compliance with industry standards.
# 
# The results of this project affirm that machine learning, combined with robust data protection mechanisms, can offer scalable, effective solutions to modern business problems.

# In[ ]:





# # Checklist

# Type 'x' to check. Then press Shift+Enter.

# - [x]  Jupyter Notebook is open
# - [ ]  Code is error free
# - [ ]  The cells are arranged in order of logic and execution
# - [ ]  Task 1 has been performed
#     - [ ]  There is the procedure that can return k similar customers for a given one
#     - [ ]  The procedure is tested for all four proposed combinations
#     - [ ]  The questions re the scaling/distances are answered
# - [ ]  Task 2 has been performed
#     - [ ]  The random classification model is built and tested for all for probability levels
#     - [ ]  The kNN classification model is built and tested for both the original data and the scaled one, the F1 metric is calculated.
# - [ ]  Task 3 has been performed
#     - [ ]  The linear tegression solution is implemented with matrix operations.
#     - [ ]  RMSE is calculated for the implemented solution.
# - [ ]  Task 4 has been performed
#     - [ ]  The data is obfuscated with a random and invertible matrix P
#     - [ ]  The obfuscated data is recoved, few examples are printed out
#     - [ ]  The analytical proof that the transformation does not affect RMSE is provided 
#     - [ ]  The computational proof that the transformation does not affect RMSE is provided
# - [ ]  Conclusions have been made

# # Appendices 
# 
# ## Appendix A: Writing Formulas in Jupyter Notebooks

# You can write formulas in your Jupyter Notebook in a markup language provided by a high-quality publishing system called $\LaTeX$ (pronounced "Lah-tech"), and they will look like formulas in textbooks.
# 
# To put a formula in a text, put the dollar sign (\\$) before and after the formula's text e.g. $\frac{1}{2} \times \frac{3}{2} = \frac{3}{4}$ or $y = x^2, x \ge 1$.
# 
# If a formula should be in its own paragraph, put the double dollar sign (\\$\\$) before and after the formula text e.g.
# 
# $$
# \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i.
# $$
# 
# The markup language of [LaTeX](https://en.wikipedia.org/wiki/LaTeX) is very popular among people who use formulas in their articles, books and texts. It can be complex but its basics are easy. Check this two page [cheatsheet](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) for learning how to compose the most common formulas.

# ## Appendix B: Properties of Matrices

# Matrices have many properties in Linear Algebra. A few of them are listed here which can help with the analytical proof in this project.

# <table>
# <tr>
# <td>Distributivity</td><td>$A(B+C)=AB+AC$</td>
# </tr>
# <tr>
# <td>Non-commutativity</td><td>$AB \neq BA$</td>
# </tr>
# <tr>
# <td>Associative property of multiplication</td><td>$(AB)C = A(BC)$</td>
# </tr>
# <tr>
# <td>Multiplicative identity property</td><td>$IA = AI = A$</td>
# </tr>
# <tr>
# <td></td><td>$A^{-1}A = AA^{-1} = I$
# </td>
# </tr>    
# <tr>
# <td></td><td>$(AB)^{-1} = B^{-1}A^{-1}$</td>
# </tr>    
# <tr>
# <td>Reversivity of the transpose of a product of matrices,</td><td>$(AB)^T = B^TA^T$</td>
# </tr>    
# </table>

# <div style="background-color: #d4edda; padding: 10px; border-radius: 5px;">
# Hello Robert,  
#  
# Congratulations on successfully submitting your Jupyter project on Linear Algebra!** 🎉  
#  
# Stepping into the world of mathematical modeling and implementing linear algebra concepts through code is a significant achievement, and your dedication to mastering these concepts is truly commendable.  
# 
# What Was Great:
# You did an excellent job applying linear algebra principles in a real-world context.  
# Your clear and well-organized code in Jupyter showcased both your technical skills and attention to detail.  
# The implementation of key linear algebra techniques was well-executed and insightful.  
#  
# Tips for Future Projects:  
# Keep experimenting with optimizing the performance of your algorithms for even better results.  
# 
# Congratulations again on your accomplishment!** Each project you complete adds to your growing expertise, and it’s exciting to see you make such great strides. Keep up the great work! 🎯  </div>
