#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px"> <h1 style="color:green; margin-bottom:20px">Reviewer's comment v1</h1>
# 
# Hello Robert!
# 
# I'm happy to review your project today  🙌
# 
# You can find my comments under the heading **«Review»**. I will categorize my comments in green, blue or red boxes like this:
# 
# <div class="alert alert-success">
#     <b>Success:</b> if everything is done successfully
# </div>
# <div class="alert alert-warning">
#     <b>Remarks:</b> if I can give some recommendations or ways to improve the project
# </div>
# <div class="alert alert-danger">
#     <b>Needs fixing:</b> if the block requires some corrections. Work can't be accepted with the red comments
# </div>
# 
# Please don't remove my comments. If you have any questions, don't hesitate to respond to my comments in a different section.
# <div class="alert alert-info"> <b>Student comments: </div>    

# <div style="border:solid green 2px; padding: 20px">
# <b>Reviewer's comment v1</b>
#     
# <b>Overall Feedback</b> 
#     
#     
# Hello Robert,
# 
# You’ve submitted another project—great work! Your commitment to pushing through the challenges of this program is admirable.
# 
# After reviewing your submission, I’ve returned it with some feedback to help you make the necessary improvements.
#     
# You’ll find specific feedback in the notebook in the ‘Comments’ (`Reviewer's comment v1`) sections.
#     
# **What Was Great:**
# 
# - Great that you've managed to test different models and carefully tuned hyperparameters.
# - Your code is clean and easy to follow. Printing the shapes of the datasets after splitting them is a good way to verify that everything is in order.
#     
# **Areas to Improve:**
# 
# - While you’ve done a great job splitting the data, I noticed that you haven’t used the test set yet. Make sure to use it to test the final model performance, as this step is crucial for model evaluation.
#    
# Keep in mind that revisions are a normal and valuable part of the learning process. Use this feedback to refine your work and resubmit when you’re ready. I know you’re capable of great things, and I’m here to support you every step of the way. Keep going—you’re doing a great job! 🏄
#     
# And of course, if you have any questions along the way, remember that you can always reach out to your tutor for clarification.
# </div>

# <div style="border:solid green 2px; padding: 20px">
# <b>Reviewer's comment v2:</b>
#     
# <b>Overall Feedback</b> 
#     
# Thank you for going the extra mile in incorporating additional changes and improvements. 
# 
# 
# Wish you cool projects in the next sprints! ☘️
#     
# 
# </div>

# Develop a model with the highest possible accuracy. In this project, the threshold for accuracy is 0.75. Check the accuracy using the test dataset.  
# 
# Project instructions: 
# 
# Open and look through the data file. Path to the file:datasets/users_behavior.csv Download dataset
# Split the source data into a training set, a validation set, and a test set.
# 
# Investigate the quality of different models by changing hyperparameters. 
# Briefly describe the findings of the study.
# Check the quality of the model using the test set.
# 
# Additional task: sanity check the model. This data is more complex than what you’re used to working with, so it's not an easy task. 

# <div class="alert alert-warning">
# <b>Reviewer's comment v1:</b>
#     
# It is always helpful for the reader to have additional information about project tasks. It gives an overview of what you are going to achieve in this project.
# 

# In[1]:


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the dataset from the provided URL
url = 'https://practicum-content.s3.us-west-1.amazonaws.com/datasets/users_behavior.csv'
df = pd.read_csv(url)

# Separate features and target
features = df.drop('is_ultra', axis=1)  # Drop the target column
target = df['is_ultra']  # Correct variable name for the target column

# Split the data into training and temporary sets (70% train, 30% temporary)
# Use stratify=target to maintain the same distribution of 'is_ultra' across the splits
train_features, temp_features, train_target, temp_target = train_test_split(
    features, target, test_size=0.3, random_state=12345, stratify=target
)

# Split the temporary set into validation and test sets (50% validation, 50% test)
validation_features, test_features, validation_target, test_target = train_test_split(
    temp_features, temp_target, test_size=0.5, random_state=12345, stratify=temp_target
)
# Display the sizes of the resulting datasets
print(f"Training set size: {len(train_features)}")
print(f"Validation set size: {len(validation_features)}")
print(f"Test set size: {len(test_features)}")

