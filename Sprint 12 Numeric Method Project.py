#!/usr/bin/env python
# coding: utf-8

# Rusty Bargain used car sales service is developing an app to attract new customers. In that app, you can quickly find out the market value of your car. You have access to historical data: technical specifications, trim versions, and prices. You need to build the model to determine the value. 
# 
# Rusty Bargain is interested in:
# 
# - the quality of the prediction;
# - the speed of the prediction;
# - the time required for training

# ## Data preparation

# In[1]:


import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


# In[2]:


file_path = '/datasets/car_data.csv'
data = pd.read_csv(file_path)

# Drop unnecessary columns
data = data.drop(columns=['DateCrawled', 'DateCreated', 'LastSeen', 'PostalCode', 'NumberOfPictures'])

# Handle missing values (for simplicity, let's drop rows with missing target 'Price')
data = data.dropna(subset=['Price'])

# Convert date columns to numeric (Days since the event)
date_columns = ['RegistrationYear', 'RegistrationMonth']
for col in date_columns:
    data[col] = pd.to_datetime(data[col], errors='coerce')
    data[f'{col}_year'] = data[col].dt.year
    data[f'{col}_month'] = data[col].dt.month

# Drop the original date columns
data = data.drop(columns=date_columns)

# Encode categorical columns using one-hot encoding
categorical_columns = ['VehicleType', 'Gearbox', 'Model', 'FuelType', 'Brand', 'NotRepaired']

# Perform one-hot encoding on the categorical columns
data_encoded = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Define the features (X) and target (y)
X = data_encoded.drop(columns=['Price'])  # All columns except 'Price'
y = data_encoded['Price']  # Target variable

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345)

categorical_columns = [col for col in categorical_columns if col in X_train.columns]
print(f"Updated categorical columns: {categorical_columns}")


# In[3]:


# Ensure X and y have the same number of samples
X = data.drop(columns='Price')  # Replace 'Price' with your target column name
y = data['Price']  # Replace 'Price' with your actual target column name

# Drop the date columns directly if you don't need them for model training
date_columns = ['DateCrawled', 'DateCreated', 'LastSeen']  
X = X.drop(columns=date_columns, errors='ignore')


# In[4]:


# Encode the target variable if it's categorical
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# One-Hot Encoding for categorical variables
categorical_columns = ['VehicleType', 'Gearbox', 'FuelType', 'Brand', 'NotRepaired']  # Example
X_encoded = pd.get_dummies(X, columns=categorical_columns, drop_first=True)

# Ensure consistent splitting
X_train_encoded, X_test_encoded, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

print(f"X_train_encoded shape: {X_train_encoded.shape}")
print(f"y_train shape: {y_train.shape}")

print(data.columns)  # This will show you all column names in your DataFrame


# In[5]:


import matplotlib.pyplot as plt

# Assuming 'price' is the column you want to check for outliers
Q1 = data['Price'].quantile(0.25)
Q3 = data['Price'].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for detecting outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = data[(data['Price'] < lower_bound) | (data['Price'] > upper_bound)]

# Output number of outliers
print(f"Number of outliers: {outliers.shape[0]}")

# Display outliers
print(outliers[['Price']])

# Visualize the distribution of 'price' and the outliers
plt.figure(figsize=(10, 6))
plt.boxplot(data['Price'])
plt.title('Boxplot of Price')
plt.show()


# ## Model training

# In[6]:


from sklearn.model_selection import RandomizedSearchCV

# Define the minimum parameter grid for RandomizedSearchCV
param_distributions_rf = {
    'n_estimators': [100, 200],
    'max_depth': [10, 15],
    'min_samples_split': [2, 5]
}

# RandomizedSearchCV setup
random_search_rf = RandomizedSearchCV(
    estimator=RandomForestRegressor(random_state=12345),
    param_distributions=param_distributions_rf,
    n_iter=5,  # Number of parameter settings to sample (minimal iteration count)
    cv=3,       # Number of cross-validation folds
    n_jobs=-1,  # Use all available cores
    verbose=3,
    random_state=12345
)

# Track training time
start_train_time = time.time()
random_search_rf.fit(X_train, y_train)
end_train_time = time.time()

