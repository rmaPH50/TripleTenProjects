#!/usr/bin/env python
# coding: utf-8

# **Review**
# 
# Hello Robert!
# 
# I'm happy to review your project today.
#   
# You can find my comments in colored markdown cells:
#   
# <div class="alert alert-success">
#   If everything is done successfully.
# </div>
#   
# <div class="alert alert-warning">
#   If I have some (optional) suggestions, or questions to think about, or general comments.
# </div>
#   
# <div class="alert alert-danger">
#   If a section requires some corrections. Work can't be accepted with red comments.
# </div>
#   
# Please don't remove my comments, as it will make further review iterations much harder for me.
#   
# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
#   Thank you so much for your feedbacks. I've split the cells into multiple so it's easier. Hopefully i got it right this time. Thank you!
# </div>
#   
# First of all, thank you for turning in the project! You did a great job overall, but there are some small problems that need to be fixed before the project will be accepted. Let me know if you have any questions!
# 

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# Introduction is missed
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

#   
# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# 
#     See introduction below. 
#     
# </div>
#   
# First of all, thank you for turning in the project! You did a great job overall, but there are some small problems that need to be fixed before the project will be accepted. Let me know if you have any questions!
# 

# Introduction
# 
# This project focuses on analyzing and modeling data from the gold recovery industry, with the ultimate goal of predicting recovery efficiency at various stages of the process. The data for this project is provided in three separate files:
# 
# ### gold_recovery_train.csv: The training dataset.
# ### gold_recovery_test.csv: The test dataset without target values.
# ### gold_recovery_full.csv: The complete source dataset containing both the training and test data along with all features.
# 
# The datasets are indexed by the date and time of data acquisition, reflecting the temporal nature of the parameters. Parameters measured or calculated at similar times often display correlation. However, due to operational constraints, some features measured or calculated later are missing from the test dataset, while the source dataset contains all features.
# 
# Objectives
# 
# Before building the predictive model, the project involves several critical tasks to ensure the reliability of the data and the resulting predictions:
# 
# Data Verification: Validate the correctness of the data using provided guidelines.
# 
# Data Preprocessing: Handle missing values, anomalies, and feature alignment between training and test datasets.
# 
# Exploratory Data Analysis (EDA): Examine key trends in metal concentration, particle size, and recovery efficiency.
# 
# Model Development: Train a machine learning model to predict recovery efficiency at the "rougher" and "final" stages.
# 
# Model Evaluation: Use metrics such as Symmetric Mean Absolute Percentage Error (sMAPE) to assess the model’s performance.
# 
# This structured approach ensures that the model is built on accurate, clean data and aligns with industry-specific requirements, allowing it to provide valuable insights for optimizing the gold recovery process.

# In[1]:


import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error

# Load datasets
train_data = pd.read_csv('/datasets/gold_recovery_train.csv', index_col='date', parse_dates=True)
test_data = pd.read_csv('/datasets/gold_recovery_test.csv', index_col='date', parse_dates=True)
full_data = pd.read_csv('/datasets/gold_recovery_full.csv', index_col='date', parse_dates=True)

# Quick inspection of the datasets
print("Train Data:")
print(train_data.info())
print(train_data.head())

print("\nTest Data:")
print(test_data.info())
print(test_data.head())

print("\nFull Data:")
print(full_data.info())
print(full_data.head())

# Display the first few rows of the training data to inspect columns and data types
print(train_data.head())


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# If you fill NaNs here, you won't receive a correct result for MAE below. You need to fill all the NaNs after the task with MAE calculation.
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

# In[2]:


# Remove excessively large values and clean up the data
max_value = 1e10
train_data_cleaned = train_data.copy()

# Apply map to check and replace values above threshold
train_data_cleaned = train_data_cleaned.applymap(
    lambda x: x if abs(x) < max_value else np.nan
)


# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# 
#     Deleted Code for fill NaN. 
# </div>
#   
# First of all, thank you for turning in the project! You did a great job overall, but there are some small problems that need to be fixed before the project will be accepted. Let me know if you have any questions!
# 

# In[3]:


# Make a copy of the original DataFrame
train_data_cleaned = train_data.copy()

# Define the columns to check for excessively large values
columns_to_check = train_data_cleaned.columns  # or specify a subset of columns

# Set the threshold for large values
max_value = 1e10  

# Check for excessively large values and replace with np.nan
train_data_cleaned[columns_to_check] = train_data_cleaned[columns_to_check].applymap(
    lambda x: x if abs(x) < max_value else np.nan  # Replace excessively large values with np.nan
)

# Check for excessively large values in the dataset
train_data_cleaned = train_data_cleaned[
    (train_data_cleaned[columns_to_check].abs() < max_value).all(axis=1)
]

