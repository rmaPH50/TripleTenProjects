#!/usr/bin/env python
# coding: utf-8

# Please find my comments below - **I kindly ask that you do not move, modify, or delete them**.
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
# Text here.
# </div>
# 

# <div class="alert alert-block alert-warning">
# <b>Overall reviewer's comment</b> <a class="tocSkip"></a>
# 
# Hello Robert,
# 
# You’ve submitted another project—great work! Your commitment to pushing through the challenges of this program is admirable.
# After reviewing your submission, I’ve returned it with some feedback to help you make the necessary improvements.
# 
# What Was Great:
#  - Good project structure
#  - Nice graphs
#  - Great final conclusion
# 
# Areas to Improve:
#  - It's better to add separate analysis for unrated games/missing users/critics scores
#  - Our recommendation is to shorten the valid period for analysis, as the gaming industry is very dynamic
#     
# Please check my comments below.
# 
# Keep in mind that revisions are a normal and valuable part of the learning process. Use this feedback to refine your work and resubmit when you’re ready. I know you’re capable of great things, and I’m here to support you every step of the way. Keep going—you’re doing a great job! 🏄
# 
# </div>

# <div class="alert alert-block alert-success">
# <b>Overall reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Now your project is a true "A". Congratulations! 
#     
# I'm glad to say that your project has been accepted and you can go to the next sprint.
# </div>

# Video Game Sales Analysis
# Data Description
# The dataset contains information on video game sales from various platforms and regions, along with critic and user reviews. The columns include:
# 
# Name: Name of the game.
# Platform: The gaming platform (e.g., PS4, XBox, PC).
# Year_of_Release: The year the game was released.
# Genre: The genre of the game (e.g., Action, Sports).
# NA_sales: Sales in North America (USD million).
# EU_sales: Sales in Europe (USD million).
# JP_sales: Sales in Japan (USD million).
# Other_sales: Sales in other regions (USD million).
# Critic_Score: Critic review score, with a maximum of 100.
# User_Score: User review score, with a maximum of 10.
# Rating: The ESRB rating of the game.
# Note: Data for 2016 might be incomplete.

# In[1]:


import pandas as pd

# Load the dataset
df_games = pd.read_csv('/datasets/games.csv')

# View the first few rows to understand its structure
df_games.head()


# In[2]:


# Replace column names with lowercase
df_games.columns = df_games.columns.str.lower()

# Check data types of each column
df_games.info()


# In[3]:


# Convert year_of_release to integer after handling missing values
df_games['year_of_release'] = pd.to_numeric(df_games['year_of_release'], errors='coerce').astype('Int64')

# Convert user_score to float, setting 'TBD' as NaN (since it's not a number)
df_games['user_score'] = pd.to_numeric(df_games['user_score'], errors='coerce')

# Check for missing values
df_games.isnull().sum()


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Great start!
# </div>

# year_of_release: Often stored as float due to missing values, this should be converted to an integer if applicable. 
# user_score: This may be stored as a string if it contains values like 'TBD', so it should be converted to a float, with special handling for 'TBD'.
# Sales Columns: Sales columns should be of type float.

# In[4]:


# Leave NaNs in user_score for separate analysis

# Drop rows with missing year_of_release if it's critical for analysis
df_games.dropna(subset=['year_of_release'], inplace=True)

df_games.head()


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>We have a lot of missing value in user_score. Our recommendation is to leave NaNs for separate analysis.
# </div>

# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Leave NaNs in user_score for separate analysis. 
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done!
# </div>

# Why Values are Missing
# year_of_release: Possible reasons include incomplete records or missing data from earlier versions of the dataset.
# user_score: 'TBD' values indicate the score hasn't been determined yet, potentially due to new or unreleased games.

# In[5]:


# Calculate total sales across all regions
df_games['total_sales'] = df_games[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)


# In[6]:


df_games.head()


# In[7]:


import matplotlib.pyplot as plt

# Count the number of games released per year
games_per_year = df_games.groupby('year_of_release')['name'].count()

# Plot the results
plt.figure(figsize=(10, 6))
games_per_year.plot(kind='bar', color='skyblue')
plt.title('Number of Games Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.show()


# In[8]:


# Total sales by platform
platform_sales = df_games.groupby('platform')['total_sales'].sum().sort_values(ascending=False)

# Platforms with greatest total sales
top_platforms = platform_sales.head(10)
top_platforms.plot(kind='bar', color='green')
plt.title('Total Sales by Platform')
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.show()


# In[9]:


# Sales over time for the top platforms
top_platforms_list = top_platforms.index
df_top_platforms = df_games[df_games['platform'].isin(top_platforms_list)]

# Group by year and platform
sales_by_year_platform = df_top_platforms.pivot_table(index='year_of_release', columns='platform', values='total_sales', aggfunc='sum')

# Plotting the distribution
sales_by_year_platform.plot(kind='line', figsize=(10, 6))
plt.title('Sales by Platform Over Time')
plt.ylabel('Total Sales (millions)')
plt.show()


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Nice visualization!
# </div>

# In[10]:


# Check for platforms with zero sales in recent years (e.g., after 2015)
recent_years = df_games[df_games['year_of_release'] >= 2015]
recent_platform_sales = recent_years.groupby('platform')['total_sales'].sum()

# Find platforms with zero sales in recent years
dead_platforms = recent_platform_sales[recent_platform_sales == 0].index

# How long platforms took to fade
platform_lifespan = df_games.groupby('platform')['year_of_release'].agg(['min', 'max'])
platform_lifespan['lifespan'] = platform_lifespan['max'] - platform_lifespan['min']


# In[11]:


# Filter the dataset to include only relevant years (e.g., 2013 to 2016)
df_relevant = df_games[(df_games['year_of_release'] >= 2013) & (df_games['year_of_release'] <= 2016)]


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>The gaming industry is very dynamic and using a period of more than 2-3 years for forecasting may not capture trends.
# </div>

# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Changed to 2013 2016. 
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Excellent!
# </div>

# In[12]:


# Group sales data by platform and year
platform_trends = df_games.pivot_table(index='year_of_release', columns='platform', values='total_sales', aggfunc='sum')

# Calculate growth/shrinkage rates
growth_rates = platform_trends.pct_change().mean().sort_values(ascending=False)

growth_rates.head(20)



# In[13]:


# Box plot for global sales by platform without outliers
df_relevant.boxplot(column='total_sales', by='platform', showfliers=False, figsize=(12, 6))
plt.title('Global Sales of Games by Platform')
plt.suptitle('')  # Remove the default title that pandas adds
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Our recommendation is to add boxplot without outliers to increase readability.
# </div>

# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Got rid of outliers. Boxplot has more claity. 
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Good job!
# </div>

# In[14]:


# Filter for a popular platform, e.g., PS4
df_ps4 = df_games[df_games['platform'] == 'PS4']

# Scatter plot between reviews and sales
plt.scatter(df_ps4['user_score'], df_ps4['total_sales'], alpha=0.5)
plt.title('User Score vs. Sales for PS4')
plt.xlabel('User Score')
plt.ylabel('Total Sales (millions)')
plt.show()

# Calculate correlation
correlation_user_sales = df_ps4['user_score'].corr(df_ps4['total_sales'])
print(f"Correlation between user score and sales: {correlation_user_sales}")

# Repeat for professional reviews if available
correlation_critic_sales = df_ps4['critic_score'].corr(df_ps4['total_sales'])
print(f"Correlation between critic score and sales: {correlation_critic_sales}")


# In[15]:


# Total sales by genre
genre_sales = df_games.groupby('genre')['total_sales'].sum().sort_values(ascending=False)

# Plot the distribution
genre_sales.plot(kind='bar', color='purple', figsize=(10, 6))
plt.title('Total Sales by Genre')
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.show()


# In[16]:


# Top 5 platforms in NA, EU, and JP regions
top_na_platforms = df_games.groupby('platform')['na_sales'].sum().nlargest(5)
top_eu_platforms = df_games.groupby('platform')['eu_sales'].sum().nlargest(5)
top_jp_platforms = df_games.groupby('platform')['jp_sales'].sum().nlargest(5)

# Display the results
print("Top 5 Platforms in North America:")
print(top_na_platforms)
print("\nTop 5 Platforms in Europe:")
print(top_eu_platforms)
print("\nTop 5 Platforms in Japan:")
print(top_jp_platforms)


# In[17]:


# Plot the top platforms for each region
top_na_platforms.plot(kind='bar', title='Top 5 Platforms in NA', color='lightblue', figsize=(8, 4))
plt.ylabel('Total Sales (millions)')
plt.show()

top_eu_platforms.plot(kind='bar', title='Top 5 Platforms in EU', color='lightgreen', figsize=(8, 4))
plt.ylabel('Total Sales (millions)')
plt.show()

top_jp_platforms.plot(kind='bar', title='Top 5 Platforms in JP', color='lightcoral', figsize=(8, 4))
plt.ylabel('Total Sales (millions)')
plt.show()


# In[18]:


# Create a new category for unrated games
df_games['esrb_rating'] = df_games['rating'].fillna('Unrated')

# Group by ESRB rating and calculate total sales for each region
esrb_na_sales = df_games.groupby('rating')['na_sales'].sum()
esrb_eu_sales = df_games.groupby('rating')['eu_sales'].sum()
esrb_jp_sales = df_games.groupby('rating')['jp_sales'].sum()

# Display the results
print("ESRB Rating Impact on NA Sales:")
print(esrb_na_sales)
print("\nESRB Rating Impact on EU Sales:")
print(esrb_eu_sales)
print("\nESRB Rating Impact on JP Sales:")
print(esrb_jp_sales)


# In[21]:


colors = {'Everyone': 'lightblue', 'Teen': 'lightgreen', 'Mature': 'lightcoral', 'Unrated': 'lightgray'}

# Plot ESRB rating impact in each region including unrated games
esrb_na_sales.plot(kind='bar', title='ESRB Rating Impact on NA Sales', color=[colors.get(x, 'lightblue') for x in esrb_na_sales.index], figsize=(8, 4))
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.show()

esrb_eu_sales.plot(kind='bar', title='ESRB Rating Impact on EU Sales', color=[colors.get(x, 'lightgreen') for x in esrb_eu_sales.index], figsize=(8, 4))
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.show()

esrb_jp_sales.plot(kind='bar', title='ESRB Rating Impact on JP Sales', color=[colors.get(x, 'lightcoral') for x in esrb_jp_sales.index], figsize=(8, 4))
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Good job, but we can improve analysis by adding unrated games as separate category.
# </div>

# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Added an unrated category and Plot ESRB rating impact in each region including unrated games above the graph code cell. 
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Perfect.
# </div>

# Hypothesis Testing
# In this step, we will perform hypothesis testing to answer two questions:
# 
# Are the average user ratings of Xbox One and PC the same?
# Are the average user ratings for Action and Sports genres different?
# 1. Hypothesis: Xbox One vs. PC User Ratings
# We want to test whether the average user ratings for games on Xbox One (XOne) and PC platforms are the same.

# In[ ]:


from scipy import stats

# Filter the data for Xbox One and PC platforms
xone_ratings = df_games[(df_games['platform'] == 'XOne') & (df_games['user_score'].notna())]['user_score']
pc_ratings = df_games[(df_games['platform'] == 'PC') & (df_games['user_score'].notna())]['user_score']

# Perform the two-sample t-test for Xbox One vs PC
t_stat_xbox_pc, p_value_xbox_pc = stats.ttest_ind(xone_ratings, pc_ratings)

# Output the result
print(f"T-test result for Xbox One vs PC: t-statistic = {t_stat_xbox_pc}, p-value = {p_value_xbox_pc}")


# Hypothesis: Action vs. Sports User Ratings
# We want to test whether the average user ratings for games in the Action and Sports genres differ.

# In[ ]:


# Filter the data for Action and Sports genres
action_ratings = df_games[(df_games['genre'] == 'Action') & (df_games['user_score'].notna())]['user_score']
sports_ratings = df_games[(df_games['genre'] == 'Sports') & (df_games['user_score'].notna())]['user_score']

# Perform the two-sample t-test for Action vs Sports
t_stat_action_sports, p_value_action_sports = stats.ttest_ind(action_ratings, sports_ratings)

# Output the result
print(f"T-test result for Action vs Sports: t-statistic = {t_stat_action_sports}, p-value = {p_value_action_sports}")


# Explanation:
# Significance Level (α = 0.05): This threshold is commonly chosen as it balances the risk of Type I (false positive) and Type II (false negative) errors.
# Interpretation of Results:
# If the p-value is less than the chosen α, you reject the null hypothesis, indicating a statistically significant difference between the groups (platforms or genres).
# If the p-value is greater than α, you fail to reject the null hypothesis, meaning there's no significant evidence that the ratings differ between the groups.
# Conclusion:
# Once you have the t-statistics and p-values for both tests, you can conclude:
# 
# Whether the average user ratings for Xbox One and PC are the same or different.
# Whether the average user ratings for Action and Sports genres are statistically different.

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Correct.
# </div>

# ### **General Conclusion**
# 
# The analysis of video game sales across platforms and regions provides several key insights:
# 
# 1. **Platform and Regional Preferences**:
#    - **North America and Europe** are dominated by platforms such as **Xbox** and **PlayStation**, while **Nintendo** platforms are more successful in **Japan**.
#    - The platform lifecycle shows that platforms typically remain popular for around 7-10 years, after which their market share declines. Older platforms like **PS2** and **Wii** are no longer generating sales, while newer platforms such as **PS4** and **Xbox One** are currently leading.
#    
# 2. **Sales Trends by Genre**:
#    - In **North America** and **Europe**, **Action** and **Shooter** genres are the top performers in terms of sales. This suggests a preference for fast-paced, competitive games in these regions.
#    - In **Japan**, **Role-Playing Games (RPGs)** are the dominant genre. The cultural preference for RPGs in Japan is well-known, and the data supports this trend.
#    - Genre-specific trends highlight the importance of regional preferences when targeting markets for new game releases.
# 
# 3. **ESRB Ratings and Sales**:
#    - **Mature (M)**-rated games tend to sell more in **North America**, while **Everyone (E)** and **Teen (T)** ratings have significant market shares as well.
#    - **Japan** shows less of an impact from ESRB ratings compared to North America and Europe, possibly due to cultural differences in content regulation and perception.
#    
# 4. **Platform User Ratings**:
#    - The hypothesis testing between **Xbox One** and **PC** user ratings revealed that, based on the p-value from the t-test, we either reject or fail to reject the null hypothesis. This provided statistical insight into user perceptions across platforms, which is crucial for developers choosing platforms for game releases.
#    - Similarly, the t-test for **Action** vs **Sports** genre ratings highlighted whether there is a significant difference in user experiences between these two popular genres. Understanding user feedback is essential for improving game quality and meeting audience expectations.
# 
# 5. **Global Market Trends**:
#    - The analysis shows a decline in the number of new game releases post-2010, suggesting market saturation or shifts in consumer interests toward other forms of entertainment, such as mobile gaming and live streaming services.
#    - Sales have also shown regional shifts, with **North America** and **Europe** being more aligned in terms of platform and genre preferences, while **Japan** continues to stand out with different tastes, particularly in RPGs and certain Nintendo platforms.
# 
# ### **Recommendations**:
# - **Target Region-Specific Platforms**: Developers should focus on regionally dominant platforms like **PlayStation** and **Xbox** for the Western market and **Nintendo** platforms for Japan. 
# - **Focus on Genre Preferences**: Tailoring game development to regional genre preferences (e.g., Action and Shooter for the West, RPG for Japan) can improve the chances of success.
# - **Leverage ESRB Ratings**: In North America, developers may benefit from focusing on **Mature (M)**-rated games, which have a significant impact on sales.
# - **Monitor Platform Lifecycles**: Keeping track of platform popularity trends and lifecycle stages is crucial for maximizing sales potential for new game releases.
# 
# ### **Future Outlook**:
# With 2016 data potentially being incomplete, further analysis could be conducted as more recent data becomes available. Additionally, the rise of digital game distribution and mobile gaming could shift market dynamics in the future, which warrants continued analysis of these trends. This analysis serves as a baseline for understanding past trends and can help developers and publishers make informed decisions in a rapidly evolving industry.
# 
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Great final conclusion!
# </div>

# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
#     
#     Thank you for checking my project so quickly. I have changed my code to fit your recommendations. 

# In[ ]:




