#!/usr/bin/env python
# coding: utf-8

# Hello Robert!
# 
# I’m happy to review your project today.
# I will mark your mistakes and give you some hints how it is possible to fix them. We are getting ready for real job, where your team leader/senior colleague will do exactly the same. Don't worry and study with pleasure! 
# 
# Below you will find my comments - **please do not move, modify or delete them**.
# 
# You can find my comments in green, yellow or red boxes like this:
# 
# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Success. Everything is done succesfully.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Remarks. Some recommendations.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
# 
# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Thank you so much for the feedback, I appreacaite it! I should have double checked before submitting. Thanks! 
# </div>
# 

# Project Description: 
# 
# The user is working for OilyGiant Mining Company, tasked with identifying the best location for a new oil well. The project involves the following steps:
# 
# Collecting Data: Gather data on oil well parameters in selected regions, including oil quality and volume of reserves.
# 
# Building a Predictive Model: Develop a model to predict the volume of reserves in new wells.
# 
# Selecting Top Wells: Identify the oil wells with the highest predicted reserve volumes.
# 
# Profit Analysis: Determine the region with the highest total profit for the selected oil wells.
# 
# The user is analyzing the potential profit and associated risks by using the Bootstrapping technique to assess the profitability of wells across three regions, ultimately choosing the region that offers the best profit margin.

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Constants
NUM_WELLS = 200            # Number of wells to develop
BUDGET = 100_000_000       # Development budget in USD
REVENUE_PER_UNIT = 4_500    # Revenue per unit of reserves 
COST_PER_WELL = BUDGET / NUM_WELLS

# URLs of the datasets
url_0 = 'https://practicum-content.s3.us-west-1.amazonaws.com/datasets/geo_data_0.csv'
url_1 = 'https://practicum-content.s3.us-west-1.amazonaws.com/datasets/geo_data_1.csv'
url_2 = 'https://practicum-content.s3.us-west-1.amazonaws.com/datasets/geo_data_2.csv'

# Load data
geo_data_0 = pd.read_csv(url_0)
geo_data_1 = pd.read_csv(url_1)
geo_data_2 = pd.read_csv(url_2)

# Drop 'id' column from each region's DataFrame
geo_data_0 = geo_data_0.drop(columns=['id'])
geo_data_1 = geo_data_1.drop(columns=['id'])
geo_data_2 = geo_data_2.drop(columns=['id'])

# Display the first few rows of each DataFrame (optional)
print("Geo Data 0:")
print(geo_data_0.head())

print("\nGeo Data 1:")
print(geo_data_1.head())

print("\nGeo Data 2:")
print(geo_data_2.head())


# In[2]:


# Check for missing values in each DataFrame
print("Missing values in geo_data_0:")
print(geo_data_0.isnull().sum())

print("\nMissing values in geo_data_1:")
print(geo_data_1.isnull().sum())

print("\nMissing values in geo_data_2:")
print(geo_data_2.isnull().sum())


# <div class="alert alert-success">
# <b>Reviewer's comment V1</b>
# 
# Correct
# 
# </div>

# <div class="alert alert-warning">
# <b>Reviewer's comment V1</b>
# 
# Actually you it's better to drop this field at all. You will not use it
# 
# </div>

# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Drop 'id' column from each region's DataFrame
# geo_data_0 = geo_data_0.drop(columns=['id'])
# geo_data_1 = geo_data_1.drop(columns=['id'])
# geo_data_2 = geo_data_2.drop(columns=['id'])
# 
#  
# </div>

# <div class="alert alert-success">
# <b>Reviewer's comment V2</b>
# 
# Good job!
# 
# </div>

# In[7]:


def train_and_evaluate_model(df):
   
    # Train a Linear Regression model and evaluate its performance.
    
    X = df[['f0', 'f1', 'f2']]
    y = df['product']
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the validation set
    predictions = model.predict(X_valid)
    
    # Save the predictions and actual values for analysis
    df_predictions = pd.DataFrame({'predicted': predictions, 'actual': y_valid.reset_index(drop=True)})
    
    # Calculate metrics
    avg_predicted_volume = predictions.mean()
    rmse = mean_squared_error(y_valid, predictions, squared=False)
    
    print(f"Average predicted reserves volume: {avg_predicted_volume}")
    print(f"RMSE: {rmse}")
    
    return df_predictions, model


# In[8]:


# Train and evaluate the model for each region
results = []
models = []
for i, geo_data in enumerate([geo_data_0, geo_data_1, geo_data_2]):
    print(f"\nRegion {i}:")
    df_predictions, model = train_and_evaluate_model(geo_data)
    results.append(df_predictions)
    models.append(model)

# Profit Calculation Preparation
sufficient_volume = BUDGET / (REVENUE_PER_UNIT * NUM_WELLS)  # Break-even volume per well
average_volumes = [df['product'].mean() for df in [geo_data_0, geo_data_1, geo_data_2]]

print("\nPreparation for Profit Calculation:")
print(f"Break-even volume per well: {sufficient_volume}")
for i, avg_volume in enumerate(average_volumes):
    print(f"Region {i} average reserves volume: {avg_volume}")


# <div class="alert alert-success">
# <b>Reviewer's comment V1</b>
# 
# Correct. Good job!
# 
# </div>

# In[9]:


def calculate_profit(df, prediction_column='predicted'):
    
    # Calculate profit from selected top wells based on predictions.
    
    # Select top wells based on predicted production
    selected_wells = df.sort_values(by=prediction_column, ascending=False).head(NUM_WELLS)
    total_production = selected_wells['actual'].sum()
    total_revenue = total_production * REVENUE_PER_UNIT
    total_cost = NUM_WELLS * COST_PER_WELL
    profit = total_revenue - total_cost
    
    return profit

# Calculate profit for each region
profits = []
for i, df in enumerate(results):
    profit = calculate_profit(df)
    profits.append(profit)
    print(f"Estimated profit for Region {i}: ${profit}")


# <div class="alert alert-success">
# <b>Reviewer's comment V1</b>
# 
# The function looks correct
# 
# </div>

# In[11]:


risk_threshold = 2.5

# Function to calculate profit for each sample
def calculate_profit(df, prediction_column='predicted'):
    selected_wells = df.sort_values(by=prediction_column, ascending=False).head(NUM_WELLS)
    total_production = selected_wells['actual'].sum()
    total_revenue = total_production * REVENUE_PER_UNIT
    total_cost = NUM_WELLS * COST_PER_WELL
    return total_revenue - total_cost

# Bootstrapping function for profit calculation
def bootstrap_profit(df, prediction_column='predicted', n_samples=1000):
    profits = []
    for _ in range(n_samples):
        sample_df = df.sample(n=500, replace=True)
        profit = calculate_profit(sample_df, prediction_column)
        profits.append(profit)
    
    avg_profit = np.mean(profits)
    lower_bound = np.percentile(profits, 2.5)
    upper_bound = np.percentile(profits, 97.5)
    loss_risk = (np.array(profits) < 0).mean() * 100  # Percentage of samples with negative profit
    
    return avg_profit, (lower_bound, upper_bound), loss_risk
bootstrapped_results = []

# Apply bootstrapping to each region
for i, df in enumerate(results):
    avg_profit, confidence_interval, loss_risk = bootstrap_profit(df)
    bootstrapped_results.append({
        'region': i,
        'average_profit': avg_profit,
        'confidence_interval': confidence_interval,
        'loss_risk': loss_risk
    })
    print(f"\nRegion {i} - Average Profit: ${avg_profit:.2f}")
    print(f"Region {i} - 95% Confidence Interval: ${confidence_interval[0]:.2f} to ${confidence_interval[1]:.2f}")
    print(f"Region {i} - Risk of Loss: {loss_risk:.2f}%")

# Filter regions that meet the acceptable risk threshold
acceptable_regions = [
    r for r in bootstrapped_results if r['loss_risk'] <= risk_threshold
]

# Select the best region based on average profit
if acceptable_regions:
    best_region = max(acceptable_regions, key=lambda x: x['average_profit'])
    print(f"\nSuggested region for development: Region {best_region['region']}")
    print(f"Expected average profit: ${best_region['average_profit']:.2f}")
    print(f"Risk of loss: {best_region['loss_risk']:.2f}%")
    print(f"95% Confidence Interval: ${best_region['confidence_interval'][0]:.2f} to ${best_region['confidence_interval'][1]:.2f}")
else:
    print("No region meets the risk threshold.")


# <div class="alert alert-danger">
# <b>Reviewer's comment V1</b>
# 
# 1. The code is broken because there is not function `bootstrap_profit_with_noise`
# 2. The results I saw before I ran your code were incorrect. In the correct results risk in each region should be a value between 0 and 10% but not exact 0. 
# 
# </div>

# You can answer me by using this:
# 
# 
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# I changed the below code and fixed the issus. 
#     sample_df = df.sample(n=500, replace=True)
#      return avg_profit, (lower_bound, upper_bound), loss_risk
# bootstrapped_results = []
#     
#    Deleted: bootstrap_profit_with_noise
# </div>

# <div class="alert alert-success">
# <b>Reviewer's comment V2</b>
# 
# Everything is correct now. Well done!
# 
# </div>

# Based on the analysis, Region 1 is the most suitable location for oil well development. The key factors in this decision are as follows:
# 
# Average Profit: 
# 
# Region 1 offers the highest expected average profit, estimated at approximately $4,464,520.26. This is a favorable indicator of the region's potential return compared to the other regions.
# 
# Risk of Loss: 
# 
# Region 1 meets the acceptable risk threshold, with only a 1.9% risk of incurring losses. This is well within the company’s risk tolerance of 2.5%, unlike Regions 0 and 2, which have higher risks of 7.0% and 8.9%, respectively.
# 
# Confidence Interval: 
# 
# The 95% confidence interval for Region 1’s profit ranges from $408,833.00 to $8,296,767.05. Although this range suggests some variability, it remains positive throughout, indicating a strong likelihood of profit.
# 
# In conclusion, Region 1 has the highest profitability with a manageable risk, making it the recommended choice for new well development. This decision is expected to maximize returns while adhering to the company's risk management criteria.