# Check if any values exceed the threshold
if (train_data_cleaned[columns_to_check].abs() > max_value).any().any():
    print("There are still values larger than the threshold.")
else:
    print("All values are within the acceptable range.")


# In[4]:


# Assuming train_data_cleaned is your cleaned DataFrame
actual_recovery = train_data_cleaned['rougher.output.recovery']

# Calculate the recovery based on the formula
calculated_recovery = np.where(
    train_data_cleaned['rougher.input.feed_au'] != 0,
    (train_data_cleaned['rougher.output.concentrate_au'] * (train_data_cleaned['rougher.input.feed_au'] - train_data_cleaned['rougher.output.tail_au'])) / 
    (train_data_cleaned['rougher.input.feed_au'] * (train_data_cleaned['rougher.output.concentrate_au'] - train_data_cleaned['rougher.output.tail_au'])),
    np.nan  # Replace division by zero with NaN
)

# Check for NaN values in actual and calculated recovery
print("Number of NaN values in actual recovery:", actual_recovery.isna().sum())
print("Number of NaN values in calculated recovery:", np.isnan(calculated_recovery).sum())


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# It's better to use NaNs in such cases because zeros can affect on MAE but NaNs can't
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# 
#     Replace division by zero with NaN 
# </div>

# In[5]:


# Recovery calculation (fixing the formula)
F = train_data_cleaned['rougher.input.feed_au']
C = train_data_cleaned['rougher.output.concentrate_au']
T = train_data_cleaned['rougher.output.tail_au']

# Ensure no division by zero or negative values
epsilon = 1e-10
calculated_recovery = (C * (F - T)) / (F * (C - T) + epsilon) * 100  # Adding epsilon to avoid division by zero

# Compare with actual recovery values
actual_recovery = train_data_cleaned['rougher.output.recovery']
mae = mean_absolute_error(actual_recovery, calculated_recovery)
print(f"MAE for recovery calculation: {mae}")


# Conclusion:
# The Mean Absolute Error (MAE) between the actual recovery values (rougher.output.recovery) and the calculated recovery values is 9.3e-15, which is effectively zero. This indicates that the recovery formula has been correctly applied.
# 
# Key Takeaways:
# Accuracy of the Formula:
# 
# The calculated recovery values match almost perfectly with the actual recovery values in the dataset. This confirms the correctness of the formula:
# Recovery
# =
# (
# C
# ×
# (
# F
# −
# T
# )
# F
# ×
# (
# C
# −
# T
# )
# )
# ×
# 100
# Recovery=( 
# F×(C−T)
# C×(F−T)
# ​
#  )×100
# Importance of Preprocessing:
# 
# Dropping rows with missing values in the relevant columns ensures accurate calculations and avoids issues like NaNs or infinities.
# Verification of Dataset Integrity:
# 
# The near-zero MAE suggests that the dataset is consistent with the theoretical recovery formula.

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# The result is incorrect. In the correct result MAE should be alsmost zero. 
#     
# 1. You used wrong formula for recovery. Check the formula in the lesson
# 2. You should do this task before to fill NaNs. Filled NaNs won't allow you to get the correct result
# 3. You don't need to clip the data or replace NaNs to complete this task
# 4. Don't forget to write a conclusion
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# The result is correct now. Good job!
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
#     Select the required columns for recovery calculation
#     Drop rows with missing values in these columns
#     Apply the corrected recovery formula
#     
#         calculated_recovery = (C * (F - T) / (F * (C - T))) * 100
#     
#     Compare with the actual recovery values
#     Calculate the MAE
#     
# MAE for recovery calculation: 9.303415616264301e-15
# 
# </div>

# In[6]:


# Identify columns missing from the test set
missing_columns = [col for col in train_data.columns if col not in test_data.columns]
print("Missing columns in the test set:", missing_columns)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# Correct
#   
# </div>

# In[7]:


# Fill NaNs in train and test data
train_data = train_data.fillna(method='ffill')
test_data = test_data.fillna(method='ffill')

# Ensure numeric types
train_data = train_data.apply(pd.to_numeric, errors='coerce')
test_data = test_data.apply(pd.to_numeric, errors='coerce')

# Check the first few rows
train_data.head()
test_data.head()


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# Correct. But why did you drop NaNs in the train data? It's better to fill NaNs in train in the same way you did it in the test data.
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Correct
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# 
#    Fill NaNs in both train and test data using forward fill
# </div>

# In[8]:


import matplotlib.pyplot as plt

# Define colors and labels for the stages
colors = ['blue', 'green', 'red', 'purple']
labels = ['Rougher Input Feed', 'Rougher Output', 'Primary Cleaner Output', 'Final Output']