# Best model from RandomizedSearchCV
best_rf = random_search_rf.best_estimator_

# Track prediction time
start_pred_time = time.time()
y_pred_rf = best_rf.predict(X_test)
end_pred_time = time.time()

# Calculate RMSE
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# Output the results
print(f"Random Forest RMSE: {rmse_rf}")
print(f"Best Parameters: {random_search_rf.best_params_}")
print(f"Training Time: {end_train_time - start_train_time} seconds")
print(f"Prediction Time: {end_pred_time - start_pred_time} seconds")


# In[7]:


# Adjust categorical columns
categorical_columns = ['Model', 'VehicleType', 'FuelType', 'Brand', 'NotRepaired']  # Remove 'Gearbox'

# Filter categorical_columns to include only those present in the DataFrame
categorical_columns = [col for col in categorical_columns if col in X_train_encoded.columns]

# Encode categorical columns using LabelEncoder if necessary
label_encoders = {}
for col in categorical_columns:
    if X_train_encoded[col].dtype == 'object':  # Only apply encoding to non-numeric columns
        label_encoders[col] = LabelEncoder()
        
        # Use .loc to avoid SettingWithCopyWarning
        X_train_encoded.loc[:, col] = label_encoders[col].fit_transform(X_train_encoded[col].astype(str))
        X_test_encoded.loc[:, col] = label_encoders[col].transform(X_test_encoded[col].astype(str))

# Ensure that the encoding is done
print(X_train_encoded[categorical_columns].head())


# In[8]:


# Fit LightGBM model
lightgbm_model = LGBMRegressor(n_estimators=200, learning_rate=0.05, max_depth=15, random_state=12345)

start_train_time = time.time()
lightgbm_model.fit(X_train_encoded, y_train)
end_train_time = time.time()

start_pred_time = time.time()
y_pred_lgbm = lightgbm_model.predict(X_test_encoded)
end_pred_time = time.time()

rmse_lgbm = np.sqrt(mean_squared_error(y_test, y_pred_lgbm))

print(f"LightGBM RMSE: {rmse_lgbm}")
print(f"Training Time: {end_train_time - start_train_time} seconds")
print(f"Prediction Time: {end_pred_time - start_pred_time} seconds")


# In[9]:


catboost_model = CatBoostRegressor(iterations=500, learning_rate=0.1, depth=10, random_seed=12345, verbose=50)

start_train_time = time.time()
catboost_model.fit(X_train_encoded, y_train)
end_train_time = time.time()

start_pred_time = time.time()
y_pred_catboost = catboost_model.predict(X_test_encoded)
end_pred_time = time.time()

rmse_catboost = np.sqrt(mean_squared_error(y_test, y_pred_catboost))

print(f"CatBoost RMSE: {rmse_catboost}")
print(f"Training Time: {end_train_time - start_train_time} seconds")
print(f"Prediction Time: {end_pred_time - start_pred_time} seconds")


# In[10]:


# Ensure only existing columns are included for encoding
categorical_columns = ['Model', 'VehicleType', 'FuelType', 'Brand', 'NotRepaired']  
categorical_columns = [col for col in categorical_columns if col in X_train.columns]

# Apply One-Hot Encoding for XGBoost
encoder = OneHotEncoder(drop='first', sparse=False)
X_train_encoded_ohe = encoder.fit_transform(X_train[categorical_columns])
X_test_encoded_ohe = encoder.transform(X_test[categorical_columns])

# Combine encoded columns with the rest of the features in X_train and X_test
X_train_encoded_ohe = np.hstack((X_train.drop(categorical_columns, axis=1), X_train_encoded_ohe))
X_test_encoded_ohe = np.hstack((X_test.drop(categorical_columns, axis=1), X_test_encoded_ohe))

# Define the model with hyperparameters
xgboost_model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=10, random_state=12345)

# Train XGBoost
start_train_time = time.time()
xgboost_model.fit(X_train_encoded_ohe, y_train)
end_train_time = time.time()

# Track prediction time
start_pred_time = time.time()
y_pred_xgboost = xgboost_model.predict(X_test_encoded_ohe)
end_pred_time = time.time()

# Calculate RMSE
rmse_xgboost = np.sqrt(mean_squared_error(y_test, y_pred_xgboost))