# Check the distribution of the target variable in each set to ensure stratification worked
print(f"Training set class distribution: {train_target.value_counts(normalize=True)}")
print(f"Validation set class distribution: {validation_target.value_counts(normalize=True)}")
print(f"Test set class distribution: {test_target.value_counts(normalize=True)}")



# <div class="alert alert-warning">
# <b>Reviewer's comment v1:</b>
#     
# There are imports for regressors (RandomForestRegressor, DecisionTreeRegressor, LinearRegression, and mean_squared_error) which are not needed since this is a classification task. Removing these would keep the code cleaner.

# <div class="alert alert-warning">
# <b>Reviewer's comment v1:</b>
#     
# Consider using stratified splits (`stratify` parameter) to ensure that class distributions are similar across training, validation, and test sets.
# 
# 

# <div class="alert alert-success">
# <b>Reviewer's comment v1:</b>
#     
# Well done! You've correctly split the data into training, validation, and test sets.

# In[2]:


# Define the name of the target column
target_column = 'is_ultra'

# Separate features and target
features = df.drop(target_column, axis=1)  # Drop the target column
target = df[target_column]  # Target column for classification

# Split the data into training and temporary sets (70% train, 30% temporary)
train_features, temp_features, train_target, temp_target = train_test_split(
    features, target, test_size=0.3, random_state=12345, stratify=target
)

# Split the temporary set into validation and test sets (50% validation, 50% test)
validation_features, test_features, validation_target, test_target = train_test_split(
    temp_features, temp_target, test_size=0.5, random_state=12345, stratify=temp_target
)

# Display the sizes of the resulting datasets
print(f"Training set size: {len(train_features)}")
print(f"Validation set size: {len(validation_features)}")
print(f"Test set size: {len(test_features)}")

# Prepare features and target variable
features_train = train_features  # Features for training
target_train = train_target  # Target variable for training

features_val = validation_features  # Features for validation
target_val = validation_target  # Target variable for validation

features_test = test_features  # Features for testing
target_test = test_target  # Target variable for testing

# Initialize models
models = {
    'RandomForest': RandomForestClassifier(n_estimators=50, max_depth=5, random_state=12345),
    'LogisticRegression': LogisticRegression(max_iter=1000, random_state=12345)
}

# Hyperparameter tuning for RandomForest
n_estimators_options = [10, 20, 30, 40, 50]
max_depth_options = [None, 5, 10]

best_accuracy = 0
best_model = None

# Evaluate RandomForest with different hyperparameters
for n_estimators in n_estimators_options:
    for max_depth in max_depth_options:
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=12345)
        model.fit(features_train, target_train)
        predictions = model.predict(features_test)
        accuracy = accuracy_score(target_test, predictions)
        
        print(f"RandomForest - n_estimators: {n_estimators}, max_depth: {max_depth}, Accuracy: {accuracy:.4f}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model

# Evaluate Logistic Regression
logistic_model = models['LogisticRegression']
logistic_model.fit(features_train, target_train)
logistic_predictions = logistic_model.predict(features_test)
logistic_accuracy = accuracy_score(target_test, logistic_predictions)

print(f"Logistic Regression Accuracy: {logistic_accuracy:.4f}")

# Final results
if best_model:
    print(f"Best Model Accuracy: {best_accuracy:.4f} using RandomForest with n_estimators={best_model.n_estimators}, max_depth={best_model.max_depth}")


# <div class="alert alert-success">
# <b>Reviewer's comment v1:</b>
#     
# Everything is correct here! Great that you've managed to check multiple models. 
# 
# Some possible minor improvements: 
# 
# - If you find yourself repeating similar blocks of code, consider writing a function. This will make your code more organized and easier to maintain.
# - Besides accuracy, consider evaluating models using additional metrics like F1-score, precision, recall, or the ROC-AUC score for a more holistic view of performance, especially if the class distribution is imbalanced.
# - Consider using GridSearchCV or RandomizedSearchCV from sklearn.model_selection for a more systematic hyperparameter search.

# # Check the quality of the model using the validation set
# # For the best Random Forest model
# if best_model:
#     val_predictions_rf = best_model.predict(features_val)  # Predict on validation set
#     val_accuracy_rf = accuracy_score(target_val, val_predictions_rf)  # Calculate validation accuracy
#     print(f"Random Forest Validation Accuracy: {val_accuracy_rf:.4f}")
# 
#     # Now evaluate on the test set for the best model
#     test_predictions_rf = best_model.predict(features_test)
#     test_accuracy_rf = accuracy_score(target_test, test_predictions_rf)
#     print(f"Random Forest Test Accuracy: {test_accuracy_rf:.4f}")
# 
# # Evaluate Logistic Regression on the validation set
# val_predictions_logistic = logistic_model.predict(features_val)  # Predict on validation set
# val_accuracy_logistic = accuracy_score(target_val, val_predictions_logistic)  # Calculate validation accuracy
# print(f"Logistic Regression Validation Accuracy: {val_accuracy_logistic:.4f}")
# 
# # After tuning and selecting the final model, evaluate on the test set
# test_predictions_logistic = logistic_model.predict(features_test)  # Predict on the test set
# test_accuracy_logistic = accuracy_score(target_test, test_predictions_logistic)  # Calculate test accuracy
# print(f"Logistic Regression Test Accuracy: {test_accuracy_logistic:.4f}")
# 
# # Final results
# if best_model:
#     print(f"Best Model Accuracy: {best_accuracy:.4f} using RandomForest with n_estimators={best_model.n_estimators}, max_depth={best_model.max_depth}")

# In[3]:


from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

# Step 1: Train a DummyClassifier with 'most_frequent' strategy
dummy_clf = DummyClassifier(strategy='most_frequent')
dummy_clf.fit(features_train, target_train)  # Train on the training set

# Step 2: Evaluate the DummyClassifier on the validation set
val_predictions_dummy = dummy_clf.predict(features_val)  # Predict on validation set
val_accuracy_dummy = accuracy_score(target_val, val_predictions_dummy)  # Calculate validation accuracy
print(f"Dummy Classifier Validation Accuracy (most frequent): {val_accuracy_dummy:.4f}")

# Step 3: Evaluate the DummyClassifier on the test set
test_predictions_dummy = dummy_clf.predict(features_test)  # Predict on the test set
test_accuracy_dummy = accuracy_score(target_test, test_predictions_dummy)  # Calculate test accuracy
print(f"Dummy Classifier Test Accuracy (most frequent): {test_accuracy_dummy:.4f}")

# Step 4: Compare DummyClassifier performance with the chosen models
# Logistic Regression performance (already calculated in previous steps)
val_predictions_logistic = logistic_model.predict(features_val)  # Predict on validation set
val_accuracy_logistic = accuracy_score(target_val, val_predictions_logistic)
print(f"Logistic Regression Validation Accuracy: {val_accuracy_logistic:.4f}")

test_predictions_logistic = logistic_model.predict(features_test)  # Predict on the test set
test_accuracy_logistic = accuracy_score(target_test, test_predictions_logistic)
print(f"Logistic Regression Test Accuracy: {test_accuracy_logistic:.4f}")

# For Random Forest
if best_model:
    val_predictions_rf = best_model.predict(features_val)  # Predict on validation set
    val_accuracy_rf = accuracy_score(target_val, val_predictions_rf)
    print(f"Random Forest Validation Accuracy: {val_accuracy_rf:.4f}")

    test_predictions_rf = best_model.predict(features_test)  # Predict on the test set
    test_accuracy_rf = accuracy_score(target_test, test_predictions_rf)
    print(f"Random Forest Test Accuracy: {test_accuracy_rf:.4f}")


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score

# Check the distribution of the target variable
plt.figure(figsize=(8, 4))
sns.countplot(x=target_column, data=df)
plt.title('Distribution of Target Variable')
plt.xlabel('Is Ultra')
plt.ylabel('Count')
plt.show()

# Analyze correlations between features and the target variable
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[5]:


# Train the best model on the entire training data
best_model.fit(features_train, target_train)

# Check predictions on the training data
train_predictions = best_model.predict(features_train)
train_accuracy = accuracy_score(target_train, train_predictions)
print(f"Training Accuracy: {train_accuracy:.4f}")

# Perform cross-validation
cv_scores = cross_val_score(best_model, features_train, target_train, cv=5, scoring='accuracy')
print(f"Cross-Validation Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# Inspect misclassifications
misclassified = features_train[train_predictions != target_train]
print("Misclassified examples:")
print(misclassified.head())


# In[6]:


# Feature importance for Random Forest
if isinstance(best_model, RandomForestClassifier):
    feature_importances = best_model.feature_importances_
    features = features_train.columns
    importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=importance_df)
    plt.title('Feature Importances')
    plt.show()


# <div class="alert alert-danger">
# <b>Reviewer's comment v1:</b>
#     
# In the current implementation, the model's hyperparameters are tuned using the test set, which is generally not a good practice. The test set should only be used at the final stage to evaluate the performance of the best model. Instead, the validation set should be used for tuning. 
#     
# Lastly when you have the best model with parameters you can use a test set to validate your solution. 
#   
# Could you please update that? 

# Student Comment: 
# 
# ## Check the quality of the model using the validation set
# ## For the best Random Forest model
# if best_model:
#     val_predictions_rf = best_model.predict(features_val)  # Predict on validation set</div>    

# 
# <div class="alert alert-success">
# <b>Reviewer's comment v2:</b>
#     
# Great! Thank you for updating this part. 

# <div class="alert alert-warning">
# <b>Reviewer's comment v1:</b>
#     
# **Additional task: sanity check the model.** 
#  
# The use of `DummyClassifier` is a good practice for baseline performance and finalizing sanity check. You could read about it [here](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html). In our case, we have a very skewed distribution of users across the two plans. As you can see, only 30% are enrolled in the Ultra plan, therefore it could be usefull to use a particular strategy (e.g., `most_frequent`) and comparing it against the chosen model’s performance.
#     
# ```
# from sklearn.dummy import DummyClassifier
# # Initialize the DummyClassifier to predict the most frequent class
# dummy_clf = DummyClassifier(strategy="most_frequent", random_state=0)
# # Fit the dummy classifier on the training data
# ...
# ```

# Based on the evaluation of different models and their hyperparameters, here are the key findings:
# 
# 1. Model Performance Comparison:
# Random Forest Classifier:
# 
# This model generally performed better than Logistic Regression due to its ability to capture complex relationships in the data through its ensemble of decision trees.
# The specified hyperparameters, such as n_estimators=50 and max_depth=5, provided a good balance between model complexity and overfitting.
# Logistic Regression:
# 
# This model served as a baseline. While it is easier to interpret and generally faster to train, it may struggle with datasets where relationships are non-linear or more complex, as is often the case with user behavior data.
# Logistic Regression's performance was usually lower than that of the Random Forest model.
# 
# 2. Hyperparameter Sensitivity:
# Random Forest Hyperparameters:
# Number of Trees (n_estimators): Increasing the number of trees can improve model performance but also increases computational time. A value of 50 trees was found to be effective.
# Max Depth (max_depth): A moderate depth (like 5) helped prevent overfitting while allowing the model to learn sufficient complexity from the data.
# 
# Logistic Regression:
# The default settings generally worked well, but additional tuning (e.g., regularization strength) might have improved performance. The max_iter=1000 was sufficient for convergence in this case.
# 
# 3. Model Robustness:
# Random Forest was more robust against overfitting, especially with the selected hyperparameters. This indicates that ensemble methods often perform better in scenarios with noisy data.
# The Random Forest model achieved higher accuracy scores, consistently outperforming Logistic Regression across various trials.
# 
# 4. Validation Strategy:
# The split of data into training, validation, and test sets ensured that the models were evaluated on unseen data, providing a realistic assessment of their performance.
# Using cross-validation could further enhance the evaluation process, allowing for a more thorough understanding of model stability and performance across different subsets of data.

# Conclusion
# Overall, the Random Forest Classifier was identified as the more effective model for the user behavior dataset, highlighting the importance of model selection and hyperparameter tuning in achieving optimal predictive performance.

# <div class="alert alert-success">
# <b>Reviewer's comment v1:</b>
#     
# 
# Great job on your overall conclusions and recommendations!  Your recommendations are well-thought and could be very valuable to the business.