# Extract concentration data for each metal at the four stages
stages = [
    'rougher.input.feed',
    'rougher.output.concentrate',
    'primary_cleaner.output.concentrate',
    'final.output.concentrate'
]

# Create separate DataFrames for each metal's concentration at different stages
concentration_au = train_data[[f'{stage}_au' for stage in stages]]
concentration_ag = train_data[[f'{stage}_ag' for stage in stages]]
concentration_pb = train_data[[f'{stage}_pb' for stage in stages]]

# Filter out near-zero concentrations for all metals at all stages
threshold = 0.01

# Apply the threshold to filter data
concentration_au_filtered = concentration_au[concentration_au > threshold].dropna()
concentration_ag_filtered = concentration_ag[concentration_ag > threshold].dropna()
concentration_pb_filtered = concentration_pb[concentration_pb > threshold].dropna()


# In[9]:


# Feature Engineering: Calculate total concentrations for different stages
train_data['total_feed_concentration'] = (
    train_data['rougher.input.feed_au'] + train_data['rougher.input.feed_ag'] + train_data['rougher.input.feed_pb']
)
train_data['total_rougher_concentrate'] = (
    train_data['rougher.output.concentrate_au'] + train_data['rougher.output.concentrate_ag'] + train_data['rougher.output.concentrate_pb']
)
train_data['total_final_concentrate'] = (
    train_data['final.output.concentrate_au'] + train_data['final.output.concentrate_ag'] + train_data['final.output.concentrate_pb']
)


# In[10]:


# Plot histograms with filtered data
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot for Au
axs[0].hist(
    [concentration_au_filtered[f'{stage}_au'].dropna() for stage in stages],
    bins=50, color=colors, label=labels, alpha=0.7
)
axs[0].set_title('Concentration of Au Across Stages (Filtered)')
axs[0].set_xlabel('Concentration of Au')
axs[0].set_ylabel('Frequency')
axs[0].legend()

# Plot for Ag
axs[1].hist(
    [concentration_ag_filtered[f'{stage}_ag'].dropna() for stage in stages],
    bins=50, color=colors, label=labels, alpha=0.7
)
axs[1].set_title('Concentration of Ag Across Stages (Filtered)')
axs[1].set_xlabel('Concentration of Ag')
axs[1].set_ylabel('Frequency')
axs[1].legend()

# Plot for Pb
axs[2].hist(
    [concentration_pb_filtered[f'{stage}_pb'].dropna() for stage in stages],
    bins=50, color=colors, label=labels, alpha=0.7
)
axs[2].set_title('Concentration of Pb Across Stages (Filtered)')
axs[2].set_xlabel('Concentration of Pb')
axs[2].set_ylabel('Frequency')
axs[2].legend()

plt.tight_layout()
plt.show()


# Conclusion
# 
# The analysis of metal concentration at different stages of the refining process reveals the following insights:
# 
# Gold (Au) Concentration:
# 
# The concentration of gold increases consistently across the stages, with the highest values observed at the final output stage.
# Filtering out near-zero values has highlighted a distinct distribution at each stage, confirming the effectiveness of the refining process in concentrating gold.
# Silver (Ag) Concentration:
# 
# Silver shows a gradual increase in concentration across stages, although the increments are less pronounced than gold.
# The filtered data emphasizes the refinement efficiency while revealing some overlap between stages.
# Lead (Pb) Concentration:
# 
# Lead concentrations demonstrate a steady upward trend through the process stages.
# Despite this increase, the distributions are narrower compared to gold and silver, suggesting more controlled refinement behavior.
# Impact of Filtering:
# 
# Excluding near-zero concentrations improved the clarity of the histograms, ensuring that only meaningful data contributes to the analysis.
# 
# This approach minimizes the influence of outliers and potential data entry errors.
# Overall, the visualizations provide a comprehensive view of how metal concentrations evolve during processing. These findings can guide further optimization of the refining process to maximize metal recovery while minimizing waste.
# 

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# 1. I don't understand where did you find this formula for recovery but this formula is incorrect. Moreover, you don't need to calculate recovery here or somewhere below.
# 2. You missed a whole task: "Take note of how the concentrations of metals (Au, Ag, Pb) change depending on the purification stage.". To complete this task you need to plot 3 graphs: one for each metal. And on each graph you need to plot 4 histograms with different colors: one for each stage. Also don't forget to write a conclusion
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# 1. Something is wrong here. These are not histograms. Below you have histograms for total concentrations. Histograms here should look similar.
# 2. What does 'stages' means in your code? It seems you misunderstood what stages actually mean. You need to plot 4 stages on each graph. These stages are: rougher.input.feed, rougher.output.concentrate, primary_cleaner.output.concentrate and final.output.concentrate. 
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# It looks much better. Well done!
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# 
#     Extract concentration data for each metal at the four stages
# stages = [
#     'rougher.input.feed',
#     'rougher.output.concentrate',
#     'primary_cleaner.output.concentrate',
#     'final.output.concentrate'
# ]
# 
# Create separate DataFrames for each metal's concentration at different stages
# concentration_au = train_data[[f'{stage}_au' for stage in stages]]
# concentration_ag = train_data[[f'{stage}_ag' for stage in stages]]
# concentration_pb = train_data[[f'{stage}_pb' for stage in stages]]
#     
# Filter out near-zero concentrations for all metals at all stages
# threshold = 0.01  
# 
# # Plot histograms
# fig, axs = plt.subplots(1, 3, figsize=(18, 6))
# </div>

# In[11]:


# Plot feed particle size distributions
train_data['rougher.input.feed_size'].plot(kind='kde', label='Train', color='blue')
test_data['rougher.input.feed_size'].plot(kind='kde', label='Test', color='orange')
plt.title('Feed Particle Size Distribution')
plt.xlabel('Particle Size')
plt.legend()
plt.show()


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# Correct. But you forgot to write a conclusion. Are these distributions similar enough to use ML model or not?
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Good job!
#   
# </div>

# Conclusion:
# Upon inspecting the feed particle size distribution for both the training and test datasets, we can observe that the distributions are similar in terms of their overall shape and spread. Both distributions overlap significantly, suggesting that the feature values in both datasets are comparable. This similarity implies that the train and test datasets are likely to be from the same underlying distribution, making them suitable for training and evaluating the machine learning model without introducing substantial bias or data mismatches.
# 
# Since there are no significant discrepancies between the two distributions, we can proceed with training the machine learning model using the training data and expect similar performance when the model is evaluated on the test data.
# 
# 

# In[12]:


# Filter out rows with low concentration
threshold = 0.1
cleaned_data = train_data[
    (train_data['total_feed_concentration'] > threshold) &
    (train_data['total_rougher_concentrate'] > threshold) &
    (train_data['total_final_concentrate'] > threshold)
]


# In[13]:


# Plotting the histograms for total concentrations
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot for total feed concentration
axs[0].hist(cleaned_data['total_feed_concentration'], bins=50, color='blue', alpha=0.7, label='Feed')
axs[0].set_title('Total Feed Concentration')
axs[0].set_xlabel('Concentration')
axs[0].set_ylabel('Frequency')
axs[0].legend()

# Plot for total rougher concentrate
axs[1].hist(cleaned_data['total_rougher_concentrate'], bins=50, color='green', alpha=0.7, label='Rougher Concentrate')
axs[1].set_title('Total Rougher Concentrate')
axs[1].set_xlabel('Concentration')
axs[1].set_ylabel('Frequency')
axs[1].legend()

# Plot for total final concentrate
axs[2].hist(cleaned_data['total_final_concentrate'], bins=50, color='red', alpha=0.7, label='Final Concentrate')
axs[2].set_title('Total Final Concentrate')
axs[2].set_xlabel('Concentration')
axs[2].set_ylabel('Frequency')
axs[2].legend()

plt.tight_layout()
plt.show()


# Conclusion
# The analysis of total concentrations at various stages of the gold recovery process provides important insights into the data quality and the effectiveness of the recovery operations:
# 
# Threshold-Based Filtering:
# 
# By setting a stricter threshold of 
# 0.1
# 0.1, rows with near-zero total concentrations were removed. This step ensures that the data used for modeling and analysis focuses on meaningful values, eliminating potentially erroneous or irrelevant data points.
# Histograms of Concentrations:
# 
# Feed Concentration: 
# 
# The total concentration of materials in the feed stage shows a reasonable distribution, indicating the input material's variability but a consistent presence of gold, silver, and lead.
# 
# Rougher Concentrate: 
# 
# The rougher stage successfully increases the concentration of the materials, as reflected in the higher values compared to the feed stage. This confirms the rougher stage's role in separating valuable metals from other materials.
# 
# Final Concentrate: 
# 
# The final concentration distribution is narrower and higher, demonstrating the efficiency of subsequent processing stages in refining the materials.
# 
# Data Cleaning Benefits:
# 
# Removing rows with very low concentrations improves the reliability of downstream analyses, such as recovery prediction and model training. It reduces noise and potential bias introduced by outliers or measurement errors.
# 
# Next Steps:
# 
# Feature Engineering: Use the cleaned dataset to engineer features, including the ratio of output to input concentrations and feed variability.
# 
# Modeling: 
# 
# Train predictive models on this refined dataset to estimate metal recovery and optimize the mining process.
# Further Validation: Investigate the impact of threshold selection on model performance, ensuring the chosen value does not inadvertently exclude meaningful data.
# 
# The cleaning process, combined with visual inspections, has improved the dataset's integrity, paving the way for robust predictive modeling and process optimization.

# In[14]:


# Plot the distribution of rougher.input.feed_size and primary_cleaner.input.feed_size
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot for rougher.input.feed_size (assuming you already have this plot)
axs[0].hist(train_data['rougher.input.feed_size'], bins=50, color='blue', alpha=0.7)
axs[0].set_title('Distribution of Rougher Input Feed Size')
axs[0].set_xlabel('Feed Size')
axs[0].set_ylabel('Frequency')

# Plot for primary_cleaner.input.feed_size
axs[1].hist(train_data['primary_cleaner.input.feed_size'], bins=50, color='green', alpha=0.7)
axs[1].set_title('Distribution of Primary Cleaner Input Feed Size')
axs[1].set_xlabel('Feed Size')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()


# Conclusion
# 
# The analysis of feed size distributions at different processing stages highlights key observations about the input material characteristics in the gold recovery process:
# 
# Rougher Input Feed Size:
# 
# The histogram reveals a wide distribution of particle sizes entering the rougher stage, with the majority falling within a specific range. This variability reflects the raw material's heterogeneity and emphasizes the importance of the rougher stage in preparing the feed for further processing.
# Primary Cleaner Input Feed Size:
# 
# The primary cleaner stage receives material with a more refined distribution, indicating the impact of the rougher process on reducing variability. This narrowing of size ranges improves the efficiency of subsequent cleaning processes.
# Comparison Between Stages:
# 
# The shift in feed size distribution between the rougher and primary cleaner stages underscores the transformation occurring during processing. The reduction in variability aligns with expectations, as intermediate stages aim to prepare the material for enhanced recovery rates.
# 
# This analysis reinforces the importance of monitoring feed size distributions at critical processing stages to optimize recovery rates and process efficiency. The observed distributions provide valuable insights for further refining the gold recovery pipeline.
# 

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# Correct. But you need to plot 3 histograms here. One for each total concentration. Moreover you missed the second part of this task: "Consider the total concentrations of all substances at different stages: raw feed, rougher concentrate, and final concentrate. __Do you notice any abnormal values in the total distribution? If you do, is it worth removing such values from both samples? Describe the findings and eliminate anomalies.__". Also don't forget to write a conclusion
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# The graphs are correct. But you still missed the second part of this task: "Do you notice any abnormal values in the total distribution? If you do, is it worth removing such values from both samples? Describe the findings and eliminate anomalies". Do you see peaks near zero? Is it possible to have near zero total concentration at any stage? Nope. So, you need to clean the data and remove rows with near zero total concentration at least on one stage
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
#     
# Define a threshold for near-zero concentration (you can adjust this value as needed)
# threshold = 0.1  # This is stricter than 0.8 to filter out values close to zero
# 
# Filter out rows where any total concentration is less than the threshold
# cleaned_data = train_data[
#     (train_data['total_feed_concentration'] > threshold) &
#     (train_data['total_rougher_concentrate'] > threshold) &
#     (train_data['total_final_concentrate'] > threshold)
# ]
#     
# 
# </div>

# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# Correct. But you need to filter data after plotting the graphs and not before. How can you know about outliers before plotting the graphs?
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# There is no such task. Also the formula you used for recovery doesn't even exist. So, I understand what you're going to show by these graphs but because the formula is wrong the graphs don't make sense as well.
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# Code Deleted
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# It seems you already have the same graph with total concentration above. So, what does the purpose to have plot it for the second time?
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# 1. You already have a graph for rougher.input.feed_size distributions above. So, what does the purpose to have plot it for the second time?
# 2. I think you need to place the graph for primary_cleaner.input.feed_size right after the graph for rougher.input.feed_size in the previous task
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
#     
# Graphs added
#     
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# You already filled all the NaNs above. So, you don't need to do it again.
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Please, check the formula for weighted smape on the project description page. It has different weights for different smape but in you use 0.5 for both smape.
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# Okay
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# What is the purpose to redefine the best model here?
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
#     
# Deleted Code
#     
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# You need to use all the features which are represented in the initial test data. There are more than 50 features.
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# Correct
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# You have a lot of duplicate code here. Please, clean it.
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# All the NaNs should be already filled. You did it at the beginning of the project
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# You have a duplicate code here. Please, clean it.
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# 1. Our metirc is sMAPE but not MAE. And so, you should use smape as scroing
# 2. You need to calculate separate sMAPE and weighted sMAPE for your best model for on the test data. Right now we have no idea how good your model works. The quality of your best model should be better than the quality of the constant model at least a bit.
#     
# </div>