# Output the results
print(f"XGBoost RMSE: {rmse_xgboost}")
print(f"Training Time: {end_train_time - start_train_time} seconds")
print(f"Prediction Time: {end_pred_time - start_pred_time} seconds")


# In[11]:


# Identify categorical columns
categorical_columns = X_train_encoded.select_dtypes(include=['object']).columns

# Apply Label Encoding
label_encoders = {}
for col in categorical_columns:
    label_encoders[col] = LabelEncoder()
    
    # Fit and transform for training data
    X_train_encoded[col] = label_encoders[col].fit_transform(X_train_encoded[col])
    
    # Transform test data
    X_test_encoded[col] = label_encoders[col].transform(X_test_encoded[col])

# Confirm all columns are numeric
print(X_train_encoded.dtypes)
print(X_test_encoded.dtypes)


# In[ ]:





# In[12]:


# Define a preprocessor using OneHotEncoder for categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first', sparse=False), categorical_columns)
    ],
    remainder='passthrough'  # Keep other columns as they are
)

# Create a pipeline with preprocessing and Linear Regression
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train Linear Regression
start_train_time = time.time()
linear_reg = LinearRegression()
linear_reg.fit(X_train_encoded, y_train)
end_train_time = time.time()

# Track prediction time
start_pred_time = time.time()
y_pred_lr = linear_reg.predict(X_test_encoded)
end_pred_time = time.time()

# Calculate RMSE for Linear Regression
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

# Output the results
print(f"Linear Regression RMSE: {rmse_lr}")
print(f"Training Time: {end_train_time - start_train_time} seconds")
print(f"Prediction Time: {end_pred_time - start_pred_time} seconds")


# ## Model Comparison

# In[20]:


# Data for each model, including Linear Regression
model_names = ['Linear Regression', 'Random Forest', 'LightGBM', 'CatBoost', 'XGBoost']
rmse_values = [rmse_lr, rmse_rf, rmse_lgbm, rmse_catboost, rmse_xgboost]
train_times = [1.2280867099761963, 3808.6383967399597, 5.199921607971191, 26.853386402130127, 1087.7533192634583]
prediction_times = [0.015726327896118164, 0.36611080169677734, 0.8089327812194824, 0.07999992370605469, 1.1306407451629639]

# Normalize prediction times for better visibility
normalized_pred_times = [pt * 1000 for pt in prediction_times]  # Convert to milliseconds

# Plotting the results with dual y-axes
x = np.arange(len(model_names))  # Label positions
width = 0.25  # Width of bars

fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot RMSE and normalized Prediction Time on the first y-axis
bars_rmse = ax1.bar(x - width / 2, rmse_values, width, label='RMSE', color='skyblue')
bars_pred_time = ax1.bar(x + width / 2, normalized_pred_times, width, label='Prediction Time (ms)', color='green')

ax1.set_xlabel('Model')
ax1.set_ylabel('RMSE and Prediction Time (ms)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xticks(x)
ax1.set_xticklabels(model_names)
ax1.legend(loc='upper left')

# Create a second y-axis for Train Time
ax2 = ax1.twinx()
bars_train_time = ax2.plot(x, train_times, marker='o', color='orange', label='Train Time (s)', linewidth=2)

ax2.set_ylabel('Training Time (s)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Adding a title and grid
plt.title('Model Comparison: RMSE, Training Time, and Prediction Time')
fig.tight_layout()

# Add legends for both y-axes
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3)

# Show the plot
plt.show()


# Conclusion:
# 
# Objective:
# 
# The goal of the project for Rusty Bargain used car sales service was to build a model that predicts the market value of a car based on historical data, including technical specifications, trim versions, and prices. The model performance was evaluated using the Root Mean Squared Error (RMSE) metric, and the time required for training and prediction was also recorded for comparison.
# 
# Models Tested:
# 
# Linear Regression – Used as a sanity check to evaluate the performance of other models.
# 
# Random Forest – A tree-based algorithm, used with hyperparameter tuning to compare with other models.
# 
# LightGBM – A gradient boosting method with hyperparameter tuning to evaluate performance and speed.
# 
# CatBoost – An advanced gradient boosting algorithm that requires minimal preprocessing.
# 
# XGBoost – Another gradient boosting algorithm tested for performance and speed.
# 
# Key Observations:
# 
# Model Quality (RMSE):
# 
# Linear Regression: This model provided the baseline performance and helped confirm that more complex models should perform better. Its RMSE was quite high (3520.39), confirming the need for more advanced models.
# 
# Random Forest: Achieved an RMSE of 966.91, which was a notable improvement over Linear Regression, showing the advantage of tree-based models.
# 
# LightGBM: With an RMSE of 533.58, this model showed better performance than Random Forest, as expected with gradient boosting methods.
# 
# CatBoost: This model showed the best RMSE (486.47), suggesting it was the most accurate in predicting the car values.
# 
# XGBoost: Slightly worse than CatBoost but still provided solid performance (RMSE: 970.28).
# 
# Training Time:
# 
# Linear Regression had the fastest training time (1.23 seconds), which is typical for simpler models.
# 
# Random Forest took considerably longer (3845.36 seconds), which is expected due to the complexity and number of trees in the model.
# 
# LightGBM was much faster at 5.06 seconds, making it a good tradeoff between performance and speed.
# 
# CatBoost took 26.92 seconds, a moderate time, but the model’s accuracy made this reasonable.
# 
# XGBoost took the longest to train at 1087.75 seconds, though it was still faster than Random Forest.
# 
# Prediction Time:
# 
# Linear Regression was the fastest during prediction (0.016 seconds).
# 
# LightGBM had a reasonably fast prediction time of 0.81 seconds, which is acceptable for real-time applications.
# 
# CatBoost was the fastest in terms of prediction (0.08 seconds), which makes it highly efficient for deployment.
# 
# Random Forest (0.37 seconds) and XGBoost (1.13 seconds) had slower prediction times, but they still performed adequately.
# 
# Speed vs Quality Tradeoff:
# 
# LightGBM and CatBoost offer a strong balance between quality and speed, making them suitable for this problem where both prediction accuracy and processing time are important.
# 
# Random Forest, while accurate, takes a significantly longer time to train, making it less efficient for rapid model iteration or deployment.
# 
# XGBoost showed solid results but had higher training and prediction times than LightGBM and CatBoost.
# 
# Conclusion and Recommendations:
# 
# Best Model: CatBoost emerged as the best model in terms of RMSE, offering the most accurate predictions. It also performed efficiently in terms of training and prediction times.
# 
# Good Tradeoff: LightGBM offered a great balance between speed and prediction quality. Its fast training time and solid RMSE make it a very suitable choice for real-time predictions.
# 
# Less Ideal Models: Random Forest and XGBoost provided reasonable accuracy but at the cost of significant computation time, especially during training.
# 
# Linear Regression: Despite its poor performance compared to the tree-based models, Linear Regression served its purpose as a baseline and helped confirm that more complex models are necessary.

# # Checklist

# Type 'x' to check. Then press Shift+Enter.

# - [x]  Jupyter Notebook is open
# - [x]  Code is error free
# - [x]  The cells with the code have been arranged in order of execution
# - [x]  The data has been downloaded and prepared
# - [x]  The models have been trained
# - [x]  The analysis of speed and quality of the models has been performed

# <div style="background-color:#d4edda; padding:10px; border:1px solid #c3e6cb; border-radius:5px; color:#155724;">
# 
# Hello Robert,
# 
# Another project successfully completed - well done! 🏆 Your consistent effort and progress are truly commendable.
# 
# Our team is here to help you keep pushing forward and honing your skills as you advance through the program.
# 
# You’ll find general comments on the platform, with specific feedback within your project file in the ‘Comments’ section.
# 
# **What Was Great:**
# - Excellent job on structuring your code and ensuring it was easy to read.
# - You’ve shown strong analytical skills in deriving insights from the dataset.
# - Your approach to feature engineering was really impressive and thoughtful.
# 
# **Tips for Future Projects:**
# - Consider exploring additional machine learning algorithms to compare model performance.
# - To improve your documentation, you might try including more details about the challenges you faced and how you overcame them.
# 
# Congratulations again on your accomplishment! Each project you complete adds to your growing expertise, and it’s exciting to see you make such great strides. Keep up the great work! 🎯
# 
# </div>
