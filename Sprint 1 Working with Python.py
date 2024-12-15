#!/usr/bin/env python
# coding: utf-8

# ## Basic Python - Project <a id='intro'></a>

# ## Introduction <a id='intro'></a>
# In this project, you will work with data from the entertainment industry. You will study a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of *The Sopranos* and is still ongoing.
# 
# The aim of this project is to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.
# 
# ### Stages 
# Data on movies and shows is stored in the `/datasets/movies_and_shows.csv` file. There is no information about the quality of the data, so you will need to explore it before doing the analysis.
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Data analysis

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open and explore the data.

# You'll need `pandas`, so import it.

# In[1]:


import pandas as pd # importing pandas


# Read the `movies_and_shows.csv` file from the `datasets` folder and save it in the `df` variable:

# In[2]:


df = pd.read_csv('/datasets/movies_and_shows.csv') # reading the files and storing them to df


# Print the first 10 table rows:

# In[3]:


df.head(10) # obtaining the first 10 rows from the df table
# hint: you can use head() and tail() in Jupyter Notebook without wrapping them into print()


# Obtain the general information about the table with one command:

# In[4]:


df.info() # obtaining general information about the data in df


# The table contains nine columns. The majority store the same data type: object. The only exceptions are `'release Year'` (int64 type), `'imdb sc0re'` (float64 type) and `'imdb v0tes'` (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns (`'TITLE'`, `'imdb sc0re'` and `'imdb v0tes'`) have missing values.
# 
# According to the documentation:
# - `'name'` — actor/director's name and last name
# - `'Character'` — character played (for actors)
# - `'r0le '` — the person's contribution to the title (it can be in the capacity of either actor or director)
# - `'TITLE '` — title of the movie (show)
# - `'  Type'` — show or movie
# - `'release Year'` — year when movie (show) was released
# - `'genres'` — list of genres under which the movie (show) falls
# - `'imdb sc0re'` — score on IMDb
# - `'imdb v0tes'` — votes on IMDb
# 
# We can see three issues with the column names:
# 1. Some names are uppercase, while others are lowercase.
# 2. There are names containing whitespace.
# 3. A few column names have digit '0' instead of letter 'o'. 
# 

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data about a movie or show. The columns can be divided into two categories: the first is about the roles held by different people who worked on the movie or show (role, name of the actor or director, and character if the row is about an actor); the second category is information about the movie or show itself (title, release year, genre, imdb figures).
# 
# It's clear that there is sufficient data to do the analysis and evaluate our assumption. However, to move forward, we need to preprocess the data.

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# In[5]:


column_names = [
    'name', 
'Character', 
'r0le ', 
'TITLE ', 
'  Type', 
'release Year', 
'genres', 
'imdb sc0re', 
'imdb v0tes'
]

print(column_names)


# Change the column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Remove whitespace
# * Replace zero with letter 'o'

# In[6]:


def convert_to_good_style(column_names):
    new_column_names = []
    for column_name in column_names:
        # Convert to lowercase
        column_name = column_name.lower()
        column_name = column_name.strip() 
         # Replace " " with "_"      
        column_name = column_name.replace(" ", "_")
        # Replace '0' with 'o'
        column_name = column_name.replace('0', 'o')
        new_column_names.append(column_name)
    return new_column_names

# Convert column names to good style
good_style_column_names = convert_to_good_style(column_names) # renaming columns


# In[7]:


df.columns = good_style_column_names


# Check the result. Print the names of the columns once more:

# In[8]:


df.head() # checking result: the list of column names


# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, combine two `pandas` methods:

# In[9]:


missing_values = df.isnull().sum() # calculating missing values
print(missing_values)


# Not all missing values affect the research: the single missing value in `'title'` is not critical. The missing values in columns `'imdb_score'` and `'imdb_votes'` represent around 6% of all records (4,609 and 4,726, respectively, of the total 85,579). This could potentially affect our research. To avoid this issue, we will drop rows with missing values in the `'imdb_score'` and `'imdb_votes'` columns.

# In[10]:


# Dropping rows where 'TITLE', 'imdb score', or 'imdb votes' have missing values
df_cleaned = df.dropna(subset=['title', 'imdb_score', 'imdb_votes'])

# Resetting the index
df_cleaned = df_cleaned.reset_index(drop=True)

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df_cleaned)


# Make sure the table doesn't contain any more missing values. Count the missing values again.

# In[11]:


missing_values_after_drop = df.isnull().sum() # counting missing values

print(missing_values_after_drop)


# ### Duplicates <a id='duplicates'></a>
# Find the number of duplicate rows in the table using one command:

# In[12]:


num_duplicates = df.duplicated().sum() # counting duplicate rows

print(num_duplicates)


# Review the duplicate rows to determine if removing them would distort our dataset.

# In[13]:


duplicates_df = df[df.duplicated(keep=False)]
print(duplicates_df.tail()) # Produce table with duplicates (with original rows included) and review last 5 rows


# There are two clear duplicates in the printed rows. We can safely remove them.
# Call the `pandas` method for getting rid of duplicate rows:

# In[14]:


df = df.drop_duplicates() # removing duplicate rows


# Check for duplicate rows once more to make sure you have removed all of them:

# In[15]:


duplicate_rows = df[df.duplicated()] # checking for duplicates

num_duplicates = duplicate_rows.shape[0]
print(f"Number of duplicate rows: {num_duplicates}")


# Now get rid of implicit duplicates in the `'type'` column. For example, the string `'SHOW'` can be written in different ways. These kinds of errors will also affect the result.

# Print a list of unique `'type'` names, sorted in alphabetical order. To do so:
# * Retrieve the intended dataframe column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# In[16]:


df_cleaned.head()


# In[17]:


# Extract the 'Type' column
type_column = df_cleaned['type']

# Apply a sorting method to the 'Type' column
sorted_type_column = type_column.sort_values()

# Call the unique method on the sorted column to get all unique values
unique_types = sorted_type_column.unique()

# Print the list of unique 'Type' names sorted in alphabetical order
print("\nUnique 'Type' names sorted in alphabetical order:")
print(unique_types)


# Look through the list to find implicit duplicates of `'show'` (`'movie'` duplicates will be ignored since the assumption is about shows). These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `'shows'`
# * `'SHOW'`
# * `'tv show'`
# * `'tv shows'`
# * `'tv series'`
# * `'tv'`
# 
# To get rid of them, declare the function `replace_wrong_show()` with two parameters: 
# * `wrong_shows_list=` — the list of duplicates
# * `correct_show=` — the string with the correct value
# 
# The function should correct the names in the `'type'` column from the `df` table (i.e., replace each value from the `wrong_shows_list` list with the value in `correct_show`).

# In[18]:


data = ['MOVIE', 'SHOW', 'movies', 'shows', 'the movie', 'tv', 'tv series', 'tv show',
 'tv shows']

# Create the DataFrame
df = pd.DataFrame(data, columns=['type'])
print("Original DataFrame:")
print(df)

# Define the function
def replace_wrong_show(df, wrong_shows_list, correct_show):
    # Ensure the 'type' column exists
    if 'type' in df.columns:
        # Iterate through the list of wrong show names and replace them in the 'type' column
        for wrong_show in wrong_shows_list:
            df['type'] = df['type'].replace(wrong_show, correct_show)
   
    return df

# Define the list of wrong show names and the correct show name
wrong_shows_list = ['shows', 'SHOW', 'tv show', 'tv shows', 'tv series', 'tv']
correct_show = 'show'

# Apply the function to the DataFrame
df = replace_wrong_show(df, wrong_shows_list, correct_show)
print("\nDataFrame after replacing wrong show names:")
print(df)

# To verify, get unique 'type' names sorted in alphabetical order
unique_types = sorted(df['type'].unique())
print("\nUnique 'Type' names sorted in alphabetical order:")
print(unique_types)


# Call `replace_wrong_show()` and pass it arguments so that it clears implicit duplicates and replaces them with `SHOW`:

# In[19]:


# Call the function to replace wrong show names
df = replace_wrong_show(df, wrong_shows_list, correct_show)
print("\nDataFrame after correction:")
print(df)# removing implicit duplicates


# Make sure the duplicate names are removed. Print the list of unique values from the `'type'` column:

# In[20]:


# Print the list of unique values from the 'type' column
unique_types = df['type'].unique()
print("\nUnique 'type' values:")
print(unique_types)


# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Duplicate rows and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All rows with missing values have been removed. 
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to our analysis of the prepared data.

# ## Stage 3. Data analysis <a id='hypotheses'></a>

# Based on the previous project stages, you can now define how the assumption will be checked. Calculate the average amount of votes for each score (this data is available in the `imdb_score` and `imdb_votes` columns), and then check how these averages relate to each other. If the averages for shows with the highest scores are bigger than those for shows with lower scores, the assumption appears to be true.
# 
# Based on this, complete the following steps:
# 
# - Filter the dataframe to only include shows released in 1999 or later.
# - Group scores into buckets by rounding the values of the appropriate column (a set of 1-10 integers will help us make the outcome of our calculations more evident without damaging the quality of our research).
# - Identify outliers among scores based on their number of votes, and exclude scores with few votes.
# - Calculate the average votes for each score and check whether the assumption matches the results.

# To filter the dataframe and only include shows released in 1999 or later, you will take two steps. First, keep only titles published in 1999 or later in our dataframe. Then, filter the table to only contain shows (movies will be removed).

# In[21]:


print(df.head)


# In[22]:


# Step 1: Filter titles released in 1999 or later
filtered_df = df_cleaned[df_cleaned['release_year'] >= 1999]

# Step 2: Filter out rows with 'MOVIE' in the 'type' column
filtered_df = filtered_df[filtered_df['type'] == 'SHOW']

print(filtered_df)


# In[23]:


## Step 3: Group scores into buckets by rounding the values to integers from 1 to 10

# Ensure the 'imdb_score' column is of numeric type
filtered_df['imdb_score'] = pd.to_numeric(filtered_df['imdb_score'], errors='coerce')

# Create a new column 'score_bucket' with rounded imdb scores
filtered_df['score_bucket'] = filtered_df['imdb_score'].round().astype(int)

# Display the DataFrame with the new 'score_bucket' column
print(filtered_df[['title', 'release_year', 'imdb_score', 'score_bucket', 'imdb_votes']])


# The scores that are to be grouped should be rounded. For instance, titles with scores like 7.8, 8.1, and 8.3 will all be placed in the same bucket with a score of 8.

# In[24]:


# Group scores into buckets by rounding the values to integers from 1 to 10
filtered_df['score_bucket'] = filtered_df['imdb_score'].round().astype(int)

# Display the DataFrame with the new 'score_bucket' column
print(filtered_df[['title', 'release_year', 'imdb_score', 'score_bucket', 'imdb_votes']])


# It is now time to identify outliers based on the number of votes.

# In[25]:


# Group by 'score_bucket' and count all unique values in each group
grouped_counts = filtered_df.groupby('score_bucket').size().reset_index(name='count')

# Display the grouped counts
print(grouped_counts)


# Based on the aggregation performed, it is evident that scores 2 (24 voted shows), 3 (27 voted shows), and 10 (only 8 voted shows) are outliers. There isn't enough data for these scores for the average number of votes to be meaningful.

# To obtain the mean numbers of votes for the selected scores (we identified a range of 4-9 as acceptable), use conditional filtering and grouping.

# In[26]:


# Filter dataframe to include only scores in the range 4-9
filtered_df = filtered_df[(filtered_df['score_bucket'] >= 4) & (filtered_df['score_bucket'] <= 9)]

# Group by 'score_bucket' and calculate the mean number of votes for each bucket
grouped_df = filtered_df.groupby('score_bucket')['imdb_votes'].mean().reset_index()

# Print the result
print(grouped_df)


# Now for the final step! Round the column with the averages, rename both columns, and print the dataframe in descending order.

# In[27]:


# Round the average votes to 2 decimal places
grouped_df['imdb_votes'] = grouped_df['imdb_votes'].round(2)

# Rename the columns for clarity
grouped_df.columns = ['Score Bucket', 'Average Votes']

# Sort the DataFrame in descending order by the score bucket
sorted_df = grouped_df.sort_values(by='Score Bucket', ascending=False)

# Print the resulting DataFrame
print(sorted_df)


# The assumption macthes the analysis: the shows with the top 3 scores have the most amounts of votes.

# ## Conclusion <a id='hypotheses'></a>

# The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.