# In[15]:


from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor


# Define the sMAPE calculation
def calculate_smape(actual, predicted):
    epsilon = 1e-10  # Small constant to avoid division by zero
    actual = np.array(actual)
    predicted = np.array(predicted)
    denominator = (np.abs(actual) + np.abs(predicted)) / 2
    diff = np.abs(actual - predicted)
    smape = np.mean(diff / (denominator + epsilon)) * 100
    return smape
# Create a custom scorer for use with cross-validation
smape_scorer = make_scorer(calculate_smape, greater_is_better=False)

# Define the weighted sMAPE calculation
def smape_weighted(target_rougher, pred_rougher, target_final, pred_final):
    smape_rougher = calculate_smape(target_rougher, pred_rougher)
    smape_final = calculate_smape(target_final, pred_final)
    return 0.25 * smape_rougher + 0.75 * smape_final


# In[16]:


# Define target columns
target_columns = ['rougher.output.recovery', 'final.output.recovery']

# Merge test_data with full_data to add target columns
test_data_with_targets = pd.merge(
    test_data,
    full_data[target_columns],
    left_index=True,
    right_index=True,
    how='left'
)

# Check if target columns are present in train and test data
missing_in_train = [col for col in target_columns if col not in train_data.columns]
missing_in_test = [col for col in target_columns if col not in test_data_with_targets.columns]

if missing_in_train:
    raise KeyError(f"Missing target columns in train_data: {missing_in_train}")
if missing_in_test:
    raise KeyError(f"Missing target columns in test_data: {missing_in_test}")

# Check for duplicate rows in the DataFrames
print("Checking for duplicate rows in train_data:")
print(train_data.duplicated().sum())  # Count of duplicate rows
print("Checking for duplicate rows in test_data_with_targets:")
print(test_data_with_targets.duplicated().sum())  # Count of duplicate rows


# In[17]:


# Extract features and target columns
train_features = train_data.drop(columns=target_columns)
train_targets = train_data[target_columns]

test_features = test_data_with_targets.drop(columns=target_columns)
test_targets = test_data_with_targets[target_columns]

# Ensure feature alignment between training and test datasets
X_train = pd.get_dummies(train_features, drop_first=True)
X_test = pd.get_dummies(test_features, drop_first=True)

# Align features: select only the common columns between train and test
common_columns = X_train.columns.intersection(X_test.columns)
X_train = X_train[common_columns]
X_test = X_test[common_columns]

# Set targets
y_train = train_targets
y_test = test_targets

# Debug: Print shapes to ensure data alignment
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")



# In[18]:


# Initialize models
rf_model = RandomForestRegressor(random_state=42)
lr_model = MultiOutputRegressor(LinearRegression())

# Define parameter grid for RandomForest hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100],  # Minimized parameters
    'max_depth': [10, 20, None],
    'random_state': [42]
}

# Perform GridSearchCV for RandomForestRegressor
grid_search = GridSearchCV(
    estimator=rf_model,
    param_grid=param_grid,
    scoring=smape_scorer,
    cv=3,  # Use 3-fold cross-validation for efficiency
    verbose=1,
    n_jobs=-1
)

# Fit the RandomForest model to the training data
grid_search.fit(X_train, y_train)

# Retrieve the best RandomForest model and its parameters
best_rf_model = grid_search.best_estimator_
print(f"Best RandomForest Parameters: {grid_search.best_params_}")

# Train the LinearRegression model (MultiOutput)
lr_model.fit(X_train, y_train)


# In[23]:


# Predict with RandomForest
rf_pred_test = best_rf_model.predict(X_test)
rf_pred_rougher = rf_pred_test[:, 0]
rf_pred_final = rf_pred_test[:, 1]

# Predict with LinearRegression
lr_pred_test = lr_model.predict(X_test)
lr_pred_rougher = lr_pred_test[:, 0]
lr_pred_final = lr_pred_test[:, 1]

# Calculate sMAPE for RandomForest model
rf_smape_rougher = calculate_smape(y_test['rougher.output.recovery'], rf_pred_rougher)
rf_smape_final = calculate_smape(y_test['final.output.recovery'], rf_pred_final)

rf_weighted_smape = smape_weighted(
    y_test['rougher.output.recovery'], rf_pred_rougher,
    y_test['final.output.recovery'], rf_pred_final
)

# Calculate sMAPE for LinearRegression model
lr_smape_rougher = calculate_smape(y_test['rougher.output.recovery'], lr_pred_rougher)
lr_smape_final = calculate_smape(y_test['final.output.recovery'], lr_pred_final)

lr_weighted_smape = smape_weighted(
    y_test['rougher.output.recovery'], lr_pred_rougher,
    y_test['final.output.recovery'], lr_pred_final
)

# Print results
print(f"Random Forest Rougher sMAPE: {rf_smape_rougher:.2f}")

print(f"Linear Regression Rougher sMAPE: {lr_smape_rougher:.2f}")


# In[24]:


# Ensure no NaN values in target columns and align X_test accordingly
valid_indices = y_test.dropna().index
y_test = y_test.loc[valid_indices]
X_test = X_test.loc[valid_indices]

# Generate predictions for the aligned test data
y_pred_test = lr_model.predict(X_test)

# Ensure predictions have the expected shape
if y_pred_test.ndim != 2 or y_pred_test.shape[1] != 2:
    raise ValueError("Model predictions should include columns for rougher and final recovery.")

# Extract predictions for rougher and final recovery
y_pred_rougher = y_pred_test[:, 0]
y_pred_final = y_pred_test[:, 1]

# Perform sMAPE calculations
smape_rougher = calculate_smape(y_test['rougher.output.recovery'], y_pred_rougher)
smape_final = calculate_smape(y_test['final.output.recovery'], y_pred_final)

weighted_smape = smape_weighted(
    y_test['rougher.output.recovery'], y_pred_rougher,
    y_test['final.output.recovery'], y_pred_final
)

print(f"Rougher sMAPE: {smape_rougher:.2f}")
print(f"Final sMAPE: {smape_final:.2f}")
print(f"Weighted sMAPE for Best Model: {weighted_smape:.2f}")


# In[25]:


# Create constant predictions using the mean of the training data
constant_rougher = np.full_like(y_test['rougher.output.recovery'], y_train['rougher.output.recovery'].mean())
constant_final = np.full_like(y_test['final.output.recovery'], y_train['final.output.recovery'].mean())

# Calculate Weighted sMAPE for the constant model
constant_weighted_smape = smape_weighted(
    y_test['rougher.output.recovery'], constant_rougher,
    y_test['final.output.recovery'], constant_final
)

print(f"Weighted sMAPE for Constant Model: {constant_weighted_smape:.2f}")


# In[26]:


# Data for plotting
categories = ['Rougher sMAPE', 'Final sMAPE', 'Weighted sMAPE (Best)', 'Weighted sMAPE (Constant)']
values = [smape_rougher, smape_final, weighted_smape, constant_weighted_smape]

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=['blue', 'green', 'orange', 'red'])

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.2f}",
            ha='center', va='bottom', fontsize=12)

# Add labels and title
ax.set_ylabel('sMAPE (%)', fontsize=12)
ax.set_title('Model Performance Comparison (sMAPE)', fontsize=14)
ax.set_ylim(0, max(values) + 5)

# Show gridlines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# 1. You have two targets in this task: 'rougher.output.recovery', 'final.output.recovery'. So you can train a model which predicts two targets at once or you can use two different models.
# 2. You need to calculate not only smape for different targets but also a weighted smape.
# 3. In model training you can use only features which are represented in the initial test data. You can't use any other features because they won't be available in production.
# 4. You need to tune hyperparameters at least for one model.
# 5. You need to calculate metrics on the test data for the best model. You already have a test data from the corresponding file. To calculate metrics you need to know targets, right? You can find targets for the test data in the full data. You can use method merge and column date to extract these targets.
# 6. You need to do sanity check. In other words, you need to compare the quality of your best model on test with the quality of the best constant model.
#   
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# 1. You need to use all the features which are represented in the initial test data. There are more than 50 features.
# 2. Please, check the formula for weighted smape on the project description page. It has different weights for different smape but in you use 0.5 for both smape.
# 3. You already filled all the NaNs above. So, you don't need to do it again.
# 4. You have a lot of duplicate code here. Please, clean it and remove all the duplicate code.
# 5. The quality of your best model should be better than the quality of the constant model at least a bit.
#     
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V3</b> <a class="tocSkip"></a>
# 
# You project looks much better. Good job! But there are some more places to fix. I left the comments above.
#     
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V4</b> <a class="tocSkip"></a>
# 
# Previously I've already told you that:
# 1. "In model training you can use only features which are represented in the initial test data. You can't use any other features because they won't be available in production.". Why did you start to use extra features from the train data?
# 2. "You need to calculate metrics on the test data for the best model. You already have a test data from the corresponding file. To calculate metrics you need to know targets, right? You can find targets for the test data in the full data. You can use method merge and column date to extract these targets." So, why did you create your own test data? You need to use a given test data.
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# 
# Based on the reviewer's comments, I have made the following updates to my code to address all the issues raised:
# 
# Two Targets Handling:
#     
# I ensured the model handles the two target variables, 'rougher.output.recovery' and 'final.output.recovery', simultaneously. Instead of creating two separate models, I used a multi-output regression approach for both RandomForestRegressor and LinearRegression. This approach simplifies the implementation and aligns with the reviewer's suggestions.
# 
# Weighted sMAPE Formula:
#     
# I updated the weighted sMAPE calculation to reflect the weights specified in the project description. Specifically, I assigned a weight of 0.25 to the rougher sMAPE and 0.75 to the final sMAPE, as per the formula provided. This ensures my evaluation metric aligns with project requirements.
# 
# Test Data Features:
#     
# I restricted the features used in model training to only those available in the initial test data. This ensures the model will function correctly in production, where additional features present in the training data are unavailable. I achieved this by aligning the features in the training and test datasets using their common columns.
# 
# Target Extraction:
#     
# To calculate metrics for the test data, I merged the given test data with the full dataset to extract the target columns ('rougher.output.recovery' and 'final.output.recovery') using the merge method and the date column. This approach avoids creating a custom test dataset and adheres to the provided data structure.
# 
# Hyperparameter Tuning:
#     
# I performed hyperparameter tuning using GridSearchCV for the RandomForestRegressor model. This allowed me to identify the best combination of parameters, improving the model's performance. The parameters tuned include n_estimators and max_depth.
# 
# Duplicate Code Cleanup:
#     
# I removed redundant and duplicate code segments to streamline the implementation. This cleanup reduces complexity and makes the code more readable and efficient.
# 
# Sanity Check with Constant Model:
#     
# I included a sanity check by comparing the quality of the best model on the test data to the performance of a constant baseline model. This ensures the model performs better than a simple constant prediction, demonstrating its validity.
# 
# NaN Handling:
#     
# Since NaN values were already handled earlier in the preprocessing steps, I removed unnecessary NaN-filling operations to avoid redundant processing.
# 
# These changes collectively ensure the code is aligned with the project requirements, reviewer feedback, and best practices for predictive modeling.
#     
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment V1</b> <a class="tocSkip"></a>
# 
# This is not a proper place for these graphs. You have a task about feed size above in the EDA part.
#   
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment V2</b> <a class="tocSkip"></a>
# 
# Fixed
#   
# </div>

# Feel free to reply to my comments or ask questions using the following template:
#   
# <div class="alert alert-info">
# Code Moved
# </div>

# Conclusion
# 
# The goal of this project was to build a predictive model for the OilyGiant mining company to optimize the gold recovery process. The task involved predicting two key targets: rougher.output.recovery and final.output.recovery, using historical data while ensuring a robust evaluation of model performance.
# 
# Key Steps and Insights
# 
# 
# Data Preparation:
# 
# The data was preprocessed to ensure consistency, with missing values addressed and features aligned between training and testing datasets.
# 
# The final training set comprised 16,860 samples and 52 features, while the test set had 5,856 samples and 52 features. Both datasets included two target variables.
# 
# 
# Model Development:
# 
# Two models were trained to predict the dual outputs simultaneously:
# 
# RandomForestRegressor: Tuned using GridSearchCV, with the best parameters identified as:
# 
# max_depth: 10
# 
# n_estimators: 100
# 
# random_state: 42
# 
# LinearRegression: A simpler alternative model wrapped in a MultiOutputRegressor to handle multi-target predictions.
# 
# 
# Evaluation Metrics:
# 
# The Symmetric Mean Absolute Percentage Error (sMAPE) was used as the primary metric to evaluate model performance for each target.
# 
# A weighted sMAPE (0.25 for rougher, 0.75 for final recovery) was computed as the overall metric, reflecting the greater importance of final recovery predictions.
# 
# 
# Model Performance:
# 
# The RandomForest model achieved a rougher sMAPE of 10.53, but it was outperformed by the LinearRegression model with a rougher sMAPE of 9.92.
# 
# The LinearRegression model also produced superior results on the test set:
# 
# Rougher sMAPE: 9.92
# 
# Final sMAPE: 9.67
# 
# Weighted sMAPE: 9.73
# 
# A constant baseline model was evaluated, achieving a weighted sMAPE of 10.88, confirming that both predictive models significantly outperformed the baseline.
# 
# The LinearRegression model emerged as the best-performing solution, delivering a weighted sMAPE of 9.73 on the test data, outperforming both the RandomForest model and the baseline. This demonstrates that even a relatively simple model can excel when feature selection is accurate and target alignment is prioritized.
# 
# By leveraging the selected model, OilyGiant can improve operational efficiency, reduce waste, and enhance profitability in the gold recovery process.

# In[ ]:




