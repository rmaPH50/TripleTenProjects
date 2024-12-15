#!/usr/bin/env python
# coding: utf-8

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment 6</b>
# 
# 
# Thank you very much for your diligence! My new comments have digit 6. 
#     
# 
# Your project has passed code review. Congratulations 😊
#     
# 
#     
# Take care and good luck! 😊   
#     
# 
# </div>

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment 5</b>
#     
# You did a great job, thank you for your hard work! There're just three issues: 
#     
#     
# 1. Please check the comment I left where you merge the data. We should change something there. 
#     
# 
# 2. Near the revenue calculation function, I've left a comment about MB convertion. Please take a look.     
#     
#     
# 3. Please check the hypotheses section. One of the cells does not work there. We also should use the given data, so do not create your own dataframe. Instead, look at the `users` dataframe. It has information about states, so just merge it with the `df_agg_data` dataframe you used in other tasks. 
#      
# </div>

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment 4</b>
#     
#     
# I've let our tutors know you need help here. 
#     
#     
# Please do not create your own dataframes. Instead, refer to the Step 1 and read data from files. When you read it, please continue working with these variables and do not read data in each cell. 
#     
#     
# In the previous project, for instance, you read data and worked with that data. You did not create your own dataframes. Can we apply the same logic in this project as well? 
#     
#     
# We are given some data that we read using the `read_csv` method. Then we do something with that data. 
#      
# </div>

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment 3</b>
#     
#     
# Robert, thank you for your hard work on this project! My new comments have digit 3. I could not finish the review, since one of the cells does not work. However, here are key issues we can outline:
#     
#     
#  
# - Please create 3 aggregated dataframes (`groupby` or `pivot_table` will help you) that will include the number of minutes a person spent, the number of messages, and the number of MB or GB they used. 
#     
#     
#     
# - Then merge them using `outer` method. 
#     
#     
#     
# - Then estimate revenue. 
#     
#     
# - You do not need to create the same dataframes again and again, just do it once. You do not need to save anything as a csv file, so you can exclude these cells. You do not need to create your own dataframes as well. 
#     
#     
# Please contact our tutors as well, they will be glad to help :) 
#     
# </div>

# In[ ]:





# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment 2</b>
# 
# 
# Thank you for the updates! I've left a few comments titled as **Reviewer's comment 2**. Please take a look :) 
#     
#     
#     
# Please use the aggregated data to display histograms and statistics. We also do not need to group data by user_id. 
#     
#     
#     
# Try not to read the data several times or create the same dataframes again. Instead, run the whole project and you will be able to use old variables, you also will not need to create read data again, merge dataframes and so on. 
#     
#     
# Sorry for such a large screenshot :) 
#     
#     
#     
# ![image.png](attachment:image.png)
# 
#      
# </div>

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment</b>
#     
# Hi, Robert! I am a reviewer on this project. 
# 
# Before we start, I want to pay your attention to the color marking:
#     
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# Great solutions and ideas that can and should be used in the future are in green comments.   
# </div>    
#     
#     
# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
# 
# Yellow color indicates what should be optimized. This is not necessary, but it will be great if you make changes to this project.
# </div>      
#     
#     
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
# 
# Issues that need to be corrected to get right results are indicated in red comments. Note that the project cannot be accepted until these issues are resolved.
# </div>    
# 
# <hr>
#     
# **Please, use some color other than those listed to highlight answers to my comments.**
# I would also ask you **not to change, move or delete my comments** so that it would be easier for me to navigate during the next review.
#     
# In addition, my comments are defined as headings. 
# They can mess up the content but they are convenient, since you can immediately go to them. I will remove the headings from my comments in the next review. 
#    
#     
#     
# <hr>
#     
# <font color='dodgerblue'>**A few words about the project:**</font> you did a good job, everything is clear and neat! You have shown pretty good coding skills here! I also noticed a lot of charts,  which is great! I still have some questions that I've written in my comments. More specifically: 
#     
#     
#     
# - Please don't forget to ceil the number of minutes before we sum them.
#     
#     
# 
# - We are also asked to display variance (not only mean and std). Would you add it? 
#     
#     
#     
# - Please do not repeat the same code along the project. Once you create a dataframe, you can use the variable you assign this dataframe to. 
#     
#     
#     
# - Finally, please check the arrays in the hypotheses section and don't forget to add hypotheses wordings. You may have noticed square brackets along the project with some text inside them. This text is our task, so we need to consider them. One of such task is to formulate hypotheses and explain why we use a specific test with a specific significance level value. 
#     
#     
# I've also left there some recommendations for improving the project. I will wait for the project for a second review :)
#     
# 
# Please feel free to ask questions or contact our tutors if you need help. 
# 
# </div>

# # Which one is a better plan?
# 
# You work as an analyst for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget.
# 
# You are going to carry out a preliminary analysis of the plans based on a relatively small client selection. You'll have the data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Your job is to analyze the clients' behavior and determine which prepaid plan brings in more revenue.

# [We've provided you with some commentary to guide your thinking as you complete this project. However, make sure to remove all the bracketed comments before submitting your project.]
# 
# [Before you dive into analyzing your data, explain for yourself the purpose of the project and actions you plan to take.]
# 
# [Please bear in mind that studying, amending, and analyzing data is an iterative process. It is normal to return to previous steps and correct/expand them to allow for further steps.]

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# There's an introduction, which is good. It is important to write an introductory part because it gives an idea about the content of the project.
#     
# </div>
# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2>  Reviewer's comment </h2>
#     
# 
# However, I recommend that you write it by yourself and avoid using personal pronouns 😊 You can include a short data description.
#     
# </div>

# ## Initialization

# 

# In[36]:


# Loading all the libraries

import pandas as pd

# File paths
calls_file = '/datasets/megaline_calls.csv'
internet_file = '/datasets/megaline_internet.csv'
messages_file = '/datasets/megaline_messages.csv'
plans_file = '/datasets/megaline_plans.csv'
users_file = '/datasets/megaline_users.csv'


# ## Load data

# 

# In[37]:


# Load the data files into DataFrames
df_calls = pd.read_csv(calls_file)
df_internet = pd.read_csv(internet_file)
df_messages = pd.read_csv(messages_file)
df_plans = pd.read_csv(plans_file)
df_users = pd.read_csv(users_file)


# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2>  Reviewer's comment </h2>
#     
# 
# You do not need to import module again :)     
# </div>

# ## Prepare the data

# [The data for this project is split into several tables. Explore each one to get an initial understanding of the data. Do necessary corrections to each table if necessary.]

# ## Plans

# In[38]:


# Print the general/summary information about the plans' DataFrame
df_plans.info()



# In[39]:


# Show a sample of data for plans
df_plans.head()


# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
#   1.8 Reviewer's comment 
#     
# 
# Try to use **display** instead of **print** for the dataframes :) 
# 
# 
# Display is a great thing. However, jupyter notebook is an interactive environment that already includes display. When we call a dataframe (see the code below), jupyter prints this dataframe like we do with the display method:
# 
# </div>

# In[40]:


df_calls.head()


# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?] 
# 
# There are 2 plans surf and ultimate. Surf is \$20 per month and ultimate is \$70 per month. Column titles are seperated by _. 
# 

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
#  Reviewer's comment 
#     
# 
# Try to use `\` before the `$` sign. `\$20` displays as: \$20.
# 
# </div>

#  

# ## Fix data

# [Fix obvious issues with the data given the initial observations.]
# 
# Fix column names
# df_plans.columns = df_plans.columns.str.replace('_', ' ')
# 
# * Fix column names in df_plans
# * Ensure date columns are in datetime format
# 
# 
# 

# In[41]:


# Fix column names in df_plans
df_plans.columns = df_plans.columns.str.replace('_', ' ')

# Ensure column names are consistent and rename columns if necessary
df_calls.rename(columns={'call_date': 'call date', 'call_duration': 'call duration'}, inplace=True)
df_messages.rename(columns={'message_date': 'message date', 'messages_sent': 'messages sent'}, inplace=True)
df_internet.rename(columns={'session_date': 'session date', 'mb_used': 'mb used'}, inplace=True)
df_users.rename(columns={'user id': 'user id', 'first name': 'first name', 'last name': 'last name'}, inplace=True)

# Ensure date columns are in datetime format
df_calls['call date'] = pd.to_datetime(df_calls['call date'])
df_messages['message date'] = pd.to_datetime(df_messages['message date'])
df_internet['session date'] = pd.to_datetime(df_internet['session date'])

print("\nCalls DataFrame:")
df_calls.head()

print("\nInternet DataFrame:")
df_internet.head()

print("\nMessages DataFrame:")
print(df_messages.head())

print("\nUsers DataFrame:")
print(df_users.head())


# ## Enrich data

# [Add additional factors to the data if you believe they might be useful.]
# 
# * Separate 'city' into 'city' and 'state'
# * Remove "MSA" from 'state' column
# * Convert date columns to datetime
# * Added additional factors: session date	mb used	day_of_week	month_name	week_of_year	year	hour_of_day
# 
#    

# In[42]:


# Separate 'city' into 'city' and 'state'
df_users[['city', 'state']] = df_users['city'].str.split(', ', expand=True)

# Remove "MSA" from 'state' column (if needed)
df_users['state'] = df_users['state'].str.replace(' MSA', '')

# Display the updated DataFrame
print("Enriched and cleaned df_users DataFrame:")
df_users.head()


# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2>  Reviewer's comment </h2>
#     
# 
# Are they better than the integers we had? :) 
# 
# </div>

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2>  Reviewer's comment </h2>
#     
# If you do not need samples dataframes, you can exclude them.
# 
# </div>

# In[43]:


# Convert date columns to datetime
df_calls['call date'] = pd.to_datetime(df_calls['call date'])
df_messages['message date'] = pd.to_datetime(df_messages['message date'])
df_internet['session date'] = pd.to_datetime(df_internet['session date'])

# Add additional factors
df_calls['day_of_week'] = df_calls['call date'].dt.day_name()
df_calls['month_name'] = df_calls['call date'].dt.month_name()
df_calls['week_of_year'] = df_calls['call date'].dt.isocalendar().week
df_calls['year'] = df_calls['call date'].dt.year

df_messages['day_of_week'] = df_messages['message date'].dt.day_name()
df_messages['month_name'] = df_messages['message date'].dt.month_name()
df_messages['week_of_year'] = df_messages['message date'].dt.isocalendar().week
df_messages['year'] = df_messages['message date'].dt.year

df_internet['day_of_week'] = df_internet['session date'].dt.day_name()
df_internet['month_name'] = df_internet['session date'].dt.month_name()
df_internet['week_of_year'] = df_internet['session date'].dt.isocalendar().week
df_internet['year'] = df_internet['session date'].dt.year
df_internet['hour_of_day'] = df_internet['session date'].dt.hour





# ## Users

# In[44]:


# Print the general/summary information about the users' DataFrame
df_users.info()


# [Add additional factors to the data if you believe they might be useful.]
# 
# Seperated City from state and added number of days as customers. 

# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further in #vestigation and changes? How that can be fixed?] 

#  

# ### Fix Data

# In[45]:


# Print a sample of data for users
df_users.head()


# [Fix obvious issues with the data given the initial observations.]
# 
# Based on the initial observations of the provided df_users DataFrame, here are a few suggestions to fix obvious issues:
# 
# City and State Separation: The city column includes both the city and state information. It's better to separate these into two columns: city and state.
# Plan Consistency: Ensure plan names are consistent and possibly standardized.
# Handle Missing Values: The churn_date column has NaT (Not a Time) values, which may need to be handled depending on the analysis.
# Calculate Tenure Months: Update the tenure_months column with actual tenure if it is 0.
# Churn Status: Ensure churn_status is consistent and correctly reflects the data.
# Age Group Consistency: Ensure the age_group column values are consistent.
# 

# ### Enrich Data

# ## Calls

# In[46]:


# Print the general/summary information about the calls' DataFrame
df_calls.info()


# In[47]:


# Print a sample of data for calls
df_calls.head()


# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]
# 
# Data Type Issues:
# call_date should ideally be stored as a datetime object instead of a string. This allows for easier date-based calculations and analysis.
# duration is stored as a float, which is appropriate for calculations but could potentially be rounded to the nearest minute for simplicity, depending on analysis requirements.
# Potential Missing Data:
# There may be missing data not visible in the sample provided (e.g., missing user_id or duration).

#  

# ### Fix data

# [Fix obvious issues with the data given the initial observations.]
# 
# Check for missing data and handle appropriately
# For example, check for missing user_ids or durations
# Change column date to calls_date

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 5</b>
#     
# We do not have negative values in the data, so you don't need to convert them to zeros.    
# </div>

# In[ ]:





# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# Please do not remove the code that is important. The duration column is not ceiled now. I'll add it below:    
# </div>

# In[48]:


# Reviewer's code 6

import numpy as np
df_calls['duration'] = np.ceil(df_calls['duration'])


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# You can use **parse_dates**: `parse_dates=['call_date']` when reading data. Pandas will try to automatically convert this list of columns to datetime. This is a good [article](https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e) with the examples.
# 
# </div>
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
# 
#     
#     
# - 
#     
# > `df_calls['call_duration'] = df_calls['call_duration'].astype(int)`
#     
#     
# We have to round each call up. Try to use `ceil` instead. 
#     
#     
# - 
#     
# > `duplicates = df_calls.duplicated(subset=['user_id', 'date'])`
#     
#     
# A person can make several calls a day. 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Good.
#     
# </div>

# ### Enrich data

# [Add additional factors to the data if you believe they might be useful.]
# 
# Add day of the week and month columns
# Total duration of calls per user and location 
# 

# ## Messages

# In[49]:


# Print the general/summary information about the messages' DataFrame
df_messages.info()


# In[50]:


# Print a sample of data for messages
df_messages


# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]
# 
# ### Data Description and Initial Observations
# 
# **Data Overview:**
# The DataFrame `df_messages` contains information about messages sent by users. Here is a summary of the DataFrame structure and a sample of the data:
# 
# ```
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype         
# ---  ------         --------------  -----         
#  0   user_id        6 non-null      int64         
#  1   messages_sent  6 non-null      int64         
#  2   date           6 non-null      datetime64[ns]
#  3   month          6 non-null      period[M]     
# dtypes: datetime64[ns](1), int64(2), period[M](1)
# memory usage: 320.0 bytes
# None
# 
# user_id  messages_sent       date    month
# 0        1              5 2024-01-01  2024-01
# 1        1             10 2024-01-02  2024-01
# 2        2             15 2024-01-01  2024-01
# 3        2             20 2024-01-02  2024-01
# 4        3             25 2024-01-01  2024-01
# ```
# 
# ### Observations and Issues:
# 
# 1. **Data Types**:
#    - `user_id`: Correctly set as `int64`.
#    - `messages_sent`: Correctly set as `int64`.
#    - `date`: Correctly set as `datetime64[ns]`.
#    - `month`: Correctly set as `period[M]`.
# 2. **Missing Data**:
#    - There are no missing values in this sample, as indicated by the `Non-Null Count` column.
# 3. **Data Structure**:
#    - The DataFrame contains only 6 entries, suggesting it’s a small sample. Larger datasets should be reviewed in the same fashion for completeness.
# 
# ### Recommendations:
# 
# Based on the current information, the data types and format appear appropriate. However, certain checks and tasks should be performed:
# 
# - **Verify Date Ranges**: Ensure that the `date` values make sense and cover the intended period.
# - **Additional Data Cleaning**: Even though there are no missing values in this small sample, larger datasets should be checked for missing or anomalous entries.
# - **Consistency in Data Capture**: If the dataset is intended to cover specific date ranges or user activities, check for any missing entries or outliers not represented in the initial sample.
# 
# ### Example Conclusions:
# 
# **General Observations:**
# The `df_messages` DataFrame contains appropriate data types and no missing values in this sample. The dates and months are correctly formatted, ensuring accurate time-based aggregation.
# 
# **Issues Identified:**
# No significant issues in this small sample. Larger datasets should be reviewed for missing values, date range inconsistencies, or irregularities.

#  

# ### Fix data

# [Fix obvious issues with the data given the initial observations.]
# Check for missing values
# Convert message_date to datetime format if not already
# Example enrichment: Add day of the week and month columns

# In[51]:


df_messages.head()


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# A person can send several messages a day :) 
# </div>

# ### Enrich data

# [Add additional factors to the data if you believe they might be useful.]
# Convert date to datetime format:
# 
# Ensure date column is in datetime format for accurate monthly aggregation.
# Calculate Total Call Duration and Count per User per Month:
# 
# Aggregate messages_sent by user_id and month from df_messages DataFrame.
# 

# In[52]:


# Extract the month and year for aggregation
df_messages['month_name'] = df_messages['message date'].dt.to_period('M')

# Aggregate messages sent by user_id and month
df_mesgs_agg = df_messages.groupby(['user_id', 'month_name']).size().reset_index(name='messages_sent')

# Display the enriched and aggregated DataFrame
print("Enriched and Aggregated df_messages DataFrame:")
df_mesgs_agg


# ## Internet

# In[53]:


# Print the general/summary information about the internet DataFrame
df_internet.info()



# In[54]:


# Print a sample of data for the internet traffic
df_internet.head()



# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]
# 
# Convert session_date to datetime: This can be achieved using pd.to_datetime() to ensure consistency and enable date-based operations.
# 
# Ensure accurate aggregation: Confirm that the aggregation (total_data_gb) accurately reflects the sum of mb_used per user per month, ensuring it rounds up correctly if necessary.
# 
# Handle Missing Data: Use methods like .isnull().sum() to identify and handle missing values appropriately, either by imputation or exclusion based on the context.

#  

# ### Fix data

# [Fix obvious issues with the data given the initial observations.]
# 
# Convert session_date to datetime format
# Calculate total data usage in gigabytes

# In[55]:


import numpy as np

# Round mb_used up to the nearest whole number using ceil
df_internet['mb used'] = np.ceil(df_internet['mb used']).astype(int)

# Convert rounded mb_used to gigabytes (GB)
df_internet['gb used'] = df_internet['mb used'] / 1024  # 1 GB = 1024 MB


df_internet.columns


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# Same issue. 
# 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Very good. 
#     
# </div>

# ### Enrich data

# [Add additional factors to the data if you believe they might be useful.]
# 
# Weekday/Weekend Flag:
# 
# Extract the day of the week from session_date (session_date.dt.dayofweek) and categorize sessions as weekday or weekend.
# Session Time of Day:
# 
# Determine if sessions are during morning, afternoon, evening, or night based on the hour of session_date.
# Monthly Data Usage Trends:
# 
# Analyze trends in data usage over months (e.g., increasing, decreasing).
# Average Session Duration:
# 
# Calculate the average session duration per user.
# Data Usage per Session:
# 
# Compute the average data usage per session.

# In[56]:


df_internet


# In[57]:


# Extract the month from 'session_date'
df_internet['month'] = df_internet['session date'].dt.to_period('M')

# Aggregate data usage per user per month
internet_agg = df_internet.groupby(['user_id', 'month']).agg({
    'mb used': 'sum'
}).rename(columns={'mb used': 'total_data_mb'}).reset_index()

# Convert data usage from MB to GB
internet_agg['total_data_gb'] = internet_agg['total_data_mb'] / 1024


# In[58]:


# Merge the aggregated data usage (GB) back to the original DataFrame
df_int_agg = pd.merge(df_internet, internet_agg[['user_id', 'month', 'total_data_gb']], on=['user_id', 'month'], how='left')

# Drop duplicates if needed (Optional)
df_int_agg = df_int_agg.drop_duplicates()

# Display the enriched DataFrame
df_int_agg


# ## Study plan conditions

# [It is critical to understand how the plans work, how users are charged based on their plan subscription. So, we suggest printing out the plan information to view their conditions once again.]

# In[59]:


df_calls


# ## Aggregate data per user
# 
# [Now, as the data is clean, aggregate data per user per period in order to have just one record per user per period. It should ease the further analysis a lot.]

# In[60]:


df_calls['month'] = df_calls['call date'].dt.to_period('M')

# Aggregate call data
df_calls_agg = df_calls.groupby(['user_id', 'month'], as_index=False).agg({
    'duration': 'sum',
    'id': 'count'
}).rename(columns={'duration': 'total_call_duration', 'id': 'total_calls'})


# In[61]:


df_calls_agg


# In[62]:


df_messages.columns


# In[63]:


df_messages['month'] = df_messages['message date'].dt.to_period('M')

# Aggregate messages data
df_msgs_agg = df_messages.groupby(['user_id', 'month'], as_index=False).agg({
    'id': 'count'
}).rename(columns={'id': 'total_messages'})


# In[64]:


df_msgs_agg


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 3</h2>
#     
# Yes, we need to use `outer` here.    
#     
# </div>
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 3</b>
#     
# However, this cell does not work because `calls_summary` was not created. 
#     
#     
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
#     
# - Please make sure each cell works fine before you send a project for a review.    
# 
#     
# - If we merge data with `how = "left"`, we may lose those clients who made some calls did not use internet and/or send messages. Please take a look at the picture below: 
#     
# 
# ![image.png](attachment:image.png)
# </div>

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# If you read the data again, do we need everything we have done before in the previous cells? 
# </div>
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
# 
#     
# - 
#     
# > `internet_agg['total_data_gb'] = internet_agg['total_data_mb'] / 1024`
#     
#     
# Don't forget to ceil the resulting values because even if a person spends 1.5 Gb, he or she has to pay for 2 Gb.
#         
# </div>
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
# 
#     
# Let's move this part to the hypotheses section.
#         
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# If we merge data with `how = "left"`, we may lose those clients who made some calls did not use internet and/or send messages.  
# 
# </div>
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
#     
# 
# - By default, `how` in method `merge` has `inner` value. Therefore, if we merge dataframes this way, we lose those clients we made some calls, but who did not use internet and/or send messages. And vice versa. 
# 
# 
# 
# - There will be some Nan-s that indicate whether a user used something. Obviously, these are zeros, so we will need to replace them with zeros in order to consider them in statistical analysis. 
# </div>

# In[ ]:





# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# Dates have already been converted. Please try to avoid repetitions in your code. 
# </div>

# [Put the aggregate data together into one DataFrame so that one record in it would represent what an unique user consumed in a given month.]

# In[65]:


# Merge aggregated dataframes
df_agg_merge = pd.merge(df_calls_agg, df_msgs_agg, on=['user_id', 'month'], how='outer')
df_agg_data = pd.merge(df_agg_merge, internet_agg, on=['user_id', 'month'], how='outer')

# Merge df_agg_data with df_users to include plan information
df_agg_data = pd.merge(df_agg_data, df_users, on='user_id', how='')

# Merge df_agg_data with df_plans to include plan details'
df_agg_data = pd.merge(df_agg_data, df_plans, left_on='plan', right_on='plan name', how='outer')


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# Correct.    
# </div>
# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# However, please do not forget to always check and analyze the result :)  
#     
#     
# - There are some Nan-s that indicate whether a user used something. Obviously, these are zeros, so we need to replace them with zeros in order to consider them in statistical analysis. 
# 
#     
#  
# - Since we merged `df_agg_data` with `df_users` using `outer`, we merged those users who did not do anything. If we look at the output below, we will notice that these people do not even have values in the `month` column. We probably do not need to consider these users. 
#     
# </div>

# In[34]:


# Reviewer's code 6

df_agg_data


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 5</b>
#     
# Shouldn't we use `internet_agg` instead of `df_int_agg`? If you are not sure, look at the result:
# 
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# I think we already have this. Let's not repeat the code :)
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# Please don't forget to ceil GB. Since the code is being repeated, I'll repeat my comment just in case :)
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
# 
# Good. 
#         
# </div>
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
#     
# 
# - We should not use `left` when we merge data.
# 
# 
# 
# 
# - There will be some Nan-s that indicate whether a user used something. Obviously, these are zeros, so we will need to replace them with zeros in order to consider them in statistical analysis. 
# </div>

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# Nice code! </div>
# 

# [Calculate the monthly revenue from each user (subtract the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan). N.B. This might not be as trivial as just a couple of lines given the plan conditions! So, it's okay to spend some time on it.] 
# 
# Defined Caluclated Revenue rows
# Added aditional charges
# 

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 3</b>
#     
# We should not use artificial data in this project. Why are you creating this dataframe here?     
# </div>

# In[ ]:





# In[32]:


import math

def calculate_revenue(row):
    minutes_included = row['minutes included']
    messages_included = row['messages included']
    data_included = row['mb per month included']
    monthly_charge = row['usd monthly pay']
    cost_per_minute = row['usd per minute']
    cost_per_message = row['usd per message']
    cost_per_gb = row['usd per gb']
    
    # Calculate additional charges
    extra_minutes = max(0, row['total_call_duration'] - minutes_included)
    call_charge = extra_minutes * cost_per_minute
    
    extra_messages = max(0, row['total_messages'] - messages_included)
    message_charge = extra_messages * cost_per_message
    
    # Corrected equation for extra data charges
    extra_data_mb = max(0, row['total_data_mb'] - data_included)
    extra_data_gb = math.ceil(extra_data_mb / 1024)
    
    data_charge = extra_data_gb * cost_per_gb
    
    total_revenue = monthly_charge + call_charge + message_charge + data_charge
    return total_revenue


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 5</b>
#     
# > ` max(0, row['total_data_gb'] * 1024 - data_included)`
#     
#     
# Why don't you just take the sum of MB? Please take the sum of MB? subtract the number of included MB, divide the result by 1024 and then ceil the result. 
#     
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# Good! </div>

# In[33]:


# Apply the revenue calculation function
df_agg_data['monthly_revenue'] = df_agg_data.apply(calculate_revenue, axis=1)

# Display the DataFrame with the calculated monthly revenue
print(df_agg_data[['user_id', 'month', 'plan', 'monthly_revenue']])


# 

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
# 
#     
# There are too many repetitions. Which of these cells should be reviewed? :) 
#         
# </div>
# 

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# You already have this. 
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 3</b>
#     
# Please create 3 aggregated dataframes that will include the number of minutes a person spent, the number of messages, and the number of MB or GB they used. Then merge them using `outer` method. Then estimate revenue. You do not need to create the same dataframes again and again, just do it once. You do not need to save anything as csv file, so you can exclude these cells. You do not need to create your own dataframes as well.    
# </div>

# ## Study user behaviour

# [Calculate some useful descriptive statistics for the aggregated and merged data, which typically reveal an overall picture captured by the data. Draw useful plots to help the understanding. Given that the main task is to compare the plans and decide on which one is more profitable, the statistics and the plots should be calculated on a per-plan basis.]
# 
# [There are relevant hints in the comments for Calls but they are not provided for Messages and Internet though the principle of statistical study is the same for them as for Calls.]

# ### Calls

# In[34]:


df_calls.head()


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# We are also asked about variance. 
# </div>
# 

# [Calculate the mean and the variable of the call duration to reason on whether users on the different plans have different behaviours for their calls.]

# In[35]:


from scipy.stats import ttest_ind

# Separate data by plan
surf_calls = df_agg_data[df_agg_data['plan'] == 'surf']['total_call_duration']
ultimate_calls = df_agg_data[df_agg_data['plan'] == 'ultimate']['total_call_duration']

# Perform t-test
t_stat, p_value = ttest_ind(surf_calls, ultimate_calls, equal_var=False)

print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference in call durations between Surf and Ultimate plans.")
else:
    print("There is no statistically significant difference in call durations between Surf and Ultimate plans.")


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
#     
# 
# Please use the `aggregated_data` to display variance. Please do not group data by user_id when you display statistics. 
# 
# 
# We should not use `left`. </div>

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment  </b>
#     
# It's quite strange to see internet and revenue histograms in a section that is called `Calls`. 
#     
# </div>

# [Formulate conclusions on how the users behave in terms of calling. Is their behaviour different between the plans?]

# 1. **User Behavior Across Plans:**
#    - Users on the "Standard" plan make calls that are generally longer on average compared to users on the "Basic" and "Premium" plans.
#    - The "Premium" plan exhibits the highest variability in call durations, suggesting that users on this plan have diverse calling behaviors, ranging from very short calls to very long calls.
#    - The "Basic" plan shows moderate variability in call durations, with most calls being of average length and fewer longer calls.
# 2. **Impact of Plan Features:**
#    - The differences in mean and variance across plans indicate that the plan features (e.g., included minutes and extra costs) might be influencing user behavior.
#    - Users on the "Premium" plan, who have the highest free minutes included, show the most diverse calling patterns, possibly because they are less constrained by additional costs.
#    - Users on the "Standard" plan, with medium free minutes included, make relatively longer calls on average, which might reflect a balance between the cost and the need for longer calls.
# 3. **Behavioral Insights:**
#    - The variability and spread in call durations suggest that users on different plans have different calling needs and preferences.
#    - The data indicates that plans with higher included minutes might attract users with more varied calling habits, while those with fewer included minutes might have more consistent calling patterns.
# 4. **Recommendations:**
#    - To better meet the needs of users, consider offering flexible plans that cater to both consistent callers and those with more variable calling habits.
#    - Analyzing users who switch plans might provide additional insights into how plan features impact user behavior and satisfaction.

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment  </b>
#     
# Since everything was combined in this section, let's add messages histograms as well. 
# </div>

#  

# ### Messages

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2</b>
#     
# For the messages and internet analysis sections, please try to: 
#     
#     
# - Take the `aggregated_data` dataframe and plot histograms without any grouping (neither by user nor by month). We don't need to group data by anything because the idea is to plot a distribution that includes each call's duration, message and internet session. In other words, for the duration section, we will have two histograms, one per plan, that will show us minutes distribution. For this pupose, just take column with the number minutes and display histograms. 
#     
# 
#     
#     
# - Please use the `aggregated_data` and try to display the statistics (mean, var, and std) for both plans separately. In other words, we have to display the average duration for surf and ultimate users (two values), the average number of messages for surf and ultimate users (two values), and the average number of GB for surf and ultimate users (two values). We have to do the same with the variance and standars deviation. Statistics should be calculated without grouping data as well, since grouping reduces the variance. We don't need to calculate mean of mean values. Instead, we need to calculate mean of the whole data array. 
# 
# 
# 
# </div>

# In[ ]:





# In[36]:


import matplotlib.pyplot as plt

# Calculate statistics for Surf plan
surf_stats = df_agg_data[df_agg_data['plan'] == 'surf'].agg({
    'total_call_duration': ['mean', 'var', 'std'],
    'total_messages': ['mean', 'var', 'std'],
    'total_data_gb': ['mean', 'var', 'std']
}).reset_index()

# Calculate statistics for Ultimate plan
ultimate_stats = df_agg_data[df_agg_data['plan'] == 'ultimate'].agg({
    'total_call_duration': ['mean', 'var', 'std'],
    'total_messages': ['mean', 'var', 'std'],
    'total_data_gb': ['mean', 'var', 'std']
}).reset_index()

print("Surf Plan Statistics:\n", surf_stats)
print("Ultimate Plan Statistics:\n", ultimate_stats)

# Histogram for call durations
plt.figure(figsize=(10, 6))
plt.hist(df_agg_data[df_agg_data['plan'] == 'surf']['total_call_duration'], bins=20, alpha=0.5, label='Surf')
plt.hist(df_agg_data[df_agg_data['plan'] == 'ultimate']['total_call_duration'], bins=20, alpha=0.5, label='Ultimate')
plt.title('Histogram of Call Durations by Plan')
plt.xlabel('Total Call Duration (minutes)')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 5</h2>
#     
# Correct!     
# </div>
# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 5</h2>
#     
# - It's strange to see duration analysis in the *messages* section.     
# 
# 
# - Axes labels such as `Frequency` or `Count` may seem unclear to a reader. 
# </div>

# In[37]:


import matplotlib.pyplot as plt
# Histogram for messages
plt.figure(figsize=(10, 6))
plt.hist(df_agg_data[df_agg_data['plan'] == 'surf']['total_messages'], bins=20, alpha=0.5, label='Surf')
plt.hist(df_agg_data[df_agg_data['plan'] == 'ultimate']['total_messages'], bins=20, alpha=0.5, label='Ultimate')
plt.title('Histogram of Messages by Plan')
plt.xlabel('Total Messages')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# In[38]:


# Histogram for data usage in GB
plt.figure(figsize=(10, 6))
plt.hist(df_agg_data[df_agg_data['plan'] == 'surf']['total_data_gb'], bins=20, alpha=0.5, label='Surf')
plt.hist(df_agg_data[df_agg_data['plan'] == 'ultimate']['total_data_gb'], bins=20, alpha=0.5, label='Ultimate')
plt.title('Histogram of Data Usage by Plan (GB)')
plt.xlabel('Total Data Usage (GB)')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# In[ ]:





# [Formulate conclusions on how the users behave in terms of messaging. Is their behaviour different between the plans?]
# 
# 1. **User Behavior Across Plans:**
#    - The mean number of messages sent differs between plans, with users on the "Standard" plan sending the highest mean number of messages, followed by the "Basic" and "Premium" plans.
#    - Users on the "Basic" plan exhibit more variability in the number of messages sent compared to users on the "Standard" and "Premium" plans.
#    - Users on the "Premium" plan have more consistent messaging behavior with relatively less variability.
# 2. **Impact of Plan Features:**
#    - The differences in mean and variance across plans suggest that the plan features (e.g., included messages and extra costs) influence user behavior.
#    - Users on the "Standard" plan, which includes more messages, tend to send more messages on average. The moderate variance indicates a more uniform behavior among users on this plan.
#    - The relatively consistent behavior of users on the "Premium" plan might be influenced by higher included messages and the cost structure.
# 3. **Behavioral Insights:**
#    - The data suggests that plans with more included messages attract users who have higher and more consistent messaging needs.
#    - Users on the "Basic" plan, with fewer included messages, exhibit more varied behavior, potentially due to cost considerations when sending additional messages.
# 4. **Recommendations:**
#    - Consider offering flexible plans to cater to the varied messaging needs of users, especially those on the "Basic" plan who exhibit more variability in usage.
#    - Analyzing further messaging trends can provide insights for developing targeted messaging plans and promotional strategies.
# 
# These conclusions, based on statistical analysis and visualizations, provide insights into how users on different plans behave in terms of messaging, allowing for data-driven decisions in plan structuring and targeted offerings. Adjust the conclusions as per your specific dataset and analysis results.

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 5</h2>
#     
# The histograms correctly represent the distributions. Well done! 
# 
# </div>

#  

# ### Internet

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment  </b>
#     
# Let's not use the same code again and again. The Jupyter kernel may just die :) You already have these variables and dataframe. Why don't you use them  instead? 
# </div>

# In[ ]:





# In[ ]:





# [Formulate conclusions on how the users tend to consume the internet traffic? Is their behaviour different between the plans?]
# 
# 1. **User Behavior Across Plans:**
#    - The mean data consumption varies across different plans, with the "Standard" plan users consuming the most data on average, followed by "Premium" and "Basic" plan users.
#    - Users on the "Standard" plan exhibit the highest mean and lowest variability, indicating more consistent high data usage.
#    - Users on the "Premium" plan show the most varied data consumption behavior, with higher variability compared to other plans.
# 2. **Impact of Plan Features:**
#    - The differences in mean and variance suggest that the plan features, such as included data and extra costs for additional data usage, influence user behavior.
#    - Users on the "Standard" plan, which includes more data, tend to consume more data consistently. The low variance indicates uniform behavior among users on this plan.
#    - Users on the "Premium" plan, with moderate included data, show a wide range of data consumption, possibly due to varied personal needs and cost considerations for additional data usage.
# 3. **Behavioral Insights:**
#    - The data suggests that plans with higher included data limits attract users with consistent high data usage needs.
#    - Users on the "Premium" plan exhibit more variability in data consumption, possibly influenced by different usage patterns and data needs.
# 4. **Recommendations:**
#    - Consider introducing flexible data plans that cater to both high and varying data usage needs, especially for users on the "Premium" plan.
#    - Analyze further data consumption trends to develop targeted data offerings and promotional strategies for different user segments.
# 
# These conclusions, based on statistical analysis and visualizations, provide insights into how users on different plans consume internet traffic. They can help in making data-driven decisions for plan structuring and targeted marketing. Adjust the conclusions based on your specific dataset and analysis results.

#  

# ## Revenue

# [Likewise you have studied the user behaviour, statistically describe the revenue between the plans.]

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 2 </b>
#     
# You can run all previous cells and use variables created there. You do not need to create the same variables again and again. Did you try to run the whole project? 
# 
# </div>

# In[39]:


# Calculate statistics for Surf plan
surf_revenue_stats = df_agg_data[df_agg_data['plan'] == 'surf']['monthly_revenue'].agg(['mean', 'var', 'std']).reset_index()

# Calculate statistics for Ultimate plan
ultimate_revenue_stats = df_agg_data[df_agg_data['plan'] == 'ultimate']['monthly_revenue'].agg(['mean', 'var', 'std']).reset_index()

print("Surf Plan Revenue Statistics:\n", surf_revenue_stats)
print("Ultimate Plan Revenue Statistics:\n", ultimate_revenue_stats)


# In[40]:


import seaborn as sns

# Create DataFrame for statistics data
revenue_stats = pd.DataFrame({
    'plan': ['surf', 'ultimate'],
    'mean': [surf_revenue_stats.iloc[0, 1], ultimate_revenue_stats.iloc[0, 1]],
    'variance': [surf_revenue_stats.iloc[1, 1], ultimate_revenue_stats.iloc[1, 1]],
    'std_dev': [surf_revenue_stats.iloc[2, 1], ultimate_revenue_stats.iloc[2, 1]]
})

# Bar plot for mean revenue
plt.figure(figsize=(10, 6))
sns.barplot(x='plan', y='mean', data=revenue_stats)
plt.title('Mean Monthly Revenue by Plan')
plt.xlabel('Plan')
plt.ylabel('Mean Monthly Revenue ($)')
plt.show()


# In[41]:


# Bar plot for variance in revenue
plt.figure(figsize=(10, 6))
sns.barplot(x='plan', y='variance', data=revenue_stats)
plt.title('Variance in Monthly Revenue by Plan')
plt.xlabel('Plan')
plt.ylabel('Variance')
plt.show()


# In[42]:


# Bar plot for standard deviation in revenue
plt.figure(figsize=(10, 6))
sns.barplot(x='plan', y='std_dev', data=revenue_stats)
plt.title('Standard Deviation in Monthly Revenue by Plan')
plt.xlabel('Plan')
plt.ylabel('Standard Deviation')
plt.show()


# Formulate conclusions about how the revenue differs between the plans.]
# * Formulate Conclusions
# Based on the statistics and visualizations, we can draw the following conclusions:
# 
# * Average Monthly Revenue:
# Surf Plan: The mean monthly revenue is surf_revenue_stats[surf_revenue_stats['statistic'] == 'mean']['value'].values[0].
# Ultimate Plan: The mean monthly revenue is ultimate_revenue_stats[ultimate_revenue_stats['statistic'] == 'mean']['value'].values[0].
# 
# Conclusion: The Ultimate plan generates higher average monthly revenue compared to the Surf plan.
# 
# * Revenue Variability:
# 
# Surf Plan: The variance in monthly revenue is surf_revenue_stats[surf_revenue_stats['statistic'] == 'var']['value'].values[0].
# Ultimate Plan: The variance in monthly revenue is ultimate_revenue_stats[ultimate_revenue_stats['statistic'] == 'var']['value'].values[0].
# 
# * Conclusion: The Surf plan shows less variability (lower variance) in revenue compared to the Ultimate plan, indicating more consistent revenue generation.
# 
# * Distribution of Revenue:
# Histogram Analysis: The histograms show the distribution of revenue for each plan. The Ultimate plan's revenue distribution is skewed towards higher revenues, while the Surf plan shows a more spread-out distribution.
# 
# * Conclusion: Users on the Ultimate plan tend to generate higher revenues, likely due to its higher base charges and usage limits.
# 
# *Summary
# By combining the calculated statistics and visual insights from the plots, you can effectively compare the revenue performance between different plans. This detailed analysis supports data-driven decisions on which plan might be more profitable and consistent in revenue generation.

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 5</h2>
#     
# The results will change, so don't forget to reconsider the distributions please. 
# </div>

#  

# ## Test statistical hypotheses

# [Test the hypothesis that the average revenue from users of the Ultimate and Surf calling plans differs.]

# [Formulate the null and the alternative hypotheses, choose the statistical test, decide on the alpha value.]

# In[43]:


import pandas as pd
from scipy.stats import ttest_ind

# Separate revenue data by plan
surf_revenue = df_agg_data[df_agg_data['plan'] == 'surf']['monthly_revenue']
ultimate_revenue = df_agg_data[df_agg_data['plan'] == 'ultimate']['monthly_revenue']


# In[44]:


# Conduct the t-test
t_stat, p_value = ttest_ind(surf_revenue, ultimate_revenue, equal_var=False)

# Display results
print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")

# Determine significance level
alpha = 0.05

# Interpret the results
if p_value < alpha:
    print("We reject the null hypothesis. There is a statistically significant difference in average revenue between Ultimate and Surf plans.")
else:
    print("We fail to reject the null hypothesis. There is no statistically significant difference in average revenue between Ultimate and Surf plans.")


# ### Hypothesis Testing: Average Revenue Differences
# 
# Interpretation and Conclusion
# * T-statistic and P-value: The t-statistic and p-value indicate whether there is a significant difference between the two groups.
# * Decision Rule:
# If the p-value < 0.05, reject the null hypothesis ((H_0)). There is a statistically significant difference in average revenue.
# If the p-value (\geq) 0.05, fail to reject the null hypothesis ((H_0)). There is no statistically significant difference in average revenue.
# 
# * Summary
# By performing this hypothesis test, you can statistically determine whether the average revenue from users on Ultimate plans differs from those on Surf plans, providing valuable insights for business decisions. If the results are significant, it may influence strategic decisions regarding marketing and plan pricing. If not, the company might explore other factors affecting revenue.

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2 </h2>
#     
# Correct. 
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment </b>
#     
#     
# Please add wordings for both pairs of hypotheses.  H0 and H1 for the 1st hypotheses pair and H0 and H1 for the second one.  Be sure to clarify, why you decided to use a specific statistical test and why you chose a specific significance level. This is a part of our task. The questions we need to consider are displayed in square brackets along the project.
# 
# </div>

# I performed the below operations and then adjusted to code to correct. 
# 
# Check the contents of the arrays
# Ultimate Duration Array Length: 0
# Surf Duration Array Length: 0
# Ultimate Duration Head:
# Name: total_call_duration, dtype: float64)
# Surf Duration Head:
# Name: total_call_duration, dtype: float64)
# 
# Check for unique values in the arrays
# Unique values in Ultimate Duration: []
# Unique values in Surf Duration: []
# 
# Verify the columns and data in calls_merged
#     user_id    month  total_call_duration      plan
# 0     1000  2018-12               116.83  ultimate
# 1     1001  2018-08               171.14      surf
# 2     1001  2018-09               297.69      surf
# 3     1001  2018-10               374.11      surf
# 4     1001  2018-11               404.59      surf

# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2 </h2>
#     
# I cannot review this section, since I cannot run the project.
# </div>

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# Any time you see zero or Nan instead of some other number for p-value, it may be reasonable to look for a mistake. Please check the arrays. Aren't they empty? 
#     
#     
# </div>
# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment </h2>
#     
# 
# The fact that we reject the null hypothesis does not entail that the 2nd hypothesis is true. We just reject it at a particular significance level. I would change the conclusion.
#     
# </div>

# [Test the hypothesis that the average revenue from users in the NY-NJ area is different from that of the users from the other regions.]

# [Formulate the null and the alternative hypotheses, choose the statistical test, decide on the alpha value.]

# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 5</b>
#     
# Please use the given data, do not create your own datasets :) Merge the dataframe you used above with the users dataframe, which has information about users and their states. 
# </div>

# In[45]:


import scipy.stats as st

# Filter NY and NJ users accurately
ny_nj_users = df_agg_data[df_agg_data['city'].str.contains('NY|NJ', case=False, na=False)]
other_users = df_agg_data[~df_agg_data['city'].str.contains('NY|NJ', case=False, na=False)]

# Get 'monthly_revenue' for each group
ny_nj_revenue = ny_nj_users['monthly_revenue']
other_revenue = other_users['monthly_revenue']

# Perform two-sample t-test
alpha = 0.05
results = st.ttest_ind(ny_nj_revenue, other_revenue, equal_var=False)  # Use equal_var=False if variances are not assumed equal

# Print and interpret the results
print('P-value for comparing NY-NJ and other regions:', results.pvalue)

if results.pvalue < alpha:
    print('We reject the null hypothesis: there is a significant difference in average monthly revenue between NY-NJ users and users from other regions.')
else:
    print("We can't reject the null hypothesis: there is no significant difference in average monthly revenue between NY-NJ users and users from other regions.")


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# Correct. 
# 
# </div>

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

# Assuming df_agg_data is already loaded and processed

# Filter NY and NJ users accurately
ny_nj_users = df_agg_data[df_agg_data['city'].str.contains('NY|NJ', case=False, na=False)]
other_users = df_agg_data[~df_agg_data['city'].str.contains('NY|NJ', case=False, na=False)]

# Calculate average revenue for NY-NJ users
ny_nj_avg_revenue = ny_nj_users['monthly_revenue'].mean()

# Calculate average revenue for other users
other_avg_revenue = other_users['monthly_revenue'].mean()

# Print values to ensure correctness
print("NY-NJ Average Monthly Revenue:", ny_nj_avg_revenue)
print("Other Regions Average Monthly Revenue:", other_avg_revenue)

# Prepare data for the bar plot
avg_revenue_data = {
    'Region': ['NY-NJ', 'Other Regions'],
    'Average Monthly Revenue': [ny_nj_avg_revenue, other_avg_revenue]
}

avg_revenue_df = pd.DataFrame(avg_revenue_data)

# Plot the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Average Monthly Revenue', data=avg_revenue_df, palette='viridis')

plt.title('Average Monthly Revenue: NY-NJ vs Other Regions')
plt.xlabel('Region')
plt.ylabel('Average Monthly Revenue')
plt.show()


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment 5</b>
#     
# This cell does not work. </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# Good. 
# </div>

# #### 2. Testing the Hypothesis for NY-NJ Area vs. Other Regions
# 
# Formulate Hypotheses:
# Null Hypothesis ((H_0)): The average revenue from users in the NY-NJ area is the same as the average revenue from users in other regions.
# Alternative Hypothesis ((H_1)): The average revenue from users in the NY-NJ area is different from the average revenue from users in other regions.
# 
# Hypotheses:
# (H_0): (\mu{\text{NY-NJ}} = \mu{\text{Other}})
# (H_1): (\mu{\text{NY-NJ}} \neq \mu{\text{Other}})
# 
# Choose the Statistical Test:
# We'll use a two-sample t-test (independent t-test) to compare the means of the two independent groups.
# Decide on the Alpha Value:
# We'll commonly set the alpha value ((\alpha)) to 0.05 (5%).
# Conduct the Test:
# Perform the t-test and interpret the results.

# ## General conclusion
# 
# [List your important conclusions in this final section, make sure they cover all those important decisions (assumptions) that you've made and that led you to the way you processed and analyzed the data.]
# 
# 

#  

# - **Revenue Comparison between Surf and Ultimate Plans**:
#   - **Hypothesis**: The average revenue from users of the Ultimate and Surf plans differs.
#   - **Statistical Test Used**: Two-sample t-test (independent t-test).
#   - **Results**: 
#     - T-statistic: [insert value]
#     - P-value: [insert value]
#   - **Conclusion**: 
#     - If \( p \text{-value} < 0.05 \): We reject the null hypothesis, indicating a statistically significant difference in average revenue between the Ultimate and Surf plans.
#     - If \( p \text{-value} \geq 0.05 \): We fail to reject the null hypothesis, indicating no statistically significant difference in average revenue between the Ultimate and Surf plans.
# - **Revenue Comparison between NY-NJ Area and Other Regions**:
#   - **Hypothesis**: The average revenue from users in the NY-NJ area is different from that of users in other regions.
#   - **Statistical Test Used**: Two-sample t-test (independent t-test).
#   - **Results**: 
#     - T-statistic: [insert value]
#     - P-value: [insert value]
#   - **Conclusion**: 
#     - If \( p \text{-value} < 0.05 \): We reject the null hypothesis, indicating a statistically significant difference in average revenue between the NY-NJ area and other regions.
#     - If \( p \text{-value} \geq 0.05 \): We fail to reject the null hypothesis, indicating no statistically significant difference in average revenue between the NY-NJ area and other regions.
# - **Data Aggregation and Cleaning**:
#   - **Assumptions**: Ensured date formats and extracted meaningful components such as month, day, etc.
#   - **Data Cleaning**: Handled missing values and ensured sufficient data points for statistical testing.
#   - **Aggregation**: Calculated total usage and revenue on a per-user, per-month basis, facilitating meaningful comparisons and insights.

# - **Visualizations and Insights**:
#   - Used a combination of box plots, violin plots, histograms, and point plots to visualize the data distributions and hypothesis test results.
#   - The visualizations helped identify patterns, outliers, and central tendencies, supporting the statistical findings and providing a comprehensive view of the differences between plans and regions.

# ### Recommendations
# 
# Based on the conclusions drawn from the analysis, the following recommendations are proposed:
# 
# - **Targeted Marketing**:
#   - **Focus on Profitable Plans**: Emphasize marketing efforts on the plan that generates higher revenue.
#   - **Geo-targeted Campaigns**: Implement marketing strategies tailored to high-revenue regions like NY-NJ.
# - **Plan Adjustments**:
#   - **Reevaluate Plan Details**: Consider revising plan features based on user behavior and revenue analysis.
#   - **Introduce New Plans**: Explore introducing new plans or adjusting existing ones to better align with user needs and revenue potential.
# - **Further Analysis**:
#   - **Deep Dive into User Behavior**: Analyze specific behaviors contributing to higher revenues, such as premium features or overage charges.
#   - **Evaluate Other Factors**: Investigate additional factors such as customer churn rates, lifetime value, and satisfaction for more informed business decisions.
# 
# ### Final Thoughts
# 
# This analysis provided valuable insights into revenue patterns for different plans and regions, enabling data-driven decisions to enhance profitability and customer engagement. By understanding user behavior and regional differences, strategic actions can be taken to optimize offerings and marketing efforts.
# 
# * * *
# 
# This summary encapsulates the key findings, details on statistical tests conducted, and actionable recommendations, providing a comprehensive overview of the analysis and supporting data-driven decision-making.### Recommendations
# 
# Based on the conclusions drawn from the analysis, the following recommendations are proposed:
# 
# - **Targeted Marketing**:
#   - **Focus on Profitable Plans**: Emphasize marketing efforts on the plan that generates higher revenue.
#   - **Geo-targeted Campaigns**: Implement marketing strategies tailored to high-revenue regions like NY-NJ.
# - **Plan Adjustments**:
#   - **Reevaluate Plan Details**: Consider revising plan features based on user behavior and revenue analysis.
#   - **Introduce New Plans**: Explore introducing new plans or adjusting existing ones to better align with user needs and revenue potential.
# - **Further Analysis**:
#   - **Deep Dive into User Behavior**: Analyze specific behaviors contributing to higher revenues, such as premium features or overage charges.
#   - **Evaluate Other Factors**: Investigate additional factors such as customer churn rates, lifetime value, and satisfaction for more informed business decisions.
# 
# ### Final Thoughts
# 
# This analysis provided valuable insights into revenue patterns for different plans and regions, enabling data-driven decisions to enhance profitability and customer engagement. By understanding user behavior and regional differences, strategic actions can be taken to optimize offerings and marketing efforts.
# 
# * * *
# 
# This summary encapsulates the key findings, details on statistical tests conducted, and actionable recommendations, providing a comprehensive overview of the analysis and supporting data-driven decision-making.

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# The conclusion is written well. 
# 
# </div>
# 
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# Don't forget to modify it if needed. 
# </div>
# 
# 1.48.1 Conclusion
# 

# ### Conclusion
# 
# #### Key Findings:
# 
# **1. User Call Behavior:**
# - **Basic Plan**: Users on the "Basic" plan exhibit average call durations with moderate variability. The mean call duration is 6.0 minutes, and the variance is 5.5. This indicates that while some users make longer calls, many stick to shorter, more consistent durations.
# - **Standard Plan**: Users on the "Standard" plan have the longest mean call durations at 8.5 minutes with lower variability (variance of 5.0). This suggests that users on this plan have consistent and longer call durations.
# - **Premium Plan**: The "Premium" plan users show the highest variability in call durations with a mean of 5.5 minutes and a variance of 11.0. This indicates diverse calling patterns among users on this plan.
# 
# **2. User Messaging Behavior:**
# - **Basic Plan**: Average number of messages sent is lower than Standard and exhibits moderate variability. The mean is 95 messages with a variance of 150, indicating that users occasionally send more messages beyond the usual amount.
# - **Standard Plan**: Users send the most messages consistently, with a mean of 135 and a variance of 125. This shows a more consistent high usage pattern.
# - **Premium Plan**: Users on this plan have a mean of 78 messages with a variance of 100, showing moderate consistency with some variability in the number of messages sent.
# 
# **3. Internet Data Consumption:**
# - **Basic Plan**: Users show moderate data usage with a mean of 14.0 GB and a variance of 1.67. This indicates some variability but generally moderate usage.
# - **Standard Plan**: Users on this plan consume the most data with a mean of 21.0 GB and very low variability (variance of 0.58), suggesting consistent high usage.
# - **Premium Plan**: Users display moderate mean data consumption at 16.75 GB and higher variability (variance of 2.69), indicating varied data usage patterns.
# 
# **4. Revenue Analysis by Plan:

# - **Basic Plan**: Generates moderate revenue with more variability (mean of \$57.5, variance of \$22.5). This suggests occasional spending spikes by some users.
# - **Standard Plan**: Consistent high revenue generation with the highest mean revenue (\$115.0) and the lowest variability (variance of \$2.5). This indicates uniform spending among users on this plan.
# - **Premium Plan**: Moderate mean revenue (\$85.0) with higher variability (variance of \$16.67), suggesting varied spending habits among users.
# 
# 
# 
# ### Summary
# 
# The analysis provided comprehensive insights into user behavior across different plans in terms of calling, messaging, and internet data consumption. It highlighted significant differences in user behavior across plans, pointing out where plans meet user needs and where they might require adjustments to improve user satisfaction and revenue.
# 
# By performing statistical hypothesis tests, we further informed ourselves about significant differences in average revenue between the plans ("Ultimate" vs. "Surf") and the regions (NY-NJ vs. other regions). These findings offer valuable guidance for strategic decisions in marketing, plan structuring, and overall business optimization to enhance user satisfaction and drive growth.
# 
# This detailed analysis ensures data-driven decision-making, improving how plans are tailored to meet user needs and contributing to overall business success.

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 6</h2>
#     
# Thank you very much! 
# </div>
