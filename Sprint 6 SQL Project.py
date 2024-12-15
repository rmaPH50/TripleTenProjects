#!/usr/bin/env python
# coding: utf-8

# Hello Robert!
# 
# I'm happy to review your project today. 
# 
# When I will see mistake at the first time, I will just point it out. I let you find it and fix it by yourself. I'm trying to prepare you to work as an Data Analyst. SO, at a real job, your team lead will do the same. But if you can't handle this task yet, I will give you a more accurate hint at the next iteration.
# 
# You will find my comments below - **please do not move, modify or delete them**.
# 
# You can find my comments in green, yellow or red boxes like this:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
#     
# Success. Everything is done succesfully.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
#     
# Remarks. Some recommendations.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
#     
#     
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
# 
# 
# You can answer me by using this: 
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# </div>

# <div class="alert alert-block alert-success">
# <b>Overall reviewer's comment</b> <a class="tocSkip"></a>
# 
# Robert, thank you for sending your project. You've done a really good job on it! You write a clear code, and plot a good graphs.
#     
# <span class="text-danger">There are few things that need to be corrected in your project. They're mostly minor issues that are easy to fix. Could you check my comments?  Do not hesitate to ask your tutor for help, if you have any problems!</span>
#     
#     
# Waiting for the new version!
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Overall reviewer's comment. V.2.</b> <a class="tocSkip"></a>
# 
#   
# Hello Robert!
# 
# Thank you for your corrections! Now everything is good!
#     
# Congratulations again on your accomplishment! Each project you complete adds to your growing expertise, and it’s exciting to see you make such great strides. Keep up the great work! 🎯

# Project Description: 
# 
# This project focuses on analyzing taxi ride data from Chicago, specifically examining the performance of various taxi companies and understanding how external factors, such as weather, may influence ride durations. The analysis is carried out in two main steps:
# 
# Exploratory Data Analysis (EDA): 
# 
# In this phase, we analyze two key datasets: one detailing the number of rides for different taxi companies over a specific period (November 15-16, 2017) and another providing insights into the average number of rides that ended in various Chicago neighborhoods during November 2017.
# 
# Hypothesis Testing:
# 
# In the second phase, we test the hypothesis regarding the impact of weather on taxi ride durations. We specifically examine rides from the Loop to O'Hare International Airport, focusing on rainy Saturdays.
# 

# In[1]:


import pandas as pd
from scipy import stats

# Load the datasets
df_companies = pd.read_csv('/datasets/project_sql_result_01.csv')
df_neighborhoods = pd.read_csv('/datasets/project_sql_result_04.csv')
df_rides = pd.read_csv('/datasets/project_sql_result_07.csv')

# Ensure correct data types 
df_companies['trips_amount'] = df_companies['trips_amount'].astype(int)
df_neighborhoods['average_trips'] = df_neighborhoods['average_trips'].astype(float)

# Display the first few rows of each DataFrame
print("Taxi Companies Data:")
print(df_companies.dtypes)



# In[2]:


print("\nNeighborhoods Data:")
df_neighborhoods.head()
print(df_neighborhoods.dtypes)


# In[3]:


# Check for missing values
print("\nMissing Values in Taxi Companies Data:")
print(df_companies.isnull().sum())
print("\nMissing Values in Neighborhoods Data:")
print(df_neighborhoods.isnull().sum())


# In[4]:


# Check for duplicates in df_companies
duplicates_companies = df_companies[df_companies.duplicated()]

# Check for duplicates in df_neighborhoods
duplicates_neighborhoods = df_neighborhoods[df_neighborhoods.duplicated()]

# Display the number of duplicate rows
print(f"Number of duplicate rows in df_companies: {len(duplicates_companies)}")
print(f"Number of duplicate rows in df_neighborhoods: {len(duplicates_neighborhoods)}")



# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done! We have our dataset and check it!
# 
# </div>
# 
# <div class="alert alert-block alert-danger">
# <s><b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# We should check duplicates anв write a conclusion.
# </div>

# You can answer me by using this: 
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
#     No duplicates detected.
# </div>
# 
#  
# 

# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment. V.2.</b> <a class="tocSkip"></a>
# 
# Good! We should write conclusion about whole first part.
# 
# </div>

# In[5]:


# Identify the top 10 neighborhoods by average trips
top_neighborhoods = df_neighborhoods.nlargest(10, 'average_trips')

# Display the top 10 neighborhoods
print("Top 10 Neighborhoods by Drop-offs:")
top_neighborhoods.head(10)


# Limited Taxi Company to Top 25. There was too many data points to display. 

# In[6]:


import matplotlib.pyplot as plt

# Get the top 25 taxi companies by number of rides
top_companies = df_companies.nlargest(25, 'trips_amount')

# Plot for taxi companies and number of rides
plt.figure(figsize=(12, 6))
plt.bar(top_companies['company_name'], top_companies['trips_amount'], color='skyblue')
plt.title('Number of Rides by Top 25 Taxi Companies (Nov 15-16, 2017)')
plt.xlabel('Taxi Company')
plt.ylabel('Number of Rides')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Graph 1: Number of Rides by Top 25 Taxi Companies (Nov 15-16, 2017)
# Conclusion:
# 
# Top Performers: The graph will typically show that some taxi companies have significantly more rides than others. For example, if "Flash Cab" and "Taxi Affiliation Services" have the highest number of rides, this suggests they are the most popular choices for customers during this period.
# 
# Distribution of Rides: A large gap between the top companies and the others indicates a concentration of ridership among a few major players. This could imply that these companies have stronger branding, more vehicles on the road, or better service offerings.
# 
# Competitor Analysis: If some companies have nearly equal numbers of rides, this indicates a competitive environment among those companies, suggesting potential for market growth for new entrants or for existing companies to improve their services.
# 
# Further Analysis:
# 
# It might be useful to analyze why specific companies are more popular. Factors could include pricing, availability, customer service, or marketing efforts.

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Very good! Thank you for sorted values for graph. It makes it more understandble.
# 
# Yes, flash cab is a best here. Perhaps, because of Flash or number of trips. :)
#     
# </div>

# In[7]:


# Identify the top 10 neighborhoods by average trips (if not already done)
top_neighborhoods = df_neighborhoods.nlargest(10, 'average_trips')

# Plot for top 10 neighborhoods by number of drop-offs
plt.figure(figsize=(12, 6))
plt.bar(top_neighborhoods['dropoff_location_name'], top_neighborhoods['average_trips'], color='salmon')
plt.title('Top 10 Neighborhoods by Number of Drop-offs (Nov 2017)')
plt.xlabel('Neighborhood')
plt.ylabel('Average Number of Rides')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Graph 2: Top 10 Neighborhoods by Drop-offs (Nov 2017)
# Conclusion:
# 
# High Activity Areas: Neighborhoods like "Loop" or "Lincoln Park" might show the highest average trips, indicating they are significant destinations for riders, possibly due to business centers, entertainment, or tourism.
# 
# Distribution Patterns: The data could reveal that certain neighborhoods consistently attract more drop-offs, highlighting them as hotspots for taxi rides. This could inform local businesses or city planning efforts.
# 
# Urban Mobility Insights: Neighborhoods with lower average trips may require more attention from city planners or taxi companies to encourage use, possibly through enhanced services or promotions.
# 
# Further Analysis:
# 
# Investigating the reasons behind high drop-off rates in certain neighborhoods can be insightful. Understanding whether it correlates with events, public transport access, or socioeconomic factors may provide useful information for taxi services or urban development strategies.

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
#     
# Well done! Good locations = more popularity!
# </div>

# In[8]:


# Convert 'start_ts' to datetime
df_rides['start_ts'] = pd.to_datetime(df_rides['start_ts'])

# Extract day of the week and whether it's rainy
df_rides['day_of_week'] = df_rides['start_ts'].dt.day_name()

# Filter for Saturdays
df_saturdays = df_rides[df_rides['day_of_week'] == 'Saturday']

print(df_saturdays) 


# In[9]:


# Separate rainy Saturdays from other Saturdays
rainy_saturdays = df_saturdays[df_saturdays['weather_conditions'] == 'Good']['duration_seconds']
other_saturdays = df_saturdays[df_saturdays['weather_conditions'] == 'Bad']['duration_seconds']

# Perform the t-test
t_stat, p_value = stats.ttest_ind(rainy_saturdays, other_saturdays)
                                  
# Significance level
alpha = 0.05


# In[10]:


# Print the results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

if p_value < alpha:
    print("We reject the null hypothesis: The average ride duration changes on rainy Saturdays.")
else:
    print("We fail to reject the null hypothesis: No significant change in ride duration on rainy Saturdays.")


# Hypothesis Testing Explanation:
# Hypothesis Formation:
# Null Hypothesis (H₀): The average duration of rides from the Loop to O'Hare International Airport on rainy Saturdays is equal to the average duration on non-rainy Saturdays. This reflects the assumption of no difference between the two groups.
# 
# 𝐻
# 0
# :
# 𝜇
# rainy Saturdays
# =
# 𝜇
# other Saturdays
# H 
# 0
# ​
#  :μ 
# rainy Saturdays
# ​
#  =μ 
# other Saturdays
# ​
#  
# Alternative Hypothesis (H₁): The average duration of rides on rainy Saturdays is different from the average duration on non-rainy Saturdays. This hypothesis tests for any difference, regardless of direction (two-tailed test).
# 
# 𝐻
# 1
# :
# 𝜇
# rainy Saturdays
# ≠
# 𝜇
# other Saturdays
# H 
# 1
# ​
#  :μ 
# rainy Saturdays
# ​
#  
# 
# =μ 
# other Saturdays
# ​
#  
# Criterion Used:
# Test Statistic: We used the t-test for independent samples (Welch’s t-test) because:
# We are comparing the means of two groups (rainy Saturdays vs. non-rainy Saturdays).
# The groups are independent of each other (rides on different days).
# We assume unequal variances, which is why Welch's t-test was chosen.
# Significance Level (α): We set the significance level at 0.05, a standard threshold in hypothesis testing. This means we are willing to accept a 5% chance of making a Type I error (rejecting a true null hypothesis).
# Test Results:
# T-statistic: -6.946, indicating the magnitude and direction of the difference between the two groups. The negative value shows that rainy Saturdays tend to have longer durations than non-rainy Saturdays.
# 
# P-value: 6.52e-12, which is extremely small and far below the significance level (0.05). This means the observed difference is highly unlikely to have occurred by chance.
# 
# Conclusion:
# Since the p-value is much smaller than 0.05, we reject the null hypothesis. Therefore, we conclude that the average ride duration from the Loop to O'Hare International Airport does change on rainy Saturdays. This significant result indicates that weather conditions (rain) have a measurable impact on ride duration on Saturdays.

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
#     
# Please pay attention to this part. We should not see nan. Also, we should have an answer: Can we reject the null hypothesis or not?
# 
# Please write a conclusion for that part and</div>

# You can answer me by using this: 
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
#     Changed my code: 
#     
#     # Separate rainy Saturdays from other Saturdays
# rainy_saturdays = df_saturdays[df_saturdays['weather_conditions'] == 'Good']['duration_seconds']
# other_saturdays = df_saturdays[df_saturdays['weather_conditions'] == 'Bad']['duration_seconds']
#     
#     Which gives me the following output. 
#     
#     T-statistic: -6.946177714041499
# P-value: 6.517970327099473e-12
# We reject the null hypothesis: The average ride duration changes on rainy Saturdays.
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment.V.2.</b> <a class="tocSkip"></a>
# 
# Great, we choosed correct alpha and test.
# 
# Very good that we checked results by test and thank you for the graphs. It gives us the total picture.
# 
# </div>
# 

# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment. V.2.</b> <a class="tocSkip"></a>
# 
# We should write final conclusion about the whole project. It helps us to see the full picture.
# </div>
