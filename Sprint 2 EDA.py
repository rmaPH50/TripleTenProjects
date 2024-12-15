{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b0d96818",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\"> <h1 style=\"color:green; margin-bottom:20px\">Reviewer's comment v1</h1>\n",
    "\n",
    "Hello Robert!\n",
    "\n",
    "I'm happy to review your project today 🙌\n",
    "\n",
    "You can find my comments under the heading **«Review»**. I will categorize my comments in green, blue or red boxes like this:\n",
    "\n",
    "<div class=\"alert alert-success\">\n",
    "    <b>Success:</b> if everything is done successfully\n",
    "</div>\n",
    "<div class=\"alert alert-warning\">\n",
    "    <b>Remarks:</b> if I can give some recommendations or ways to improve the project\n",
    "</div>\n",
    "<div class=\"alert alert-danger\">\n",
    "    <b>Needs fixing:</b> if the block requires some corrections. Work can't be accepted with the red comments\n",
    "</div>\n",
    "\n",
    "Please don't remove my comments :) If you have any questions don't hesitate to respond to my comments in a different section. \n",
    "<div class=\"alert alert-info\"> <b>Student comments:</b> For example like this</div>    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3fbb2bb",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\">\n",
    "<b>Reviewer's comment v1:</b>\n",
    "\n",
    "    \n",
    "<b>Overall Feedback</b> \n",
    "    \n",
    "First and foremost, kudos on your progress so far! Your dedication and effort are evident in the work you've presented.\n",
    "\n",
    "However, there are a few areas, highlighted in red comments, that need some attention. Addressing these will undoubtedly elevate your project further.\n",
    "\n",
    "If you find yourself uncertain or in need of further insights, never hesitate to consult with your tutor or ask your questions here. We are here to guide and assist you.\n",
    "\n",
    "I will wait for you to send me a new version of the project :)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75b14507",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\">\n",
    "<b>Reviewer's comment v2:</b>\n",
    "\n",
    "Unfortunately, I did not notice any changes in the notebook.\n",
    "\n",
    "Could you please let your tutor (on Discord) or me know if my comments, theory or the project are not clear?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8db5569",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\">\n",
    "<b>Reviewer's comment v3:</b>\n",
    "    \n",
    "<b>Overall Feedback</b> \n",
    "    \n",
    "Thank you for the great improvements in your project.  I left an additional information regarding your comments. You could find them with the following title `Reviewer's comment v3`\n",
    "\n",
    "And of course, if you have any questions along the way, remember that you can always reach out to your tutor for any clarification.\n",
    "    \n",
    "\n",
    "I will wait for you to send me a new version of the project :)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f154cd4f",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\">\n",
    "<b>Reviewer's comment v4:</b>\n",
    "    \n",
    "<b>Overall Feedback</b> \n",
    "    \n",
    "Thank you for going an extra mile and making changes in your project.\n",
    "\n",
    "Now everything is perfect. No critial issues left, so your project has been accepted!\n",
    "    \n",
    "Wish you cool projects in the next sprints! ☘️   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d071984",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Reviewer's comment v1</b>\n",
    "    \n",
    "It would be immensely helpful if you can add some contextual information at the beginning of the notebook, covering:\n",
    "\n",
    "- A brief description of the project's objective.\n",
    "- An overview of the data you're working with.\n",
    "- Any expected outcomes or results you aim to achieve.\n",
    "\n",
    "Providing such context allows anyone reviewing or revisiting the notebook to quickly understand its purpose and the data being used, ensuring smoother collaboration and more intuitive navigation.\n",
    "\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72d13745",
   "metadata": {},
   "source": [
    "Project Objectives: clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers. \n",
    "Data Overview: Using instacart_orders.csv, products.csv, order_products.csv, aisles.csv and departments.csv contains lists of columns which need to processed. \n",
    "Preprocess the data by doing the following:\n",
    "\n",
    "Verify and fix data types (e.g. make sure ID columns are integers)\n",
    "Identify and fill in missing values\n",
    "Identify and remove duplicate values\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f52a72f",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v1</b>\n",
    "\n",
    "The import pandas as pd statement should be included only once at the beginning of your script. Importing a library multiple times is redundant and unnecessary.\n",
    "    \n",
    "Once the library is imported, you can use it throughout your script for various DataFrame operations.\n",
    "    \n",
    "This approach makes your code cleaner and avoids unnecessary repeated import statements.\n",
    "    \n",
    "Could you please remove all redundant library import in your notebook?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63d5bf57",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v2</b>\n",
    "\n",
    "Unfortunately, I did not notice any changes in the notebook. Could you please let me know if smth is not clear or you have any technical issues? # I tired doing this and then all of my code had failures. Should I input at the top of my code under my Project Objectives, or in the cells when needed? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7f379275",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_instacart_orders = pd.read_csv('/datasets/instacart_orders.csv', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "36a21d00",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_instacart_products = pd.read_csv('/datasets/products.csv', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bd972090",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_instacart_order_products = pd.read_csv('/datasets/order_products.csv', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6bdc8396",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_instacart_aisles= pd.read_csv('/datasets/aisles.csv', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "58379337",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_instacart_departments = pd.read_csv('/datasets/departments.csv', sep=';')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07357848-dc64-4156-9cc3-01ff4365226d",
   "metadata": {},
   "source": [
    "## Find and remove duplicate values (and describe why you make your choices)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f179f0a9",
   "metadata": {},
   "source": [
    "### `orders` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0d44de5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        order_id  user_id  order_number  order_dow  order_hour_of_day  \\\n",
      "4838     2766110   162084            41          3                  2   \n",
      "5156     2190225   138285            18          3                  2   \n",
      "15506     553049    58599            13          3                  2   \n",
      "18420     382357   120200            19          3                  2   \n",
      "24691     690242    77357             2          3                  2   \n",
      "...          ...      ...           ...        ...                ...   \n",
      "457013   3384021    14881             6          3                  2   \n",
      "458816    910166   164782            18          3                  2   \n",
      "459635   1680532   106435             6          3                  2   \n",
      "468324    222962    54979            59          3                  2   \n",
      "477526   2592344    46860            38          3                  2   \n",
      "\n",
      "        days_since_prior_order  \n",
      "4838                      16.0  \n",
      "5156                      11.0  \n",
      "15506                      7.0  \n",
      "18420                     11.0  \n",
      "24691                      9.0  \n",
      "...                        ...  \n",
      "457013                    30.0  \n",
      "458816                     4.0  \n",
      "459635                    21.0  \n",
      "468324                     3.0  \n",
      "477526                     3.0  \n",
      "\n",
      "[121 rows x 6 columns]\n"
     ]
    }
   ],
   "source": [
    "# Filter orders placed on Wednesday (order_dow = 3) at 2:00 AM (order_hour_of_day = 2)\n",
    "wednesday_2am_orders = df_instacart_orders[(df_instacart_orders['order_dow'] == 3) & (df_instacart_orders['order_hour_of_day'] == 2)]\n",
    "\n",
    "# Print the filtered DataFrame\n",
    "print(wednesday_2am_orders)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0319867e",
   "metadata": {},
   "source": [
    "Filter orders placed on Wednesday at 2:00 AM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b99297a5-405a-463d-8535-9adc3da4ad74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate rows before removal: 15\n",
      "Number of duplicate rows after removal: 0\n",
      "   order_id  user_id  order_number  order_dow  order_hour_of_day  \\\n",
      "0   1515936   183418            11          6                 13   \n",
      "1   1690866   163593             5          5                 12   \n",
      "2   1454967    39980             4          5                 19   \n",
      "3   1768857    82516            56          0                 20   \n",
      "4   3007858   196724             2          4                 12   \n",
      "\n",
      "   days_since_prior_order  \n",
      "0                    30.0  \n",
      "1                     9.0  \n",
      "2                     2.0  \n",
      "3                    10.0  \n",
      "4                    17.0  \n"
     ]
    }
   ],
   "source": [
    "df_instacart_orders\n",
    "\n",
    "# Check for duplicated rows\n",
    "print(\"Number of duplicate rows before removal:\", df_instacart_orders.duplicated().sum())\n",
    "\n",
    "# Remove duplicate rows\n",
    "df_instacart_orders = df_instacart_orders.drop_duplicates().reset_index(drop=True) # Added .reset_index(drop=True)\n",
    "\n",
    "# Check again for duplicates after removal\n",
    "print(\"Number of duplicate rows after removal:\", df_instacart_orders.duplicated().sum())\n",
    "\n",
    "# Print the first few rows of the cleaned DataFrame\n",
    "print(df_instacart_orders.head())\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b73261b1",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Reviewer's comment v1</b>\n",
    "\n",
    "This code removes the duplicate rows from the instacart DataFrame.\n",
    "However it doesn't reset the index of the DataFrame. This means that if rows were removed, there could be gaps in the DataFrame's index.\n",
    "\n",
    "In many cases, especially when the index doesn't have any specific meaning, resetting the index after dropping duplicates provides a cleaner result. You can achieve that in the following way: \n",
    "\n",
    "`orders.drop_duplicates().reset_index(drop=True)`\n",
    "\n",
    "The `reset_index(drop=True)` method is then called on the result, which resets the DataFrame's index and drops the old index. This ensures there are no gaps in the index after removing duplicates.\n",
    "    \n",
    "   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60dfb20b",
   "metadata": {},
   "source": [
    "I checked for duplicated rows using df_instacart_orders.duplicated().sum() to understand the extent of duplicate entries.\n",
    "I used df_instacart_orders.drop_duplicates() to remove duplicate rows based on all columns by default.\n",
    "I verified the removal of duplicates again using df_instacart_orders.duplicated().sum() to ensure no duplicates remain.\n",
    "reset the index & finally, I printed the first few rows of the cleaned DataFrame to inspect the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "480563c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate rows after removal: 0\n",
      "   order_id  user_id  order_number  order_dow  order_hour_of_day  \\\n",
      "0   1515936   183418            11          6                 13   \n",
      "1   1690866   163593             5          5                 12   \n",
      "2   1454967    39980             4          5                 19   \n",
      "3   1768857    82516            56          0                 20   \n",
      "4   3007858   196724             2          4                 12   \n",
      "\n",
      "   days_since_prior_order  \n",
      "0                    30.0  \n",
      "1                     9.0  \n",
      "2                     2.0  \n",
      "3                    10.0  \n",
      "4                    17.0  \n"
     ]
    }
   ],
   "source": [
    "# Remove duplicate rows\n",
    "df_instacart_orders = df_instacart_orders.drop_duplicates()\n",
    "\n",
    "# Check again for duplicates after removal\n",
    "print(\"Number of duplicate rows after removal:\", df_instacart_orders.duplicated().sum())\n",
    "\n",
    "# Print the first few rows of the cleaned DataFrame\n",
    "print(df_instacart_orders.head()) # Remove duplicate orders\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0b2396a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate rows: 0\n",
      "No duplicated rows found.\n"
     ]
    }
   ],
   "source": [
    "# Check for duplicate rows\n",
    "duplicates = df_instacart_orders[df_instacart_orders.duplicated()]\n",
    "\n",
    "# Print the number of duplicate rows\n",
    "print(\"Number of duplicate rows:\", len(duplicates))\n",
    "\n",
    "# Print the duplicated rows for inspection\n",
    "if len(duplicates) > 0:\n",
    "    print(\"Duplicated rows:\")\n",
    "    print(duplicates)\n",
    "else:\n",
    "    print(\"No duplicated rows found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f6113ef1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate order IDs: 0\n",
      "No duplicated order IDs found.\n"
     ]
    }
   ],
   "source": [
    "# Check for duplicate order IDs\n",
    "duplicates_order_id = df_instacart_orders[df_instacart_orders.duplicated(subset=['order_id'], keep=False)]\n",
    "\n",
    "# Print the number of duplicate order IDs\n",
    "print(\"Number of duplicate order IDs:\", len(duplicates_order_id))\n",
    "\n",
    "# Print the duplicated order IDs for inspection\n",
    "if len(duplicates_order_id) > 0:\n",
    "    print(\"Duplicated order IDs:\")\n",
    "    print(duplicates_order_id[['order_id']])\n",
    "else:\n",
    "    print(\"No duplicated order IDs found.\") # Double check for duplicate order IDs only\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e8905ae",
   "metadata": {},
   "source": [
    "Checked for duplicate rows and order id using duplicated() and print using if else. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45e6bc46",
   "metadata": {},
   "source": [
    "### `products` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5f526b5b-8175-46fa-a0fd-441767d50e64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of fully duplicate rows before removal: 0\n",
      "Number of fully duplicate rows after removal: 0\n",
      "   product_id                                       product_name  aisle_id  \\\n",
      "0           1                         Chocolate Sandwich Cookies        61   \n",
      "1           2                                   All-Seasons Salt       104   \n",
      "2           3               Robust Golden Unsweetened Oolong Tea        94   \n",
      "3           4  Smart Ones Classic Favorites Mini Rigatoni Wit...        38   \n",
      "4           5                          Green Chile Anytime Sauce         5   \n",
      "\n",
      "   department_id  \n",
      "0             19  \n",
      "1             13  \n",
      "2              7  \n",
      "3              1  \n",
      "4             13  \n"
     ]
    }
   ],
   "source": [
    "df_instacart_products \n",
    "\n",
    "# Check for fully duplicate rows\n",
    "print(\"Number of fully duplicate rows before removal:\", df_instacart_products.duplicated().sum())\n",
    "\n",
    "# Remove fully duplicate rows\n",
    "df_instacart_products = df_instacart_products.drop_duplicates()\n",
    "\n",
    "# Check again for fully duplicate rows after removal\n",
    "print(\"Number of fully duplicate rows after removal:\", df_instacart_products.duplicated().sum())\n",
    "\n",
    "# Print the first few rows of the cleaned DataFrame\n",
    "print(df_instacart_products.head()) # Check for fully duplicate rows\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "88daa4f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate product IDs: 0\n",
      "No duplicated product IDs found.\n"
     ]
    }
   ],
   "source": [
    "# Check for duplicate product IDs\n",
    "duplicates_product_id = df_instacart_products[df_instacart_products.duplicated(subset=['product_id'], keep=False)]\n",
    "\n",
    "# Print the number of duplicate product IDs\n",
    "print(\"Number of duplicate product IDs:\", len(duplicates_product_id))\n",
    "\n",
    "# Print the duplicated product IDs for inspection\n",
    "if len(duplicates_product_id) > 0:\n",
    "    print(\"Duplicated product IDs:\")\n",
    "    print(duplicates_product_id[['product_id']])\n",
    "else:\n",
    "    print(\"No duplicated product IDs found.\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c773f0bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate product names: 1465\n",
      "Duplicated product names:\n",
      "                                          product_name\n",
      "37                                                 NaN\n",
      "41                                     Biotin 1000 mcg\n",
      "71                                                 NaN\n",
      "109                                                NaN\n",
      "185         Fresh Scent Dishwasher Detergent with Dawn\n",
      "...                                                ...\n",
      "49689                    HIGH PERFORMANCE ENERGY DRINK\n",
      "49690                    ORIGINAL PANCAKE & WAFFLE MIX\n",
      "49691  ORGANIC INSTANT OATMEAL LIGHT MAPLE BROWN SUGAR\n",
      "49692                           SPRING WATER BODY WASH\n",
      "49693                          BURRITO- STEAK & CHEESE\n",
      "\n",
      "[1465 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "# Convert product names to lowercase\n",
    "df_instacart_products['product_name_lower'] = df_instacart_products['product_name'].str.lower()\n",
    "\n",
    "# Check for duplicate product names\n",
    "duplicates_product_name = df_instacart_products[df_instacart_products.duplicated(subset=['product_name_lower'], keep=False)]\n",
    "\n",
    "# Print the number of duplicate product names\n",
    "print(\"Number of duplicate product names:\", len(duplicates_product_name))\n",
    "\n",
    "# Print the duplicated product names for inspection\n",
    "if len(duplicates_product_name) > 0:\n",
    "    print(\"Duplicated product names:\")\n",
    "    print(duplicates_product_name[['product_name']])\n",
    "else:\n",
    "    print(\"No duplicated product names found.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "01efd02e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate product names (not missing): 207\n",
      "Duplicated product names (not missing):\n",
      "                                          product_name\n",
      "41                                     Biotin 1000 mcg\n",
      "185         Fresh Scent Dishwasher Detergent with Dawn\n",
      "515                             American Cheese Slices\n",
      "1538                                  Cauliflower head\n",
      "1783               NUTrition Protein Mix Blueberry Nut\n",
      "...                                                ...\n",
      "49689                    HIGH PERFORMANCE ENERGY DRINK\n",
      "49690                    ORIGINAL PANCAKE & WAFFLE MIX\n",
      "49691  ORGANIC INSTANT OATMEAL LIGHT MAPLE BROWN SUGAR\n",
      "49692                           SPRING WATER BODY WASH\n",
      "49693                          BURRITO- STEAK & CHEESE\n",
      "\n",
      "[207 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "# Check for duplicates only where product names are not missing\n",
    "not_missing = df_instacart_products['product_name'].notna()\n",
    "duplicates_product_name = df_instacart_products[not_missing & df_instacart_products.duplicated(subset=['product_name_lower'], keep=False)]\n",
    "\n",
    "# Print the number of duplicate product names that are not missing\n",
    "print(\"Number of duplicate product names (not missing):\", len(duplicates_product_name))\n",
    "\n",
    "# Print the duplicated product names for inspection\n",
    "if len(duplicates_product_name) > 0:\n",
    "    print(\"Duplicated product names (not missing):\")\n",
    "    print(duplicates_product_name[['product_name']])\n",
    "else:\n",
    "    print(\"No duplicated product names (not missing) found.\") \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9da8d293",
   "metadata": {},
   "source": [
    "Check for duplicates only where product names are not missing, ame'].notna(), and set to lower case. Printed duplicated product names for inspection using if else. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60f30db1",
   "metadata": {},
   "source": [
    "### `departments` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "332b12bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "bd30d78e",
   "metadata": {},
   "source": [
    "read csv departments and definiee df_instacart_departments. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "889349c1",
   "metadata": {},
   "source": [
    "### `aisles` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da7c2822",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "ac63826f",
   "metadata": {},
   "source": [
    "read csv aisles and defined df_instacart_aisles "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "274cd06a",
   "metadata": {},
   "source": [
    "### `order_products` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "52326689-84a8-4b8f-a881-7c68780f62c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of fully duplicate rows: 0\n",
      "No fully duplicated rows found.\n"
     ]
    }
   ],
   "source": [
    "df_instacart_order_products \n",
    "\n",
    "# Check for fully duplicate rows\n",
    "duplicates = df_instacart_order_products[df_instacart_order_products.duplicated()]\n",
    "\n",
    "# Print the number of fully duplicate rows\n",
    "print(\"Number of fully duplicate rows:\", len(duplicates))\n",
    "\n",
    "# Print the fully duplicated rows for inspection\n",
    "if len(duplicates) > 0:\n",
    "    print(\"Duplicated rows:\")\n",
    "    print(duplicates)\n",
    "else:\n",
    "    print(\"No fully duplicated rows found.\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7b861391",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of fully duplicate rows: 0\n",
      "No fully duplicated rows found.\n",
      "\n",
      "Number of duplicates based on specific columns (e.g., order_id and product_id): 0\n",
      "No duplicates based on specific columns found.\n"
     ]
    }
   ],
   "source": [
    "# Check for fully duplicate rows\n",
    "duplicates_full = df_instacart_order_products[df_instacart_order_products.duplicated()]\n",
    "\n",
    "# Check for duplicates based on specific columns or combinations\n",
    "# For example, check based on 'order_id' and 'product_id' combination\n",
    "duplicates_specific = df_instacart_order_products[df_instacart_order_products.duplicated(subset=['order_id', 'product_id'], keep=False)]\n",
    "\n",
    "# Print the number of fully duplicate rows\n",
    "print(\"Number of fully duplicate rows:\", len(duplicates_full))\n",
    "\n",
    "# Print the fully duplicated rows for inspection\n",
    "if len(duplicates_full) > 0:\n",
    "    print(\"Fully duplicated rows:\")\n",
    "    print(duplicates_full)\n",
    "else:\n",
    "    print(\"No fully duplicated rows found.\")\n",
    "\n",
    "# Print the number of duplicates based on specific columns\n",
    "print(\"\\nNumber of duplicates based on specific columns (e.g., order_id and product_id):\", len(duplicates_specific))\n",
    "\n",
    "# Print the duplicated rows based on specific columns for inspection\n",
    "if len(duplicates_specific) > 0:\n",
    "    print(\"Duplicated rows based on specific columns:\")\n",
    "    print(duplicates_specific)\n",
    "else:\n",
    "    print(\"No duplicates based on specific columns found.\") # Double check for any other tricky duplicates\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b890492",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v1</b>\n",
    "\n",
    "You've done a good job at checking duplicates in the table."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e46de76",
   "metadata": {},
   "source": [
    "## Find and remove missing values\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0aebd78",
   "metadata": {},
   "source": [
    "### `products` data frame"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "529755ca",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v1</b>\n",
    "\n",
    "Reading the same CSV file multiple times is unnecessary and can significantly slow down your notebook, especially with large files.\n",
    "Load the CSV file once into a DataFrame (e.g. `df_instacart_products`) at the beggining of the notebook and reuse this DataFrame throughout your notebook.\n",
    "This practice improves the efficiency of your code, reducing the time spent on I/O operations and making your notebook more readable and maintainable.\n",
    "    \n",
    "Could you please remove duplicate data imports in this notebook and utilize the same file that has been loaded in the first step? \n",
    "    \n",
    "    \n",
    "The rest of the project could be only checked afterwards, as by overwriting data in every task you are using data with missing values and duplicates. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e96167bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Are all missing product names associated with aisle ID 100? True\n",
      "Rows with missing product names:\n",
      "       product_id product_name  aisle_id  department_id product_name_lower\n",
      "37             38          NaN       100             21                NaN\n",
      "71             72          NaN       100             21                NaN\n",
      "109           110          NaN       100             21                NaN\n",
      "296           297          NaN       100             21                NaN\n",
      "416           417          NaN       100             21                NaN\n",
      "...           ...          ...       ...            ...                ...\n",
      "49552       49553          NaN       100             21                NaN\n",
      "49574       49575          NaN       100             21                NaN\n",
      "49640       49641          NaN       100             21                NaN\n",
      "49663       49664          NaN       100             21                NaN\n",
      "49668       49669          NaN       100             21                NaN\n",
      "\n",
      "[1258 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "# Filter rows where the product name is missing (NaN)\n",
    "missing_product_names = df_instacart_products[df_instacart_products['product_name'].isna()]\n",
    "\n",
    "# Check if all missing product names are associated with aisle ID 100\n",
    "all_missing_associated_with_aisle_100 = missing_product_names['aisle_id'].eq(100).all()\n",
    "\n",
    "# Print the result\n",
    "print(\"Are all missing product names associated with aisle ID 100?\", all_missing_associated_with_aisle_100)\n",
    "\n",
    "# Are all of the missing product names associated with aisle ID 100?\n",
    "# Optionally, print the rows with missing product names for inspection\n",
    "print(\"Rows with missing product names:\")\n",
    "print(missing_product_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8fd0a541",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Are all missing product names associated with department ID 21? True\n",
      "Rows with missing product names:\n",
      "       product_id product_name  aisle_id  department_id product_name_lower\n",
      "37             38          NaN       100             21                NaN\n",
      "71             72          NaN       100             21                NaN\n",
      "109           110          NaN       100             21                NaN\n",
      "296           297          NaN       100             21                NaN\n",
      "416           417          NaN       100             21                NaN\n",
      "...           ...          ...       ...            ...                ...\n",
      "49552       49553          NaN       100             21                NaN\n",
      "49574       49575          NaN       100             21                NaN\n",
      "49640       49641          NaN       100             21                NaN\n",
      "49663       49664          NaN       100             21                NaN\n",
      "49668       49669          NaN       100             21                NaN\n",
      "\n",
      "[1258 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "# Check if all missing product names are associated with department ID 21\n",
    "all_missing_associated_with_department_21 = missing_product_names['department_id'].eq(21).all()\n",
    "\n",
    "# Print the result\n",
    "print(\"Are all missing product names associated with department ID 21?\", all_missing_associated_with_department_21)\n",
    "\n",
    "# Are all of the missing product names associated with department ID 21?\n",
    "# Optionally, print the rows with missing product names for inspection\n",
    "print(\"Rows with missing product names:\")\n",
    "print(missing_product_names)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "325c3464",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Aisle ID 100 corresponds to: missing\n",
      "Department ID 21 corresponds to: missing\n"
     ]
    }
   ],
   "source": [
    "# Load the datasets\n",
    "df_instacart_aisles \n",
    "df_instacart_departments\n",
    "df_instacart_products \n",
    "\n",
    "# Identify the aisle and department names for the specified IDs\n",
    "aisle_id = 100\n",
    "department_id = 21\n",
    "\n",
    "aisle_name = df_instacart_aisles.loc[df_instacart_aisles['aisle_id'] == aisle_id, 'aisle'].values[0]\n",
    "department_name = df_instacart_departments.loc[df_instacart_departments['department_id'] == department_id, 'department'].values[0]\n",
    "\n",
    "print(f\"\\nAisle ID {aisle_id} corresponds to: {aisle_name}\")\n",
    "print(f\"Department ID {department_id} corresponds to: {department_name}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6b295120",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   product_id                                       product_name  aisle_id  \\\n",
      "0           1                         Chocolate Sandwich Cookies        61   \n",
      "1           2                                   All-Seasons Salt       104   \n",
      "2           3               Robust Golden Unsweetened Oolong Tea        94   \n",
      "3           4  Smart Ones Classic Favorites Mini Rigatoni Wit...        38   \n",
      "4           5                          Green Chile Anytime Sauce         5   \n",
      "\n",
      "   department_id                                 product_name_lower  \n",
      "0             19                         chocolate sandwich cookies  \n",
      "1             13                                   all-seasons salt  \n",
      "2              7               robust golden unsweetened oolong tea  \n",
      "3              1  smart ones classic favorites mini rigatoni wit...  \n",
      "4             13                          green chile anytime sauce  \n",
      "\n",
      "Number of missing product names after fillna: 0\n"
     ]
    }
   ],
   "source": [
    "# Fill missing product names with 'Unknown'\n",
    "df_instacart_products['product_name'].fillna('Unknown', inplace=True)\n",
    "\n",
    "# Verify the result by printing the DataFrame\n",
    "print(df_instacart_products.head())\n",
    "print(\"\\nNumber of missing product names after fillna:\", df_instacart_products['product_name'].isna().sum())# Fill missing product names with 'Unknown'\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc70e5ad",
   "metadata": {},
   "source": [
    "Found and removed missing values associated with aisle_id 100 and user_id 21. filled missing data names with unkown using .filna() "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7eb45c86",
   "metadata": {},
   "source": [
    "### `orders` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "166e5a86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of missing 'days_since_prior_order' values where it's not the customer's first order: 0\n"
     ]
    }
   ],
   "source": [
    "df_instacart_orders \n",
    "# Filter rows where it's not the customer's first order and check for missing values in 'days_since_prior_order'\n",
    "missing_not_first_order = df_instacart_orders[(df_instacart_orders['order_number'] > 1) & (df_instacart_orders['days_since_prior_order'].isna())]\n",
    "\n",
    "# Check if there are any missing values\n",
    "missing_count = len(missing_not_first_order)\n",
    "\n",
    "print(\"Number of missing 'days_since_prior_order' values where it's not the customer's first order:\", missing_count)\n",
    "# Are there any missing values where it's not a customer's first order?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e23d089",
   "metadata": {},
   "source": [
    "Filter rows where it's not the customer's first order and check for missing values in 'days_since_prior_order'\n",
    "Check if there are any missing values\n",
    "Are there any missing values where it's not a customer's first order? Print "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69dc9ca4",
   "metadata": {},
   "source": [
    "### `order_products` data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9a78e5ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum value in 'days_since_prior_order': 0.0\n",
      "Maximum value in 'days_since_prior_order': 30.0\n"
     ]
    }
   ],
   "source": [
    "df_instacart_order_products \n",
    "# Drop any NaN values to correctly calculate min and max\n",
    "days_since_prior_order_cleaned = df_instacart_orders['days_since_prior_order'].dropna()\n",
    "\n",
    "# Find the minimum and maximum values\n",
    "min_value = days_since_prior_order_cleaned.min()\n",
    "max_value = days_since_prior_order_cleaned.max()\n",
    "\n",
    "print(\"Minimum value in 'days_since_prior_order':\", min_value)\n",
    "print(\"Maximum value in 'days_since_prior_order':\", max_value)# What are the min and max values in this column?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ab9d0c2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Order IDs with missing 'add_to_cart_order' values:\n",
      "    order_id\n",
      "0    2449164\n",
      "1    1968313\n",
      "2    2926893\n",
      "3    1717990\n",
      "4    1959075\n",
      "..       ...\n",
      "65      9310\n",
      "66   2170451\n",
      "67   2979697\n",
      "68   1625713\n",
      "69   1529171\n",
      "\n",
      "[70 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "# Find order IDs with at least one missing value in 'add_to_cart_order'\n",
    "order_ids_with_missing_add_to_cart_order = df_instacart_order_products[df_instacart_order_products['add_to_cart_order'].isna()]['order_id'].unique()\n",
    "\n",
    "# Convert the result to a DataFrame\n",
    "df_order_ids_with_missing = pd.DataFrame(order_ids_with_missing_add_to_cart_order, columns=['order_id'])\n",
    "\n",
    "# Print the result\n",
    "print(\"Order IDs with missing 'add_to_cart_order' values:\")\n",
    "print(df_order_ids_with_missing)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "54c31695",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All orders with missing 'add_to_cart_order' values have more than 64 products.\n"
     ]
    }
   ],
   "source": [
    "# Find order IDs with at least one missing value in 'add_to_cart_order'\n",
    "order_ids_with_missing_add_to_cart_order = df_instacart_order_products[df_instacart_order_products['add_to_cart_order'].isna()]['order_id'].unique()\n",
    "\n",
    "# Filter order products for orders with missing 'add_to_cart_order' values\n",
    "missing_orders_products = df_instacart_order_products[df_instacart_order_products['order_id'].isin(order_ids_with_missing_add_to_cart_order)]\n",
    "\n",
    "# Group by order_id and count the number of products per order\n",
    "product_counts_per_order = missing_orders_products.groupby('order_id')['product_id'].count()\n",
    "\n",
    "# Check if all orders with missing 'add_to_cart_order' values have more than 64 products\n",
    "all_missing_orders_more_than_64 = all(product_counts_per_order > 64)\n",
    "\n",
    "if all_missing_orders_more_than_64:\n",
    "    print(\"All orders with missing 'add_to_cart_order' values have more than 64 products.\")\n",
    "else:\n",
    "    print(\"Not all orders with missing 'add_to_cart_order' values have more than 64 products.\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7a987d08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   order_id  product_id  add_to_cart_order  reordered\n",
      "0   2141543       11440                 17          0\n",
      "1    567889        1560                  1          1\n",
      "2   2261212       26683                  1          1\n",
      "3    491251        8670                 35          1\n",
      "4   2571142        1940                  5          1\n",
      "5   2456893       21616                  4          1\n",
      "6    644579       12341                  5          1\n",
      "7   2231852       44925                 10          1\n",
      "8   3185766       36259                 14          1\n",
      "9    420019       23315                  4          1\n"
     ]
    }
   ],
   "source": [
    "# Replace missing values with 999 in 'add_to_cart_order'\n",
    "df_instacart_order_products['add_to_cart_order'].fillna(999, inplace=True)\n",
    "\n",
    "# Convert 'add_to_cart_order' column to integer type\n",
    "df_instacart_order_products['add_to_cart_order'] = df_instacart_order_products['add_to_cart_order'].astype(int)\n",
    "\n",
    "# Print the first few rows to verify\n",
    "print(df_instacart_order_products.head(10)) # Replace missing values with 999 and convert column to integer type\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fea4bcc7",
   "metadata": {},
   "source": [
    "Replace missing values with 999 in 'add_to_cart_order' .fillna(999, inplace=True)\n",
    "Convert 'add_to_cart_order' column to integer .astype(int) \n",
    "rint the first few rows to verify"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3fb6ee47",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "Overall, your exploration and cleaning process is well-thought-out. \n",
    "\n",
    "You correctly identified and addressed NaN values in `product_name`, `days_since_prior_order`, `add_to_cart_order`. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "869369b9",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "If you're repeating the same set of operations (like checking info, printing the head, checking for NaNs, and checking for duplicates) for each dataframe, consider creating a function to perform these checks. This will make your code cleaner and more efficient.\n",
    "\n",
    "````\n",
    "def analyze_data(df):\n",
    "    # Info\n",
    "    print(df.info())\n",
    "    \n",
    "    # First few rows\n",
    "    print(df.head())\n",
    "    \n",
    "    # Missing values\n",
    "    print(df.isna().sum())\n",
    "    \n",
    "    # Duplicates\n",
    "    print(df.duplicated().sum())\n",
    "\n",
    "# Use the function\n",
    "analyze_data(aisles)\n",
    "analyze_data(departments)\n",
    "# ... and so on for other dataframes\n",
    "````"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "turkish-kidney",
   "metadata": {},
   "source": [
    "# [A] Easy (must complete all to pass)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "short-capability",
   "metadata": {},
   "source": [
    "### [A1] Verify that the `'order_hour_of_day'` and `'order_dow'` values in the `orders` tables are sensible (i.e. `'order_hour_of_day'` ranges from 0 to 23 and `'order_dow'` ranges from 0 to 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "accessory-malaysia",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Order Hour of Day Range Valid: True\n",
      "Order Day of Week Range Valid: True\n"
     ]
    }
   ],
   "source": [
    "df_instacart_orders\n",
    "# Check 'order_hour_of_day' range\n",
    "hour_range_valid = df_instacart_orders['order_hour_of_day'].between(0, 23).all()\n",
    "\n",
    "# Check 'order_dow' range\n",
    "dow_range_valid = df_instacart_orders['order_dow'].between(0, 6).all()\n",
    "\n",
    "# Print the validation results\n",
    "print(f\"Order Hour of Day Range Valid: {hour_range_valid}\")\n",
    "print(f\"Order Day of Week Range Valid: {dow_range_valid}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d75d9f74",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "As a second approach you could use `.describe()` function for getting an initial understanding of data, especially for numeric columns. However, this function might return descriptive statistics for all numeric columns in the dataframe. If you are interested in specific columns, you might want to narrow it down.\n",
    "\n",
    "`instacart[['order_hour_of_day', 'order_dow']].describe()`\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6743a70",
   "metadata": {},
   "source": [
    "### [A2] What time of day do people shop for groceries?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a36cca27",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAACWg0lEQVR4nOzdeVxU9f7H8feZQRZRRFE0xRS1cklxzWi1NNG83SzrtliZWf3q4i21m0u3LPV2XcrSyrJupVbabd+0JK6l3ZIWEFNzq6SsFBFlUVQQ5vz+oDnOAKMMzJGl1/Px8FF85suZz3c+Z74zH76zGKZpmgIAAAAAAAHnqOkEAAAAAACor2i6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQA1YvXq1TIMQ2+++WZNp1Ipe/bs0VVXXaWoqCgZhqF58+bVaD4PPfSQDMOo0Rw8tW/fXn/6059qOo0675FHHlGHDh3kdDrVs2dPv3+/rt2vAOCPgKYbAOqxxYsXyzAMhYaG6rfffit3+YABA3TmmWfWQGZ1z/jx45WUlKQpU6bo5Zdf1pAhQ447vqCgQDNmzFCPHj3UsGFDNWnSROeff75eeuklmaZ5krKuX3766ScZhqFHH320wsvdf4jIzs4+yZkFxscff6yJEyfq3HPP1aJFi/Svf/3L59hly5bV6B9+3LVw/2vQoIGaN2+uc845R/fdd5927txZY7kBQG0TVNMJAADsV1hYqFmzZunJJ5+s6VTqrE8++USXX365/v73v59w7J49ezRw4EBt2bJF1157rcaOHasjR47orbfe0qhRo/Thhx9q6dKlcjqdJyFz1BWffPKJHA6HXnjhBQUHBx937LJly7Rp0yaNGzfu5CTnw3XXXadLL71ULpdLOTk5+uabbzRv3jzNnz9fL7zwgq699toazQ8AagOabgD4A+jZs6f+/e9/a8qUKWrdunVNp3NSFRQUKDw8vNrHycrKUmRkZKXGjho1Slu2bNE777yjP//5z1b8rrvu0r333qtHH31UvXr10qRJk3weo7i4WC6X64TNV6AcOnRIDRs2PCnXVd8EqlZZWVkKCws7aTUPhN69e+uGG27wiv38888aPHiwRo0apS5duiguLq6GsgOA2oGXlwPAH8B9992nkpISzZo167jj3C8ZXbx4cbnLDMPQQw89ZP3sfinv9u3bdcMNN6hJkyZq0aKFHnjgAZmmqV9++UWXX365IiIi1KpVK82dO7fC6ywpKdF9992nVq1aKTw8XH/+85/1yy+/lBv31VdfaciQIWrSpIkaNmyoCy+8UF988YXXGHdOmzdv1vXXX6+mTZvqvPPOO+6cd+zYoauvvlrNmjVTw4YNdfbZZ2vFihXW5e6X6JumqQULFlgvp/Xlyy+/VFJSkm6++Wavhttt5syZOu200zR79mwdPnxYkvfLpufNm6eOHTsqJCREmzdvliR9/vnn6tevn0JDQ9WxY0c9++yzPq//lVdeUZ8+fRQWFqZmzZrp2muvLXd7ut9WkJaWpgsuuEANGzbUfffdJ0lKTU1VQkKCmjdvrrCwMMXGxuqWW2457m3o6eOPP1bPnj0VGhqqrl276u2337Yu27FjhwzD0OOPP17u99auXSvDMPTqq69W+roq64033rBuk+bNm+uGG24o93aLAQMGaMCAAeV+9+abb1b79u2tn09Uq4oUFxdrxowZ1tj27dvrvvvuU2FhoTXGMAwtWrRIBQUF1jlW0f3QneuKFSv0888/W2M9c5Qkl8ulhx9+WDExMQoNDdXAgQP1ww8/lDtWZe5X/mrXrp0WL16soqIizZkzx4rv379ff//739W9e3c1atRIERERGjp0qL799ltrzMGDBxUeHq6777673HF//fVXOZ1OzZw5s1r5AcDJxk43APwBxMbG6qabbtK///1vTZ48OaC73ddcc426dOmiWbNmacWKFfrnP/+pZs2a6dlnn9XFF1+s2bNna+nSpfr73/+ufv366YILLvD6/YcffliGYWjSpEnKysrSvHnzNGjQIK1fv15hYWGSSl92O3ToUPXp00cPPvigHA6HFi1apIsvvlj/+9//dNZZZ3kd8+qrr9Zpp52mf/3rX8d9//SePXt0zjnn6NChQ7rrrrsUFRWlJUuW6M9//rPefPNNXXHFFbrgggv08ssv68Ybb9Qll1yim2666bi3xwcffCBJPscFBQXp+uuv17Rp0/TFF19o0KBB1mWLFi3SkSNHdPvttyskJETNmjXTxo0bNXjwYLVo0UIPPfSQiouL9eCDD6ply5bljv3www/rgQce0F/+8hfdeuut2rt3r5588kldcMEFSk9P99qp37dvn4YOHaprr71WN9xwg1q2bKmsrCzruiZPnqzIyEj99NNPXo3z8Xz//fe65pprdMcdd2jUqFFatGiRrr76aq1cuVKXXHKJOnTooHPPPVdLly7V+PHjvX536dKlaty4sS6//PITXs+hQ4cqfN/2oUOHysUWL16s0aNHq1+/fpo5c6b27Nmj+fPn64svvih3m/ijolr5cuutt2rJkiW66qqrdM899+irr77SzJkzrVdDSNLLL7+s5557Tl9//bWef/55SdI555xT4fH+8Y9/KC8vT7/++qv1B4xGjRp5jZk1a5YcDof+/ve/Ky8vT3PmzNHIkSP11VdfWWP8vV/5Iz4+Xh07dlRycrIV27Fjh959911dffXVio2N1Z49e/Tss8/qwgsv1ObNm9W6dWs1atRIV1xxhV577TU99thjXm/BePXVV2WapkaOHFnlvACgRpgAgHpr0aJFpiTzm2++MX/88UczKCjIvOuuu6zLL7zwQrNbt27WzxkZGaYkc9GiReWOJcl88MEHrZ8ffPBBU5J5++23W7Hi4mIzJibGNAzDnDVrlhXPyckxw8LCzFGjRlmxTz/91JRktmnTxszPz7fir7/+uinJnD9/vmmapulyuczTTjvNTEhIMF0ulzXu0KFDZmxsrHnJJZeUy+m6666r1O0zbtw4U5L5v//9z4odOHDAjI2NNdu3b2+WlJR4zT8xMfGExxw+fLgpyczJyfE55u233zYlmU888YRpmsdu94iICDMrK6vc8UJDQ82ff/7Zim3evNl0Op2m58P4Tz/9ZDqdTvPhhx/2+v2NGzeaQUFBXvELL7zQlGQuXLjQa+w777xjnS/+ateunSnJfOutt6xYXl6eecopp5i9evWyYs8++6wpydyyZYsVKyoqMps3b+51flTEfTud6N/evXut40ZHR5tnnnmmefjwYes4y5cvNyWZU6dO9bpNLrzwwnLXOWrUKLNdu3blcqioVhVZv369Kcm89dZbveJ///vfTUnmJ5984nVd4eHhJzymaZrmsGHDvPJyc9+vunTpYhYWFlrx+fPnm5LMjRs3mqbp3/2qIu7b4ZFHHvE55vLLLzclmXl5eaZpmuaRI0e87lPu44SEhJjTp0+3YklJSaYk86OPPvIa26NHjwprBAC1HS8vB4A/iA4dOujGG2/Uc889p927dwfsuLfeeqv1/06nU3379pVpmhozZowVj4yM1BlnnKEdO3aU+/2bbrpJjRs3tn6+6qqrdMopp+jDDz+UJK1fv17ff/+9rr/+eu3bt0/Z2dnKzs5WQUGBBg4cqM8++0wul8vrmHfccUelcv/www911llneb0EvVGjRrr99tv1008/Hfclw74cOHBAkrzmVJb7svz8fK/4iBEj1KJFC+vnkpISJSUlafjw4Tr11FOteJcuXZSQkOD1u2+//bZcLpf+8pe/WLdRdna2WrVqpdNOO02ffvqp1/iQkBCNHj3aK+be9V2+fLmOHj1ayRkf07p1a11xxRXWzxEREbrpppuUnp6uzMxMSdJf/vIXhYaGaunSpda4pKQkZWdnl3tvsC+33367kpOTy/278cYbvcalpqYqKytLf/3rXxUaGmrFhw0bps6dO3u9jcBfZWvli/s8njBhglf8nnvukaRq5XA8o0eP9npv+Pnnny9J1n2wKvcrf7l33933iZCQEDkcpU89S0pKtG/fPjVq1EhnnHGG1q1bZ/3eoEGD1Lp1a69zZNOmTdqwYUOlzxEAqE14eTkA/IHcf//9evnllzVr1izNnz8/IMf0bAYlqUmTJgoNDVXz5s3Lxfft21fu90877TSvnw3DUKdOnfTTTz9JKn3JslT64WS+5OXlqWnTptbPsbGxlcr9559/Vv/+/cvFu3TpYl3u71equRvqAwcO+Hzpsq/GvGzee/fu1eHDh8vdRpJ0xhlnWA2dVHo7maZZ4VhJatCggdfPbdq0KfeBXRdeeKFGjBihadOm6fHHH9eAAQM0fPhwXX/99QoJCanwuJ46depU7v3up59+uqTS90K3atVKkZGRuuyyy7Rs2TLNmDFDUulLy9u0aaOLL774hNchlZ4zni/Ld/v888+9fv75558lld5WZXXu3LnceH/4c445HA516tTJK+6+Ldw5BlrZ+6X7/pGTkyOpavcrfx08eFDSsfPc5XJp/vz5evrpp5WRkaGSkhJrbFRUlPX/DodDI0eO1DPPPGN9wN/SpUsVGhqqq6++usr5AEBNoekGgD+QDh066IYbbtBzzz2nyZMnl7vc1weEeT45Lquir73y9VVYZhW+n9q92/bII4+oZ8+eFY4p+35W93vBa0KXLl307rvvasOGDeXev+62YcMGSVLXrl294tXJ2+VyyTAMffTRRxXe/pW5jQzD0Jtvvqkvv/xSH3zwgZKSknTLLbdo7ty5+vLLL8sdo6puuukmvfHGG1q7dq26d++u999/X3/961+tXdCa4P6wvLJ8nfv+1up4H75nhxPdB6tyv/LXpk2bFB0drYiICEnSv/71Lz3wwAO65ZZbNGPGDDVr1kwOh0Pjxo0rt6t+00036ZFHHtG7776r6667TsuWLdOf/vQnNWnSpFo5AUBNoOkGgD+Y+++/X6+88opmz55d7jL3rlZubq5X3K7dOOnYjpubaZr64Ycf1KNHD0lSx44dJZW+VLmi3c3qaNeunbZt21YuvnXrVutyf/3pT3/SzJkz9dJLL1XYdJeUlGjZsmVq2rSpzj333OMeq0WLFgoLCyt3G0kql3fHjh1lmqZiY2Ot3eWqOvvss3X22Wfr4Ycf1rJlyzRy5Ej95z//8XorQUV++OEHmabp1WBu375dkrw+XXvIkCFq0aKFli5dqv79++vQoUPlXhoeCO76bdu2rdwu+rZt27zq27Rp0wrf/lDdc79du3ZyuVz6/vvvrVdQSKUf4pebm1ulc0yqfhNv5/1KklJSUvTjjz96vRz8zTff1EUXXaQXXnjBa2xubm65V8aceeaZ6tWrl5YuXaqYmBjt3LlTTz75ZMDzBICTgfd0A8AfTMeOHXXDDTfo2Weftd5n6xYREaHmzZvrs88+84o//fTTtuXz0ksvWS+3lkqfmO/evVtDhw6VJPXp00cdO3bUo48+ar1c1dPevXurfN2XXnqpvv76a6WkpFixgoICPffcc2rfvn25nejKOOecczRo0CAtWrRIy5cvL3f5P/7xD23fvl0TJ0484W6p0+lUQkKC3n33Xe3cudOKb9myRUlJSV5jr7zySjmdTk2bNq3cjq1pmhW+tL+snJyccr/r3gX1/HorX3bt2mV9GrdU+p71l156ST179lSrVq2seFBQkK677jq9/vrrWrx4sbp37279kSWQ+vbtq+joaC1cuNAr/48++khbtmzRsGHDrFjHjh21detWr/Pp22+/rfbXZ1166aWSpHnz5nnFH3vsMUnyysEf4eHhysvLq3Jedt6vfv75Z918880KDg7Wvffea8WdTme58+uNN94o9/VtbjfeeKM+/vhjzZs3T1FRUdaaAAB1DTvdAPAH9I9//EMvv/yytm3bpm7dunldduutt2rWrFm69dZb1bdvX3322WfWbqUdmjVrpvPOO0+jR4/Wnj17NG/ePHXq1Em33XabpNL3dz7//PMaOnSounXrptGjR6tNmzb67bff9OmnnyoiIsL6mi5/TZ48Wa+++qqGDh2qu+66S82aNdOSJUuUkZGht956q8ovd37ppZc0cOBAXX755br++ut1/vnnq7CwUG+//bZWr16ta665xqsZOZ5p06Zp5cqVOv/88/XXv/5VxcXFevLJJ9WtWzfrZepSadP4z3/+U1OmTNFPP/2k4cOHq3HjxsrIyNA777yj22+/XX//+9+Pe11LlizR008/rSuuuEIdO3bUgQMH9O9//1sRERFW83g8p59+usaMGaNvvvlGLVu21Isvvqg9e/Zo0aJF5cbedNNNeuKJJ/Tpp59W+KqLQGjQoIFmz56t0aNH68ILL9R1111nfWVY+/btvb627JZbbtFjjz2mhIQEjRkzRllZWVq4cKG6detW7gPv/BEXF6dRo0bpueeeU25uri688EJ9/fXXWrJkiYYPH66LLrqoSsft06ePXnvtNU2YMEH9+vVTo0aNdNlll1X69wN1v1q3bp1eeeUVuVwu5ebm6ptvvtFbb70lwzD08ssve/0x5U9/+pOmT5+u0aNH65xzztHGjRu1dOlSdejQocJjX3/99Zo4caLeeecd3XnnneU+lwAA6oya+dB0AMDJ4PmVYWWNGjXKlOT1lWGmWfqVQWPGjDGbNGliNm7c2PzLX/5iZmVl+fzKMPfXM3ket6KvPSr79WTurzZ69dVXzSlTppjR0dFmWFiYOWzYMK+vx3JLT083r7zySjMqKsoMCQkx27VrZ/7lL38xV61adcKcjufHH380r7rqKjMyMtIMDQ01zzrrLHP58uXlxqmSXxnmduDAAfOhhx4yu3XrZoaFhZmNGzc2zz33XHPx4sVeX9Fkmif++qU1a9aYffr0MYODg80OHTqYCxcutOZa1ltvvWWed955Znh4uBkeHm527tzZTExMNLdt22aNKVsLt3Xr1pnXXXedeeqpp5ohISFmdHS0+ac//clMTU094XzbtWtnDhs2zExKSjJ79OhhhoSEmJ07dzbfeOMNn7/TrVs30+FwmL/++usJj2+aJ76dfNX/tddeM3v16mWGhISYzZo1M0eOHFnhdb7yyitmhw4dzODgYLNnz55mUlKSz68MO95XZZV19OhRc9q0aWZsbKzZoEEDs23btuaUKVPM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IUnatm2bdu7cqfj4eElSfHy8Hn74YWVlZSk6OlqSlJycrIiICHXt2tUa8+GHH3pdR3JysnWM4OBg9enTR6tWrbKabpfLpVWrVmns2LE+8wwJCVFISEi5eFBQkIKCvG9W98lQlru4lY2XPW5V4oZhVBj3laO/cebEnHzFmRNzkgIwp99fGm4aFY+vMG4YFcYDNafSJ8oV5eIj7vCde0W3fVXr5HU9hkNmBbn4invm7nk91T73jlc/H3UKVP185V6VOvmKl51vde5PlalfZc49z+sPxBrhb5185R6oNaIqdSqfo1Fh/aqzRnjmVZ01oqr1q/VreRXizIk5SbVvTr6OU+64lRplkylTpmjo0KE69dRTdeDAAS1btkyrV69WUlKSmjRpojFjxmjChAlq1qyZIiIi9Le//U3x8fE6++yzJUmDBw9W165ddeONN2rOnDnKzMzU/fffr8TERKshvuOOO/TUU09p4sSJuuWWW/TJJ5/o9ddf14oVK6w8JkyYoFGjRqlv374666yzNG/ePBUUFGj06NE1crsAAAAAAOqHGm26s7KydNNNN2n37t1q0qSJevTooaSkJF1yySWSpMcff1wOh0MjRoxQYWGhEhIS9PTTT1u/73Q6tXz5ct15552Kj49XeHi4Ro0apenTp1tjYmNjtWLFCo0fP17z589XTEyMnn/+eSUkJFhjrrnmGu3du1dTp05VZmamevbsqZUrV5b7cDUAAAAAAPxRo033Cy+8cNzLQ0NDtWDBAi1YsMDnmHbt2pV7+XhZAwYMUHp6+nHHjB079rgvJwcAAAAAwF+15nu6AQAAAACob2i6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAA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/DFVqekOlGeeeUaSNGDAAK/4okWLdPPNNys4OFj//e9/rQa4bdu2GjFihO6//35rrNPp1PLly3XnnXcqPj5e4eHhGjVqlKZPn26NiY2N1YoVKzR+/HjNnz9fMTExev7555WQkGCNueaaa7R3715NnTpVmZmZ6tmzp1auXFnuw9UAAAAAAKisSjXdTZs2Pfaphyewf//+Sl/5id5O3rZtW61Zs+aEx2nXrl25l4+XNWDAAKWnpx93zNixY32+nBwAAAAAAH9Vqun2/ACyffv26Z///KcSEhKs90SnpKQoKSlJDzzwgC1JAgAAAABQF1Wq6R41apT1/yNGjND06dO9doTvuusuPfXUU/rvf/+r8ePHBz5LAAAAAADqoPIfCXcCSUlJGjJkSLn4kCFD9N///jcgSQEAAAAAUB/43XRHRUVV+L3V7733nqKioir4DQAAAAAA/pj8/vTyadOm6dZbb9Xq1avVv39/SdJXX32llStX6t///nfAEwQAAAAAoK7yu+m++eab1aVLFz3xxBN6++23JUldunTR559/bjXhAAAAAADAz6b76NGj+r//+z898MADWrp0qV05AQAAAABQL/j1nu4GDRrorbfesisXAAAAAADqFb8/SG348OF69913bUgFAAAAAID6xe/3dJ922mmaPn26vvjiC/Xp00fh4eFel991110BSw4AAAAAgLrM76b7hRdeUGRkpNLS0pSWluZ1mWEYNN0AAAAAAPzO76Y7IyPDjjwAAAAAAKh3/H5Pt1t2drays7MDmQsAAAAAAPWKX013bm6uEhMT1bx5c7Vs2VItW7ZU8+bNNXbsWOXm5tqUIgAAAAAAdVOlX16+f/9+xcfH67ffftPIkSPVpUsXSdLmzZu1ePFirVq1SmvXrlXTpk1tSxYAAAAAgLqk0k339OnTFRwcrB9//FEtW7Ysd9ngwYM1ffp0Pf744wFPEgAAAACAuqjSLy9/99139eijj5ZruCWpVatWmjNnjt55552AJgcAAAAAQF1W6aZ79+7d6tatm8/LzzzzTGVmZgYkKQAAAAAA6oNKN93NmzfXTz/95PPyjIwMNWvWLBA5AQAAAABQL1S66U5ISNA//vEPFRUVlbussLBQDzzwgIYMGRLQ5AAAAAAAqMv8+iC1vn376rTTTlNiYqI6d+4s0zS1ZcsWPf300yosLNTLL79sZ64A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ffv2VVFRkdfXuzmdTvXr1095eXlef0gICwtTXFycsrOztWPHDivepEkTdenSRbt27dKvv/5qxZkTc2JOf4w5tckrkiQVB4Uos1lHhR/JVdMDu63xR4LDlR3ZThGH9imi4FjuBWGRymncWk0PZir8cK4kKTU1OGBzCnK2VYkjSG2yvT9087fmZ8jpKlar/T9aMdPh0G/NOyv0aIGa5+604sVBIZKiA1anqLxfFFp07LNIchqfooKwpmqZk6Gg4mN/nM2OPFVHghup9f7vZXg8kchs1tGaU2pqsF91cqvo3GuTV+RXnSQpP7yF8sNbeM0pNTU4YOee0SDWrzod79wL1P2pKnXy5HnuuesXiDWiTV6RX3WSKj73UlODA7ZGKCjW7zr5OvcCte5VpU5uZc89d/0CsZa3ySvyq05SxedeampwwB6fpDbVWsulY+cej7nMiTmVzmnjxo2qDMP083XhrVq1UlJSkuLi4tS4cWN9++236tChg3bs2KEePXro4MGD/hxOkjR27Fi99957+uyzzxQbG2vFP/nkEw0cOFA5OTleu93t2rXTuHHjNH78eE2dOlXvv/++14e4ZWRkqEOHDlq3bp169eqlCy64QL1799a8efOsMYsWLdK4ceOUl5enoqIiNWzYUG+++aaGDx9ujRk1apRyc3P13nvvlcu5op3utm3bat++fYqIiJBU9/5SUx//+sScmBNzqtqc5n67z518tXe674mLCticHt2QU3r11dzpntQ7OmB1mr0uK2A73ffERXndBlLVz7253+4LyE738ern77nns35V2OmeGNcsIPcnn/Wrwg6qZ/2qu0bM/XZfQHa674mLCtga8ejG3IDtdPuqn79rxOw072+0qc5Ot7t+gVjLPetXnZ1ud/2k6j8+PbIhJ2A73ff2aMpjLnNiTi6XcnNzFRUVpby8PKsHrIjfO90FBQVq2LBhufj+/fsVEhLi17FM09Tf/vY3vfPOO1q9erVXwy1Jffr0UYMGDbRq1SqNGDFCkrRt2zbt3LlT8fHxkqT4+Hg9/PDDysrKUnR0tCQpOTlZERER6tq1qzXmww8/9Dp2cnKydYzg4GD16dNHq1atsppul8ulVatWaezYsRXmHhISUuF8g4KCFBTkfbO6T4ay3MWtbLzscasSNwyjwrivHP2NMyfm5CvOnOrWnEyHs+wFMo0KrtdwyDQq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veqs5Z4C9fjkV/1OcO5Vt348j2BOvuLHm5Ov45QbW6lRtcSvv/6qffv26ZRTTpEkxcfHKzc3V2lpadaYTz75RC6XS/3797fGfPbZZzp69Kg1Jjk5WWeccYaaNm1qjVm1apXXdSUnJys+Pt7uKQEAAAAA6rEabboPHjyo9evXa/369ZKkjIwMrV+/Xjt37tTBgwd177336ssvv9RPP/2kVatW6fLLL1enTp2UkJAgSerSpYuGDBmi2267TV9//bW++OILjR07Vtdee61at24tSbr++usVHBysMWPG6LvvvtNrr72m+fPne31w2t13362VK1dq7ty52rp1qx566CGlpqZq7NixJ/02AQAAAADUHzX68vLU1FRddNFF1s/uRnjUqFF65plntGHDBi1ZskS5ublq3bq1Bg8erBkzZni9rHvp0qUaO3asBg4cKIfDoREjRuiJJ56wLm/SpIk+/vhjJSYmqk+fPmrevLmmTp3q9V3e55xzjpYtW6b7779f9913n0477TS9++67OvPMM0/CrQAAAACgtpiVnh2wY03u1Txgx0LdVaNN94ABA7ze8F5WUlLSCY/RrFkzLVu27LhjevToof/973/HHXP11Vfr6quvPuH1AQAAAABQWXXqPd0AAAAAANQlNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2CarpBADgj25WenbAjjW5V/OAHQsAAADVx043AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATYJqOgEAAAAAgG+z0rMDdqzJvZoH7FioHHa6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsA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dPDgQY0dO1YxMTEKCwtT165dtXDhQtvyqWxee/bs0c0336zWrVurYcOGGjJkiK1raGWebx45ckSJiYmKiopSo0aNNGLECO3Zs8e2nCqb13PPPacBAwYoIiJChmEoNze3RnPav3+//va3v+mMM85QWFiYTj31VN11113Ky8ur0bwk6f/+7//UsWNHhYWFqUWLFrr88su1devWgOdC012LvPbaa5owYYIefPBBrVu3TnFxcUpISFBWVlaN5VRQUKC4uDgtWLCgxnIoa82aNUpMTNSXX36p5ORkHT16VIMHD1ZBQUGN5hUTE6NZs2YpLS1Nqampuvjii3X55Zfru+++q9G83L755hs9++yz6tGjR02nom7dumn37t3Wv88//7ymU1JOTo7OPfdcNWjQQB999JE2b96suXPnqmnTpjWW0zfffON1OyUnJ0uSrr766hrLafbs2XrmmWf01FNPacuWLZo9e7bmzJmjJ598ssZycrv11luVnJysl19+WRs3btTgwYM1aNAg/fbbbyfl+k+0Xs6ZM0dPPPGEFi5cqK+++krh4eFKSEjQkSNHajSvgoICnXfeeZo9e7ateVQ2p0OHDmndunV64IEHtG7dOr399tvatm2b/vznP9dYTpJ0+umn66mnntLGjRv1+eefq3379ho8eLD27t1bo3m5vfPOO/ryyy/VunVrW/OpbE5DhgzxWr9effXVGs3pxx9/1HnnnafOnTtr9erV2rBhgx544AGFhobWaF6et9Hu3bv14osvyjAMjRgxosZymjBhglauXKlXXnlFW7Zs0bhx4zR27Fi9//77tuV0orxM09Tw4cO1Y8cOvffee0pPT1e7du00aNAg257/Veb55vjx4/XBBx/ojTfe0Jo1a7Rr1y5deeWVtuTjT16HDh3SkCFDdN9999maS2Vz2rVrl3bt2qVHH31UmzZt0uLFi7Vy5UqNGTOmRvOSpD59+mjRokXasmWLkpKSZJqmBg8erJKSksAmY6LWOOuss8zExETr55KSErN169bmzJkzazCrYySZ77zzTk2nUU5WVpYpyVyzZk1Np1JO06ZNzeeff76m0zAPHDhgnnbaaWZycrJ54YUXmnfffXeN5fLggw+acXFxNXb9vkyaNMk877zzajqN47r77rvNjh07mi6Xq8ZyGDZsmHnLLbd4xa688kpz5MiRNZRRqUOHDplOp9Ncvny5V7x3797mP/7xj5OeT9n10uVyma1atTIfeeQRK5abm2uGhISYr776ao3l5SkjI8OUZKanp5+0fE6Uk9vXX39tSjJ//vnnWpNTXl6eKcn873//e1JyMk3fef36669mmzZtzE2bNpnt2rUzH3/88RrNadSoUebll19+0nIoq6KcrrnmGvOGG26omYR+V5nz6vLLLzcvvvjik5OQWXFO3bp1M6dPn+4VO9lradm8tm3bZkoyN23aZMVKSkrMFi1amP/+979PSk5ln2/m5uaaDRo0MN944w1rzJYtW0xJZkpKyknJqaK8PH366aemJDMnJ+ek5XOinNxef/11Mzg42Dx69Gityuvbb781JZk//PBDQK+bne5aoqioSGlpaRo0aJAVczgcGjRokFJSUmows9rP/dKUZs2a1XAmx5SUlOg///mPCgoKFB8fX9PpKDExUcOGDfM6v2rS999/r9atW6tDhw4aOXKk7S/vq4z3339fffv21dVXX63o6Gj16tVL//73v2s6LUtRUZFeeeUV3XLLLTIMo8byOOecc7Rq1Spt375dkvTtt9/q888/19ChQ2ssJ0kqLi5WSUlJuV2rsLCwWvFKioyMDGVmZnrdB5s0aaL+/fuzxldCXl6eDMNQZGRkTaciqfT++Nxzz6lJkyaKi4ur0VxcLpduvPFG3XvvverWrVuN5uJp9erVio6O1hlnnKE777xT+/btq7FcXC6XVqxYodNPP10JCQmKjo5W//79a8Vb5jzt2bNHK1assH3370TOOeccvf/++/rtt99kmqY+/fRTbd++XYMHD66xnAoLCyXJa413OBwKCQk5aWt82eebaWlpOnr0qNe63rlzZ5166qkndV2vjc+DK5NTXl6eIiIiFBQUdLLSOmFeBQUFWrRokWJjY9W2bduAXjdNdy2RnZ2tkpIStWzZ0ivesmVLZWZm1lBWtZ/L5dK4ceN07rnn6swzz6zpdLRx40Y1atRIISEhuuOOO/TOO++oa9euNZrTf/7zH61bt04zZ86s0Tzc+vfvb72s6JlnnlFGRobOP/98HThwoEbz2rFjh5555hmddtppSkpK0p133qm77rpLS5YsqdG83N59913l5ubq5ptvrtE8Jk+erGuvvVadO3dWgwYN1KtXL40bN04jR46s0bwaN26s+Ph4zZgxQ7t27VJJSYleeeUVpaSk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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df_instacart_orders\n",
    "\n",
    "# Count orders by hour of the day\n",
    "hourly_order_counts = df_instacart_orders['order_hour_of_day'].value_counts().sort_index()\n",
    "\n",
    "# Plotting the distribution of orders by hour\n",
    "plt.figure(figsize=(10, 6))\n",
    "hourly_order_counts.plot(kind='bar', color='skyblue')\n",
    "plt.title('Number of Orders by Hour of the Day')\n",
    "plt.xlabel('Hour of the Day (1-24)')\n",
    "plt.ylabel('Number of Orders')\n",
    "plt.xticks(rotation=0)\n",
    "plt.grid(axis='y', linestyle='--', alpha=0.7)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11270eed",
   "metadata": {},
   "source": [
    "Count orders by hour of the day using value_counts and plot using a bar graph for 24 hours. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eedd922f",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Everything is correct here. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "documented-command",
   "metadata": {},
   "source": [
    "### [A3] What day of the week do people shop for groceries?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "chief-digit",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAADDWUlEQVR4nOzdeVxU9f7H8feZQRZRFhEwRM0tt9wtxcqyTDLrZtmiWZpZ/m5XK7U0LXNrccutsrzdzKXyVlpZqWmmpbfEHXPJraTMFBVlUVQQ5vz+sDkyAgrGEQZfz8ejx718znfOfL7n8wXnc86ZGcM0TVMAAAAAAKDIOYo7AQAAAAAASiuabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgDAJfP999/LMAzNmzevuFMpkIMHD+ree+9VWFiYDMPQ5MmTizWfESNGyDCMYs0hpyuvvFJ33HFHcadR4mVlZWnQoEGqUqWKHA6HOnXqVOh9zJw5U4ZhaP369UWfYAl2uc4bQOlC0w0ApYz7Raq/v7/+/PPPXNtvuukmXX311cWQmffp37+/lixZoiFDhuj999/Xbbfddt7x6enpeumll9SoUSOVLVtWwcHBuuGGGzR79myZpnmJsi5dfvvtNxmGYf1XpkwZVaxYUa1bt9bzzz+vvXv3FneKF/Tee+9p/PjxuvfeezVr1iz1798/37FvvfWWZs6ceemSy2Ht2rUyDEOTJk3Kte2uu+6SYRiaMWNGrm1t2rRR5cqVL0WKAOCVaLoBoJTKyMjQmDFjijsNr7Z8+XLdddddevbZZ/XQQw+pbt26+Y49ePCgWrZsqREjRqhhw4aaPHmyXnrpJTkcDvXo0UNdu3ZVdnb2Jcy+dOnatavef/99TZ8+XS+++KJq1KihyZMnq169evroo4+KO73zWr58uSpXrqxJkybp4Ycf1o033pjv2OJsups1a6ayZcvqhx9+yLVt1apV8vHx0Y8//ugRz8zM1Lp163TdddddqjQBwOv4FHcCAAB7NGnSRP/5z380ZMgQRUVFFXc6l1R6eroCAwP/9n4OHTqkkJCQAo3t0aOHtm/frs8//1z/+Mc/rPhTTz2lgQMH6rXXXlPTpk313HPP5buPrKwsuVwu+fr6/t3UC+TEiRMqW7bsJXmuv6tZs2Z66KGHPGK///672rdvrx49eqhevXpq3LhxMWV3foVZR8XJx8dHLVu2zNVY79y5U0lJSXrwwQdzNeQbNmzQqVOndP3111/KVAHAq3ClGwBKqeeff17Z2dkXvNrtvn03r6trhmFoxIgR1s/u9xTv2rVLDz30kIKDgxUeHq4XX3xRpmnqjz/+0F133aWgoCBVqlRJEyZMyPM5s7Oz9fzzz6tSpUoKDAzUP/7xD/3xxx+5xq1Zs0a33XabgoODVbZsWd144425GgJ3Tj///LMefPBBhYaGXrAB2LNnj+677z5VqFBBZcuWVatWrbRw4UJru/sWfdM0NXXqVOvW5vysXr1aS5Ys0SOPPOLRcLuNHj1atWvX1tixY3Xy5ElJZ4/7a6+9psmTJ6tmzZry8/PTzz//LEn64YcfdM0118jf3181a9bUv//973yf/4MPPlDz5s0VEBCgChUqqEuXLrmOp/ttBRs2bFCbNm1UtmxZPf/885Kk9evXKzY2VhUrVlRAQICqV6+uRx999LzHMKdvvvlGTZo0kb+/v+rXr6/PPvvM2rZnz558b1letWqVDMPQf//73wI/V07VqlXTzJkzlZmZqXHjxlnxo0eP6tlnn1XDhg1Vrlw5BQUFqUOHDvrpp5+sMcePH1dgYKCefvrpXPvdt2+fnE6nRo8efd7nT09P1zPPPKMqVarIz89PderU0WuvvWa9lcBd4++++07btm2z1tH333+f5/6uvPJKbdu2TStWrLDG3nTTTR5jMjIyNGDAAIWHhyswMFB33323Dh8+nGtfX3/9tW644QYFBgaqfPny6tixo7Zt23be+UjS9ddfr4MHD+qXX36xYj/++KOCgoLUu3dvqwHPuc39uMI+944dO3TvvfeqQoUK8vf3V4sWLfTll19eMMfk5GRde+21io6O1s6dOy84HgCKG003AJRS1atXV/fu3fWf//xH+/fvL9J9P/DAA3K5XBozZoxatmypl19+WZMnT9att96qypUra+zYsapVq5aeffZZrVy5MtfjX3nlFS1cuFDPPfecnnrqKS1dulTt2rWzGlLpzC25bdq0UVpamoYPH65XX31VKSkpuvnmm7V27dpc+7zvvvt04sQJvfrqq3r88cfzzf3gwYNq3bq1lixZon/961965ZVXdOrUKf3jH//Q559/LunMe1Tff/99SdKtt96q999/3/o5L1999ZUkqXv37nlu9/Hx0YMPPqjk5ORcJw1mzJihN954Q71799aECRNUoUIFbdmyRe3bt9ehQ4c0YsQI9ezZU8OHD7fyO/dYdu/eXbVr19bEiRPVr18/LVu2TG3atFFKSorH2CNHjqhDhw5q0qSJJk+erLZt2+rQoUNq3769fvvtNw0ePFhvvPGGunXrptWrV+c735x2796tBx54QB06dNDo0aPl4+Oj++67T0uXLpUk1ahRQ9ddd50+/PDDXI/98MMPVb58ed11110Feq68xMTEqGbNmtbzSWca/fnz5+uOO+7QxIkTNXDgQG3ZskU33nij9btQrlw53X333fr4449z3fb/3//+V6Zpqlu3bvk+r2ma+sc//qFJkybptttu08SJE1WnTh0NHDhQAwYMkCSFh4fr/fffV926dRUdHW2to3r16uW5z8mTJys6Olp169a1xr7wwgseY5588kn99NNPGj58uJ544gl99dVX6tu3r8eY999/Xx07dlS5cuU0duxYvfjii/r55591/fXX67fffjvv8XQ3zzmvaP/4449q1aqVWrZsqTJlymjVqlUe28qXL2/dZVDQ5962bZtatWql7du3a/DgwZowYYICAwPVqVOnPNe5W1JSkm6++WYdPHhQK1asUJ06dc47HwAoEUwAQKkyY8YMU5K5bt0689dffzV9fHzMp556ytp+4403mg0aNLB+TkhIMCWZM2bMyLUvSebw4cOtn4cPH25KMnv37m3FsrKyzOjoaNMwDHPMmDFWPDk52QwICDB79Ohhxb777jtTklm5cmUzLS3Nin/yySemJHPKlCmmaZqmy+Uya9eubcbGxpoul8sad+LECbN69ermrbfemiunrl27Fuj49OvXz5Rk/u9//7Nix44dM6tXr25eeeWVZnZ2tsf8+/Tpc8F9durUyZRkJicn5zvms88+MyWZr7/+ummaZ497UFCQeejQoVz78/f3N3///Xcr9vPPP5tOp9PM+U/3b7/9ZjqdTvOVV17xePyWLVtMHx8fj/iNN95oSjKnTZvmMfbzzz+31kthVatWzZRkfvrpp1YsNTXVvOKKK8ymTZtasX//+9+mJHP79u1WLDMz06xYsaLH+siL+ziNHz8+3zF33XWXKclMTU01TdM0T5065VFH9378/PzMUaNGWbElS5aYksyvv/7aY2yjRo3MG2+88bx5zZ8/35Rkvvzyyx7xe++91zQMw/zll1+s2Lm/c+fToEGDPJ/b/Xvdrl07j9+J/v37m06n00xJSTFN88xaDgkJMR9//HGPxycmJprBwcG54udKS0sznU6n2atXLytWp04dc+TIkaZpmua1115rDhw40NoWHh5u/T4W5rlvueUWs2HDhuapU6esmMvlMlu3bm3Wrl0717zXrVtnHjhwwGzQoIFZo0YN87fffjvvPACgJOFKNwCUYjVq1NDDDz+sd955RwcOHCiy/T722GPW/3c6nWrRooVM01SvXr2seEhIiOrUqaM9e/bkenz37t1Vvnx56+d7771XV1xxhRYtWiRJ2rRpk3bv3q0HH3xQR44cUVJSkpKSkpSenq5bbrlFK1eulMvl8tjnP//5zwLlvmjRIl177bUet8OWK1dOvXv31m+//Wbd3l0Yx44dkySPOZ3LvS0tLc0j3rlzZ4WHh1s/Z2dna8mSJerUqZOqVq1qxevVq6fY2FiPx3722WdyuVy6//77rWOUlJSkSpUqqXbt2vruu+88xvv5+alnz54eMfd7jRcsWKDTp08XcMZnRUVF6e6777Z+DgoKUvfu3RUfH6/ExERJ0v333y9/f3+Pq91LlixRUlJSrvdpX4xy5cpJOlsHPz8/ORxnXuJkZ2fryJEjKleunOrUqaONGzdaj2vXrp2ioqI88tq6das2b958wbwWLVokp9Opp556yiP+zDPPyDRNff311397Xnnp3bu3x1sdbrjhBmVnZ+v333+XJC1dulQpKSnq2rWrx5pwOp1q2bJlrjVxrvLly6tRo0bWle6kpCTt3LlTrVu3liRdd9111t0au3bt0uHDh63fpYI+99GjR7V8+XLdf//9OnbsmDXuyJEjio2N1e7du3N988K+fft044036vTp01q5cqWqVatWBEcTAC4Nmm4AKOWGDh2qrKysIv0k85zNoCQFBwfL399fFStWzBVPTk7O9fjatWt7/GwYhmrVqmXdfrp7925JZz6cLDw83OO/d999VxkZGUpNTfXYR/Xq1QuU+++//57nLanuW37dzUthuBtqd9OXl/wa83PzPnz4sE6ePJnrGEnKlffu3btlmqZq166d6zht375dhw4d8hhfuXLlXB/SduONN6pz584aOXKkKlasqLvuukszZsxQRkbGBWZ9Rq1atXK93/2qq66SJKueISEhuvPOOzVnzhxrzIcffqjKlSvr5ptvLtDznM/x48clnT22LpdLkyZNUu3ateXn56eKFSsqPDxcmzdv9lg3DodD3bp10/z583XixAkrL39/f913333nfc7ff/9dUVFRuer5d9ZRQZz7uxcaGipJ1u+Z+3fn5ptvzrUmvvnmm1xrIi/XX3+99d7tVatWyel0qlWrVpKk1q1ba8OGDcrIyMj1fu6CPvcvv/wi0zT14osv5ho3fPhwScqV58MPP6xDhw5pxYoVfD0ZAK/Dp5cDQClXo0YNPfTQQ3rnnXc0ePDgXNvz+4Cw8329ldPpLFBM0kV9P7X7Kvb48ePVpEmTPMe4r266BQQEFPp5ikq9evU0f/58bd68WW3atMlzzObNmyVJ9evX94j/nbxdLpcMw9DXX3+d5/EvyDEyDEPz5s3T6tWr9dVXX2nJkiV69NFHNWHCBK1evTrXPi5W9+7dNXfuXK1atUoNGzbUl19+qX/961/WFem/Y+vWrYqIiFBQUJAk6dVXX9WLL76oRx99VC+99JIqVKggh8Ohfv365bpDonv37ho/frzmz5+vrl27as6cObrjjjsUHBz8t/Oyw4V+z9zze//991WpUqVc43x8LvzS7/rrr9cbb7yhH3/80aqXex20bt1aGRkZWrdunX744Qf5+PhYDXlBn9s97tlnn81194ZbrVq1PH6+5557NHv2bE2ZMuWCH3AHACUNTTcAXAaGDh2qDz74QGPHjs21zX2l7NwP3bLrSp109oqYm2ma+uWXX9SoUSNJUs2aNSWduVW5Xbt2Rfrc1apVy/MTj3fs2GFtL6w77rhDo0eP1uzZs/NsurOzszVnzhyFhoZe8PuMw8PDFRAQkOsYScqVd82aNWWapqpXr25dXb5YrVq1UqtWrfTKK69ozpw56tatmz766COPtxLkxX3VMufJm127dkk682ncbrfddpvCw8P14YcfqmXLljpx4oQefvjhv5WzJMXFxenXX3/1uB183rx5atu2raZPn+4xNiUlJdfdGFdffbWaNm2qDz/8UNHR0dq7d6/eeOONCz5vtWrV9O233+rYsWMeV7v/zjqS8j8JVlDu352IiIiL/t3J+WFqcXFxHms2KipK1apV048//qgff/xRTZs2tb52rqDPXaNGDUlSmTJlCpzjk08+qVq1amnYsGEKDg7O8wQiAJRU3F4OAJeBmjVr6qGHHtK///1v6322bkFBQapYsWKuTxl/6623bMtn9uzZHrdiz5s3TwcOHFCHDh0kSc2bN1fNmjX12muvWbcO55TXVyQV1O233661a9cqLi7OiqWnp+udd97RlVdemetKdEG0bt1a7dq104wZM7RgwYJc21944QXt2rVLgwYNuuCVbafTqdjYWM2fP1979+614tu3b9eSJUs8xt5zzz1yOp0aOXJkrjsKTNPUkSNHLph7cnJyrse67y4oyC3m+/fv9/i06bS0NM2ePVtNmjTxuNrp4+Ojrl276pNPPtHMmTPVsGFD6yTLxfr999/1yCOPyNfXVwMHDrTiTqcz15zmzp2b633Cbg8//LC++eYbTZ48WWFhYdY6PJ/bb79d2dnZevPNNz3ikyZNkmEYBdpHXgIDA3OdACuM2NhYBQUF6dVXX83zPfoF+d2JiopS9erVtWzZMq1fv956P7db69atNX/+fO3cudPjsxEK+twRERG66aab9O9//zvPz5rIL8cXX3xRzz77rIYMGaK33377gvMAgJKCK90AcJl44YUX9P7772vnzp1q0KCBx7bHHntMY8aM0WOPPaYWLVpo5cqV1tVKO1SoUEHXX3+9evbsqYMHD2ry5MmqVauW9VVfDodD7777rjp06KAGDRqoZ8+eqly5sv7880999913CgoKsr6mq7AGDx6s//73v+rQoYOeeuopVahQQbNmzVJCQoI+/fTTi77defbs2brlllt011136cEHH9QNN9ygjIwMffbZZ/r+++/1wAMPeDSG5zNy5EgtXrxYN9xwg/71r38pKytLb7zxhho0aGDdpi6dOZny8ssva8iQIfrtt9/UqVMnlS9fXgkJCfr888/Vu3dvPfvss+d9rlmzZumtt97S3XffrZo1a+rYsWP6z3/+o6CgIN1+++0XzPWqq65Sr169tG7dOkVGRuq9997TwYMHNWPGjFxju3fvrtdff13fffddnnddnM/GjRv1wQcfyOVyKSUlRevWrdOnn34qwzD0/vvvezTwd9xxh0aNGqWePXuqdevW2rJliz788EPrCuu5HnzwQQ0aNEiff/65nnjiCZUpU+aC+dx5551q27atXnjhBf32229q3LixvvnmG33xxRfq16+fddW3sJo3b663335bL7/8smrVqqWIiIhCve89KChIb7/9th5++GE1a9ZMXbp0UXh4uPbu3auFCxfquuuuy3WiIC/XX3+99TV5596d0bp1a+u71XM23YV57qlTp+r6669Xw4YN9fjjj6tGjRo6ePCg4uLitG/fPo/vVM9p/PjxSk1NVZ8+fVS+fPki+SA+ALBdsXxmOgDANjm/YudcPXr0MCXl+vqiEydOmL169TKDg4PN8uXLm/fff7956NChfL8y7PDhw7n2GxgYmOv5zv2qJPdXhv33v/81hwwZYkZERJgBAQFmx44dPb4eyy0+Pt685557zLCwMNPPz8+sVq2aef/995vLli27YE7n8+uvv5r33nuvGRISYvr7+5vXXnutuWDBglzjVMCvDHM7duyYOWLECLNBgwZmQECAWb58efO6664zZ86c6fE1T6Z54a/CWrFihdm8eXPT19fXrFGjhjlt2jRrruf69NNPzeuvv94MDAw0AwMDzbp165p9+vQxd+7caY3J72urNm7caHbt2tWsWrWq6efnZ0ZERJh33HGHuX79+gvOt1q1ambHjh3NJUuWmI0aNTL9/PzMunXrmnPnzs33MQ0aNDAdDoe5b9++C+7fNM8eJ/d/Pj4+ZoUKFcyWLVuaQ4YMyXPdnDp1ynzmmWfMK664wgwICDCvu+46My4uzrzxxhvz/Sqw22+/3ZRkrlq1qkB5meaZevfv39+Miooyy5QpY9auXdscP358rloX5ivDEhMTzY4dO5rly5c3JVn55vd77f6d+u6773LFY2NjzeDgYNPf39+sWbOm+cgjjxSorqZ59mveKleunGvbxo0brXocPHgw1/aCPvevv/5qdu/e3axUqZJZpkwZs3LlyuYdd9xhzps3zxqT17yzs7PNrl27mj4+Pub8+fMLNB8AKE6GaV7EJ9wAAABchKZNm6pChQpatmxZcafi4e6779aWLVv0yy+/FHcqAIBShvd0AwCAS2L9+vXatGmTunfvXtypeDhw4IAWLlxYJB/sBgDAubjSDQAAbLV161Zt2LBBEyZMUFJSkvbs2SN/f//iTksJCQn68ccf9e6772rdunX69ddf8/yqKwAA/g6udAMAAFvNmzdPPXv21OnTp/Xf//63RDTckrRixQo9/PDDSkhI0KxZs2i4AQC24Eo3AAAAAAA24Uo3AAAAAAA2oekGAAAAAMAmPsWdQGnhcrm0f/9+lS9fXoZhFHc6AAAA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AAAAQKlS7E33t99+q7179+rRRx/NtW3SpElyOBzq3LmzMjIyFBsbq7feesva7nQ6tWDBAj3xxBOKiYlRYGCgevTooVGjRlljqlevroULF6p///6aMmWKoqOj9e677yo2NtYa88ADD+jw4cMaNmyYEhMT1aRJEy1evDjXh6sBAAAAAFAYJeI93aUB39Nd/C7372mm/pd3/QEAAHBped33dAMAAAAAUNrQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmNN0AAAAAANiEphsAAAAAAJvQdAMAAAAAYBOabgAAAAAAbELTDQAAAACATWi6AQAAAACwCU03AAAAAAA2oekGAAAAAMAmPsWdAADg7xsTn1TcKRSrwU0rFncKAAAAeeJKNwAAAAAANqHpBgAAAADAJjTdAAAAAADYhKYbAAAAAACb0HQDAAAAAGATmm4AAAAAAGxC0w0AAAAAgE1ougEAAAAAsAlNNwAAAAAANqHpBgAAAADAJjTdAAAAAADYxKe4EwAAAABw8cbEJxV3CsVqcNOKxZ0CcF5c6QYAAAAAwCY03QAAAAAA2ISmGwAAAAAAm/CebgAAAADwUrynv+S/p58r3QAAAAAA2ISmGwAAAAAAm9B0AwAAAABgE5puAAAAAABsQtMNAAAAAIBNaLoBAAAAALAJTTcAAAAAADah6QYAAAAAwCY+xZ0AAAD4+8bEJxV3CsVqcNOKxZ0CAAB5KvYr3X/++aceeughhYWFKSAgQA0bNtT69eut7aZpatiwYbriiisUEBCgdu3aaffu3R77OHr0qLp166agoCCFhISoV69eOn78uMeYzZs364YbbpC/v7+qVKmicePG5cpl7ty5qlu3rvz9/dWwYUMtWrTInkkDAAAAAC4Lxdp0Jycn67rrrlOZMmX09ddf6+eff9aECRMUGhpqjRk3bpxef/11TZs2TWvWrFFgYKBiY2N16tQpa0y3bt20bds2LV26VAsWLNDKlSvVu3dva3taWprat2+vatWqacOGDRo/frxGjBihd955xxqzatUqde3aVb169VJ8fLw6deqkTp06aevWrZfmYAAAAAAASp1ivb187NixqlKlimbMmGHFqlevbv1/0zQ1efJkDR06VHfddZckafbs2YqMjNT8+fPVpUsXbd++XYsXL9a6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7NmztWDBAjtyBAAAAADAKxX6Svddd92lr776St9++60CAwM1bNgwbd++XV999ZVuvfVWO3IEAAAAAMArFfpKtyTdcMMNWrp0aVHnAgAAAABAqVLoK90AAAAAAKBgCnSlOzQ0VIZhFGiHR48e/VsJAQAAAABQWhSo6Z48ebL1/48cOaKXX35ZsbGxiomJkSTFxcVpyZIlevHFF21JEgAAAAAAb1SgprtHjx7W/+/cubNGjRqlvn37WrGnnnpKb775pr799lv179+/6LMEAAAAAMALFfo93UuWLNFtt92WK37bbbfp22+/LZKkAAAAAAAoDQrddIeFhemLL77IFf/iiy8UFhZWJEkBAAAAAFAaFLrpHjlypJ577jndeeedevnll/Xyyy/rzjvv1ODBgzVy5MhC7WvEiBEyDMPjv7p161rbT506pT59+igsLEzlypVT586ddfDgQY997N27Vx07dlTZsmUVERGhgQMHKisry2PM999/r2bNmsnPz0+1atXSzJkzc+UydepUXXnllfL391fLli21du3aQs0FAAAAAIBzFbrpfuSRR/Tjjz8qKChIn332mT777DMFBQXphx9+0COPPFLoBBo0aKADBw5Y//3www/Wtv79++urr77S3LlztWLFCu3fv1/33HOPtT07O1sdO3ZUZmamVq1apVmzZmnmzJkaNmyYNSYhIUEdO3ZU27ZttWnTJvXr10+PPfaYlixZYo35+OOPNWDAAA0fPlwbN25U48aNFRsbq0OHDhV6PgAAAAAAuBXog9TcTp8+rf/7v//Tiy++qA8//LBoEvDxUaVKlXLFU1NTNX36dM2ZM0c333yzJGnGjBmqV6+eVq9erVatWumbb77Rzz//rG+//VaRkZFq0qSJXnrpJT333HMaMWKEfH19NW3aNFWvXl0TJkyQJNWrV08//PCDJk2apNjYWEnSxIkT9fjjj6tnz56SpGnTpmnhwoV67733NHjw4CKZJwAAAADg8lOoprtMmTL69NNPi/SrwXbv3q2oqCj5+/srJiZGo0ePVtWqVbVhwwadPn1a7dq1s8bWrVtXVatWVVxcnFq1aqW4uDg1bNhQkZGR1pjY2Fg98cQT2rZtm5o2baq4uDiPfbjH9OvXT5KUmZmpDRs2aMiQIdZ2h8Ohdu3aKS4uLt+8MzIylJGRYf2clpYmScrKyrJub3c4HHI4HHK5XHK5XB77dzgcys7OlmmaF4w7nU4ZhpHrtnmn0ynpzBV/STJcZ/7XNM7cwGCYLo/xpsMpmaZn3DDOjM837pKRIxfTMKTzxA3TJXnEHZJh5B//K2ePeF65F2BO7uNjGIacTmeu455f/FLX6UJxHx8fmabpES/InHIey5JcpxzJF+na85Y62bX2JHlFnWxbe389tqTXyc6199eBKNl1snHtuVwur6iTXWvPcGV7RZ3sWnvuepX0Op0v/nfWnsdrgBJcJ4+4im7t5TxmJblOORXl2vOWOtm29qRiq9O5+89PoZpuSerUqZPmz59fJF8N1rJlS82cOVN16tTRgQMHNHLkSN1www3aunWrEhMT5evrq5CQEI/HREZGKjExUZKUmJjo0XC7t7u3nW9MWlqaTp48qeTkZGVnZ+c5ZseOHfnmPnr06Dzfwx4fH6/AwEBJUnh4uGrWrKmEhAQdPnzYGhMdHa3o6Gjt2rVLqampVrxGjRqKiIjQ1q1bdfLkSStet25dhYSEKD4+3qPgjRo1kq+vr9avXy9JqpyaKUn6s2IdOV1ZqnT0V2us6XDoz4p15X86XRVT9lrxLB8/JVaoqcBTKQo9dsCKn/INVFJINQWdOKKg9LO5pweEKLl8lEKPJyrwZIoVTwsMV1pguMJS/5B/ZroVTy5/hdIDQhWZnCCfrLMnKZJCquqUbzlFHd0tI8cfj8QKNZXt8FHlpJ0ex7Ugc1q/3leSFBAQoMaNGyspKUl79uyxxgcHB6tevXrav3+/9u3bZ8UvdZ3cWrRooczMTG3evNmKOZ1OXXPNNUpNTfVYfwWZU+Wks/GSXCe3ol573lInu9aeJK+ok11rLzs7zCvqZOfakyqX+DrZufYSEo57RZ3sWnuVUzO9ok52rT33a4CSXifJnrXnfg1Y0uvkVtRrb/36s+NLcp3cinrteUud7Fp7Unix1WnLli0qCMPMeUqgAF5++WVNmDBBt9xyi5o3b241mG5PPfVUYXbnISUlRdWqVdPEiRMVEBCgnj17elxNlqRrr71Wbdu21dixY9W7d2/9/vvvHu/PPnHihAIDA7Vo0SJ16NBBV111lXr27OlxJXvRokXq2LGjTpw4oeTkZFWuXFmrVq1STEyMNWbQoEFasWKF1qxZk2eueV3prlKlio4cOaKgoCBJl/6M2oSfjkgqgWefLtEZtWcah/2Vuvedoc7pYs98jo8/+werJNcpR/JFuvYGNgr1ijrZtfbGbjriFXWya+0NahYhqeTXyc61N35zcomvk51rb2DTcK+ok11rb8JPR7yiTnatPfdrgJJep/PF/87ac78GlEp2nTziKrq192yj0BzhklunnIpy7Y3ZeMgr6mTX2hvcLLzY6pSSkqKwsDClpqZaPWBeCn2le/r06QoJCdGGDRu0YcMGj22GYfytpjskJERXXXWVfvnlF916663KzMxUSkqKx9XugwcPWu8Br1SpUq5PGXd/unnOMed+4vnBgwcVFBSkgIAAOZ1OOZ3OPMfk9V5zNz8/P/n5+eWK+/j4yMfH87Bat36cw13cgsbP3e+5cdPh+TjTyGM/hlHIuEOmkceT5hM/80tbiLgj77nmmUt+8b9yL+hxL2y8qOtUkLhhGHnGz5d7nseyBNap4PHCrT1vqZOda88b6mTX2nPfXu0NdbJz7ZX0Op03/jfXnrs23lAnO9ZezhqU5DpdKH6xa+/c41xS61SQ+MWsvVy1LaF1yj2+aNZeUdTPm/9GeEud7Fx7xVWn/PaTa2yBRuWQkJCQ7385b4O4GMePH9evv/6qK664Qs2bN1eZMmW0bNkya/vOnTu1d+9e64p0TEyMtmzZ4vEp40uXLlVQUJDq169vjcm5D/cY9z58fX3VvHlzjzEul0vLli3zuPINAAAAAEBhFbrpdktKSlJSUtLfevJnn31WK1as0G+//aZVq1bp7rvvltPpVNeuXRUcHKxevXppwIAB+u6777Rhwwb17NlTMTExatWqlSSpffv2ql+/vh5++GH99NNPWrJkiYYOHao+ffpYV6H/+c9/as+ePRo0aJB27Niht956S5988onHe9IHDBig//znP5o1a5a2b9+uJ554Qunp6danmQMAAAAAcDEKdXt5SkqKXnjhBX388cdKTk6WJIWGhqpLly56+eWXc33o2YXs27dPXbt21ZEjRxQeHq7rr79eq1evVnh4uCRp0qRJcjgc6ty5szIyMhQbG6u33nrLerzT6dSCBQv0xBNPKCYmRoGBgerRo4dGjRpljalevboWLlyo/v37a8qUKYqOjta7775rfV2YJD3wwAM6fPiwhg0bpsTERDVp0kSLFy/O9eFqAAAAAAAURoGb7qNHjyomJkZ//vmnunXrpnr16kmSfv75Z82cOVPLli3TqlWrFBoaeoE9nfXRRx+dd7u/v7+mTp2qqVOn5jumWrVqWrRo0Xn3c9NNNyk+Pv68Y/r27au+ffuedwwAAAAAAIVR4KZ71KhR8vX11a+//prrCvCoUaPUvn17jRo1SpMmTSryJAEAAAAA8EYFfk/3/Pnz9dprr+V5y3WlSpU0btw4ff7550WaHAAAAAAA3qzATfeBAwfUoEGDfLdfffXVSkxMLJKkAAAAAAAoDQrcdFesWFG//fZbvtsTEhJUoUKFosgJAAAAAIBSocBNd2xsrF544QVlZmbm2paRkaEXX3xRt912W5EmBwAAAACANyvUB6m1aNFCtWvXVp8+fVS3bl2Zpqnt27frrbfeUkZGht5//307cwUAAAAAwKsUuOmOjo5WXFyc/vWvf2nIkCEyTVOSZBiGbr31Vr355puqUqWKbYkCAAAAAOBtCtx0S1L16tX19ddfKzk5Wbt375Yk1apVi/dyAwAAAACQh0I13W6hoaG69tprizoXAAAAAABKlQJ/kBoAAAAAACgcmm4AAAAAAGxC0w0AAAAAgE0K1HQ3a9ZMycnJks58ddiJEydsTQoAAAAAgNKgQE339u3blZ6eLkkaOXKkjh8/bmtSAAAAAACUBgX69PImTZqoZ8+euv7662Wapl577TWVK1cuz7HDhg0r0gQBAAAAAPBWBWq6Z86cqeHDh2vBggUyDENff/21fHxyP9QwDJpuAAAAAAD+UqCmu06dOvroo48kSQ6HQ8uWLVNERIStiQEAAAAA4O0K1HTn5HK57MgDAAAAAIBSp9BNtyT9+uuvmjx5srZv3y5Jql+/vp5++mnVrFmzSJMDAAAAAMCbFfp7upcsWaL69etr7dq1atSokRo1aqQ1a9aoQYMGWrp0qR05AgAAAADglQp9pXvw4MHq37+/xowZkyv+3HPP6dZbby2y5AAAAAAA8GaFvtK9fft29erVK1f80Ucf1c8//1wkSQEAAAAAUBoUuukODw/Xpk2bcsU3bdrEJ5oDAAAAAJBDoW8vf/zxx9W7d2/t2bNHrVu3liT9+OOPGjt2rAYMGFDkCQIAAAAA4K0K3XS/+OKLKl++vCZMmKAhQ4ZIkqKiojRixAg99dRTRZ4gAAAAAADeqtBNt2EY6t+/v/r3769jx45JksqXL1/kiQEAAAAA4O0u6nu63Wi2AQAAAADIX6E/SA0AAAAAABQMTTcAAAAAADah6QYAAAAAwCaFarpPnz6tW265Rbt377YrHwAAAAAASo1CNd1lypTR5s2b7coFAAAAAIBSpdC3lz/00EOaPn26HbkAAAAAAFCqFPorw7KysvTee+/p22+/VfPmzRUYGOixfeLEiUWWHAAAAAAA3qzQTffWrVvVrFkzSdKuXbs8thmGUTRZAQAAAABQChS66f7uu+/syAMAAAAAgFLnor8y7JdfftGSJUt08uRJSZJpmkWWFAAAAAAApUGhm+4jR47olltu0VVXXaXbb79dBw4ckCT16tVLzzzzTJEnCAAAAACAtyp0092/f3+VKVNGe/fuVdmyZa34Aw88oMWLFxdpcgAAAAAAeLNCv6f7m2++0ZIlSxQdHe0Rr127tn7//fciSwwAAAAAAG9X6Cvd6enpHle43Y4ePSo/P7+LTmTMmDEyDEP9+vWzYqdOnVKfPn0UFhamcuXKqXPnzjp48KDH4/bu3auOHTuqbNmyioiI0MCBA5WVleUx5vvvv1ezZs3k5+enWrVqaebMmbmef+rUqbryyivl7++vli1bau3atRc9FwAAAAAApItoum+44QbNnj3b+tkwDLlcLo0bN05t27a9qCTWrVunf//732rUqJFHvH///vrqq680d+5crVixQvv379c999xjbc/OzlbHjh2VmZmpVatWadasWZo5c6aGDRtmjUlISFDHjh3Vtm1bbdq0Sf369dNjjz2mJUuWWGM+/vhjDRgwQMOHD9fGjRvVuHFjxcbG6tChQxc1HwAAAAAApItouseNG6d33nlHHTp0UGZmpgYNGqSrr75aK1eu1NixYwudwPHjx9WtWzf95z//UWhoqBVPTU3V9OnTNXHiRN18881q3ry5ZsyYoVWrVmn16tWSztzq/vPPP+uDDz5QkyZN1KFDB7300kuaOnWqMjMzJUnTpk1T9erVNWHCBNWrV099+/bVvffeq0mTJlnPNXHiRD3++OPq2bOn6tevr2nTpqls2bJ67733Cj0fAAAAAADcCv2e7quvvlq7du3Sm2++qfLly+v48eO655571KdPH11xxRWFTqBPnz7q2LGj2rVrp5dfftmKb9iwQadPn1a7du2sWN26dVW1alXFxcWpVatWiouLU8OGDRUZGWmNiY2N1RNPPKFt27apadOmiouL89iHe4z7NvbMzExt2LBBQ4YMsbY7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339fr7zyiiSVuhMzpWs2KPHO/dAkl8ulW2+9Ve3bt9dXX30liRdTlxOHw6Grr75a999/v8aMGaPjx49z4uUyVLduXT3zzDP64IMPdODAgeJOB8Usr38D2rRpozp16ujZZ5+VVPpejF2O8vu3vn///jp06JDGjRsnibeclCa1atVSvXr19N5770mSnE5nMWeEksL992Dw4ME6dOiQNm/eLKl0nXTjXy1cUu5/PI8dOybDMORwOFShQgU1btxY//nPf3Tq1Cnex1WKnfsi6/Tp05KkO+64Q3/++af279+f5ziULi+99JKeffZZLVmyxIrddNNN2rNnjxISEiSxBi5n7ob6+PHjHvHBgwcrKytLixcvllS6Xoxdjtx1/uCDD/Ttt9/qxIkTkqSAgAD16dNHq1ev1uHDh4szRfwN5/4Nd1/VfuWVV/THH3/ov//9b3GkhRLi3L/f7r8Hbdq0UVJSknXnW2k66UbTjUtu5syZat++vRYsWGD9g/rKK68oLCzMuqWkNP2S4Sz3H9XvvvtOR44cUZkyZSRJDz30kDIyMkrtLUXwVLFiRf3444/q16+fOnbsqO+++05t27ZVhw4d9Nxzzyk7O5s1cJl79913VaNGDQ0bNsy64nH11VcrICBA8+bNk8S/E6XB8ePH9dJLL2nIkCGKiYnR0qVLlZiYqB49emjdunVasWJFcaeIi+T+G/7ll1/q+PHjVtNdsWJFNWzYUCtXrpTEybPLlfvv98cff6y33nrLikdERGjo0KH6+OOPrb/9pQWvanDJORwONW7cWA8//LAeeeQRjRw5UmlpaWrTpo327NnDe3xKue+++059+vTR1VdfrenTp2vNmjWSpJEjR2r37t2Kj48v5gxRlPK6Yv3EE09o/vz5mj17tk6fPq3BgwerSZMm8vPzU3JysjZs2JDvY3F5uO+++/Too49q8+bNatWqlfr376/Nmzdr/PjxWrhwoX744YfiThEX4dzf6XLlymnTpk1666231KJFCz311FO68847tWDBAv3jH//QG2+8oSNHjhRTtvi7du/era5du6pNmzbq06ePduzYoYoVK2rAgAGaOXOmfvjhB06eXcaSkpL03nvvafz48WratKmmTZumhIQEdezYUcHBwVbTXVr6AsPkFBNs5HK58r1itXr1aq1cuVJTpkxR06ZNZRiGFi5cqI8//lj33Xff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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df_instacart_orders \n",
    "\n",
    "# Count orders by day of the week (order_dow)\n",
    "daily_order_counts = df_instacart_orders['order_dow'].value_counts().sort_index()\n",
    "\n",
    "# Define day names for plotting\n",
    "day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']\n",
    "\n",
    "# Plotting the distribution of orders by day of the week\n",
    "plt.figure(figsize=(10, 6))\n",
    "daily_order_counts.plot(kind='bar', color='skyblue')\n",
    "plt.title('Number of Orders by Day of the Week')\n",
    "plt.xlabel('Day of the Week (0=Sunday, 1=Monday, ..., 6=Saturday)')\n",
    "plt.ylabel('Number of Orders')\n",
    "plt.xticks(range(7), day_names, rotation=45)\n",
    "plt.grid(axis='y', linestyle='--', alpha=0.7)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6a7b56b",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Could you please remove `import matplotlib.pyplot as plt` throughout the project?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dominant-lightning",
   "metadata": {},
   "source": [
    "Counted order by day of the week using value_counts and plotting the days of the week. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cutting-concert",
   "metadata": {},
   "source": [
    "### [A4] How long do people wait until placing another order?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c231f523",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAACmdUlEQVR4nOzdd3yT5frH8W+S7g2lAyiUspdshToAFa1aceE4DjYOBBVwHReoqKhH1jmi6JHh4qjgAEUZouAPxQVUZCsUCrSlZbSlu02e3x+xkdCWERtC4uf9evG6zf3cee7rypPUXHmWyTAMQwAAAAAAoM6ZPR0AAAAAAAC+iqIbAAAAAAA3oegGAAAAAMBNKLoBAAAAAHATim4AAAAAANyEohsAAAAAADeh6AYAAAAAwE0ougEAAAAAcBOKbgAAAAAA3ISiGwDg5Mknn5TJZDotc/Xt21d9+/Z1PF65cqVMJpMWLFhwWuYfMmSImjVrdlrmclVhYaFGjBih+Ph4mUwmjRkzxtMhedTpfH96islk0pNPPunpMOqMN3zOAMCdKLoBwIfNnTtXJpPJ8S8oKEiNGjVSSkqK/v3vf+vIkSN1Mk9mZqaefPJJpaWl1cn66tKZHNvJeO655zR37lyNHDlSb7/9tgYOHFjr2GbNmjm2tdlsVlRUlM466yzdcccd+uGHH05j1KeusLBQEyZMUMeOHRUaGqro6Gh16dJF9913nzIzMz0d3knr27ev02eufv36OvvsszV79mzZbDZPh1ejgwcP6sEHH1SbNm0UFBSk+vXrKyUlRZ999pmnQwMAn2AyDMPwdBAAAPeYO3euhg4dqqefflpJSUmqqKhQdna2Vq5cqeXLl6tp06ZatGiROnXq5HhOZWWlKisrFRQUdNLz/Pzzzzr77LM1Z84cDRky5KSfV15eLkkKCAiQZN/TfeGFF2r+/Pm6/vrrT3o9rsZWUVEhm82mwMDAOpnLHXr16iU/Pz+tXr36hGObNWumevXq6f7775ckHTlyRFu2bNH8+fOVnZ2tsWPHasqUKe4O+ZRVVFSoZ8+e2rp1qwYPHqwuXbqosLBQmzZt0qeffqr58+c7johw5f15OvXt21c7duzQpEmTJEm5ubl66623lJaWpocffljPP//8CddRWloqPz8/+fn5uTtcbdu2TRdffLFyc3M1dOhQ9ejRQ3l5eXr33XeVlpamBx54QP/617/+0hxDhgzRypUrtWvXrroJGgC8jPv/mgMAPO7yyy9Xjx49HI8feeQRffXVV7ryyit11VVXacuWLQoODpak0/Jlv7i4WCEhIY5i21P8/f09Ov/JyMnJUfv27U96fOPGjXXbbbc59b3wwgu65ZZbNHXqVLVq1UojR46s6zD/kk8++UTr16/Xu+++q1tuucVpWWlpqePHGen0vD//qsjISKdtcOedd6pNmzZ6+eWXNXHixBrfdzabTeXl5QoKCqrTHxSKiooUGhpa47KKigpdf/31Onz4sL755hv17NnTsWzs2LG69dZb9dJLL6lHjx666aabap2jtLRUAQEBMpvdfwClYRgqLS11/L0CAG/A4eUA8Dd10UUX6YknntDu3bv1zjvvOPprOmd2+fLlOv/88xUVFaWwsDC1adNGjz76qCT73umzzz5bkjR06FDHYbVz586VZN/z17FjR61du1a9e/dWSEiI47nHntNdxWq16tFHH1V8fLxCQ0N11VVXac+ePU5jmjVrVuNe9aPXeaLYajrXtKioSPfff7+aNGmiwMBAtWnTRi+99JKOPTDMZDJp9OjR+uSTT9SxY0cFBgaqQ4cOWrJkSc0v+DFycnI0fPhwxcXFKSgoSJ07d9abb77pWF51fnt6eroWL17siN2VvYXBwcF6++23Vb9+fT377LNOubz00ks699xzFR0dreDgYHXv3r3aOfV9+vRR586da1x3mzZtlJKS4nj83nvvqXv37goPD1dERITOOussTZ8+/bjx7dixQ5J03nnnVVsWFBSkiIgIx+Oa3p+nsi327dun4cOHq1GjRgoMDFRSUpJGjhzpVNjn5eVpzJgxjvdAy5Yt9cILL7h8eHhISIh69eqloqIi5ebmOsX87rvvqkOHDgoMDHTEW9M53evXr9fll1+uiIgIhYWF6eKLL9b333/vNKbqdJJVq1bp7rvvVmxsrBISEmqN68MPP9TGjRv1z3/+06ngliSLxaLXXntNUVFRTrFUvS/fe+89Pf7442rcuLFCQkJUUFAgSY5tEBQUpI4dO+rjjz+ucW6bzaZp06apQ4cOCgoKUlxcnO68804dPnzYaVyzZs105ZVXaunSperRo4eCg4P12muv1f5iA8AZ6Mz+qRgA4FYDBw7Uo48+qmXLlun222+vccymTZt05ZVXqlOnTnr66acVGBio33//Xd9++60kqV27dnr66ac1fvx43XHHHbrgggskSeeee65jHQcPHtTll1+uf/zjH7rtttsUFxd33LieffZZmUwmPfzww8rJydG0adPUr18/paWlndIerpOJ7WiGYeiqq67S119/reHDh6tLly5aunSpHnzwQe3bt09Tp051Gr969Wp99NFHuvvuuxUeHq5///vfGjBggDIyMhQdHV1rXCUlJerbt69+//13jR49WklJSZo/f76GDBmivLw83XfffWrXrp3efvttjR07VgkJCY5DxmNiYk46/6OFhYXp2muv1axZs7R582Z16NBBkjR9+nRdddVVuvXWW1VeXq733ntPN9xwgz777DOlpqZKsr9Pbr/9dm3cuFEdO3Z0rPOnn37S9u3b9fjjj0uy/zhz88036+KLL9YLL7wgSdqyZYu+/fZb3XfffbXGlpiYKEl666239Pjjj7t0obST2RaZmZk655xzlJeXpzvuuENt27bVvn37tGDBAhUXFysgIEDFxcXq06eP9u3bpzvvvFNNmzbVd999p0ceeURZWVmaNm3aKccmSTt37pTFYlFUVJSj76uvvtIHH3yg0aNHq0GDBrVebGzTpk264IILFBERoYceekj+/v567bXX1LdvX61atapawXz33XcrJiZG48ePV1FRUa0xffrpp5KkQYMG1bg8MjJSV199td588039/vvvatmypWPZxIkTFRAQoAceeEBlZWUKCAjQsmXLNGDAALVv316TJk3SwYMHNXTo0BoL/zvvvNNx+su9996r9PR0vfzyy1q/fr2+/fZbp6MBtm3bpptvvll33nmnbr/9drVp06bWnADgjGQAAHzWnDlzDEnGTz/9VOuYyMhIo2vXro7HEyZMMI7+38PUqVMNSUZubm6t6/jpp58MScacOXOqLevTp48hyZg5c2aNy/r06eN4/PXXXxuSjMaNGxsFBQWO/g8++MCQZEyfPt3Rl5iYaAwePPiE6zxebIMHDzYSExMdjz/55BNDkvHMM884jbv++usNk8lk/P77744+SUZAQIBT3y+//GJIMv7zn/9Um+to06ZNMyQZ77zzjqOvvLzcSE5ONsLCwpxyT0xMNFJTU4+7vpMdW7UtFy5c6OgrLi52GlNeXm507NjRuOiiixx9eXl5RlBQkPHwww87jb333nuN0NBQo7Cw0DAMw7jvvvuMiIgIo7Ky8qTiPTqGNm3aGJKMxMREY8iQIcasWbOM/fv3Vxt77PvTME5+WwwaNMgwm801fh5sNpthGIYxceJEIzQ01Ni+fbvT8n/+85+GxWIxMjIyjptLnz59jLZt2xq5ublGbm6usWXLFuPee+81JBn9+/d3itlsNhubNm2qtg5JxoQJExyPr7nmGiMgIMDYsWOHoy8zM9MIDw83evfu7eir+ryff/75J7UNunTpYkRGRh53zJQpUwxJxqJFiwzD+PMz2rx582rvnS5duhgNGzY08vLyHH3Lli1zbNcq//d//2dIMt59912n5y9ZsqRaf2JioiHJWLJkyQnzAYAzFYeXA8DfXFhY2HGvYl61Z27hwoUuH14bGBiooUOHnvT4QYMGKTw83PH4+uuvV8OGDfX555+7NP/J+vzzz2WxWHTvvfc69d9///0yDENffPGFU3+/fv3UokULx+NOnTopIiJCO3fuPOE88fHxuvnmmx19/v7+uvfee1VYWKhVq1bVQTbVhYWFSZLT9j76yIHDhw8rPz9fF1xwgdatW+for9rj+b///c9xaLrVatX777+va665xnHOcFRUlIqKirR8+fJTiis4OFg//PCDHnzwQUn2w6SHDx+uhg0b6p577lFZWdkJ13GibWGz2fTJJ5+of//+Ttc3qFK1d33+/Pm64IILVK9ePR04cMDxr1+/frJarfrmm29OGMvWrVsVExOjmJgYtWvXTv/5z3+Umpqq2bNnO43r06fPCc/Xt1qtWrZsma655ho1b97c0d+wYUPdcsstWr16tePQ7iq33367LBbLCeM8cuSI0+esJlXLj51j8ODBTu+drKwspaWlafDgwYqMjHT0X3LJJdVynD9/viIjI3XJJZc4vcbdu3dXWFiYvv76a6fxSUlJTqcwAIC3oegGgL+5wsLC437xvummm3TeeedpxIgRiouL0z/+8Q998MEHp1SAN27c+JQumtaqVSunxyaTSS1btnT71Y93796tRo0aVXs92rVr51h+tKZNm1ZbR7169aqdl1rTPK1atap24ana5qkrhYWFkuSU32effaZevXo5bhUVExOjV199Vfn5+U7PHTRokDIyMvR///d/kqQvv/xS+/fvd7qF2d13363WrVvr8ssvV0JCgoYNG3bS57hHRkbqxRdf1K5du7Rr1y7NmjXL6eJjJ3KibZGbm6uCggKnw+Nr8ttvv2nJkiWOornqX79+/STZz8U/kWbNmmn58uX68ssvtXr1amVnZ+uzzz5TgwYNnMYlJSWdcF25ubkqLi6u8ZDqdu3ayWazVbvewcmsV7K/D05028Cq5cd+Jo6do+o9e+xnV1K12H/77Tfl5+crNja22utcWFhY7TU+2XwA4EzFOd0A8De2d+9e5efnO52reazg4GB98803+vrrr7V48WItWbJE77//vi666CItW7bspPaoueNKw7Wd92u1Wk8qprpQ2zzGGXo3zo0bN0qSY3v/3//9n6666ir17t1br7zyiho2bCh/f3/NmTNH8+bNc3puSkqK4uLi9M4776h379565513FB8f7yhGJSk2NlZpaWlaunSpvvjiC33xxReaM2eOBg0a5HSRuBNJTEzUsGHDdO2116p58+Z699139cwzzxz3OXW1LWw2my655BI99NBDNS5v3br1CdcRGhrq9LrUxl1X4D7Z9bZr105paWnKyMio8UcLSdqwYYMkVdtb/Vdit9lsio2N1bvvvlvj8mOvW8CVygF4O4puAPgbe/vttyXphIdums1mXXzxxbr44os1ZcoUPffcc3rsscf09ddfq1+/fi5d+Op4fvvtN6fHhmHo999/d7qfeL169ZSXl1ftubt373Y6DPdUYktMTNSXX35Z7bDbrVu3OpbXhcTERG3YsEE2m81pb3ddz3O0wsJCffzxx2rSpIljj/qHH36ooKAgLV261Ole5XPmzKn2fIvFoltuuUVz587VCy+8oE8++aTGw5gDAgLUv39/9e/fXzabTXfffbdee+01PfHEE8f9cacm9erVU4sWLRw/FvwVMTExioiIOOG6WrRoocLCwpMqmk+HmJgYhYSEaNu2bdWWbd26VWazWU2aNHFp3VdeeaX+97//OS5gd6yCggItXLhQbdu2PeG2q3rPHvvZlVQt9hYtWujLL7/UeeedR0EN4G+Bw8sB4G/qq6++0sSJE5WUlKRbb7211nGHDh2q1telSxdJcpxrW3VOb01FsCveeustp8NeFyxYoKysLF1++eWOvhYtWuj77793utXTZ599Vu1Q21OJ7YorrpDVatXLL7/s1D916lSZTCan+f+KK664QtnZ2Xr//fcdfZWVlfrPf/6jsLAw9enTp07mqVJSUqKBAwfq0KFDeuyxxxw/RFgsFplMJlmtVsfYXbt26ZNPPqlxPQMHDtThw4d15513qrCwsNr9wA8ePOj02Gw2O34oOd552b/88osOHDhQrX/37t3avHlznVyt2mw265prrtGnn36qn3/+udryqj3iN954o9asWaOlS5dWG5OXl6fKysq/HMupsFgsuvTSS7Vw4UKn0yv279+vefPm6fzzz3e6pdqpuP7669W+fXs9//zz1V4Tm82mkSNH6vDhw5owYcIJ19WwYUN16dJFb775ptOpCcuXL9fmzZudxt54442yWq01njZQWVlZZ39HAOBMwZ5uAPgb+OKLL7R161ZVVlZq//79+uqrr7R8+XIlJiZq0aJFCgoKqvW5Tz/9tL755hulpqYqMTFROTk5euWVV5SQkKDzzz9fkr0AjoqK0syZMxUeHq7Q0FD17NnT5XMx69evr/PPP19Dhw7V/v37NW3aNLVs2dLptmYjRozQggULdNlll+nGG2/Ujh079M477zhdTOtUY+vfv78uvPBCPfbYY9q1a5c6d+6sZcuWaeHChRozZky1dbvqjjvu0GuvvaYhQ4Zo7dq1atasmRYsWKBvv/1W06ZNO+HFrY5n3759jvuuFxYWavPmzZo/f76ys7N1//33684773SMTU1N1ZQpU3TZZZfplltuUU5OjmbMmKGWLVs6Dis+WteuXdWxY0fNnz9f7dq1U7du3ZyWjxgxQocOHdJFF12khIQE7d69W//5z3/UpUsXx971mixfvlwTJkzQVVddpV69eiksLEw7d+7U7NmzVVZWVu2e1a567rnntGzZMvXp00d33HGH2rVrp6ysLM2fP1+rV69WVFSUHnzwQS1atEhXXnmlhgwZou7du6uoqEi//vqrFixYoF27dlU7N9vdnnnmGS1fvlznn3++7r77bvn5+em1115TWVmZXnzxRZfXGxAQoAULFujiiy92fN569OihvLw8zZs3T+vWrdP999+vf/zjHye1vkmTJik1NVXnn3++hg0bpkOHDuk///mPOnTo4LiegGS/gNydd96pSZMmKS0tTZdeeqn8/f3122+/af78+Zo+fbquv/56l/MCgDOOJy+dDgBwr6pbCFX9CwgIMOLj441LLrnEmD59utOtqaoce0umFStWGFdffbXRqFEjIyAgwGjUqJFx8803V7ul0sKFC4327dsbfn5+Trfo6tOnj9GhQ4ca46vtlmH/+9//jEceecSIjY01goODjdTUVGP37t3Vnj958mSjcePGRmBgoHHeeecZP//8c7V1Hi+2Y28ZZhiGceTIEWPs2LFGo0aNDH9/f6NVq1bGv/71L8ctpapIMkaNGlUtptpuZXas/fv3G0OHDjUaNGhgBAQEGGeddVaNtzU71VuGVW1rk8lkREREGB06dDBuv/1244cffqjxObNmzTJatWplBAYGGm3btjXmzJlT4225qrz44ouGJOO5556rtmzBggXGpZdeasTGxhoBAQFG06ZNjTvvvNPIyso6btw7d+40xo8fb/Tq1cuIjY01/Pz8jJiYGCM1NdX46quvnMbWdsuwk90Wu3fvNgYNGmTExMQYgYGBRvPmzY1Ro0YZZWVljjFHjhwxHnnkEaNly5ZGQECA0aBBA+Pcc881XnrpJaO8vPy4uRzv/X4yMVctO/qWYYZhGOvWrTNSUlKMsLAwIyQkxLjwwguN7777zmnMydwisCY5OTnGuHHjjJYtWxqBgYFGVFSU0a9fP8dtwo5W9RmdP39+jev68MMPjXbt2hmBgYFG+/btjY8++qjGz5lhGMbrr79udO/e3QgODjbCw8ONs846y3jooYeMzMxMx5hTef8DwJnKZBhn6NVeAADAGWf69OkaO3asdu3aVevFtwAAwJ8ougEAwEkxDEOdO3dWdHR0tXspAwCAmnFONwAAOK6ioiItWrRIX3/9tX799VctXLjQ0yEBAOA12NMNAACOa9euXUpKSlJUVJTuvvtuPfvss54OCQAAr0HRDQAAAACAm3CfbgAAAAAA3ISiGwAAAAAAN+FCanXEZrMpMzNT4eHhMplMng4HAAAAAOBGhmHoyJEjatSokczm2vdnU3TXkczMTDVp0sTTYQAAAAAATqM9e/YoISGh1uUU3XUkPDxckv0Fj4iI8HA0AKqkZaepz5w+WjV0lbrEd/F0ODhVaWlSnz7SqlVSly6ejgYAAMChoKBATZo0cdSCtaHoriNVh5RHRERQdANnkLCiMClICgsP47PpjcLC/mzZfgAA4Ax0otOLuZAaAAAAAABuQtENwKeZTWaFB4TLbOLPnVcym6XwcHsLAADghUyGYRieDsIXFBQUKDIyUvn5+RzCCgAAAAA+7mRrQM7pPs2sVqsqKio8HQZwWgUEBBz3NgoAAACAr6LoPk0Mw1B2drby8vI8HQpw2pnNZiUlJSkgIOC0z705d7NumH+D5t8wX+1j2p/2+fEXbd4s3XCDNH++1J7tBwAAvA9F92lSVXDHxsYqJCTkhFe4A3yFzWZTZmamsrKy1LRp09P+3i+tLNXm3M0qrSw9rfOijpSW2gvvUrYfAADwThTdp4HVanUU3NHR0Z4OBzjtYmJilJmZqcrKSvn7+3s6HAAAAOC04STL06DqHO6QkBAPRwJ4RtVh5Var1cORAAAAAKcXRfdpxCHl+LvivQ8AAIC/K4puAD6teb3mWviPhWper7mnQ4ErmjeXFi60twAAAF6Iohv4m5g7d66ioqI8HcZpFxUUpavaXKWooChPhwJXREVJV11lbwEAALwQRTdOypo1a2SxWJSamurpUDwiKytLt9xyi1q3bi2z2awxY8ZUG7Np0yYNGDBAzZo1k8lk0rRp00643tLSUg0ZMkRnnXWW/Pz8dM0119Q4buXKlerWrZsCAwPVsmVLzZ079y/l83eSXZitSf83SdmF2Z4OBa7IzpYmTbK3AAAAXoiiGydl1qxZuueee/TNN98oMzPTrXMZhqHKykq3znGqysrKFBMTo8cff1ydO3eucUxxcbGaN2+u559/XvHx8Se1XqvVquDgYN17773q169fjWPS09OVmpqqCy+8UGlpaRozZoxGjBihpUuXupzP30nmkUw9+tWjyjzi3vct3CQzU3r0UXsLAADghSi6cUKFhYV6//33NXLkSKWmpjrtZb3lllt00003OY2vqKhQgwYN9NZbb0my36d50qRJSkpKUnBwsDp37qwFCxY4xq9cuVImk0lffPGFunfvrsDAQK1evVo7duzQ1Vdfrbi4OIWFhenss8/Wl19+6TRXVlaWUlNTFRwcrKSkJM2bN0/NmjVz2sucl5enESNGKCYmRhEREbrooov0yy+/nNJr0KxZM02fPl2DBg1SZGRkjWPOPvts/etf/9I//vEPBQYGntR6Q0ND9eqrr+r222+vtVCfOXOmkpKSNHnyZLVr106jR4/W9ddfr6lTpx533XPnzlXTpk0VEhKia6+9VgcPHnRafqLX9+mnn1bHjh2rrbdLly564oknJNm33TnnnKPQ0FBFRUXpvPPO0+7du08qdwAAAODvgKIbJ/TBBx+obdu2atOmjW677TbNnj1bhmFIkm699VZ9+umnKiwsdIxfunSpiouLde2110qSJk2apLfeekszZ87Upk2bNHbsWN12221atWqV0zz//Oc/9fzzz2vLli3q1KmTCgsLdcUVV2jFihVav369LrvsMvXv318ZGRmO5wwaNEiZmZlauXKlPvzwQ73++uvKyclxWu8NN9ygnJwcffHFF1q7dq26deumiy++WIcOHZIk7dq1SyaTSStXrnTHy/eXrVmzptpe8JSUFK1Zs6bW5/zwww8aPny4Ro8erbS0NF144YV65plnnMac6PUdNmyYtmzZop9++snxnPXr12vDhg0aOnSoKisrdc0116hPnz7asGGD1qxZozvuuIMrlQMAAABH8fN0AH97WVn2f0erV09KSpJKS6XNm6s/p1s3e7ttm1RU5LysWTOpfn0pN1fas8d5WcOG9n+naNasWbrtttskSZdddpny8/O1atUq9e3bVykpKQoNDdXHH3+sgQMHSpLmzZunq666SuHh4SorK9Nzzz2nL7/8UsnJyZKk5s2ba/Xq1XrttdfUp08fxzxPP/20LrnkEsfj+vXrOx3KPXHiRH388cdatGiRRo8era1bt+rLL7/UTz/9pB49ekiS3njjDbVq1crxnNWrV+vHH39UTk6OY+/zSy+9pE8++UQLFizQHXfcIX9/f7Vp0+aMvY96dna24uLinPri4uJUUFCgkpISBQcHV3vO9OnTddlll+mhhx6SJLVu3VrfffedlixZ4hjTuXPn476+CQkJSklJ0Zw5c3T22WdLkubMmaM+ffqoefPmOnTokPLz83XllVeqRYsWkqR27drVef4AAACAN2NPt6e99prUvbvzvz8O3dXevdWXde/+53OHDKm+7PPP7cs++KD6stdeO+Xwtm3bph9//FE333yzJMnPz0833XSTZs2a5Xh844036t1335UkFRUVaeHChbr11lslSb///ruKi4t1ySWXKCwszPHvrbfe0o4dO5zmqiqcqxQWFuqBBx5Qu3btFBUVpbCwMG3ZssWxJ3bbtm3y8/NTt6ofISS1bNlS9erVczz+5ZdfVFhYqOjoaKf509PTHfM3btxYW7du1TnnnHPKr8+ZasuWLerZs6dTX9WPHlVO9PpK0u23367//e9/Ki0tVXl5uebNm6dhw4ZJsv8oMmTIEKWkpKh///6aPn26so79AekMEBUUpevbX8/Vy71VVJR0/fVcvRwAAHgt9nR72p132m+Hc7SqojEhQVq7tvbnzp1b855uSbrxRumYIsvVvdyVlZVq1KiRo88wDAUGBurll19WZGSkbr31VvXp00c5OTlavny5goODddlll0mS47DzxYsXq3Hjxk7rPva859DQUKfHDzzwgJYvX66XXnpJLVu2VHBwsK6//nqVl5efdPyFhYVq2LBhjYeOe8vts+Lj47V//36nvv379ysiIqLGvdwn62Re3/79+yswMFAff/yxAgICVFFRoeuvv96xfM6cObr33nu1ZMkSvf/++3r88ce1fPly9erVy+W46lrzes01/4b5ng4DrmreXJrP9gMAAN6LotvTjnfId1DQn4eS16RNm9qXxcTY//0FlZWVeuuttzR58mRdeumlTsuuueYa/e9//9Ndd92lc889V02aNNH777+vL774QjfccIP8/f0lSe3bt1dgYKAyMjKcDiU/Gd9++62GDBniODe8sLBQu3btcixv06aNKisrtX79enX/4wiA33//XYcPH3aM6datm7Kzs+Xn56dmVT9IeJnk5GR9XnUEwx+WL19ebc/10dq1a6cffvjBqe/77793enyi11eyH8kwePBgzZkzRwEBAfrHP/5RrdDv2rWrunbtqkceeUTJycmaN2/eGVV0l1vLlVOUo9jQWAVYAjwdDk5VebmUkyPFxkoBbD8AAOB9KLpRq88++0yHDx/W8OHDq12xe8CAAZo1a5buuusuSfarmM+cOVPbt2/X119/7RgXHh6uBx54QGPHjpXNZtP555+v/Px8ffvtt4qIiNDgwYNrnb9Vq1b66KOP1L9/f5lMJj3xxBOy2WyO5W3btlW/fv10xx136NVXX5W/v7/uv/9+BQcHOy7m1a9fPyUnJ+uaa67Riy++qNatWyszM1OLFy/Wtddeqx49emjfvn26+OKL9dZbbx33EPO0tDRJ9uI0NzdXaWlpCggIUPv27SVJ5eXl2vzHOfjl5eXat2+f0tLSFBYWppYtW0qSXn75ZX388cdasWKFY72bN29WeXm5Dh06pCNHjjjm6dKliyTprrvu0ssvv6yHHnpIw4YN01dffaUPPvhAixcvrjXWe++9V+edd55eeuklXX311Vq6dKnT+dwn8/pWGTFihONc7W+//dbRn56ertdff11XXXWVGjVqpG3btum3337ToEGDao3LEzbmbFT317tr7R1r1a3hcX7Ewplp40b76TFr1x7/R0gAAIAzFEU3ajVr1iz169evxltkDRgwQC+++KI2bNigTp066dZbb9Wzzz6rxMREnXfeeU5jJ06cqJiYGE2aNEk7d+5UVFSUunXrpkcfffS480+ZMkXDhg3TueeeqwYNGujhhx9WQUGB05i33npLw4cPV+/evRUfH69JkyZp06ZNCgoKkiSZTCZ9/vnneuyxxzR06FDl5uYqPj5evXv3dlycrKKiQtu2bVNxcfFx4+natavjv9euXat58+YpMTHRsXc4MzPTacxLL72kl156SX369HEc3n7gwIFq57JfccUVTrfZqlpH1RXik5KStHjxYo0dO1bTp09XQkKC3njjDaWkpNQaa69evfTf//5XEyZM0Pjx49WvXz89/vjjmjhx4im9vpK9OD/33HN16NAhp/PEQ0JCtHXrVr355ps6ePCgGjZsqFGjRunOO+887usIAAAA75Wbm1vjd0Z3iIiIUMxfPHr3TGAyqr7Z4y8pKChQZGSk8vPzFRER4bSstLRU6enpSkpKchSDcI+9e/eqSZMm+vLLL3XxxRd7OhyfYBiGWrVqpbvvvlvjxo1zaR2e/Aysy1rHnm5vtm4de7oBADhD5Obmatgdd+lISelpmS88OEizX595xhbex6sBj8aebni1r776SoWFhTrrrLOUlZWlhx56SM2aNVPv3r09HZpPyM3N1Xvvvafs7GwNHTrU0+EAAADAgwoKCnSkpFR9B45UdMMEt851MGuvVr79qgoKCs7YovtkUXTDq1VUVOjRRx/Vzp07FR4ernPPPVfvvvuu40Ju+GtiY2PVoEEDvf766063YgMAAMDfV3TDBMUnJnk6DK9B0Q2vlpKSctxzm/HX+MLZJ13iu6j0sVL5W/ghxit16SKVlkr8kAYAALwURTcAn2Y2mRXoF3jigTgzmc1SINsPAAB4L7OnAwAAd9p+cLv6zu2r7Qe3ezoUuGL7dqlvX3sLAADghSi6Afi0wvJCrdq9SoXlhZ4OBa4oLJRWrbK3AAAAXoiiGwAAAAAAN6HoBgAAAADATSi6AQAAAABwE4pueNzKlStlMpmUl5cnSZo7d66ioqI8GtOZaNeuXTKZTEpLS/N0KF6laWRT/bf/f9U0sqmnQ4ErmjaV/vtfewsAAOCFKLpxXEOGDJHJZNJdd91VbdmoUaNkMpk0ZMiQOp3zpptu0nYPXKm4qviv6d9PP/1U6/NKS0s1atQoRUdHKywsTAMGDND+/fudxmRkZCg1NVUhISGKjY3Vgw8+qMrKSnenBEkNQhpoRLcRahDSwNOhwBUNGkgjRthbAAAAL0TRjRNq0qSJ3nvvPZWUlDj6SktLNW/ePDV1w96n4OBgxcbG1vl6T+Tcc89VVlaW078RI0YoKSlJPXr0qPV5Y8eO1aeffqr58+dr1apVyszM1HXXXedYbrValZqaqvLycn333Xd68803NXfuXI0fP/50pPW3d6D4gN5Y94YOFB/wdChwxYED0htv2FsAAAAvRNGNE+rWrZuaNGmijz76yNH30UcfqWnTpuratavTWJvNpkmTJikpKUnBwcHq3LmzFixY4DTm888/V+vWrRUcHKwLL7xQu3btclp+7OHlO3bs0NVXX624uDiFhYXp7LPP1pdffun0nGbNmum5557TsGHDFB4erqZNm+r1118/pTwDAgIUHx/v+BcdHa2FCxdq6NChMplMNT4nPz9fs2bN0pQpU3TRRRepe/fumjNnjr777jt9//33kqRly5Zp8+bNeuedd9SlSxddfvnlmjhxombMmKHy8vJa4/nxxx/VtWtXBQUFqUePHlq/fr3TcqvVquHDhzte6zZt2mj69OmO5d988438/f2VnZ3t9LwxY8boggsukCTt3r1b/fv3V7169RQaGqoOHTro888/P6XX7UyXkZ+h2z+9XRn5GZ4OBa7IyJBuv93eAgAAeCGKbpyUYcOGac6cOY7Hs2fP1tChQ6uNmzRpkt566y3NnDlTmzZt0tixY3Xbbbdp1apVkqQ9e/bouuuuU//+/ZWWlqYRI0bon//853HnLiws1BVXXKEVK1Zo/fr1uuyyy9S/f39lHPMlfPLkyY7i9O6779bIkSO1bds2x/K+ffue0qHwixYt0sGDB2vMs8ratWtVUVGhfv36Ofratm2rpk2bas2aNZKkNWvW6KyzzlJcXJxjTEpKigoKCrRp06Zac77yyivVvn17rV27Vk8++aQeeOABpzE2m00JCQmaP3++Nm/erPHjx+vRRx/VBx98IEnq3bu3mjdvrrffftvxnIqKCr377rsaNmyYJPspAmVlZfrmm2/066+/6oUXXlBYWNhJv0YAAAAAjs/P0wH83WUdyVJWYZZTX72gekqql6TSylJtzt1c7TndGnaTJG07sE1FFUVOy5pFNVP94PrKLcrVnoI9TssahjVUw/CGLsV522236ZFHHtHu3bslSd9++63ee+89rVy50jGmrKxMzz33nL788kslJydLkpo3b67Vq1frtddeU58+ffTqq6+qRYsWmjx5siSpTZs2jmKvNp07d1bnzp0djydOnKiPP/5YixYt0ujRox39V1xxhe6++25J0sMPP6ypU6fq66+/Vps2bSRJTZs2VcOGJ5//rFmzlJKSooSEhFrHZGdnKyAgoNqF3+Li4hx7mLOzs50K7qrlVctqMm/ePNlsNs2aNUtBQUHq0KGD9u7dq5EjRzrG+Pv766mnnnI8TkpK0po1a/TBBx/oxhtvlCQNHz5cc+bM0YMPPihJ+vTTT1VaWupYnpGRoQEDBuiss86SZN9eAAAAAOoORbeHvbb2NT216imnvlvPulXvXPeO9hbsVffXu1d7jjHBkCQNWThE3+/93mnZ29e+rds63aYPNn2g0V+Mdlo2oc8EPdn3SZfijImJUWpqqubOnSvDMJSamqoGx1zY6Pfff1dxcbEuueQSp/7y8nLHYehbtmxRz549nZZXFei1KSws1JNPPqnFixcrKytLlZWVKikpqbanu1OnTo7/NplMio+PV05OjqPvrbfeOul89+7dq6VLlzr2Gp9uW7ZsUadOnRQUFOToq+l1mjFjhmbPnq2MjAyVlJSovLxcXbp0cSwfMmSIHn/8cX3//ffq1auX5s6dqxtvvFGhoaGSpHvvvVcjR47UsmXL1K9fPw0YMMDpdQQAAADw11B0e9id3e/UVW2ucuqrF1RPkpQQkaC1d6yt9blzr55b455uSbqxw41KbuJcpDUMc20vd5Vhw4Y59izPmDGj2vLCwkJJ0uLFi9W4cWOnZYGBgS7P+8ADD2j58uV66aWX1LJlSwUHB+v666+vdj60v7+/02OTySSbzebSnHPmzFF0dLSuuuqq446Lj49XeXm58vLynPZ279+/X/Hx8Y4xP/74o9Pzqq5uXjXGFe+9954eeOABTZ48WcnJyQoPD9e//vUv/fDDD44xsbGx6t+/v+bMmaOkpCR98cUXTkcnjBgxQikpKVq8eLGWLVumSZMmafLkybrnnntcjutMExYQpj6JfRQWwGHzXiksTOrTx94CAAB4IYpuD2sYXvsh30F+QY5DyWvSpkGbWpfFhMYoJjTmL8d3tMsuu0zl5eUymUxKSUmptrx9+/YKDAxURkaG+vTpU+M62rVrp0WLFjn1VV1wrDbffvuthgwZomuvvVaSvbg/9uJrdckwDM2ZM0eDBg2qVsgfq3v37vL399eKFSs0YMAASdK2bduUkZHh2DOdnJysZ599Vjk5OY6rsi9fvlwRERFq3759jett166d3n77bZWWljr2dh/7On377bc699xzHYfUS/aLzh1rxIgRuvnmm5WQkKAWLVrovPPOc1repEkT3XXXXbrrrrv0yCOP6L///a9PFd2to1tr5ZCVng4DrmrdWjrqhyIAAABvw4XUcNIsFou2bNmizZs3y2KxVFseHh6uBx54QGPHjtWbb76pHTt2aN26dfrPf/6jN998U5J011136bffftODDz6obdu2ad68eZo7d+5x523VqpU++ugjpaWl6ZdfftEtt9zi0h7sQYMG6ZFHHjnhuK+++krp6ekaMWJEtWX79u1T27ZtHXuuIyMjNXz4cI0bN05ff/211q5dq6FDhyo5OVm9evWSJF166aVq3769Bg4cqF9++UVLly7V448/rlGjRtV6BMAtt9wik8mk22+/XZs3b9bnn3+ul156yWlMq1at9PPPP2vp0qXavn27nnjiiRrvJ56SkqKIiAg988wz1S4KN2bMGC1dulTp6elat26dvv76a7Vr1+6Er5E3sRk2lVWWyWa4dtQDPMxmk8rK7C0AAIAXoujGKYmIiFBEREStyydOnKgnnnhCkyZNUrt27XTZZZdp8eLFSkpKkmS/mNmHH36oTz75RJ07d9bMmTP13HPPHXfOKVOmqF69ejr33HPVv39/paSkqFu32o8AqE1GRoaysrJOOG7WrFk699xz1bZt22rLKioqtG3bNhUXFzv6pk6dqiuvvFIDBgxQ7969FR8f73R7NYvFos8++0wWi0XJycm67bbbNGjQID399NO1xhAWFqZPP/1Uv/76q7p27arHHnus2sXm7rzzTl133XW66aab1LNnTx08eNBpr3cVs9msIUOGyGq1atCgQU7LrFarRo0a5dhWrVu31iuvvHLC18ibpGWnKejZIKVlp3k6FLgiLU0KCrK3AAAAXshkGIbh6SB8QUFBgSIjI5Wfn1+tKC0tLVV6erqSkpKcLowFnC7Dhw9Xbm5utUP7TxdPfgbWZa1T99e7a+0da497ugbOUOvWSd27S2vXSi782AYAAOrOjh07NHzUvRrw0LOK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wClzqeieNGmSXnvttWr9sbGxuuOOOyi6gTqSm5urYXfcpSMlpadlvvDgIM1+fabPFd4AAACAp7hUdGdkZCgpKalaf2JiojIyMv5yUADsCgoKdKSkVH0HjlR0wwS3znUwa69Wvv2qCgoKKLoBAACAOuJS0R0bG6sNGzZUuzr5L7/8oujo6LqIC8BRohsmKD6x+g9dAAAAAM5sLt2n++abb9a9996rr7/+WlarVVarVV999ZXuu+8+/eMf/6jrGAEAAAAA8EouFd0TJ05Uz549dfHFFys4OFjBwcG69NJLddFFF+m555476fW8+uqr6tSpkyIiIhQREaHk5GR98cUXjuWlpaUaNWqUoqOjFRYWpgEDBmj//v1O68jIyFBqaqpCQkIUGxurBx98UJWVlU5jVq5cqW7duikwMFAtW7bU3Llzq8UyY8YMNWvWTEFBQerZs6d+/PHHU3tRAJyRYvybKPaTZooLbubpUOCK9u2l336ztwAAAF7IpaI7ICBA77//vrZu3ap3331XH330kXbs2KHZs2crICDgpNeTkJCg559/XmvXrtXPP/+siy66SFdffbU2bdokSRo7dqw+/fRTzZ8/X6tWrVJmZqauu+46x/OtVqtSU1NVXl6u7777Tm+++abmzp2r8ePHO8akp6crNTVVF154odLS0jRmzBiNGDFCS5cudYx5//33NW7cOE2YMEHr1q1T586dlZKSopycHFdeHgBnED9zgPyOBMjfHOjpUOCKoCCpZUt7CwAA4IVcOqe7SuvWrdW6dWuXn9+/f3+nx88++6xeffVVff/990pISNCsWbM0b948XXTRRZLstypr166dvv/+e/Xq1UvLli3T5s2b9eWXXyouLk5dunTRxIkT9fDDD+vJJ59UQECAZs6cqaSkJE2ePFmS1K5dO61evVpTp05VSkqKJGnKlCm6/fbbNXToUEnSzJkztXjxYs2ePVv//Oc/Xc4Pvul03sJr9+7d1Y7cwKk5XJGtw+dl6VBZJrcM80bp6dITT0gTJ0o1XMATAADgTOdS0W21WjV37lytWLFCOTk5stlsTsu/+uorl9Y5f/58FRUVKTk5WWvXrlVFRYX69evnGNO2bVs1bdpUa9asUa9evbRmzRqdddZZiouLc4xJSUnRyJEjtWnTJnXt2lVr1qxxWkfVmDFjxkiSysvLtXbtWj3yyCOO5Waz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m5urRx99VIcOHdIll1yijz/++IyLqwEAAAAAUB8U3aeZPHlyjaeTewJ/f3/NnDnzjNPiAYnxgboxPlAXxgdqw9hAXRgfqIsnjQ+uXg4AAAAAgEm8rA4AAAAAAICnougGAAAAAMAkFN0AAAAAAJiEovsCsWjRIsXHxysgIEC9evXSN998Y3UkNAKzZs2SzWar9tW5c2erY8Ei//nPf3TDDTcoJiZGNptNa9eurfa4YRh69NFHFR0drSZNmigpKUl79+61Jizc7mzj4/bbbz9jPhk8eLA1YeF28+bN0+WXX66QkBC1aNFCw4YN0+7du6utU1JSokmTJikyMlLBwcG66aabdPjwYYsSw53qMz769+9/xhxy9913W5QY7vTiiy+qe/fuzvtx9+7dWx999JHzcU+YOyi6LwCrV6/W1KlTNXPmTH3//fdKTEzUoEGDdOTIEaujoRG46KKLlJOT4/z64osvrI4EixQVFSkxMVGLFi2q8fEnn3xSCxcu1OLFi7V582YFBQVp0KBBKikpcXNSWOFs40OSBg8eXG0+ef31192YEFbauHGjJk2apK+//lrr169XeXm5Bg4cqKKiIuc6999/v95//329+eab2rhxo7KzszV8+HALU8Nd6jM+JGn8+PHV5pAnn3zSosRwp9atW+uf//yntmzZou+++07XXHONhg4dqh07dkjykLnDgMfr2bOnMWnSJOfPlZWVRkxMjDFv3jwLU6ExmDlzppGYmGh1DDRCkox3333X+bPD4TCioqKMp556yrksPz/f8Pf3N15//XULEsJKp48PwzCMMWPGGEOHDrUkDxqfI0eOGJKMjRs3GoZxcr7w9fU13nzzTec6O3fuNCQZX331lVUxYZHTx4dhGEa/fv2Me++917pQaFSaNm1qLF261GPmDo50e7iysjJt2bJFSUlJzmVeXl5KSkrSV199ZWEyNBZ79+5VTEyM2rZtq9GjR+vAgQNWR0IjlJ6erkOHDlWbS8LCwtSrVy/mEjilpKSoRYsW6tSpkyZOnKi8vDyrI8Eix48flyRFRERIkrZs2aLy8vJqc0jnzp0VGxvLHHIBOn18VFm5cqWaNWumiy++WNOnT1dxcbEV8WChyspKvfHGGyoqKlLv3r09Zu7wsToAzHX06FFVVlaqZcuW1Za3bNlSu3btsigVGotevXpp+fLl6tSpk3JycjR7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unWrs/DcuXOn2rRp4yy4Jalr164KDw/Xzp07ncvi4uLqLLirGIZx1nVq22ZVlqqCW5J69+5d7Tk//PCD9u3bp5CQEOd+ioiIUElJSbV9dbZ+AwA8D0e6AQCop507dyohIUGSlJGRoeuvv14TJ07U448/roiICH3xxRcaO3asysrKnBcEGzdunBYtWqS///3vWrZsme644w5n4X7ppZcqPT1dH330kT777DONGDFCSUlJZ3wO/FS+vr7q06eP+vTpo2nTpmnu3LmaM2eOpk2bVmsxd3pBbbPZnFdib9KkSa1tVX0+/eWXX1avXr2qPebt7V3XrtLVV1+tF198UX5+foqJiZGPT/U/OYKCgup8fn3VZzsdO3asVqifqmr5qUf3XclWWFioHj16aOXKlWc8dmoB31D9BgCcPzjSDQBAPWzYsEHbtm3TTTfdJEnasmWLHA6H5s+fryuuuEIdO3ZUdnb2Gc/785//rMzMTC1cuFA//vjjGadkh4aGauTIkXr55Ze1evVqvf32287PW9dH165dVVFRoZKSEpf61b17d23atEnl5eVnPNayZUvFxMRo//79at++fbWvqn8+1CYoKEjt27dXbGzsGQV3fXTp0kVZWVnKyspyLvvxxx+Vn5+vrl27ntO2Ro0apb179+r9998/47H58+crMjJS11577Vmz5OTkOJd9/fXX1da59NJLtXfvXrVo0eKMfRUWFnZOeQEAnoWiGwCA05SWlurQoUP66aef9P333+uJJ57Q0KFDdf311+svf/mLJKl9+/YqLy/X888/r/3792vFihVavHjxGdtq2rSphg8frgcffFADBw5U69atnY8tWLBAr7/+unbt2qU9e/bozTffVFRUlMLDw2vM1b9/f7300kvasmWLMjIy9OGHH2rGjBm6+uqrFRoa6lJfJ0+eLLvdrlGjRum7777T3r17tWLFCu3evVvSyYuwzZs3TwsXLtSePXu0bds2LVu2TAsWLHCpvfpKSkpSt27dNHr0aH3//ff65ptv9Je//EX9+vXTZZdddk7bGjVqlG688UaNGTNG//rXv5SRkaGtW7fqrrvu0nvvvaelS5fWeQQ6KSlJHTt21JgxY/TDDz9o06ZNevjhh6utM3r0aDVr1kxDhw7Vpk2blJ6erpSUFN1zzz06ePCgS/sAAOAZKLoBADjNxx9/rOjoaMXHx2vw4MH6/PPPtXDhQq1bt855WnViYqIWLFig//mf/9HFF1+slStX1nq7r6pTzk+9tZckhYSE6Mknn9Rll12myy+/3FlIe3nV/PY8aNAgvfrqqxo4cKC6dOmiKVOmaNCgQVqzZo3LfY2MjNSGDRtUWFiofv36qUePHnr55Zedp6SPGzdOS5cu1bJly9StWzf169dPy5cvP+uR7t/KZrNp3bp1atq0qfr27aukpCS1bdtWq1evdmlba9as0YwZM/TMM8+oU6dO6tOnjzIzM5WSkqJhw4bV+XwvLy+9++67OnHihHr27Klx48bp8ccfr7ZOYGCg/vOf/yg2NlbDhw9Xly5dNHbsWJWUlLj8DxEAgGewGedyZREAAHDOVqxYofvvv1/Z2dlcRAsAgAsMF1IDAMAkxcXFysnJ0T//+U/dddddFNwAAFyAOL0cAACTPPnkk+rcubOioqI0ffp0q+MAAAALcHo5AAAAAAAm4Ug3AAAAAAAmoegGAAAAAMAkFN0AAAAAAJiEohsAAAAAAJNQdAMAAAAAYBKKbgAAAAAATELRDQAAAACASSi6AQAAAAAwCUU3AAAAAAAm+T/xg//cYzvHBQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df_instacart_orders \n",
    "\n",
    "# Calculate average and median days between orders\n",
    "average_days_between_orders = df_instacart_orders['days_since_prior_order'].mean()\n",
    "median_days_between_orders = df_instacart_orders['days_since_prior_order'].median()\n",
    "\n",
    "# Plotting the distribution of days since prior order\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.hist(df_instacart_orders['days_since_prior_order'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)\n",
    "plt.axvline(average_days_between_orders, color='red', linestyle='dashed', linewidth=1, label=f'Average: {average_days_between_orders:.2f} days')\n",
    "plt.axvline(median_days_between_orders, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_days_between_orders:.2f} days')\n",
    "plt.title('Distribution of Days Since Prior Order')\n",
    "plt.xlabel('Days Since Prior Order')\n",
    "plt.ylabel('Frequency')\n",
    "plt.legend()\n",
    "plt.grid(axis='y', linestyle='--', alpha=0.7)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "discrete-vertex",
   "metadata": {},
   "source": [
    "Used a bar graph and calculated the avg and median of days since prior orders and frequency of the order. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d926614",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "Your conclusions and results are correct. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "tight-staff",
   "metadata": {},
   "source": [
    "# [B] Medium (must complete all to pass)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "packed-classic",
   "metadata": {},
   "source": [
    "### [B1] Is there a difference in `'order_hour_of_day'` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d89b8403",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Z2Lv3r269tprZbVa1aZNG02fPr3KW3q8++67SkpKUnh4uPz8/NS+fXtNmzZN5eXljjZPPvmkfHx8qjxW9913n5o2ber4XH355ZdKTExUSEiIrFaroqKidO+991ZxVAHP4IpbwM3ef/99tWvXTr169apyfXx8vNq1a1dpUiBJf/7znxUdHa2nn35ahmFIkp544glNnz5d/fv3V//+/fXVV18pISFBpaWlTu8tKirSNddco0OHDun+++9XRESEtm3bpkmTJunIkSN64YUXnNovWbJExcXFuu++++Tn56fmzZufdb/KysqqfHjA0aNHKy3bu3evevXqpeDgYE2cOFE+Pj566aWX1Lt3b33yySe68sorz7qtMzlw4IAGDhyo+++/X3/5y1/UsWPHWtWRpCFDhmjdunVKS0vTxRdfXGWbV155RQ8++KBuv/12xyRy9+7d+uyzz3T33XdrwIAB+uabb5Samqo5c+YoJCREkpz+0vLxxx9r5cqVGjNmjEJCQqqc5JzujjvuULt27TRz5kxt375df//73/Xbb7/pn//8Z432rzp9O11ubq6uuuoqFRUV6cEHH1SLFi20bNky3XzzzXrzzTcrfb3xmWeekcVi0SOPPKKjR4/queee06BBg/TZZ5+dtV81/WyMHTtWzZo105NPPqkffvhBL7zwgsaMGeN0tUhVevbsqU8//VQ//PCD45hv3bpVI0eO1J/+9Cc9+eSTKigoUNOmTWUYhrZt26a4uDjHV+juv/9+LV26VMOHD9eDDz6orKwsvfjii9q5c6e2bt0qHx8fSdX//azJ/vzrX//SsGHDlJiYqGeffVZFRUVasGCBevbsqZ07dzr2Jzk5WXv37tXYsWPVrl075eXlKS0tTdnZ2Y421e3f999/r3feeUd//vOfFRUVpdzcXL300ku65pprtG/fPoWHhysoKEi33Xab3njjDc2ePVve3t6O96empsowDA0aNEjSqYn7zJkzHce7sLBQX375pb766iv169fvrGMHAKhfmPsy92Xue2Z1NfeNjIzUhg0b9NNPP6lNmzZnbTt37lzdfPPNGjRokEpLS/X666/rz3/+s1avXq2kpCRJp+ajFfO4++67T5LUvn37s9Y9k6o+Ezk5OerTp49Onjypv/71rwoMDNTLL79c5RXlS5cuVVBQkCZMmKCgoCB9/PHHeuKJJ1RYWKjnn39e0qnP99SpU/XGG29ozJgxjveWlpbqzTffVHJysvz9/ZWXl6eEhAS1bNlSf/3rX9W0aVP98MMPeuutt2q1b4BbGADcpqCgwJBk3HLLLWdtd/PNNxuSjMLCQsMwDOPJJ580JBkDBw50apeXl2f4+voaSUlJht1udyz/f//v/xmSjGHDhjmWTZs2zQgMDDS++eYbpxp//etfDW9vbyM7O9swDMPIysoyJBnBwcFGXl5etfYrMjLSkHTWP6tWrXK0v/XWWw1fX1/ju+++cyw7fPiw0bhxYyM+Pt6xrGK/f2/JkiWGJCMrK6tSHz766KNq9XnYsGFGYGDgGdfv3LnTkGSMHz/eseyaa64xrrnmGsfrW265xbjkkkvOup3nn3++Ul8rSDIsFouxd+/eKtc9+eSTjtcVx+Lmm292avfAAw8YkoyMjAzDMP43fkuWLDlnzbP1LTIy0unzM27cOEOS8emnnzqWHTt2zIiKijLatWtnlJeXG4ZhGBs3bjQkGTExMUZJSYmj7dy5cw1Jxp49eypt63TV/WxUfAb69u3r9NkfP3684e3tbRQUFJx1O2vWrDEkGf/6178MwzCMI0eOGJKMTz75xDh27Jjh7e1trFmzxjAMw/j6668NScaMGTMMwzCMTz/91JBkrFixwqnmRx995LS8Jr+f1d2fY8eOGU2bNjX+8pe/OG07JyfHaNKkiWP5b7/9Zkgynn/++TMeg5r0r7i42DHGFbKysgw/Pz9j6tSpjmVr1641JBkffvihU9vLLrvM6XenS5cuRlJS0hn7BgBoGJj7nsLc9xTmvpXV1dx38eLFhiTD19fX6NOnj/H4448bn376aaX5nWEYRlFRkdPr0tJSo3Pnzsa1117rtDwwMNDpmFUYNmyYERkZWWl5VZ/vM30mKo7/Z5995liWl5dnNGnSpNIY/r6/hmEY999/vxEQEGAUFxc7lsXFxRlXXnmlU7u33nrLkGRs3LjRMAzDePvttw1JxhdffFGpJmAW3CoBcKNjx45Jkho3bnzWdhXrCwsLnZaPGjXK6fX69etVWlqqsWPHOn3tZNy4cZVqrlq1Sr169VKzZs2Un5/v+NO3b1+Vl5dr8+bNTu2Tk5PP+C/QVbnyyiuVlpZW6c/f/vY3p3bl5eVat26dbr31Vqf7mLVu3Vp33323tmzZUmm/qysqKkqJiYm1eu/vBQUFSfrfmFWladOm+umnn/TFF1/UejvXXHONYmNjq90+JSXF6XXFPVo/+OCDWvehOj744AP96U9/crrHa1BQkO677z798MMPlb5OOHz4cKevYlVcZfP999+fcRu1+Wzcd999Tp/9Xr16qby8XD/++ONZ9+eqq66SxWJx3Lu24irZP/7xjwoKCtJll13muF1Cxc+KfV+1apWaNGmifv36Of0ude/eXUFBQdq4caOkmv1+Vnd/0tLSVFBQoIEDBzpt29vbW1deeaVj21arVb6+vtq0aVOl2zdUqEn//Pz8HFcbl5eX65dfflFQUJA6duyor776ytGub9++Cg8P14oVKxzLvv76a+3evdvpnnpNmzbV3r17dfDgwTMeCwBA/cfcl7nv7zH3/Z+6nPvee++9+uijj9S7d29t2bJF06ZNU69evRQdHa1t27Y5tT39qtbffvtNR48eVa9evZzmfK5U1Wfigw8+UI8ePfSnP/3Jsaxly5aOb2+dqb/Hjh1Tfn6+evXqpaKiIu3fv9+xbujQofrss8/03XffOZatWLFCbdu21TXXXCNJjofWrV69WmVlZS7ZP8DVuFUC4EYVk9KzTYhOX//7Se7pT7mX5PgfdHR0tNPyli1bqlmzZk7LDh48qN27d59xQvr7m9L/flvnEhISor59+1Za/vunw/78888qKiqq8qtcMTExstvt+s9//qNLLrmkRtuXat7nszl+/Liks/9F47HHHtP69ev1pz/9SR06dFBCQoLuvvtuXX311dXeTk37/Puxbt++vSwWi9M9z9zhxx9/rPJrfDExMY71Ffd/laSIiAindhWfxzOFiFLtPhu12Y50alJ2ySWXOIWzl19+uWPid9VVVzmt8/X1dUwcDx48qKNHj1a6H1iFit+lmvx+Vnd/KoLOa6+9tsr3VzwJ2s/PT88++6wefvhhtWrVSj169NCNN96ooUOHKiwsrMb9s9vtmjt3rubPn6+srCyne4a1aNHC8d8Wi0WDBg3SggULVFRUpICAAK1YsUL+/v7685//7Gg3depU3XLLLbr44ovVuXNnXX/99RoyZIguu+yyKvcLAFA/Mfdl7vt7zH3/py7nvpKUmJioxMREFRUVaceOHXrjjTe0cOFC3Xjjjdq/f79jbrt69WpNnz5du3btUklJieP9Vd1/2RWq+kyc6fhXdaz27t2ryZMn6+OPP64UdJ9+65I777xT48aN04oVK/TEE0/o6NGjWr16tcaPH+/Yt2uuuUbJycmaMmWK5syZo969e+vWW2/V3Xff3eAfYIf6g+AWcKMmTZqodevW2r1791nb7d69WxdddJEjhKlwtqfEnovdble/fv00ceLEKtf//l5W57MtVznT5OD00Oh0ruzz119/LUnq0KHDGdvExMTowIEDWr16tT766CP9+9//1vz58/XEE09oypQp1drO+fa5qhv8V+VMx8xdTr+/6emM/96fzgzb6dmzpxYuXKiCggJt3bpVV111lWPdVVddpVdffVVlZWXasmWLunfv7ni6rd1uV2hoqNNVpaerydU6v3eu/al4IMO//vUvRwB7utP/sjhu3DjddNNNeuedd7R27Vo9/vjjmjlzpj7++GNdfvnlNerX008/rccff1z33nuvpk2bpubNm8tisWjcuHGVHhIxdOhQPf/883rnnXc0cOBAvfbaa7rxxhvVpEkTR5v4+Hh99913evfdd7Vu3TotWrRIc+bM0cKFCzVy5Mga9Q0AYF7MfWuGue+5Mfc9/+0EBASoV69e6tWrl0JCQjRlyhR9+OGHGjZsmD799FPdfPPNio+P1/z589W6dWv5+PhoyZIljofQnUtdfo4LCgp0zTXXKDg4WFOnTlX79u3l7++vr776So899pjTPLVZs2a68cYbHcHtm2++qZKSEqdvhXl5eenNN9/U9u3b9f7772vt2rW69957NWvWLG3fvt1xZTrgSQS3gJvdeOONeuWVV7Rlyxanr95UqHhg0v3333/OWpGRkZJOXVFw+tdrfv7550r/6tq+fXsdP368yisD6lLLli0VEBCgAwcOVFq3f/9+WSwWtW3bVtL//gW54iFRFc71VSBX+Ne//iUvL69zPigpMDBQd955p+68806VlpZqwIABmjFjhiZNmiR/f3+X/8v0wYMHnf5V+ttvv5Xdbnc82OH0Y3a6qo5ZTfoWGRl5xjGrWH++avLZcIWePXtqwYIFWr9+vXbu3Ol40rB0Kri12Wxas2aNvv/+eyUnJzvWtW/fXuvXr9fVV1991olmTX4/q6vioQ+hoaHV+l1u3769Hn74YT388MM6ePCgunbtqlmzZmn58uU16t+bb76pPn36aPHixU7LCwoKHA/3qNC5c2ddfvnlWrFihdq0aaPs7Gz94x//qNS35s2ba/jw4Ro+fLiOHz+u+Ph4PfXUUwS3ANDAMPdl7ns+mPu6bu5blSuuuEKSdOTIEUnSv//9b/n7+2vt2rVOV5guWbKk0nvPdDybNWtWaTykmn2OIyMjq7yl1u+P1aZNm/TLL7/orbfeUnx8vGN5VlZWlXWHDh2qW265RV988YVWrFihyy+/vMqr3Xv06KEePXpoxowZeu211zRo0CC9/vrrzFNhCtzjFnCzRx99VFarVffff79++eUXp3W//vqrRo0apYCAAKcQ6Uz69u0rHx8f/eMf/3D6V9bfPyVXOvVE1vT0dK1du7bSuoKCAp08ebLmO1ML3t7eSkhI0Lvvvuv0Fafc3Fy99tpr6tmzp+Nqi4qQ6vR7kJ04cULLli1zax+feeYZrVu3TnfeeWelr2ed7vfj5+vrq9jYWBmG4bgnUmBgoKTKk8namjdvntPrikDshhtukHTqq/IhISGV7ts2f/78SrVq0rf+/fvr888/V3p6umPZiRMn9PLLL6tdu3Y1ulfZmdTks+EKFX95nD17tsrKypyuuG3Xrp1at26t5557zqmtdOp3qby8XNOmTatU8+TJk47jWZPfz+pKTExUcHCwnn766Srvu/Xzzz9LOvUk7eLiYqd17du3V+PGjR1featJ/7y9vStdybFq1SodOnSoyn5WPJn6hRdeUIsWLRyfzwq//90JCgpShw4dnL6OBwBoGJj7Mvc9H8x9XTP33bBhQ5XLK+4VXHELAm9vb3l5eTldHfvDDz/onXfeqfTewMDAKo9l+/btdfToUacr7Y8cOaK333672v3t37+/tm/frs8//9yx7Oeff670jbeKK5BPPx+UlpZWOf7Sqc9NSEiInn32WX3yySdOV9tKp2458fs5b9euXSWJeSpMgytuATeLjo7WsmXLNGjQIF166aUaMWKEoqKi9MMPP2jx4sXKz89XamqqY+J2Ni1bttQjjzyimTNn6sYbb1T//v21c+dOffjhh5Wugnv00Uf13nvv6cYbb9Q999yj7t2768SJE9qzZ4/efPNN/fDDD5Xe4y7Tp09XWlqaevbsqQceeECNGjXSSy+9pJKSEkdQJkkJCQmKiIjQiBEj9Oijj8rb21uvvvqqWrZsqezs7PPux8mTJ7V8+XJJUnFxsX788Ue999572r17t/r06aOXX375rO9PSEhQWFiYrr76arVq1UqZmZl68cUXlZSU5Lg/WPfu3SVJ//d//6e77rpLPj4+uummmxwTx5rKysrSzTffrOuvv17p6elavny57r77bnXp0sXRZuTIkXrmmWc0cuRIXXHFFdq8ebO++eabSrVq0re//vWvSk1N1Q033KAHH3xQzZs317Jly5SVlaV///vfjgdXna/qfjZcISIiQm3btlV6erratWun8PBwp/VXXXWV/v3vf8vLy8vp3m3XXHON7r//fs2cOVO7du1SQkKCfHx8dPDgQa1atUpz587V7bffXqPfz+oKDg7WggULNGTIEHXr1k133XWX4/dhzZo1uvrqq/Xiiy/qm2++0XXXXac77rhDsbGxatSokd5++23l5ubqrrvuklSz88eNN96oqVOnavjw4brqqqu0Z88erVixwulqp9Pdfffdmjhxot5++22NHj1aPj4+TutjY2PVu3dvde/eXc2bN9eXX36pN998U2PGjKnVcQEAmBdzX+a+zH3PrK7mvrfccouioqJ00003qX379jpx4oTWr1+v999/X3/84x910003SZKSkpI0e/ZsXX/99br77ruVl5enefPmqUOHDpVuedK9e3etX79es2fPVnh4uKKionTllVfqrrvu0mOPPabbbrtNDz74oIqKirRgwQJdfPHF1X7A2cSJE/Wvf/1L119/vR566CEFBgbq5ZdfVmRkpFM/rrrqKjVr1kzDhg3Tgw8+KC8vL/3rX/86460jfHx8dNddd+nFF1+Ut7e3Bg4c6LR+2bJlmj9/vm677Ta1b99ex44d0yuvvKLg4GD179+/JocccB8DQJ3YvXu3MXDgQKN169aGj4+PERYWZgwcONDYs2dPpbZPPvmkIcn4+eefK60rLy83pkyZYrRu3dqwWq1G7969ja+//tqIjIw0hg0b5tT22LFjxqRJk4wOHToYvr6+RkhIiHHVVVcZf/vb34zS0lLDMAwjKyvLkGQ8//zz1d6XyMhIIykpqcp1GzduNCQZq1atclr+1VdfGYmJiUZQUJAREBBg9OnTx9i2bVul9+/YscO48sorDV9fXyMiIsKYPXu2sWTJEkOSkZWVVa0+VGXYsGGGJMefgIAAo127dkZycrLx5ptvGuXl5ZXec8011xjXXHON4/VLL71kxMfHGy1atDD8/PyM9u3bG48++qhx9OhRp/dNmzbNuOiiiwyLxeLUb0lGSkpKlf2TZDz5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",
      "text/plain": [
       "<Figure size 1400x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load your dataset (replace with your actual dataset loading code)\n",
    "df_instacart_orders \n",
    "\n",
    "# Assuming your dataset has 'order_hour_of_day' and 'order_dow' columns\n",
    "\n",
    "# Filter orders for Wednesdays (order_dow = 3) and Saturdays (order_dow = 6)\n",
    "wednesday_orders = df_instacart_orders[df_instacart_orders['order_dow'] == 3]\n",
    "saturday_orders = df_instacart_orders[df_instacart_orders['order_dow'] == 6]\n",
    "\n",
    "# Plotting the histograms side by side\n",
    "plt.figure(figsize=(14, 6))\n",
    "\n",
    "# Plot for Wednesdays\n",
    "plt.subplot(1, 2, 1)\n",
    "plt.hist(wednesday_orders['order_hour_of_day'], bins=24, color='skyblue', edgecolor='black')\n",
    "plt.title('Order Hour Distribution on Wednesdays')\n",
    "plt.xlabel('Hour of Day')\n",
    "plt.ylabel('Frequency')\n",
    "plt.grid(True)\n",
    "\n",
    "# Plot for Saturdays\n",
    "plt.subplot(1, 2, 2)\n",
    "plt.hist(saturday_orders['order_hour_of_day'], bins=24, color='orange', edgecolor='black')\n",
    "plt.title('Order Hour Distribution on Saturdays')\n",
    "plt.xlabel('Hour of Day')\n",
    "plt.ylabel('Frequency')\n",
    "plt.grid(True)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a663982e",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "\n",
    "The error message indicates that the variable df_orders has not been defined in your code before it is used. Make sure that df_orders is properly defined and assigned a DataFrame before you attempt to use it in the code.\n",
    "    \n",
    "Could you please address issues in your notebook first? It's crucial that the notebook is fully executable from start to finish before it undergoes a code review. This ensures that anyone reviewing your work can run each cell in sequence without encountering errors, which can significantly impact the review process.\n",
    "\n",
    "Ensuring your notebook's full executability involves running all cells before submission: Before submitting your notebook, please use the `Kernel -> Run All` feature to execute all cells in sequence. This helps to catch any errors or issues that might not be immediately obvious."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9fd6556",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v4</b>\n",
    "\n",
    "\n",
    "Thank you for updating that. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "94e54e8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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oJz43//+p4iICHXs2PGi6zt16qSIiIgCv8RK0r333qv69evr1VdflWEYkqTJkyfr5Zdf1m233abbbrtNv/zyi3r27CmLxeLw3MzMTHXu3Fl///23Hn30UdWuXVubNm3SpEmTlJCQoNmzZzuMX7hwobKzs/XII4/IbDarcuXKl31dVqv1opM3pKSkFFi2b98+dezYUYGBgZo4caI8PT31zjvvqEuXLlq/fr3atWt32VqXcuDAAQ0YMECPPvqoHn74YTVs2LBY25GkwYMH64cfflBsbKwaNGhw0THvvfeennjiCd1zzz320LNnzx5t3bpVAwcOVN++ffXnn3/qs88+06xZs1S1alVJcgjZP/74o5YsWaIxY8aoatWqVzxt6L777lNERISmTZumLVu26M0339S5c+f00UcfFen1Faa3CyUmJuqmm25SZmamnnjiCVWpUkWLFi3SnXfeqWXLlhU47fW1116Tm5ubnn76aaWkpGj69OkaNGiQtm7detm+irpvPP7446pUqZJeeOEFHTlyRLNnz9aYMWMcjkheTIcOHfTzzz/ryJEj9vd848aNGjFihNq2basXXnhBycnJCg4OlmEY2rRpk6KiouynVj766KOKiYnRsGHD9MQTTyguLk5z587Vrl27tHHjRnl6ekoq/PdnUV7Pxx9/rCFDhig6Olqvv/66MjMzNX/+fHXo0EG7du2yv55+/fpp3759evzxxxUREaFTp04pNjZW8fHx9jGF7e/w4cP6+uuvde+99yoyMlKJiYl655131LlzZ+3fv181atSQv7+/+vTpoy+++EIzZ86Uu7u7/fmfffaZDMPQoEGDJJ0P+9OmTbO/36mpqdqxY4d++eUX9ejR45Jft8L0caHC7IcffPCBHn30Ud10000aO3asDh8+rDvvvFOVK1dWrVq1LtmLJIWHh0uSPv30U918882XPfV3+/bt2rRpk+6//37VrFlTR44c0fz589WlSxft379fvr6+6tSpk5544gm9+eab+te//qXGjRtLkv2/RfXYY48pJCREkydPVkZGRpFeb2pqqt5//3376ZFpaWn64IMPFB0drW3btqlly5YymUx64IEHNH36dJ09e9bh58T//vc/paam2o8QX+nzEijzDABlXnJysiHJuOuuuy477s477zQkGampqYZhGMYLL7xgSDIGDBjgMO7UqVOGl5eX0bt3b8Nms9mX/+tf/zIkGUOGDLEve+mllww/Pz/jzz//dNjGs88+a7i7uxvx8fGGYRhGXFycIckIDAw0Tp06VajXFR4ebki67L+lS5fax999992Gl5eXcejQIfuyEydOGAEBAUanTp3sy/Jf9z8tXLjQkGTExcUV6OH7778vVM9Dhgwx/Pz8Lrl+165dhiRj3Lhx9mWdO3c2OnfubH981113GU2bNr1snTfeeKNAr/kkGW5ubsa+ffsuuu6FF16wP85/L+68806HcY899pghyfj1118Nw/i/r9/ChQuvuM3L9RYeHu6w/4wdO9aQZPz888/2ZWlpaUZkZKQRERFh5OXlGYZhGGvXrjUkGY0bNzZycnLsY+fMmWNIMvbu3Vug1oUKu2/k7wPdu3d32PfHjRtnuLu7G8nJyZets3z5ckOS8fHHHxuGYRgJCQmGJGP9+vVGWlqa4e7ubixfvtwwDMP47bffDEnGK6+8YhiGYfz888+GJOPTTz912Ob333/vsLwo35+FfT1paWlGcHCw8fDDDzvUPnnypBEUFGRffu7cOUOS8cYbb1zyPShKf9nZ2favcb64uDjDbDYbL774on3ZqlWrDEnGypUrHca2aNHC4Xvn+uuvN3r37n3J3i6lsH0Udj+0WCxGtWrVjJYtWzqMe/fddw1JDj1fjM1mMzp37mxIMqpXr24MGDDAmDdvnnH06NECYzMzMwss27x5syHJ+Oijj+zLli5dakgy1q5dW2D8P7+H8/3z+zV/f+rQoYORm5trX16U15ubm+swxjDO71fVq1c3HnroIfuyAwcOGJKM+fPnO4y98847jYiICPu+VZjPS6As4zRCoBxIS0uTJAUEBFx2XP761NRUh+UjR450eLx69WpZLBY9/vjjDqfbjR07tsA2ly5dqo4dO6pSpUo6ffq0/V/37t2Vl5enn376yWF8v379LnmU42LatWun2NjYAv/+85//OIzLy8vTDz/8oLvvvtvhmrSwsDANHDhQGzZsKPC6CysyMlLR0dHFeu4/+fv7S/q/r9nFBAcH6/jx49q+fXux63Tu3FlNmjQp9PjRo0c7PM6/5mjFihXF7qEwVqxYobZt2zpcs+Tv769HHnlER44cKXCa6bBhwxyuccs/knv48OFL1ijOvvHII4847PsdO3ZUXl6ejh49etnXc9NNN8nNzc1+LVb+0agbb7xR/v7+atGihf1Uwvz/5r/2pUuXKigoSD169HD4XmrdurX8/f3tp1kV5fuzsK8nNjZWycnJGjBggENtd3d3tWvXzl7bx8dHXl5eWrduXYFTG/MVpT+z2Ww/qpeXl6czZ87I399fDRs21C+//GIf1717d9WoUUOffvqpfdlvv/2mPXv2OFwDFxwcrH379ungwYOXfC8uprB95LvSfrhjxw6dOnVKI0eOdBg3dOhQBQUFXbEfk8mkVatW6eWXX1alSpX02WefafTo0QoPD1f//v0drtm68PpRq9WqM2fOqF69egoODr5o7yXh4YcfdjjCWJTX6+7ubh9js9l09uxZ5ebmqk2bNg79NmjQQO3atXP4mp89e1YrV67UoEGD7PtWSXxeAqWJsAWUA/kh6nK/wF+4/p+h7MLZ0STZfwGrX7++w/KQkBBVqlTJYdnBgwf1/fffKyQkxOFf9+7dJUmnTp26bK0rqVq1qrp3717gX+vWrR3GJSUlKTMz86Kn+DVu3Fg2m03Hjh0rUu3i9nw56enpki4fjJ955hn5+/urbdu2ql+/vkaPHl3gWp8rKWrP//xa161bV25ubk6fJvro0aOX/Jrlr79Q7dq1HR7n74+X+sVfKt6+UZw6kuzTc18YqG644Qb7L8Q33XSTwzovLy+1bdtW0vnvpZSUFFWrVq3A91N6err9e6ko35+FfT354aRbt24Fav/www/22mazWa+//rpWrlyp6tWrq1OnTpo+fbpOnjxp33ZR+rPZbJo1a5bq168vs9msqlWrKiQkRHv27HE4VdjNzU2DBg3S119/rczMTEnnT7Hz9va2X4skSS+++KKSk5PVoEEDNW/eXBMmTNCePXsu+p4Up4/Cvp+Xeg88PT0vO0HRhcxms/7973/r999/14kTJ/TZZ5+pffv29tOD82VlZWny5Mn2a2bze09OTr5o7yWhsD8zLvV6Fy1apBYtWtivqwsJCdHy5csL9Pvggw9q48aN9u0vXbpUVqtVgwcPto8pic9LoDQRtoByICgoSGFhYVf8pWLPnj267rrrHKYdl3TZmfWuxGazqUePHhc9+hQbG6t+/fqVWK2ScrHJMaTzf9G+mJLs+bfffpMk1atX75JjGjdurAMHDujzzz9Xhw4d9N///lcdOnTQCy+8UOg6V9vzP9+jor5nznLhX9MvZPz/aw3LQp0OHTrYp3vfuHGjbrrpJvu6m266Sdu2bZPVatWGDRvUunVr+wyRNptN1apVu+T30osvvui015M/mc3HH3980drffPON/Tljx47Vn3/+qWnTpsnb21vPP/+8GjduXOD+YoXx6quvavz48erUqZM++eQTrVq1SrGxsWratGmBe9I9+OCDSk9P19dffy3DMLR48WLdfvvtDkdOOnXqpEOHDunDDz9Us2bN9P7776tVq1b2WzGURB+S6/bDfGFhYbr//vv1008/qX79+lqyZIlyc3MlnT8K/corr+i+++7TkiVL7NeEVqlS5arv6+eMz8RPPvlEQ4cOVd26dfXBBx/o+++/V2xsrLp161ag3/vvv1+enp72o1uffPKJ2rRp4/CHk5L4vARKExNkAOXE7bffrvfee08bNmy46DTS+RftXziD06XkX5x98OBBh79KJiUlFfjLft26dZWenm4/klVaQkJC5OvrqwMHDhRY98cff8jNzc1+kXb+X6HzJyrId6VTxErCxx9/LJPJdNmL9SXJz89P/fv3V//+/WWxWNS3b1+98sormjRpkry9vS8Zforr4MGDDn+t/uuvv2Sz2ewTHlz4nl3oYu9ZUXoLDw+/5Ncsf/3VKsq+URI6dOig+fPna/Xq1dq1a5d9dkbpfNjKysrS8uXLdfjwYYc/RtStW1erV6/WzTfffNlfZovy/VlYdevWlSRVq1atUN/LdevW1VNPPaWnnnpKBw8eVMuWLTVjxgx98sknRepv2bJl6tq1qz744AOH5cnJyfbJVfI1a9ZMN9xwgz799FPVrFlT8fHxeuuttwr0VrlyZQ0bNkzDhg1Tenq6OnXqpClTpmjEiBGXfD1F6aMwLnwPunXrZl9utVoVFxen66+/vsjblM4fKWrRooUOHjyo06dPKzQ0VMuWLdOQIUM0Y8YM+7js7OwC36uX+76sVKlSgfEWi0UJCQmF6qsor3fZsmWqU6eOvvzyS4eeLhaOKleurN69e+vTTz/VoEGDtHHjxgKTLklX/rwEyjKObAHlxIQJE+Tj46NHH31UZ86ccVh39uxZjRw5Ur6+vg6/+F1K9+7d5enpqbfeesvhL7UX+yF33333afPmzVq1alWBdcnJyfa/vjqbu7u7evbsqW+++cbh1LfExEQtXrxYHTp0sB/Ry//F8sLryTIyMrRo0SKn9vjaa6/phx9+UP/+/QucbnOhf379vLy81KRJExmGIavVKkn2+9qU1P125s2b5/A4/5fYXr16SZICAwNVtWrVAtfgvf322wW2VZTebrvtNm3btk2bN2+2L8vIyNC7776riIiIIl13dilF2TdKQv4fO2bOnCmr1epwZCsiIkJhYWH2WzBc+IeR++67T3l5eXrppZcKbDM3N9f+fhbl+7OwoqOjFRgYqFdffdW+j10of5r4zMxMh1sCSOe/nwICApSTk1Pk/tzd3QscDVq6dKn+/vvvi/aZP5vn7NmzVaVKFfv+me+f3zv+/v6qV6+evbdLKWofV9KmTRuFhIRowYIFDjMwxsTEFOr74uDBg4qPjy+wPDk5WZs3b1alSpXs175erPe33nqrwFGpy31f1q1bt8D39rvvvlvoI9dFeb35RwUv7Hnr1q0OnwEXGjx4sPbv368JEybI3d1d999/v8P6wnxeAmUZR7aAcqJ+/fpatGiRBg0apObNm2v48OGKjIzUkSNH9MEHH+j06dP67LPP7EHjckJCQvT0009r2rRpuv3223Xbbbdp165dWrlyZYG/8k6YMEHffvutbr/9dg0dOlStW7dWRkaG9u7dq2XLlunIkSPF+stwcbz88suKjY1Vhw4d9Nhjj8nDw0PvvPOOcnJyHO4v1rNnT9WuXVvDhw+3/wD/8MMPFRISctFfcIoqNzdXn3zyiaTzf2E+evSovv32W+3Zs0ddu3bVu+++e9nn9+zZU6Ghobr55ptVvXp1/f7775o7d6569+5tv9Yr/5q1f//73/ZTbe64445i31w0Li5Od955p2699VZt3rxZn3zyiQYOHOjwF+kRI0botdde04gRI9SmTRv99NNPDvcLy1eU3p599ll99tln6tWrl5544glVrlxZixYtUlxcnP773//aJy24WoXdN0pC7dq1VatWLW3evFkREREFpg2/6aab9N///lcmk8nhPkqdO3fWo48+qmnTpmn37t3q2bOnPD09dfDgQS1dulRz5szRPffcU6Tvz8IKDAzU/PnzNXjwYLVq1Ur333+//fth+fLluvnmmzV37lz9+eefuuWWW3TfffepSZMm8vDw0FdffaXExET7L8FF6e/222/Xiy++qGHDhummm27S3r179emnn17yuqaBAwdq4sSJ+uqrrzRq1Cj7VPj5mjRpoi5duqh169aqXLmyduzYoWXLljlc43QxRe3jSjw9PfXyyy/r0UcfVbdu3dS/f3/FxcVp4cKFhdrmr7/+qoEDB6pXr17q2LGjKleurL///luLFi3SiRMnNHv2bHtouf322/Xxxx8rKChITZo00ebNm7V69WqHe3FJUsuWLeXu7q7XX39dKSkpMpvN6tatm6pVq6YRI0Zo5MiR6tevn3r06KFff/1Vq1atKvT+VJTXe/vtt+vLL79Unz591Lt3b8XFxWnBggVq0qSJ/ZrWC/Xu3VtVqlTR0qVL1atXL1WrVs1hfWE+L4EyrTSmQARQfHv27DEGDBhghIWFGZ6enkZoaKgxYMCAi06NnT/td1JSUoF1eXl5xtSpU42wsDDDx8fH6NKli/Hbb78VmArYMM5PGz1p0iSjXr16hpeXl1G1alXjpptuMv7zn/8YFovFMIz/mzr8clNG/1N4ePglp3HOn4L5wqnfDcMwfvnlFyM6Otrw9/c3fH19ja5duxqbNm0q8PydO3ca7dq1M7y8vIzatWsbM2fOvOTU70WZSnrIkCEOU9P7+voaERERRr9+/Yxly5YVmF7aMApO/f7OO+8YnTp1MqpUqWKYzWajbt26xoQJE4yUlBSH57300kvGddddZ7i5uTn0LckYPXr0RfvTJaZ+379/v3HPPfcYAQEBRqVKlYwxY8YYWVlZDs/NzMw0hg8fbgQFBRkBAQHGfffdZ5w6deqi00ZfqreL7T+HDh0y7rnnHiM4ONjw9vY22rZta3z33XcOYy719b7clPT/VJh9I38f2L59+0XrX2za7IsZMGCAIckYOHBggXUzZ860Tx9+Me+++67RunVrw8fHxwgICDCaN29uTJw40Thx4oR9TGG/P4v6etauXWtER0cbQUFBhre3t1G3bl1j6NChxo4dOwzDMIzTp08bo0ePNho1amT4+fkZQUFBRrt27YwlS5Y4bKew/WVnZxtPPfWUfdzNN99sbN68ucD3xIVuu+02Q9JFv69ffvllo23btkZwcLDh4+NjNGrUyHjllVfsn0OXUtg+irofvv3220ZkZKRhNpuNNm3aGD/99NNlX1u+xMRE47XXXjM6d+5shIWFGR4eHkalSpWMbt26GcuWLXMYe+7cOWPYsGFG1apVDX9/fyM6Otr4448/Lvq99t577xl16tQx3N3dHb7+eXl5xjPPPGNUrVrV8PX1NaKjo42//vqr0PtTUV6vzWYzXn31VSM8PNwwm83GDTfcYHz33XfGkCFDjPDw8ItuN/9WFIsXLy6wrrCfl0BZZTIMJ13tCQAAUER9+vTR3r179ddff5V2K3CRcePG6YMPPtDJkyfl6+tb2u0AJYprtgAAQJmQkJCg5cuXO0z9jYotOztbn3zyifr160fQQoXENVsAAKBUxcXFaePGjXr//ffl6elZqFlVUb6dOnVKq1ev1rJly3TmzBk9+eSTpd0S4BSELQAAUKrWr1+vYcOGqXbt2lq0aJFCQ0NLuyU42f79+zVo0CBVq1ZNb775plq2bFnaLQFOwTVbAAAAAOAEXLMFAAAAAE5A2AIAAAAAJ+CarUKw2Ww6ceKEAgICZDKZSrsdAAAAAKXEMAylpaWpRo0acnO7/LErwlYhnDhxQrVq1SrtNgAAAACUEceOHVPNmjUvO4awVQgBAQGSzr+hgYGBpdyNZLVa9cMPP6hnz57y9PQs7XZQAbGPwdnYx+Bs7GNwNvaxa1dqaqpq1aplzwiXQ9gqhPxTBwMDA8tM2PL19VVgYCDf3HAK9jE4G/sYnI19DM7GPobCXF7EBBkAAAAA4ASELQAAAABwAsIWAAAAADgB12wBAAAA/2AYhnJzc5WXl3fR9VarVR4eHsrOzr7kGJRfnp6ecnd3v+rtELYAAACAC1gsFiUkJCgzM/OSYwzDUGhoqI4dO8Z9WCsgk8mkmjVryt/f/6q2Q9gCAAAA/j+bzaa4uDi5u7urRo0a8vLyumiYstlsSk9Pl7+//xVvbIvyxTAMJSUl6fjx46pfv/5VHeEibAEAAAD/n8Vikc1mU61ateTr63vJcTabTRaLRd7e3oStCigkJERHjhyR1Wq9qrDFngEAAAD8AwHq2lZSp4ayFwEAAACAE3AaIQAAAFAISUlJSk1NleT8a7YCAwMVEhJS4tuFaxG2AAAAgCtISkrSQ4+MVFpW9vkFhqE8m03ubm6SE2YjDPDx1ofvLihzgWvdunXq2rWrzp07p+Dg4FLrw2Qy6auvvtLdd99daj0UBmELAAAAuILU1FSlZWWry+BRqhJWU5KUl5srd4+S/3X6TMJxrft4vlJTUwsdthYsWKAJEybo3Llz8vj/PaWnp6tSpUq6+eabtW7dOvvY/MD0119/qW7duiXeP/4PYQsAAAAopCphNRUaHilJyrXmysOzbPw63bVrV6Wnp2vHjh1q3769JOnnn39WaGiotm7dquzsbHl7e0uS1q5dq9q1axO0XIAJMgAAAIByrmHDhgoLCytwBOuuu+5SZGSktmzZ4rC8a9eustlsmjZtmiIjI+Xj46Prr79ey5Ytc9juihUr1KBBA/n4+Khr1646cuSIw/qYmBgFBwdr1apVaty4sfz9/XXrrbcqISHBYdz777+vxo0by9vbW40aNdLbb79tX2exWDRmzBiFhYXJ29tb4eHhmjZtmn39wYMH1alTJ3l7e6tJkyaKjY0t8PqfeeYZNWjQQL6+vqpTp46ef/55Wa1WSdKRI0fk5uamHTt2ODxn9uzZCg8Pl81mK9ybXAyELQAAAKAC6Nq1q9auXWt/vHbtWnXp0kWdO3e2L8/KytLWrVvVtWtXTZs2TR999JEWLFigffv2ady4cXrggQe0fv16SdKxY8fUt29f3XHHHdq9e7dGjBihZ599tkDdzMxM/ec//9HHH3+sn376SfHx8Xr66aft6z/99FNNnjxZr7zyin7//Xe9+uqrev7557Vo0SJJ0ptvvqlvv/1WS5Ys0YEDB/Tpp58qIiJC0vmJSPr27SsvLy9t3bpVCxYs0DPPPFOgh4CAAMXExGj//v2aM2eO3nvvPc2aNUuSFBERoe7du2vhwoUOz1m4cKGGDh3q1Gn+y8ZxTwAAAABXpWvXrho7dqxyc3OVlZWlXbt2qXPnzrJarVqwYIEkafPmzcrJyVGXLl3UpEkTrV69WlFRUZKkOnXqaMOGDXrnnXfUuXNnzZ8/X3Xr1tWMGTMknT96tnfvXr3++usOdfO3n39a4pgxY/Tiiy/a17/wwguaMWOG+vbtK0mKjIzU/v379c4772jIkCGKj49X/fr11aFDB5lMJoWHh9ufu3r1av3xxx9atWqVatSoIUl69dVX1atXL4cennvuOfv/R0RE6Omnn9bnn3+uiRMnSpJGjBihkSNHaubMmTKbzfrll1+0d+9effPNN1f/xl8GYQsAAACoALp06aKMjAxt375d586dU4MGDRQSEqLOnTtr2LBhys7O1rp161SnTh2lp6crMzNTPXr0cNiGxWLRDTfcIEn6/fff1a5dO4f1+cHsQr6+vg7Xf4WFhenUqVOSpIyMDB06dEjDhw/Xww8/bB+Tm5uroKAgSdLQoUPVo0cPNWzYULfeeqtuv/129ezZ095DrVq17EHrUj188cUXevPNN3Xo0CGlp6crNzdXgYGB9vV33323Ro8era+++kr333+/YmJi1LVrV/sRNGchbAEAAAAVQL169VSzZk2tXbtW586dU+fOnSVJNWrUUK1atbRp0yatXbtW3bp1U3p6uiRp+fLluu666xy2Yzabi1TX09PT4bHJZJJhGJJkr/Pee+8VCG7u7u6SpFatWikuLk4rV67U6tWrdd9996l79+4Frh+7lM2bN2vQoEGaOnWqoqOjFRQUpM8//9x+RE6SvLy89OCDD2rhwoXq27evFi9erDlz5hTpdRYHYQsAAFxUSkqKMjMzXVrT19fX/tduAEXXtWtXrVu3TufOndOECRPsyzt16qSVK1dq27ZtGjVqlJo0aSKz2az4+Hh7KPunxo0b69tvv3VYduFEG4VRvXp11ahRQ4cPH9agQYMuOS4wMFD9+/dX//79dc899+jWW2/V2bNn1bhxYx07dkwJCQkKCwu7aA+bNm1SeHi4/v3vf9uXHT16tECNESNGqFmzZnr77beVm5trP63RmQhbAACggJSUFM2d+ZKsGaddWtfTr6rGjH+ewIUy60zCcfv/O/M+W8XVtWtXjR49Wlar1SFEde7cWWPGjJHFYlHXrl0VEBCgp59+WuPGjZPNZlOHDh2UkpKijRs3KjAwUEOGDNHIkSM1Y8YMTZgwQSNGjNDOnTsVExNT5J6mTp2qJ554QkFBQbr11luVk5OjHTt26Ny5cxo/frxmzpypsLAw3XDDDXJzc9PSpUsVGhqq4OBgde/eXQ0aNNCQIUP0xhtvKDU11SFUSVL9+vUVHx+vzz//XDfeeKOWL1+ur776qkAfjRs3Vvv27fXMM8/ooYceko+PT5FfS1ERtgAAQAGZmZmyZpxW3/Y+Cqnk65KaSecy9eWW08rMzCRsocwJDAxUgI+31n08//wCw1CezSZ3NzfJZCrxegE+3g7XHBVW165dlZWVpUaNGql69er25Z07d1ZaWpp9inhJeumllxQSEqJp06bp8OHDCg4OVqtWrfSvf/1LklS7dm3997//1bhx4/TWW2+pbdu2evXVV/XQQw8VqacRI0bI19dXb7zxhiZMmCA/Pz81b95cY8eOPf9aAwI0ffp0HTx4UO7u7rrxxhu1YsUK+yyBX331lYYPH662bdsqIiJCb775pm699Vb79u+8806NGzdOY8aMUU5Ojnr37q3nn39eU6ZMKdDL8OHDtWnTpiK/huIyGfknVOKSUlNTFRQUpJSUlGLt9CXNarVqxYoVuu222wqcIwuUBPYxOBv7WNmXkJCgd2ZM0qO9qigsJMA1NZPS9M7KM3r0qWn2XwaLi30MxZWdna24uDhFRkbabwKcLykpSampqZLOT0menp4uf39/p0wdHhgYqJCQkBLf7rXupZde0tKlS7Vnz57LjrvcflCUbMCRLQAAyrjSuHYqMTFRFqvFpTWBsi4kJMQegGw2m1JTUxUYGOjU+zShZKSnp+vIkSOaO3euXn75ZZfVJWwBAFCGlda1U2npmTr81z5l31pZkmuObAGAs4wZM0afffaZ7r77bpedQigRtgAAKNNK49opSdp/2Ka3/shRrtXqspoA4CwxMTHFmtzjahG2AAAoB0Iq+brs2ilJSjyT7rJaAFBRcYIpAAAAADgBYQsAAAAAnICwBQAAAABOQNgCAAAAACdgggwAAACgEC68553NZlNaWpoyMjKccp8tX19fBQUFlfh24VqELQAAAOAK/nnPO8MwZLVa5enpKZPJVOL1PP2qasz45ytc4Bo6dKiSk5P19ddfl3YrLkHYAgAAAK7gn/e8MwxDORaLzF5eJR62ks5l6sstp5WZmVmksJWUlKTJkydr+fLlSkxMVKVKlXT99ddr8uTJuvnmm6/4/JiYGI0dO1bJyclX0T0uRNgCAABlRnaORYmJiVe9nby8PElSYmKi3N3dLzuW07VQFPn3vDMMQzk5OTKbzU45siVlFfkZ/fr1k8Vi0aJFi1SnTh0lJiZqzZo1OnPmjBP6u7z8o37XOsIWAAAoE1LTc7R3zx7Z3ntVvj6+V7UtN3cPXX/THfrwrSmy5eVedmxFPV0L15bk5GT9/PPPWrdunTp37ixJCg8PV9u2be1jZs6cqYULF+rw4cOqXLmy7rjjDk2fPl3+/v5at26dhg0bJkn28PjCCy9oypQpMplM+uqrr3T33XfbtxUcHKzZs2dr6NChOnLkiCIjI/X555/r7bff1tatW7VgwQINHjxYEyZM0Icffih3d3cNHz5chmE49P3999/r5Zdf1m+//SZ3d3dFRUVpzpw5qlu3riSpW7duatKkiebOnWt/TlJSkq677jqtXLlSt9xyi1Pez5JC2AIAAGVCVo5VbrYMdW9iVc2wyx+NupI8ueuwpD7t3OUu45LjziRnafkvx4t8uhZQ1vj7+8vf319ff/212rdvL7PZXGCMm5ub3nzzTUVGRurw4cN67LHHNHHiRL399tu66aabNHv2bE2ePFkHDhywb7Monn32Wc2YMUM33HCDvL29NWPGDMXExOjDDz9U48aNNWPGDH311Vfq1q2b/TkZGRkaP368WrRoofT0dE2ePFl9+vTR7t275ebmphEjRmjMmDGaMWOG/TV98sknuu666xy2U1YRtgAAQJmQlZ2lxFOntGfPDp2I9766jbmbVandbdq5Y6OUl3PJYcnpudqwxaYHzpxRWFjY1dUESpGHh4diYmL08MMPa8GCBWrVqpU6d+6s+++/Xy1atJAkjR071j4+IiJCL7/8skaOHKm3335bXl5eCgoKkslkUmhoaLF6GDt2rPr27Wt/PHv2bE2aNMm+bMGCBVq1apXDc/r16+fw+MMPP1RISIj279+vZs2aqW/fvhozZoy++eYb3XfffZLOX1s2dOhQJ52+WbIIWwAAoEywWK0yDEM1GjRT3XrhV7Utmzx0SlLDdl3kpkufRnj8WKJyN2xXWlraVdUDyoJ+/fqpd+/e+vnnn7VlyxatXLlS06dP1/vvv6+hQ4dq9erVmjZtmv744w+lpqYqNzdX2dnZyszMlK/v1Z26K0lt2rSx/39KSooSEhLUrl07+zIPDw+1adPG4VTCgwcPavLkydq6datOnz4tm80mSYqPj1ezZs3k7e2twYMH68MPP9R9992nX375Rb/99pu+/fbbq+7XFQhbAAAUwYX32XGFxMREWawWl9UrC3x8feUfHHxV27AZ7jqVIvkHBcnNlHfJcd5nM66qDlDWeHt7q0ePHurRo4eef/55jRgxQi+88IK6dOmi22+/XaNGjdIrr7yiypUra8OGDRo+fLgsFstlw5bJZCpwrZXVai0wzs/Pr8j93nHHHQoPD9d7772nGjVqyGazqVmzZrJY/u9zb8SIEWrZsqWOHz+uhQsXqlu3bgoPv7o/yLgKYQsAUG65Ovikpqbqk4Vz5Z7ruqMgaemZOvzXPmXfWllSgMvqAqgYmjRpoq+//lo7d+6UzWbTjBkz7DdhXrJkicNYLy8v+0yeFwoJCVFCQoL98cGDB6/42RsUFKSwsDBt3bpVnTp1kiTl5uZq586datWqlSTpzJkzOnDggN577z117NhRkrRhw4YC22revLnatGmj9957T4sXL3aYLKOsI2wBAMqlf95g1BXyg8+/HmqnmtUruaTm/sM2vfVHjnIv8ldkAK6XdO58yPi/+2xZnHKfraI6c+aM7r33Xj300ENq0aKFAgICtGPHDk2fPl133XWX6tWrJ6vVqrfeekt33HGHNm7cqAULFjhsIyIiQunp6VqzZo2uv/56+fr6ytfXV926ddPcuXMVFRWlvLw8PfPMM4Wa1v3JJ5/Ua6+9pvr166tRo0aaOXOmwz28KlWqpCpVqujdd99VWFiY4uPj9eyzz150W/kTZfj5+alPnz5Ffn9KC2ELAFAu/fMGo66QH3yC/T0VFuKao0yJZ9JdUgfA5fn6+srTr6q+3HJaUpYMw7DfS8oZEzV4+lUt0nVU/v7+ateunWbNmqVDhw7JarWqVq1aevjhh/Wvf/1LPj4+mjlzpl5//XVNmjRJnTp10rRp0/Tggw/at3HTTTdp5MiR6t+/v86cOWOf+n3GjBkaNmyYOnbsqBo1amjOnDnauXPnFXt66qmnlJCQoCFDhsjNzU0PPfSQ+vTpo5SUFEnnZ0f8/PPP9cQTT6hZs2Zq2LCh3nzzTXXp0qXAtgYMGKCxY8dqwIAB8va+ygl0XIiwBQAo1/JvMOoKBB/g2hUUFKQx45+3nz5ns9mUlpamgIAA+2l5JamoN9s2m82aNm2apk2bdskx48aN07hx4xyWDR482OHx/PnzNX/+fIdlNWrUKDCL4IVHqCIiIgpc0yWdnxBj9uzZmj179iV76t69u/bv3++w7GLbOn36tLKzszV8+PBLbqssImwBAAAAhRAUFGQPQDabTX5+fgoMDHRK2MJ5VqtVZ86c0XPPPaf27dvbr/cqL9gzAAAAAJRJGzduVFhYmLZv317gGrPygCNbAAAAAMqkLl26XPS0wvKiVMPWlClTNHXqVIdlDRs21B9//CFJys7O1lNPPaXPP/9cOTk5io6O1ttvv63q1avbx8fHx2vUqFFau3at/P39NWTIEE2bNk0eHv/30tatW6fx48dr3759qlWrlp577jkNHTrUJa8RAK4FSUlJSk1NLfT4/KmF4+Li5O7uXqyap06dUnZ2drGeC1woN8+m06dPO0xt7QpFvSYHQPlT6ke2mjZtqtWrV9sfXxiSxo0bp+XLl2vp0qXnL0ocM0Z9+/bVxo0bJZ3/Yd27d2+FhoZq06ZNSkhI0IMPPihPT0+9+uqrks7/IO/du7dGjhypTz/9VGvWrNGIESMUFham6Oho175YAKiAkpKS9NAjI5WWVfjg4+XpqdEjhmnMUxNlKeaU5jk52XJP/UsP33qbuP8Uiisj06LM9FStXDZfO9dXc2ltT7+qGjP+eQJXGVWej6bg6pXU17/Uw5aHh4dCQ0MLLE9JSdEHH3ygxYsXq1u3bpKkhQsXqnHjxtqyZYvat2+vH374Qfv379fq1atVvXp1tWzZUi+99JKeeeYZTZkyRV5eXlqwYIEiIyM1Y8YMSVLjxo21YcMGzZo165JhKycnRzk5OfbH+X+ttVqtF71btqvl91AWekHFxD6Gojh37pxycvPUbfBIVQ69rlDPMRk2KeNv3fXkczJMxbt8OP6P37Rx4Qs6lZSiAH/XTAOcnJ4pN3cP5Rkestpcc9mzTR7y9DK7tGZp1TVMHvIy+0gmT9mM4h3xzGcz3Bz+eyk5VpMqBZh1Vzt/NW3gurB1OjlT325PVlpaWpGm94ZrGIah9PR0mc3my47J/6/NZnNVa3CRnJwcGYZhn+L/QkX5/chklGJsnzJlit544w0FBQXJ29tbUVFRmjZtmmrXrq0ff/xRt9xyi86dO6fg4GD7c8LDwzV27FiNGzdOkydP1rfffqvdu3fb18fFxalOnTr65ZdfdMMNN6hTp05q1aqVw5STCxcu1NixY+1z/F+sr3+e3ihJixcv5gMRAACgggsICFClSpVUtWpVeXl5OeU+Wii7DMNQUlKSzp49q3PnzhVYn5mZqYEDByolJUWBgYGX3VapHtlq166dYmJi1LBhQyUkJGjq1Knq2LGjfvvtN508eVJeXl4OQUuSqlevrpMnT0qSTp486XD9Vv76/HWXG5OamqqsrCz5+PgU6GvSpEkaP368/XFqaqpq1aqlnj17XvENdQWr1arY2Fj16NGjUHfvBoqKfQxFERcXpzFPTdSdYyereq3wwj0pL1def26RpUF7yb14P4q2xn6nNXMn6NnHOqh27RrF2kZR7d8frw8Xb9SsZ27TDc3qu6Tm3j8TNe39dXppdBfVDa9+5SeU47obfzmof89aoadH91C9RnWvals2w01HUtsoInCH3EyXPuqwe/chvf3+D3p1TGc1bRRxVTWLIvFspj5fn6FRE14r8HsKSp9hGDp16tRlr0U1DEPZ2dny9vYmjFVAHh4eatOmzUV/DyrKNcqlGrZ69epl//8WLVqoXbt2Cg8P15IlSy4aglzFbDZf9LCxp6dnmfrFs6z1g4qHfQyF4e7uLovVev50wKIGJ3ePYoetPOP8dVvePmYFBvsXaxtF5eXtKUtOltyUK08315w25KZcWS05cje5rmZp1TUZubLkZEmGVW6mvBLZppvJdtltWXLSlZmequ07t+lo3G8lUrMwktNztX6LTQMeTlbNmjVdVheFV7NmTeXl5V3ylDGr1aqffvpJnTp14mdlBeTl5XXJ+6cV5etd6tdsXSg4OFgNGjTQX3/9pR49eshisSg5Odnh6FZiYqL9Gq/Q0FBt27bNYRuJiYn2dfn/zV924ZjAwMBSDXQAAKD02XJzJZNJNRo0Vf0GdVxW9/ixROVu2K60tDSX1UTRubu7X3LGVHd3d+Xm5srb25uwhUsqU2ErPT1dhw4d0uDBg9W6dWt5enpqzZo16tevnyTpwIEDio+PV1RUlCQpKipKr7zyik6dOqVq1c5f1BobG6vAwEA1adLEPmbFihUOdWJjY+3bAAAAMPv4yv8fly44k/fZDJfVAlB6XDet0UU8/fTTWr9+vY4cOaJNmzapT58+cnd314ABAxQUFKThw4dr/PjxWrt2rXbu3Klhw4YpKipK7du3lyT17NlTTZo00eDBg/Xrr79q1apVeu655zR69Gj7aYAjR47U4cOHNXHiRP3xxx96++23tWTJEo0bN640XzoAAACACq5Uj2wdP35cAwYM0JkzZxQSEqIOHTpoy5YtCgkJkSTNmjVLbm5u6tevn8NNjfO5u7vru+++06hRoxQVFSU/Pz8NGTJEL774on1MZGSkli9frnHjxmnOnDmqWbOm3n//fe6xBQAlKNdqVcqZJJkLeXq2yZanapKSkxJluBVviu+MlGTugwMAKNNKNWx9/vnnl13v7e2tefPmad68eZccEx4eXuA0wX/q0qWLdu3aVaweAQCXl5aWptSTf2nv12/Jx79wE1V4eHjojp79tHXxa8rNzS1W3YRj8TLl5SjPainW8wEAcLYydc0WAKD8ycrKkq+HRXe0NatmrcqFeo4hd6VKGnRLJZlUvFnndmxP0Me/G8rLK5lZ6wAAKGmELQBAiagU6K2QKoU7smUz3JWaIlWt7F/sKb6D/AveogMAgLKkVCfIAAAAAICKirAFAAAAAE5A2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAE3NQYAABeVl5enlNRUnT3nmhtIp6emyZDhkloA4AqELQAAUEBWdpYST53Sup836Ldgb5fUPPR3uqzWXNlsBC4AFQNhCwAAFGCxWmUYhmo0aKa69cJdUjN9x35p42nZDJtL6gGAsxG2AADAJfn4+so/ONgltczevi6pAwCuwgQZAAAAAOAEhC0AAAAAcALCFgAAAAA4AddsAQBQBDbDUHpams6eO+uSeilpqcrLy3NJLQBAySJsAQBQSBZLjnKtVm37ZZeOHDngkppHE7N1MvGMTp1KUpUg19zvSuKeVwBQEghbAAAUki03VzKZVKNBU9VvUMclNTN3/SnLugRt3LpVBw/udUlNiXteAUBJIGwBAFBEZh/XTYfu6enl8oAncc8rACgJhC0AAMoBVwY8iXteAUBJYDZCAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE5A2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcwKO0GwAAlKykpCSlpqa6rN7x48dlM2wuqwcAQHlB2AKACiQpKUkPPTJSaVnZLquZknxWORkZstkIXAAAXIiwBQAVSGpqqtKystVl8ChVCavpkpq7f4rV5o/2cXQLAIB/IGwBQAVUJaymQsMjXVIrsGo1l9QBAKC8YYIMAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE5A2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcwKO0GwAAlKxcq1UpZ5Jk9vFxSb2MlGQZhuGSWgAAlCeELQCoQNLS0pR68i/t/fot+fj7u6RmwrF4mfJylGe1uKQeUFHk5tl0+vRpJSQkuKymr6+vgoKCXFYPuNYRtgCgAsnKypKvh0V3tDWrZq3KLqm5Y3uCPv7dUF5enkvqARVBRqZFmempWrlsvnaur+ayup5+VTVm/PMELsBFCFsAUAFVCvRWSBXXHNkK8je7pA5QkeRYcuXnZdPdbc1q3qiKS2omncvUl1tOKzMzk7AFuAhhCwAAoJRUDvJWWEiACytmubAWAGYjBAAAAAAnIGwBAAAAgBMQtgAAAADACQhbAAAAAOAEhC0AAAAAcALCFgAAAAA4AVO/AwAAlAKbYSg9LU1nz511Sb1zKRnKzs52SS0A5xG2AAAAXMxiyVGu1aptv+zSkSMHXFIzOT1XG7bY9MCZMwoLC3NJTeBaR9gCAABwMVturmQyqUaDpqrfoI5Lah4/lqjcDduVlpbmknoACFsAAAClxuzjK//gYJfU8j6b4ZI6AP4PE2QAAAAAgBMQtgAAAADACQhbAAAAAOAEhC0AAAAAcALCFgAAAAA4AWELAAAAAJyAsAUAAAAATlBmwtZrr70mk8mksWPH2pdlZ2dr9OjRqlKlivz9/dWvXz8lJiY6PC8+Pl69e/eWr6+vqlWrpgkTJig3N9dhzLp169SqVSuZzWbVq1dPMTExLnhFAAAAAK5lZSJsbd++Xe+8845atGjhsHzcuHH63//+p6VLl2r9+vU6ceKE+vbta1+fl5en3r17y2KxaNOmTVq0aJFiYmI0efJk+5i4uDj17t1bXbt21e7duzV27FiNGDFCq1atctnrAwAAAHDtKfWwlZ6erkGDBum9995TpUqV7MtTUlL0wQcfaObMmerWrZtat26thQsXatOmTdqyZYsk6YcfftD+/fv1ySefqGXLlurVq5deeuklzZs3TxaLRZK0YMECRUZGasaMGWrcuLHGjBmje+65R7NmzSqV1wsAAADg2uBR2g2MHj1avXv3Vvfu3fXyyy/bl+/cuVNWq1Xdu3e3L2vUqJFq166tzZs3q3379tq8ebOaN2+u6tWr28dER0dr1KhR2rdvn2644QZt3rzZYRv5Yy48XfGfcnJylJOTY3+cmpoqSbJarbJarVf7kq9afg9loRdUTOxj5ZfNZpOX2VuGPGQz3F1S0+TmKbPZRzJ5FrqmzXBz+K+r6l6ta6VmadUtyZqF3ceupffXkIe8zN6y2Wx8vpcAflZeu4ryNTcZhmE4sZfL+vzzz/XKK69o+/bt8vb2VpcuXdSyZUvNnj1bixcv1rBhwxxCjyS1bdtWXbt21euvv65HHnlER48edTglMDMzU35+flqxYoV69eqlBg0aaNiwYZo0aZJ9zIoVK9S7d29lZmbKx8enQF9TpkzR1KlTCyxfvHixfH19S/AdAAAAAFCeZGZmauDAgUpJSVFgYOBlx5baka1jx47pySefVGxsrLy9vUurjYuaNGmSxo8fb3+cmpqqWrVqqWfPnld8Q13BarUqNjZWPXr0kKenZ2m3gwqIfaz82rZtmyaNG6KJozoqPLKGS2pu3bxH7y5arwmPR6tR0waFeo7NcNOR1DaKCNwhN5PNZXWv1rVSs7TqlmTNwu5j19L7ezTuhKbP/1nTZi1S27ZtXVKzIuNn5bUr/6y3wii1sLVz506dOnVKrVq1si/Ly8vTTz/9pLlz52rVqlWyWCxKTk5WcHCwfUxiYqJCQ0MlSaGhodq2bZvDdvNnK7xwzD9nMExMTFRgYOBFj2pJktlsltlsLrDc09OzTH0zlbV+UPGwj5U/bm5usuRky6RcuZnyXFLTsFmVk5MlGdYi13Qz2Yrd59XULa5rpWZp1XVGzSvtY9fS+2tSriw52XJzc+OzvQTxs/LaU5Svd6lNkHHLLbdo79692r17t/1fmzZtNGjQIPv/e3p6as2aNfbnHDhwQPHx8YqKipIkRUVFae/evTp16pR9TGxsrAIDA9WkSRP7mAu3kT8mfxsAAAAA4AyldmQrICBAzZo1c1jm5+enKlWq2JcPHz5c48ePV+XKlRUYGKjHH39cUVFRat++vSSpZ8+eatKkiQYPHqzp06fr5MmTeu655zR69Gj7kamRI0dq7ty5mjhxoh566CH9+OOPWrJkiZYvX+7aFwwAAADgmlLqsxFezqxZs+Tm5qZ+/fopJydH0dHRevvtt+3r3d3d9d1332nUqFGKioqSn5+fhgwZohdffNE+JjIyUsuXL9e4ceM0Z84c1axZU++//76io6NL4yUBAAAAuEaUqbC1bt06h8fe3t6aN2+e5s2bd8nnhIeHa8WKFZfdbpcuXbRr166SaBEAAAAACqXUb2oMAAAAABURYQsAAAAAnICwBQAAAABOQNgCAAAAACcgbAEAAACAExC2AAAAAMAJCFsAAAAA4ASELQAAAABwAsIWAAAAADgBYQsAAAAAnICwBQAAAABOQNgCAAAAACcgbAEAAACAExC2AAAAAMAJCFsAAAAA4ASELQAAAABwAsIWAAAAADgBYQsAAAAAnICwBQAAAABOQNgCAAAAACcgbAEAAACAExC2AAAAAMAJCFsAAAAA4ASELQAAAABwAsIWAAAAADgBYQsAAAAAnICwBQAAAABOQNgCAAAAACcgbAEAAACAExC2AAAAAMAJCFsAAAAA4ASELQAAAABwAsIWAAAAADgBYQsAAAAAnICwBQAAAABOQNgCAAAAACfwKO0GAAAA4Bp5tjwdP35chw4dclnNwMBAhYSEuKweUJYQtgAAAK4Blpxspael6bVZbyogMNBldQN8vPXhuwsIXLgmEbYAAACuAXm5Vpnc3BR1zxA1bNnGJTXPJBzXuo/nKzU1lbCFaxJhCwAA4BpSqVp1hYZHlnYbwDWBCTIAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE7A1O8AAADXiDybobTkszp36qRL6qWcSVKu1eqSWkBZRNgCAAC4BmRkWZVrydHhHz9S8t5VLqmZlZ6u1JN/KS0tzSX1gLKGsAUAAHANsFjy5G82dMeNXqrfsLJLah4/ZtXR3yzKyspyST2grCFsAQAAXEOCA8wKqeLvkloZKSkuqQOUVUyQAQAAAABOQNgCAAAAACcgbAEAAACAExC2AAAAAMAJmCADAJwkJSVFmZmZLq15+vRp2Ww2l9YEAAAXR9gCACdISUnR3JkvyZpx2qV1TySekjUrVblWi0vrAgCAgghbAOAEmZmZsmacVt/2Pgqp5Ouyult+TdGurTbZ8nJdVhMAAFxcscLW4cOHVadOnZLuBQAqnJBKvgoLCXBZvcpB3i6rBQAALq9YE2TUq1dPXbt21SeffKLs7OyS7gkAAAAAyr1iha1ffvlFLVq00Pjx4xUaGqpHH31U27ZtK+neAAAAAKDcKlbYatmypebMmaMTJ07oww8/VEJCgjp06KBmzZpp5syZSkpKKuk+AQAAAKBcuar7bHl4eKhv375aunSpXn/9df311196+umnVatWLT344INKSEgoqT4BAAAAoFy5qrC1Y8cOPfbYYwoLC9PMmTP19NNP69ChQ4qNjdWJEyd01113lVSfAAAAAFCuFGs2wpkzZ2rhwoU6cOCAbrvtNn300Ue67bbb5OZ2PrtFRkYqJiZGERERJdkrAAAAAJQbxQpb8+fP10MPPaShQ4cqLCzsomOqVaumDz744KqaA4DyLDs7W+dSkmX2sLqsZnpqmgwZLqsHAAAurVhh6+DBg1cc4+XlpSFDhhRn8wBQ7p05c0YbNm9WqOGmYH/X3T/+0N/pslpzZbMRuAAAKG3F+g1g4cKF8vf317333uuwfOnSpcrMzCRkAbjmpaWlKTc3T7Uat1LNWtVdVjd9x35p42nZDJvLagIAgIsrVtiaNm2a3nnnnQLLq1WrpkceeYSwBQD/n7efv/yDg11Wz+zt67JaAADg8oo1G2F8fLwiIyMLLA8PD1d8fPxVNwUAAAAA5V2xwla1atW0Z8+eAst//fVXValS5aqbAgAAAIDyrlhha8CAAXriiSe0du1a5eXlKS8vTz/++KOefPJJ3X///SXdIwAAAACUO8UKWy+99JLatWunW265RT4+PvLx8VHPnj3VrVs3vfrqq4Xezvz589WiRQsFBgYqMDBQUVFRWrlypX19dna2Ro8erSpVqsjf31/9+vVTYmKiwzbi4+PVu3dv+fr6qlq1apowYYJyc3Mdxqxbt06tWrWS2WxWvXr1FBMTU5yXDQAAAACFVqyw5eXlpS+++EJ//PGHPv30U3355Zc6dOiQPvzwQ3l5eRV6OzVr1tRrr72mnTt3aseOHerWrZvuuusu7du3T5I0btw4/e9//9PSpUu1fv16nThxQn379rU/Py8vT71795bFYtGmTZu0aNEixcTEaPLkyfYxcXFx6t27t7p27ardu3dr7NixGjFihFatWlWclw4AAAAAhXJVN39p0KCBGjRoUOzn33HHHQ6PX3nlFc2fP19btmxRzZo19cEHH2jx4sXq1q2bpPNTzjdu3FhbtmxR+/bt9cMPP2j//v1avXq1qlevrpYtW+qll17SM888oylTpsjLy0sLFixQZGSkZsyYIUlq3LixNmzYoFmzZik6Orr4Lx4AAAAALqNYYSsvL08xMTFas2aNTp06JZvN8X4uP/74Y7G2uXTpUmVkZCgqKko7d+6U1WpV9+7d7WMaNWqk2rVra/PmzWrfvr02b96s5s2bq3r1/7uHTXR0tEaNGqV9+/bphhtu0ObNmx22kT9m7Nixl+wlJydHOTk59sepqamSJKvVKqvVWuTXVtLyeygLvaBiYh+7ejabTV5mbxnykM1wd1ldk5unzGYfyeTpsrrFqWkz3Bz+66q6V+taqVladUuyZmH3Md5f5zLkIS+zt2w2W4X7mcLPymtXUb7mJsMwjKIWGDNmjGJiYtS7d2+FhYXJZDI5rJ81a1aht7V3715FRUUpOztb/v7+Wrx4sW677TYtXrxYw4YNcwg9ktS2bVt17dpVr7/+uh555BEdPXrU4ZTAzMxM+fn5acWKFerVq5caNGigYcOGadKkSfYxK1asUO/evZWZmSkfH58CPU2ZMkVTp04tsHzx4sXy9eUeNgAAAMC1KjMzUwMHDlRKSooCAwMvO7ZYR7Y+//xzLVmyRLfddluxGrxQw4YNtXv3bqWkpGjZsmUaMmSI1q9ff9XbvRqTJk3S+PHj7Y9TU1NVq1Yt9ezZ84pvqCtYrVbFxsaqR48e8vT0LO12UAGxj129bdu2adK4IZo4qqPCI2u4rO7WzXv07qL1mvB4tBo1Lf5p3s6uaTPcdCS1jSICd8jNZLvyE0qo7tW6VmqWVt2SrFnYfYz317mOxp3Q9Pk/a9qsRWrbtq1LaroKPyuvXflnvRVGscKWl5eX6tWrV5ynXnZbrVu31vbt2zVnzhz1799fFotFycnJCg4Oto9PTExUaGioJCk0NFTbtm1z2F7+bIUXjvnnDIaJiYkKDAy86FEtSTKbzTKbzQWWe3p6lqlvprLWDyoe9rHic3NzkyUnWyblys2U57K6hs2qnJwsybC6rO7V1HQz2YrdZ3l7reWpZmnVdUbNK+1jvL/OZVKuLDnZcnNzq7A/T/hZee0pyte7WCfLP/XUU5ozZ46KcQbiFdlsNuXk5Kh169by9PTUmjVr7OsOHDig+Ph4RUVFSZKioqK0d+9enTp1yj4mNjZWgYGBatKkiX3MhdvIH5O/DQAAAABwhmId2dqwYYPWrl2rlStXqmnTpgXS3Zdfflmo7UyaNEm9evVS7dq1lZaWpsWLF2vdunVatWqVgoKCNHz4cI0fP16VK1dWYGCgHn/8cUVFRal9+/aSpJ49e6pJkyYaPHiwpk+frpMnT+q5557T6NGj7UemRo4cqblz52rixIl66KGH9OOPP2rJkiVavnx5cV46AAAAABRKscJWcHCw+vTpc9XFT506pQcffFAJCQkKCgpSixYttGrVKvXo0UPS+Yk23Nzc1K9fP+Xk5Cg6Olpvv/22/fnu7u767rvvNGrUKEVFRcnPz09DhgzRiy++aB8TGRmp5cuXa9y4cZozZ45q1qyp999/n2nfAQAAADhVscLWwoULS6T4Bx98cNn13t7emjdvnubNm3fJMeHh4VqxYsVlt9OlSxft2rWrWD0CAAAAQHEU+wYnubm5Wr16td555x2lpaVJkk6cOKH09PQSaw4AAAAAyqtiHdk6evSobr31VsXHxysnJ0c9evRQQECAXn/9deXk5GjBggUl3ScAAAAAlCvFOrL15JNPqk2bNjp37pzD9Ol9+vQpMPMfAAAAAFyLinVk6+eff9amTZvk5eXlsDwiIkJ///13iTQGAAAAAOVZsY5s2Ww25eUVvBne8ePHFRAQcNVNAQAAAEB5V6yw1bNnT82ePdv+2GQyKT09XS+88IJuu+22kuoNAAAAAMqtYp1GOGPGDEVHR6tJkybKzs7WwIEDdfDgQVWtWlWfffZZSfcIAAAAAOVOscJWzZo19euvv+rzzz/Xnj17lJ6eruHDh2vQoEEOE2YAAAAAwLWqWGFLkjw8PPTAAw+UZC8AAAAAUGEUK2x99NFHl13/4IMPFqsZAAAAAKgoihW2nnzySYfHVqtVmZmZ8vLykq+vL2ELAAAAwDWvWLMRnjt3zuFfenq6Dhw4oA4dOjBBBgAAAAComGHrYurXr6/XXnutwFEvAAAAALgWlVjYks5PmnHixImS3CQAAAAAlEvFumbr22+/dXhsGIYSEhI0d+5c3XzzzSXSGAAAAACUZ8UKW3fffbfDY5PJpJCQEHXr1k0zZswoib4AAAAAoFwrVtiy2Wwl3QcAAAAAVCgles0WAAAAAOC8Yh3ZGj9+fKHHzpw5szglAAAAAKBcK1bY2rVrl3bt2iWr1aqGDRtKkv7880+5u7urVatW9nEmk6lkugQAAACAcqZYYeuOO+5QQECAFi1apEqVKkk6f6PjYcOGqWPHjnrqqadKtEkAAAAAKG+KFbZmzJihH374wR60JKlSpUp6+eWX1bNnT8IWAAAAJEl5tjwdP35chw4dcmndwMBAhYSEuLQm8E/FClupqalKSkoqsDwpKUlpaWlX3RQAAADKP0tOttLT0vTarDcVEBjo0toBPt768N0FBC6UqmKFrT59+mjYsGGaMWOG2rZtK0naunWrJkyYoL59+5ZogwAAACif8nKtMrm5KeqeIWrYso3L6p5JOK51H89XamoqYQulqlhha8GCBXr66ac1cOBAWa3W8xvy8NDw4cP1xhtvlGiDAAAAKL/ybIY8vDxl9vFxWU0PL7Ny///vqEBpKlbY8vX11dtvv6033njDfv5t3bp15efnV6LNAQAAoPzKyLIq15Kjwz9+pOS9q1xWNys9Xakn/+LyFpS6YoWtfAkJCUpISFCnTp3k4+MjwzCY7h0AAACSJIslT/5mQ3fc6KX6DSu7rO7xY1Yd/c2irKwsl9UELqZYYevMmTO67777tHbtWplMJh08eFB16tTR8OHDValSJc2YMaOk+wQAAEA5FRxgVkgVf5fVy0hJcVkt4HLcivOkcePGydPTU/Hx8fL19bUv79+/v77//vsSaw4AAAAAyqtiHdn64YcftGrVKtWsWdNhef369XX06NESaQwAAAAAyrNiHdnKyMhwOKKV7+zZszKbzVfdFAAAAACUd8UKWx07dtRHH31kf2wymWSz2TR9+nR17dq1xJoDAAAAgPKqWKcRTp8+Xbfccot27Nghi8WiiRMnat++fTp79qw2btxY0j0CAAAAQLlTrCNbzZo1059//qkOHTrorrvuUkZGhvr27atdu3apbt26Jd0jAAAAAJQ7RT6yZbVadeutt2rBggX697//7YyeAAAAAKDcK/KRLU9PT+3Zs8cZvQAAAABAhVGs0wgfeOABffDBByXdCwAAAABUGMWaICM3N1cffvihVq9erdatW8vPz89h/cyZM0ukOQAAAAAor4oUtg4fPqyIiAj99ttvatWqlSTpzz//dBhjMplKrjsAAAAAKKeKFLbq16+vhIQErV27VpLUv39/vfnmm6pevbpTmgMAAACA8qpI12wZhuHweOXKlcrIyCjRhgAAAACgIijWBBn5/hm+AAAAAADnFSlsmUymAtdkcY0WAAAAABRUpGu2DMPQ0KFDZTabJUnZ2dkaOXJkgdkIv/zyy5LrEAAAAADKoSKFrSFDhjg8fuCBB0q0GQAAAACoKIoUthYuXOisPgAAAACgQrmqCTIAAAAAABdH2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE5A2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE5A2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE5QqmFr2rRpuvHGGxUQEKBq1arp7rvv1oEDBxzGZGdna/To0apSpYr8/f3Vr18/JSYmOoyJj49X79695evrq2rVqmnChAnKzc11GLNu3Tq1atVKZrNZ9erVU0xMjLNfHgAAAIBrWKmGrfXr12v06NHasmWLYmNjZbVa1bNnT2VkZNjHjBs3Tv/73/+0dOlSrV+/XidOnFDfvn3t6/Py8tS7d29ZLBZt2rRJixYtUkxMjCZPnmwfExcXp969e6tr167avXu3xo4dqxEjRmjVqlUufb0AAAAArh0epVn8+++/d3gcExOjatWqaefOnerUqZNSUlL0wQcfaPHixerWrZskaeHChWrcuLG2bNmi9u3b64cfftD+/fu1evVqVa9eXS1bttRLL72kZ555RlOmTJGXl5cWLFigyMhIzZgxQ5LUuHFjbdiwQbNmzVJ0dLTLXzcAAACAiq9Uw9Y/paSkSJIqV64sSdq5c6esVqu6d+9uH9OoUSPVrl1bmzdvVvv27bV582Y1b95c1atXt4+Jjo7WqFGjtG/fPt1www3avHmzwzbyx4wdO/aifeTk5CgnJ8f+ODU1VZJktVpltVpL5LVejfweykIvqJjYx66ezWaTl9lbhjxkM9xdVtfk5imz2UcyebqsbnFq2gw3h/+6qu7VulZqllbdkqxZ2H2M97fi1ZQkQx7yMnvLZrM57WcZPyuvXUX5mpsMwzCc2Euh2Ww23XnnnUpOTtaGDRskSYsXL9awYcMcgo8ktW3bVl27dtXrr7+uRx55REePHnU4JTAzM1N+fn5asWKFevXqpQYNGmjYsGGaNGmSfcyKFSvUu3dvZWZmysfHx2H7U6ZM0dSpUwv0uHjxYvn6+pbkywYAAABQjmRmZmrgwIFKSUlRYGDgZceWmSNbo0eP1m+//WYPWqVp0qRJGj9+vP1xamqqatWqpZ49e17xDXUFq9Wq2NhY9ejRQ56enqXdDiog9rGrt23bNk0aN0QTR3VUeGQNl9XdunmP3l20XhMej1ajpg3KbE2b4aYjqW0UEbhDbiaby+perWulZmnVLcmahd3HeH8rXk1JOhp3QtPn/6xpsxapbdu2TqnBz8prV/5Zb4VRJsLWmDFj9N133+mnn35SzZo17ctDQ0NlsViUnJys4OBg+/LExESFhobax2zbts1he/mzFV445p8zGCYmJiowMLDAUS1JMpvNMpvNBZZ7enqWqW+mstYPKh72seJzc3OTJSdbJuXKzZTnsrqGzaqcnCzJsLqs7tXUdDPZit1neXut5almadV1Rs0r7WO8vxWvpiSZlCtLTrbc3Nyc/nOMn5XXnqJ8vUt1NkLDMDRmzBh99dVX+vHHHxUZGemwvnXr1vL09NSaNWvsyw4cOKD4+HhFRUVJkqKiorR3716dOnXKPiY2NlaBgYFq0qSJfcyF28gfk78NAAAAAChppXpka/To0Vq8eLG++eYbBQQE6OTJk5KkoKAg+fj4KCgoSMOHD9f48eNVuXJlBQYG6vHHH1dUVJTat28vSerZs6eaNGmiwYMHa/r06Tp58qSee+45jR492n50auTIkZo7d64mTpyohx56SD/++KOWLFmi5cuXl9prBwAAAFCxleqRrfnz5yslJUVdunRRWFiY/d8XX3xhHzNr1izdfvvt6tevnzp16qTQ0FB9+eWX9vXu7u767rvv5O7urqioKD3wwAN68MEH9eKLL9rHREZGavny5YqNjdX111+vGTNm6P3332fadwAAAABOU6pHtgozEaK3t7fmzZunefPmXXJMeHi4VqxYcdntdOnSRbt27SpyjwAAACh/8mx5On78uA4dOuSc7eedvwYtLi5O7u7np7UPDAxUSEiIU+qhfCoTE2QAAAAAJcWSk630tDS9NutNBThpJmkvT0+NHjFMY56aKMv/v+9SgI+3Pnx3AYELdoQtAAAAVCh5uVaZ3NwUdc8QNWzZxik1TIZNSj+mO8dOlmFy05mE41r38XylpqYStmBH2AIAAECFVKladYWGR155YHHk5Uq/H1P1WuGSO79S4+JKdYIMAAAAAKioCFsAAAAA4AQc8wQAAECFk2czlJZ8VudOnXTK9k22PFWTlJyUKMPNXSlnkpT7/yfKAPIRtgAAAFChZGRZlWvJ0eEfP1Ly3lVOqeHh4aE7evbT1sWvKTc3V1np6Uo9+ZfS0tKcUg/lE2ELAAAAFYrFkid/s6E7bvRS/YaVnVLDkLtSJQ26pZJMytPxY1Yd/c2irKwsp9RD+UTYAgAAQIUUHGBWSBV/p2zbZrgrNUWqWtlfbqY8ZaSkOKUOyjcmyAAAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACZiMEcE1ISkpSamqqy+odP35cNsPmsnoAAKDsIWwBqPCSkpL00CMjlZaV7bKaKclnlZORIZuNwAUAwLWKsAWgwktNTVVaVra6DB6lKmE1XVJz90+x2vzRPo5uAQBwDSNsAbhmVAmrqdDwSJfUCqxazSV1AABA2cUEGQAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcgLAFAAAAAE7AbIQArgm5VqtSziTJ7OPjknoZKckyDMMltQAAQNlE2AJQ4aWlpSn15F/a+/Vb8vH3d0nNhGPxMuXlKM9qcUk9AABQ9hC2AFR4WVlZ8vWw6I62ZtWsVdklNXdsT9DHvxvKy8tzST0AAFD2ELYAXDMqBXorpIprjmwF+ZtdUgcAAJRdTJABAAAAAE5A2AIAAAAAJyBsAQAAAIATELYAAAAAwAkIWwAAAADgBIQtAAAAAHACwhYAAAAAOAFhCwAAAACcgJsaAwAAACUgN8+m06dPKyEhwWU1fX19FRQU5LJ6KBrCFgAAAHCVMjItykxP1cpl87VzfTWX1fX0q6ox458ncJVRhC0AAADgKuVYcuXjmafuTaxqVN/dJTXPJGdp+S/HlZmZSdgqowhbAAAAwFWyWHKUa7Xqr7/2K/XsEZfUTE7P1YYtNj1w5ozCwsJcUhNFQ9gCAAAArpItN1cymVSjQVPVb1DHJTWPH0tU7obtSktLc0k9FB1hCwAAACghZh9f+QcHu6SW99kMl9RB8TH1OwAAAAA4AWELAAAAAJyAsAUAAAAATkDYAgAAAAAnIGwBAAAAgBMQtgAAAADACQhbAAAAAOAEhC0AAAAAcALCFgAAAAA4AWELAAAAAJyAsAUAAAAATkDYAgAAAAAnIGwBAAAAgBMQtgAAAADACQhbAAAAAOAEhC0AAAAAcALCFgAAAAA4AWELAAAAAJzAo7QbAAAAAFA8uXk2nT59WgkJCS6t6+vrq6CgIJfWLI8IWwAAAEA5lJFpUWZ6qlYum6+d66u5tLanX1WNGf88gesKCFsAAABAOZRjyZWPZ566N7GqUX13l9U9k5yl5b8cV2ZmJmHrCghbAAAAQDlkseQo12rVX3/tV+rZIy6rm5yeqw1bbHrgzBmFhYW5rG55RNgCAAAAyiFbbq5kMqlGg6aq36COy+oeP5ao3A3blZaW5rKa5RVhCwAAACjHzD6+8g8Odlk977MZLqtV3jH1OwAAAAA4AWELAAAAAJyAsAUAAAAATkDYAgAAAAAnIGwBAAAAgBMQtgAAAADACUo1bP3000+64447VKNGDZlMJn399dcO6w3D0OTJkxUWFiYfHx91795dBw8edBhz9uxZDRo0SIGBgQoODtbw4cOVnp7uMGbPnj3q2LGjvL29VatWLU2fPt3ZLw0AAADANa5Uw1ZGRoauv/56zZs376Lrp0+frjfffFMLFizQ1q1b5efnp+joaGVnZ9vHDBo0SPv27VNsbKy+++47/fTTT3rkkUfs61NTU9WzZ0+Fh4dr586deuONNzRlyhS9++67Tn99AAAAAK5dpXpT4169eqlXr14XXWcYhmbPnq3nnntOd911lyTpo48+UvXq1fX111/r/vvv1++//67vv/9e27dvV5s2bSRJb731lm677Tb95z//UY0aNfTpp5/KYrHoww8/lJeXl5o2bardu3dr5syZDqEMAAAAAEpSqYaty4mLi9PJkyfVvXt3+7KgoCC1a9dOmzdv1v3336/NmzcrODjYHrQkqXv37nJzc9PWrVvVp08fbd68WZ06dZKXl5d9THR0tF5//XWdO3dOlSpVKlA7JydHOTk59sepqamSJKvVKqvV6oyXWyT5PZSFXlAxVbR9zGazycvsLUMeshnuLqlpcvOU2ewjmTxdVrO06hanps1wc/ivq+perWulZmnVLcmahd3HeH8rXk1X1f3nPnYtvb+GPORl9pbNZqswvysURVFes8kwDMOJvRSayWTSV199pbvvvluStGnTJt188806ceKEwsLC7OPuu+8+mUwmffHFF3r11Ve1aNEiHThwwGFb1apV09SpUzVq1Cj17NlTkZGReuedd+zr9+/fr6ZNm2r//v1q3LhxgV6mTJmiqVOnFli+ePFi+fr6ltArBgAAAFDeZGZmauDAgUpJSVFgYOBlx5bZI1uladKkSRo/frz9cWpqqmrVqqWePXte8Q11BavVqtjYWPXo0UOenp6l3Q4qoIq2j23btk2Txg3RxFEdFR5ZwyU1t27eo3cXrdeEx6PVqGkDl9QsrbrFqWkz3HQktY0iAnfIzWRzWd2rda3ULK26JVmzsPsY72/Fq+mquv/cx66l9/do3AlNn/+zps1apLZt27qsblmRf9ZbYZTZsBUaGipJSkxMdDiylZiYqJYtW9rHnDp1yuF5ubm5Onv2rP35oaGhSkxMdBiT/zh/zD+ZzWaZzeYCyz09PcvUL55lrR9UPBVlH3Nzc5MlJ1sm5crNlOeSmobNqpycLMmwuqxmadW9mppuJlux+yxvr7U81Sytus6oeaV9jPe34tV0dd38fexaen9NypUlJ1tubm4V4veEoirKay6z99mKjIxUaGio1qxZY1+Wmpqq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ELYAAAAAwAkIW+XMvHnzFBERIW9vb7Vr107btm0r7ZZQQUyZMkUmk8nhX6NGjUq7LZRzP/30k+644w7VqFFDJpNJX3/9tcN6wzA0efJkhYWFycfHR927d9fBgwdLp1mUS1fax4YOHVrgs+3WW28tnWZRLk2bNk033nijAgICVK1aNd199906cOCAw5js7GyNHj1aVapUkb+/v/r166fExMRS6hhlCWGrHPniiy80fvx4vfDCC/rll190/fXXKzo6WqdOnSrt1lBBNG3aVAkJCfZ/GzZsKO2WUM5lZGTo+uuv17x58y66fvr06XrzzTe1YMECbd26VX5+foqOjlZ2draLO0V5daV9TJJuvfVWh8+2zz77zIUdorxbv369Ro8erS1btig2NlZWq1U9e/ZURkaGfcy4ceP0v//9T0uXLtX69et14sQJ9e3btxS7RlnB1O/lSLt27XTjjTdq7ty5kiSbzaZatWrp8ccf17PPPlvK3aG8mzJlir7++mvt3r27tFtBBWUymfTVV1/p7rvvlnT+qFaNGjX01FNP6emnn5YkpaSkqHr16oqJidH9999fit2iPPrnPiadP7KVnJxc4IgXUFxJSUmqVq2a1q9fr06dOiklJUUhISFavHix7rnnHknSH3/8ocaNG2vz5s1q3759KXeM0sSRrXLCYrFo586d6t69u32Zm5ubunfvrs2bN5diZ6hIDh48qBo1aqhOnToaNGiQ4uPjS7slVGBxcXE6efKkw+daUFCQ2rVrx+caStS6detUrVo1NWzYUKNGjdKZM2dKuyWUYykpKZKkypUrS5J27twpq9Xq8FnWqFEj1a5dm88yELbKi9OnTysvL0/Vq1d3WF69enWdPHmylLpCRdKuXTvFxMTo+++/1/z58xUXF6eOHTsqLS2ttFtDBZX/2cXnGpzp1ltv1UcffaQ1a9bo9ddf1/r169WrVy/l5eWVdmsoh2w2m8aOHaubb75ZzZo1k3T+s8zLy0vBwcEOY/ksgyR5lHYDAMqGXr162f+/RYsWateuncLDw7VkyRINHz68FDsDgOK78HTU5s2bq0WLFqpbt67WrVunW265pRQ7Q3k0evRo/fbbb1zTjELjyFY5UbVqVbm7uxeY2SYxMVGhoaGl1BUqsuDgYDVo0EB//fVXabeCCir/s4vPNbhSnTp1VLVqVT7bUGRjxozRd999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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load your dataset (replace with your actual dataset loading code)\n",
    "df_instacart_orders \n",
    "\n",
    "# Assuming your dataset has 'order_hour_of_day' and 'order_dow' columns\n",
    "\n",
    "# Filter orders for Wednesdays (order_dow = 3) and Saturdays (order_dow = 6)\n",
    "wednesday_orders = df_instacart_orders[df_instacart_orders['order_dow'] == 3]\n",
    "saturday_orders = df_instacart_orders[df_instacart_orders['order_dow'] == 6]\n",
    "\n",
    "# Plotting the histograms overlayed\n",
    "plt.figure(figsize=(10, 6))\n",
    "\n",
    "# Plot for Wednesdays\n",
    "plt.hist(wednesday_orders['order_hour_of_day'], bins=24, color='skyblue', edgecolor='black', alpha=0.7, label='Wednesday')\n",
    "\n",
    "# Plot for Saturdays\n",
    "plt.hist(saturday_orders['order_hour_of_day'], bins=24, color='orange', edgecolor='black', alpha=0.5, label='Saturday')\n",
    "\n",
    "plt.title('Order Hour Distribution on Wednesdays and Saturdays')\n",
    "plt.xlabel('Hour of Day')\n",
    "plt.ylabel('Frequency')\n",
    "plt.grid(True)\n",
    "plt.legend()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77a6e4ec",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "\n",
    "The error message indicates that the variable df_orders has not been defined in your code before it is used. Make sure that df_orders is properly defined and assigned a DataFrame before you attempt to use it in the code.\n",
    "    \n",
    "Could you please address issues in your notebook first? It's crucial that the notebook is fully executable from start to finish before it undergoes a code review. This ensures that anyone reviewing your work can run each cell in sequence without encountering errors, which can significantly impact the review process.\n",
    "\n",
    "Ensuring your notebook's full executability involves running all cells before submission: Before submitting your notebook, please use the `Kernel -> Run All` feature to execute all cells in sequence. This helps to catch any errors or issues that might not be immediately obvious."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "652225f1",
   "metadata": {},
   "source": [
    "Not much difference in frequency until hours 11 - 14 when Saturday has a slight increase. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "charitable-congo",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v4</b>\n",
    "\n",
    "👏"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3891143",
   "metadata": {},
   "source": [
    "### [B2] What's the distribution for the number of orders per customer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d8c26c23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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jXyuAIqwQgagxtx8883685//rOXLl2vs2LEljtm0aZN+97vfqUePHpo5c6YcDoe2bdumzz77TJLUuXNnzZw5U1OnTtXtt9+uCy+8UJICTtE6cuSIhg4dquuvv1433XST4uPjS63rb3/7mwzD0P/93//p4MGDmjt3rlJTU7Vx40b/Sl55lKe2U5mmqSuuuEKrV6/WmDFj1KtXL3300Ue6//77tW/fPs2ZMydg/Keffqr//ve/uvPOOxUVFaUnn3xS11xzjXbv3q0mTZqcsa78/HwNHDhQ27Zt04QJE9SmTRu9+eabGjVqlDIzM3XPPfeoc+fOevXVVzVp0iQlJSXp3nvvlVQUEsryl7/8Ra+88kqVr5L973//07vvvqvx48dLkh555BH97ne/0wMPPKAFCxbozjvv1LFjxzRr1izdeuutWrVqVcDrjx07pssuu0zXXXedbrjhBi1ZskTjxo2T3W7XrbfeKqloleuKK67Qp59+qttvv12dO3fWDz/8oDlz5uiXX37R22+/HbDPVatWacmSJZowYYKaNm1aapOW6dOna8aMGUpNTdW4ceO0ZcsWPfPMM/rqq6/02WefyWazae7cuXrllVf01ltv6ZlnnlFkZGTAKb2nysvL08qVK3XhhReqTZs2JY4ZMWKEbr/9dr3//vsBpwIXFhYqLS1NAwYM0OOPP+4Pc7fddptee+01/eEPf9BvfvMbrVq1SsOGDSu234yMDPXv398fSuPi4vThhx9qzJgxysrKKnY63UMPPSS73a777rtPTqdTdrtd06dP1yOPPKLbbrtN559/vrKysvT111/rm2++0eDBg8/4OfpMmDBBsbGxmj59uv+z3LVrlz8ESkXNUUaOHKm0tDQ99thjysvL0zPPPKMBAwbo22+/Dfh6nekzKcl7772ntm3bVvmpoHfccYf+85//aMKECerSpYuOHDmiTz/9VD///LN69+6tv/zlLzp+/Lj27t3r/3kQGRkpqXzf16f617/+JZfLpbvuuktHjx7VrFmzdN111+mSSy7RJ598ov/7v//Ttm3b9NRTT+m+++4LCNvV9bkCOMEEgCry0ksvmZLMr7766oxjYmJizHPPPdf/eNq0aeapP4rmzJljSjIPHTp0xn189dVXpiTzpZdeKvbcb3/7W1OSuXDhwhKf++1vf+t/vHr1alOS2aJFCzMrK8u/fcmSJaYkc968ef5tycnJ5siRI8vcZ2m1jRw50kxOTvY/fvvtt01J5sMPPxww7tprrzUNwzC3bdvm3ybJtNvtAdu+++47U5L51FNPFTvWqebOnWtKMl977TX/NpfLZaakpJiRkZEB7z05OdkcNmxYqfsraezo0aPN0NBQc//+/aZpnvxs33zzzTO+f5/T54Dv/TocDnPHjh3+bc8++6wpyUxISAioecqUKaakgLG+efDEE0/4tzmdTrNXr15ms2bNTJfLZZqmab766qumxWIx//e//wUcf+HChaYk87PPPguoyWKxmJs2bSrzszl48KBpt9vNIUOGmB6Px7/96aefNiWZL774YrH3X9qcN03T3LhxoynJvOeee0od16NHD7Nx48b+xyNHjjQlmX/6059K3N+dd94ZsP0Pf/iDKcmcNm2af9uYMWPM5s2bm4cPHw4Ye/3115sxMTFmXl6eaZonv+5t27b1b/Pp2bNnuefWqXw/V/r06eP/upmmac6aNcuUZL7zzjumaZpmdna2GRsba44dOzbg9enp6WZMTEzA9jN9JiU5fvy4Kcm88sory1Xvjh07zvgz4PTPNSYmxhw/fnyp+xs2bFiJ3zfl/b721RMXF2dmZmb6x/q+b3r27Gm63W7/9htuuMG02+1mQUGBaZrV97kCOIlTFgHUqMjIyFK7Lfquo3nnnXcq3QDD4XBo9OjR5R5/yy23KCoqyv/42muvVfPmzfXBBx9U6vjl9cEHH8hqteruu+8O2H7vvffKNE19+OGHAdtTU1PVrl07/+MePXooOjpav/76a5nHSUhI0A033ODfZrPZdPfddysnJ0dr1qw56/fy4IMPqrCwUI8++uhZ78tn0KBBAf/y3q9fP0nSNddcE/D18m0//XMICQnRH//4R/9ju92uP/7xjzp48KA2bNggSXrzzTfVuXNnderUSYcPH/b/ueSSSyRJq1evDtjnb3/723JdY/fxxx/L5XJp4sSJAddOjR07VtHR0ZW63sj3fXPqey9JVFSUsrKyim0fN25cwGPf/D59/p2+2mWapv7f//t/uvzyy2WaZsDnlJaWpuPHj/tPsfMZOXJksdXl2NhYbdq0SVu3bi21/jO5/fbbA67DHDdunEJCQvzvY8WKFcrMzNQNN9wQUKPValW/fv2KfS19+yiL77Ms63OvjNjYWH3xxRdlnu5bkop+X//+979XTEyM/7Hv++amm24KuI63X79+crlc2rdvn6Tq+1wBnEQgA1CjcnJySv3FZsSIEbrgggt02223KT4+Xtdff72WLFlSoXDWokWLCjXw6NChQ8BjwzDUvn37Mq+fOlu7du1SYmJisc+jc+fO/udP1apVq2L7aNSoUYnX0Zx+nA4dOhRrqnCm41RG27ZtdfPNN+u5557TgQMHznp/UvH36/tlsmXLliVuP/1zSExMLNZM4JxzzpEk/9d269at2rRpk+Li4gL++Mb5Gm74nOlUwdP5PtOOHTsGbLfb7Wrbtm2lPnPfPCnr9hHZ2dnF5lRISIiSkpKK1WixWAJCfkk1Hzp0SJmZmXruueeKfU6+f/goz+c0c+ZMZWZm6pxzzlH37t11//336/vvvy/1vZzq9O/TyMhINW/ePOBrKRVdr3p6ncuXLy9WY0mfSUmio6Mllf25V8asWbP0448/qmXLljr//PM1ffr0Mv+Bxaei39eV/X6qrs8VwElcQwagxuzdu1fHjx8vtbV3WFiY1q5dq9WrV2vp0qVatmyZFi9erEsuuUTLly+X1Wot8zgVue6rvM5082qPx1OumqrCmY5jntYAJFj+8pe/6NVXX9Vjjz2mq666qtjzpX2GJTnT+63Kz8Hr9ap79+6aPXt2ic+f/stqdcyt8mrfvr1CQkJKDTFOp1NbtmwJ6HIqFa0aV7bLoe8fQ2666SaNHDmyxDGnX/dW0ud00UUXafv27XrnnXe0fPly/fOf/9ScOXO0cOFC3XbbbZWqraQ6X331VSUkJBR7/vRuruX9TKKjo5WYmKgff/yxXHVUZJ5fd911uvDCC/XWW29p+fLl+sc//qHHHntM//3vfzV06NByHa+8Kvv9VF2fK4CTCGQAasyrr74qSUpLSyt1nMVi0aBBgzRo0CDNnj1bf//73/WXv/xFq1evVmpq6hl/4ams00+hMk1T27ZtC/gls1GjRgHd8Xx27dqltm3b+h9XpLbk5GR9/PHHxVY0Nm/e7H++KiQnJ+v777+X1+sN+EWpqo/Trl073XTTTXr22Wf9p0OdqrTPsDrs37+/WMvtX375RZL8p0K2a9dO3333nQYNGlSl88r3mW7ZsiVgfrhcLu3YsUOpqakV3mdERIQuvvhirVq1Srt27Srx67ZkyRI5nU797ne/K1eNXq9X27dvD1gV27JlS8A4XwdGj8dTqbpP1bhxY40ePVqjR49WTk6OLrroIk2fPr1cgWzr1q26+OKL/Y9zcnJ04MABXXbZZZLkX+lr1qzZWdd5ut/97nd67rnntH79eqWkpJQ61ne7gdPn+pnmefPmzXXnnXfqzjvv1MGDB9W7d2/97W9/8weyM83Lmvy+lqrncwVQhH/CAFAjVq1apYceekht2rQptQ1ySe2WfTdY9rUh9/2CXdIv95XxyiuvBJyO9J///EcHDhwI+Bfqdu3a6fPPP5fL5fJve//994u1x69IbZdddpk8Ho+efvrpgO1z5syRYRhV9i/kl112mdLT07V48WL/tsLCQj311FOKjIzUb3/72yo5jlR0LZnb7dasWbOKPdeuXTsdP348YIXnwIEDeuutt6rs+KcqLCwMaP/ucrn07LPPKi4uTn369JFUtEKxb98+Pf/888Ven5+fr9zc3EodOzU1VXa7XU8++WTAyt0LL7yg48ePl9jJsDwefPBBmaapUaNGKT8/P+C5HTt26IEHHlDz5s0Drp07E9/8Or0z5ty5cwMeW61WXXPNNfp//+//lbhKdOjQoXLVfuTIkYDHkZGRat++fbHbC5zJc889J7fb7X/8zDPPqLCw0P8+0tLSFB0drb///e8B4ypaZ0keeOABRURE6LbbblNGRkax57dv36558+ZJKlpRa9q0qdauXRswZsGCBQGPPR6Pjh8/HrCtWbNmSkxMDPhMIiIiio2Tau77ujo/VwBFWCEDUOU+/PBDbd68WYWFhcrIyNCqVau0YsUKJScn69133y31RrozZ87U2rVrNWzYMCUnJ+vgwYNasGCBkpKSNGDAAElFv9jHxsZq4cKFioqKUkREhPr161fu63tO17hxYw0YMECjR49WRkaG5s6dq/bt2we05r/tttv0n//8R5deeqmuu+46bd++Xa+99lqx628qUtvll1+uiy++WH/5y1+0c+dO9ezZU8uXL9c777yjiRMnFtt3Zd1+++169tlnNWrUKG3YsEGtW7fWf/7zH3322WeaO3dulTYr8K2SnX4vJEm6/vrr9X//938aPny47r77bn/r7HPOOadYU4iqkJiYqMcee0w7d+7UOeeco8WLF2vjxo167rnn/M0hbr75Zi1ZskR33HGHVq9erQsuuEAej0ebN2/WkiVL9NFHHxU7/a884uLiNGXKFM2YMUOXXnqprrjiCm3ZskULFizQeeedp5tuuqlS7+miiy7S448/rsmTJ6tHjx4aNWqUmjdvrs2bN+v555+X1+vVBx98UOpNoX169eqlG264QQsWLNDx48f1m9/8RitXrtS2bduKjX300Ue1evVq9evXT2PHjlWXLl109OhRffPNN/r4449L/IeU03Xp0kUDBw5Unz591LhxY3399df+lu/l4XK5NGjQIF133XX+z3LAgAG64oorJBUFoWeeeUY333yzevfureuvv15xcXHavXu3li5dqgsuuKDYP36UV7t27fT6669rxIgR6ty5s2655RZ169ZNLpdL69at87eb97ntttv06KOP6rbbblPfvn21du1a/+qsT3Z2tpKSknTttdeqZ8+eioyM1Mcff6yvvvpKTzzxhH9cnz59tHjxYk2ePFnnnXeeIiMjdfnll9fY93V1fq4ATghaf0cA9Y6vPbXvj91uNxMSEszBgweb8+bNC2hV7nN6y/OVK1eaV155pZmYmGja7XYzMTHRvOGGG8xffvkl4HXvvPOO2aVLFzMkJCSgxfRvf/tbs2vXriXWd6a29//+97/NKVOmmM2aNTPDwsLMYcOGmbt27Sr2+ieeeMJs0aKF6XA4zAsuuMD8+uuvi+2ztNpKavuenZ1tTpo0yUxMTDRtNpvZoUMH8x//+Ifp9XoDxkkqsT32mdrxny4jI8McPXq02bRpU9Nut5vdu3cvsS13Zdven2rr1q2m1Wot1vbeNE1z+fLlZrdu3Uy73W527NjRfO21187Y9v709+tr3/2Pf/wjYHtJLfZ98+Drr782U1JSzNDQUDM5Odl8+umni9XrcrnMxx57zOzatavpcDjMRo0amX369DFnzJhhHj9+vNSayvL000+bnTp1Mm02mxkfH2+OGzfOPHbsWMCY8ra9P9XatWvNK6+80mzatKlps9nMVq1amWPHjjV37txZbOzIkSPNiIiIEveTn59v3n333WaTJk3MiIgI8/LLLzf37NlTrD27aRbNofHjx5stW7Y0bTabmZCQYA4aNMh87rnn/GNK+lr4PPzww+b5559vxsbGmmFhYWanTp3Mv/3tbwGt7Evi+7myZs0a8/bbbzcbNWpkRkZGmjfeeKN55MiRYuNXr15tpqWlmTExMWZoaKjZrl07c9SoUebXX39drs+kNL/88os5duxYs3Xr1qbdbjejoqLMCy64wHzqqaf8beJN0zTz8vLMMWPGmDExMWZUVJR53XXXmQcPHgz4XJ1Op3n//febPXv2NKOiosyIiAizZ8+e5oIFCwKOmZOTY/7hD38wY2NjTUkBP0PK831dke8b0zzz7Uuq83MFGjrDNGvJ1eAAAACnWbRokUaPHq2vvvqqUquVAFDbcQ0ZAAAAAAQJgQwAAAAAgoRABgAAAABBwjVkAAAAABAkrJABAAAAQJAQyAAAAAAgSLgxdBXxer3av3+/oqKiZBhGsMsBAAAAECSmaSo7O1uJiYmyWEpfAyOQVZH9+/erZcuWwS4DAAAAQC2xZ88eJSUllTqGQFZFoqKiJBV96NHR0SWOcbvdWr58uYYMGSKbzVaT5aGWYS5AYh7gJOYCJOYBTmIu1H1ZWVlq2bKlPyOUhkBWRXynKUZHR5cayMLDwxUdHc03VwPHXIDEPMBJzAVIzAOcxFyoP8pzKRNNPQAAAAAgSAhkAAAAABAkBDIAAAAACBICGQAAAAAECYEMAAAAAIKEQAYAAAAAQUIgAwAAAIAgIZABAAAAQJAQyAAAAAAgSAhkAAAAABAkBDIAAAAACBICGQAAAAAECYEMAAAAAIIkJNgFoGp5TVN7ctzKdZuKsBlqGWmTxTCCXRYAAACAEhDI6pEtmU59vDdX2W6vf1uUzaLUpAh1jHUEsTIAAAAAJeGUxXpiS6ZTb+3IDghjkpTt9uqtHdnakukMUmUAAAAAzoRAVg94TVMf780tdczHe3PlNc0aqggAAABAeRDI6oE9Oe5iK2Ony3Z7tSfHXUMVAQAAACgPAlk9kOsu38pXeccBAAAAqBkEsnogwla+LorlHQcAAACgZhDI6oGWkTZF2Ur/UkbZLGoZaauhigAAAACUB4GsHrAYhlKTIkodk5oUwf3IAAAAgFqGQFZPdIx1aHibqGIrZWFWQ8PbRHEfMgAAAKAW4sbQ9UjHWIc6xNi1J8et/x3I097cQvVuGkoYAwAAAGopVsjqGYthKDnKrnNOhLBDBZ4gVwQAAADgTAhk9VSzMKsk6WB+YZArAQAAAHAmBLJ6qllo0dmomS6vXB7uPwYAAADURgSyeircZlFkSNGX91ABq2QAAABAbUQgq8c4bREAAACo3Qhk9VhcWNFpiwfzaewBAAAA1EYEsnqMFTIAAACgdiOQ1WPNTqyQHcr3yDRp7AEAAADUNgSyeqxJqFVWQ3J5TWW6vMEuBwAAAMBpCGT1mMUw1DSU0xYBAACA2opAVs818zf2IJABAAAAtQ2BrJ5rRqdFAAAAoNYikNVzcXRaBAAAAGotAlk9F39ihey4yyunh8YeAAAAQG1CIKvnwkIsirIVfZkPcdoiAAAAUKsQyBoAbhANAAAA1E4EsgYgjsYeAAAAQK1EIGsAaH0PAAAA1E4EsgbAd8rioYJCmaYZ5GoAAAAA+BDIGoDGDqushuT2SsecdFoEAAAAagsCWQNgMQzFhZ44bbGA0xYBAACA2oJA1kDQaREAAACofQhkDUQzOi0CAAAAtQ6BrIGI8zX2YIUMAAAAqDUIZA1E/IkVsuMurwo8NPYAAAAAagMCWQMRGmJRtK3oy32I0xYBAACAWoFA1oDE0dgDAAAAqFUIZA3IycYeBDIAAACgNiCQNSB0WgQAAABqFwJZA9LslE6LXtMMcjUAAAAAghrIpk+fLsMwAv506tTJ/3xBQYHGjx+vJk2aKDIyUtdcc40yMjIC9rF7924NGzZM4eHhatasme6//34VFgaekvfJJ5+od+/ecjgcat++vRYtWlSslvnz56t169YKDQ1Vv3799OWXX1bLew6mRg6rQgyp0JQynXRaBAAAAIIt6CtkXbt21YEDB/x/Pv30U/9zkyZN0nvvvac333xTa9as0f79+3X11Vf7n/d4PBo2bJhcLpfWrVunl19+WYsWLdLUqVP9Y3bs2KFhw4bp4osv1saNGzVx4kTddttt+uijj/xjFi9erMmTJ2vatGn65ptv1LNnT6WlpengwYM18yHUEIthKI7ryAAAAIBaI+iBLCQkRAkJCf4/TZs2lSQdP35cL7zwgmbPnq1LLrlEffr00UsvvaR169bp888/lyQtX75cP/30k1577TX16tVLQ4cO1UMPPaT58+fL5XJJkhYuXKg2bdroiSeeUOfOnTVhwgRde+21mjNnjr+G2bNna+zYsRo9erS6dOmihQsXKjw8XC+++GLNfyDVrBmdFgEAAIBaIyTYBWzdulWJiYkKDQ1VSkqKHnnkEbVq1UobNmyQ2+1Wamqqf2ynTp3UqlUrrV+/Xv3799f69evVvXt3xcfH+8ekpaVp3Lhx2rRpk84991ytX78+YB++MRMnTpQkuVwubdiwQVOmTPE/b7FYlJqaqvXr15+xbqfTKafT6X+clZUlSXK73XK73SW+xrf9TM/XhMZ2Q5KUnnfmOlH9asNcQPAxD+DDXIDEPMBJzIW6ryJfu6AGsn79+mnRokXq2LGjDhw4oBkzZujCCy/Ujz/+qPT0dNntdsXGxga8Jj4+Xunp6ZKk9PT0gDDme973XGljsrKylJ+fr2PHjsnj8ZQ4ZvPmzWes/ZFHHtGMGTOKbV++fLnCw8NLfd8rVqwo9fnqlOeIluK7a/exHH2waU3Q6kCRYM4F1B7MA/gwFyAxD3ASc6HuysvLK/fYoAayoUOH+v/eo0cP9evXT8nJyVqyZInCwsKCWFnZpkyZosmTJ/sfZ2VlqWXLlhoyZIiio6NLfI3b7daKFSs0ePBg2Wy2mio1QIHH1Pyfs1QYEqpL0oYq1GoEpY6GrjbMBQQf8wA+zAVIzAOcxFyo+3xnz5VH0E9ZPFVsbKzOOeccbdu2TYMHD5bL5VJmZmbAKllGRoYSEhIkSQkJCcW6Ifq6MJ465vTOjBkZGYqOjlZYWJisVqusVmuJY3z7KInD4ZDD4Si23WazlfmNU54x1cVmk6JtFmW5vTrmNtQqlG/yYArmXEDtwTyAD3MBEvMAJzEX6q6KfN2C3tTjVDk5Odq+fbuaN2+uPn36yGazaeXKlf7nt2zZot27dyslJUWSlJKSoh9++CGgG+KKFSsUHR2tLl26+Mecug/fGN8+7Ha7+vTpEzDG6/Vq5cqV/jH1jf8G0QU09gAAAACCKaiB7L777tOaNWu0c+dOrVu3TsOHD5fVatUNN9ygmJgYjRkzRpMnT9bq1au1YcMGjR49WikpKerfv78kaciQIerSpYtuvvlmfffdd/roo4/04IMPavz48f7VqzvuuEO//vqrHnjgAW3evFkLFizQkiVLNGnSJH8dkydP1vPPP6+XX35ZP//8s8aNG6fc3FyNHj06KJ9LdaPTIgAAAFA7BPWUxb179+qGG27QkSNHFBcXpwEDBujzzz9XXFycJGnOnDmyWCy65ppr5HQ6lZaWpgULFvhfb7Va9f7772vcuHFKSUlRRESERo4cqZkzZ/rHtGnTRkuXLtWkSZM0b948JSUl6Z///KfS0tL8Y0aMGKFDhw5p6tSpSk9PV69evbRs2bJijT7qC/8KWb4nyJUAAAAADVtQA9kbb7xR6vOhoaGaP3++5s+ff8YxycnJ+uCDD0rdz8CBA/Xtt9+WOmbChAmaMGFCqWPqC18gO5xfKK9pymLQ2AMAAAAIhlp1DRlqRqzDIptFKjSlY05WyQAAAIBgIZA1QBbDUFwopy0CAAAAwUYga6DiaOwBAAAABB2BrIE62diDQAYAAAAEC4GsgaLTIgAAABB8BLIGynfKYrbbq/xCb5CrAQAAABomAlkDFWq1KMZe9OXntEUAAAAgOAhkDRinLQIAAADBRSBrwJrRaREAAAAIKgJZAxZHp0UAAAAgqAhkDVj8iUB2uMAjr2kGuRoAAACg4SGQNWCxdovsFkMeUzpawHVkAAAAQE0jkDVghmH429/T2AMAAACoeQSyBi4u9MR1ZAVcRwYAAADUNAJZA0enRQAAACB4CGQNHPciAwAAAIKHQNbA+a4hy3F7lVfoDXI1AAAAQMNCIGvgHFaLYu1F04DTFgEAAICaRSADpy0CAAAAQUIgwymt71khAwAAAGoSgQz+FbJDBDIAAACgRhHIoPgTgexwgUce0wxyNQAAAEDDQSCDYuwW2S2GPKZ0tIDryAAAAICaQiCDDMPgOjIAAAAgCAhkkESnRQAAACAYCGSQJDVjhQwAAACocQQySDp1hYxABgAAANQUAhkkSXGhRYEst9BUrtsb5GoAAACAhoFABkmS3WqokaNoOnA/MgAAAKBmEMjg5zttMYNABgAAANQIAhn8fKct0mkRAAAAqBkEMvj5Oi0eKmCFDAAAAKgJBDL4+U5ZPFzgkcdrBrkaAAAAoP4jkMEvxm6Rw2LIa0pHnJy2CAAAAFQ3Ahn8DMNQHDeIBgAAAGoMgQwBTt4gmhUyAAAAoLoRyBDgZCBjhQwAAACobgQyBPB3WiSQAQAAANWOQIYATU/ciyy30FSu2xvkagAAAID6jUCGAHarocYOGnsAAAAANYFAhmLotAgAAADUDAIZiqHTIgAAAFAzCGQophkrZAAAAECNIJChGN8K2ZECjwq9ZpCrAQAAAOovAhmKibZZ5LAa8qoolAEAAACoHgQyFGMYBqctAgAAADWAQIYSnWzsQSADAAAAqguBDCVqFkqnRQAAAKC6EchQIv8piwWFMk0aewAAAADVgUCGEjUNC5EhKb/QVG4hgQwAAACoDgQylMhmMdTIQWMPAAAAoDoRyHBGdFoEAAAAqheBDGd0stMijT0AAACA6kAgwxnR+h4AAACoXgQynJHvlMUjBR4VemnsAQAAAFQ1AhnOKMpmUajVkCnpcAGnLQIAAABVjUCGMzIMg9MWAQAAgGpEIEOp4ui0CAAAAFQbAhlK5VshO0SnRQAAAKDKEchQqvhTTlk0TRp7AAAAAFWJQIZSNQ21ypCU7zGV4/YGuxwAAACgXiGQoVQhFkONQ33XkXHaIgAAAFCVCGQoU7NQGnsAAAAA1YFAhjLR+h4AAACoHgQylMkfyLg5NAAAAFClak0ge/TRR2UYhiZOnOjfVlBQoPHjx6tJkyaKjIzUNddco4yMjIDX7d69W8OGDVN4eLiaNWum+++/X4WFgSs5n3zyiXr37i2Hw6H27dtr0aJFxY4/f/58tW7dWqGhoerXr5++/PLL6nibdVKzE/ciO1rgUaGXTosAAABAVakVgeyrr77Ss88+qx49egRsnzRpkt577z29+eabWrNmjfbv36+rr77a/7zH49GwYcPkcrm0bt06vfzyy1q0aJGmTp3qH7Njxw4NGzZMF198sTZu3KiJEyfqtttu00cffeQfs3jxYk2ePFnTpk3TN998o549eyotLU0HDx6s/jdfB0TaLAqzGjIlHWaVDAAAAKgyQQ9kOTk5uvHGG/X888+rUaNG/u3Hjx/XCy+8oNmzZ+uSSy5Rnz599NJLL2ndunX6/PPPJUnLly/XTz/9pNdee029evXS0KFD9dBDD2n+/PlyuVySpIULF6pNmzZ64okn1LlzZ02YMEHXXnut5syZ4z/W7NmzNXbsWI0ePVpdunTRwoULFR4erhdffLFmP4xayjAMxZ04bTGD68gAAACAKhMS7ALGjx+vYcOGKTU1VQ8//LB/+4YNG+R2u5Wamurf1qlTJ7Vq1Urr169X//79tX79enXv3l3x8fH+MWlpaRo3bpw2bdqkc889V+vXrw/Yh2+M79RIl8ulDRs2aMqUKf7nLRaLUlNTtX79+jPW7XQ65XQ6/Y+zsrIkSW63W263u8TX+Laf6fnarKnD0O4cKT3XpS7R1mCXU+fV5bmAqsM8gA9zARLzACcxF+q+inztghrI3njjDX3zzTf66quvij2Xnp4uu92u2NjYgO3x8fFKT0/3jzk1jPme9z1X2pisrCzl5+fr2LFj8ng8JY7ZvHnzGWt/5JFHNGPGjGLbly9frvDw8DO+TpJWrFhR6vO1UWZEM6lJB23Zd0gF3/4Y7HLqjbo4F1D1mAfwYS5AYh7gJOZC3ZWXl1fusUELZHv27NE999yjFStWKDQ0NFhlVNqUKVM0efJk/+OsrCy1bNlSQ4YMUXR0dImvcbvdWrFihQYPHiybzVZTpVaJjHyPXtueI29ErIYOHSrDMIJdUp1Wl+cCqg7zAD7MBUjMA5zEXKj7fGfPlUfQAtmGDRt08OBB9e7d27/N4/Fo7dq1evrpp/XRRx/J5XIpMzMzYJUsIyNDCQkJkqSEhIRi3RB9XRhPHXN6Z8aMjAxFR0crLCxMVqtVVqu1xDG+fZTE4XDI4XAU226z2cr8xinPmNomwRoiQzkq8JgqkFXRNk5brAp1cS6g6jEP4MNcgMQ8wEnMhbqrIl+3oDX1GDRokH744Qdt3LjR/6dv37668cYb/X+32WxauXKl/zVbtmzR7t27lZKSIklKSUnRDz/8ENANccWKFYqOjlaXLl38Y07dh2+Mbx92u119+vQJGOP1erVy5Ur/GEghFkNNQotC2MF8Oi0CAAAAVSFoK2RRUVHq1q1bwLaIiAg1adLEv33MmDGaPHmyGjdurOjoaN11111KSUlR//79JUlDhgxRly5ddPPNN2vWrFlKT0/Xgw8+qPHjx/tXr+644w49/fTTeuCBB3Trrbdq1apVWrJkiZYuXeo/7uTJkzVy5Ej17dtX559/vubOnavc3FyNHj26hj6NuqFZWIgOF3h0ML9Q7WPswS4HAAAAqPOC3mWxNHPmzJHFYtE111wjp9OptLQ0LViwwP+81WrV+++/r3HjxiklJUUREREaOXKkZs6c6R/Tpk0bLV26VJMmTdK8efOUlJSkf/7zn0pLS/OPGTFihA4dOqSpU6cqPT1dvXr10rJly4o1+mjomoVZ9dMx6SCt7wEAAIAqUasC2SeffBLwODQ0VPPnz9f8+fPP+Jrk5GR98MEHpe534MCB+vbbb0sdM2HCBE2YMKHctTZEzU7ci4xTFgEAAICqEfQbQ6Pu8AWyY06P3F4zyNUAAAAAdR+BDOUWEWIoPMSQKekwpy0CAAAAZ41AhnIzDENxoZy2CAAAAFQVAhkqpFnYidb3BayQAQAAAGeLQIYKOdnYg0AGAAAAnC0CGSrk1E6LpkljDwAAAOBsEMhQIU1CrbJIcnpMZbm9wS4HAAAAqNMIZKiQEIuhJqEnriPjtEUAAADgrBDIUGHcIBoAAACoGgQyVJi/0yIrZAAAAMBZIZChwnwrZIdYIQMAAADOCoEMFeYLZEedHrk8dFoEAAAAKotAhgqLsFkUHmJIkg5zg2gAAACg0ghkqBQaewAAAABnj0CGSjkZyFghAwAAACqLQIZKiQstmjo7s13ale2S1+RaMgAAAKCiQoJdAOqeLZlOrd6fJ0k66vTq39uyFGWzKDUpQh1jHUGuDgAAAKg7WCFDhWzJdOqtHdnKKwxcEct2e/XWjmxtyXQGqTIAAACg7iGQody8pqmP9+aWOubjvbmcvggAAACUE4EM5bYnx61st7fUMdlur/bkuGuoIgAAAKBuI5Ch3HLd5Vv5Ku84AAAAoKEjkKHcImxGlY4DAAAAGjoCGcqtZaRNUbbSp0yUzaKWkbYaqggAAACo2whkKDeLYSg1KaLUMalJEbIYrJABAAAA5UEgQ4V0jHVoeJuoYitlIYY0vE0U9yEDAAAAKoAbQ6PCOsY61CHGrj05bu3Icuvzg/kKDzEIYwAAAEAFsUKGSrEYhpKj7EpJCJMhKcttKtvtCXZZAAAAQJ1CIMNZcVgtiguzSpL25RQGuRoAAACgbiGQ4awlRRR1Vdybyw2hAQAAgIogkOGstYgouhRxXy4rZAAAAEBFEMhw1lqcWCHLyCuU22sGuRoAAACg7iCQ4azF2C2KtFnklbSf0xYBAACAciOQ4awZhqEkTlsEAAAAKoxAhirhO21xHytkAAAAQLkRyFAlkiKLVsj25hbKNLmODAAAACgPAhmqRLOwENksktNj6nABN4gGAAAAyoNAhiphNQw1D/edtsh1ZAAAAEB5EMhQZXyNPbhBNAAAAFA+BDJUGV9jj705BDIAAACgPAhkqDItTqyQZbq8ynV7g1wNAAAAUPsRyFBlQkMsigu1SuK0RQAAAKA8CGSoUifvR0ZjDwAAAKAsBDJUKf/9yLiODAAAACgTgQxVyrdClp5fKLeXG0QDAAAApSGQoUrF2i2KCDHkNaX0PE5bBAAAAEpDIEOVMgyD9vcAAABAORHIUOWSImnsAQAAAJQHgQxVLunE/cj25bplmlxHBgAAAJwJgQxVLj4sRCGGlO8xddTpCXY5AAAAQK1FIEOVs1oMJYSfaH/PaYsAAADAGRHIUC1815HR2AMAAAA4MwIZqkVSBI09AAAAgLIQyFAtWpxo7HHU6VFeoTfI1QAAAAC1E4EM1SIsxKImoVZJRd0WAQAAABRXqUD266+/VnUdqId87e/35nDaIgAAAFCSSgWy9u3b6+KLL9Zrr72mgoKCqq4J9UQL/3VkrJABAAAAJalUIPvmm2/Uo0cPTZ48WQkJCfrjH/+oL7/8sqprQx3na+xxIK9QhV5uEA0AAACcrlKBrFevXpo3b57279+vF198UQcOHNCAAQPUrVs3zZ49W4cOHarqOlEHNXJYFB5iyGNK6XmctggAAACc7qyaeoSEhOjqq6/Wm2++qccee0zbtm3Tfffdp5YtW+qWW27RgQMHqqpO1EGGYXDaIgAAAFCKswpkX3/9te688041b95cs2fP1n333aft27drxYoV2r9/v6688sqqqhN1lL+xB/cjAwAAAIoJqcyLZs+erZdeeklbtmzRZZddpldeeUWXXXaZLJaifNemTRstWrRIrVu3rspaUQedukJmmqYMwwhyRQAAAEDtUalA9swzz+jWW2/VqFGj1Lx58xLHNGvWTC+88MJZFYe6LyE8RFZDyis0dczpVeMT9yYDAAAAUMlAtnXr1jLH2O12jRw5sjK7Rz0SYjHUPDxEe3MLtTfXTSADAAAATlGpa8heeuklvfnmm8W2v/nmm3r55ZfPuijULzT2AAAAAEpWqUD2yCOPqGnTpsW2N2vWTH//+9/PuijULy1o7AEAAACUqFKBbPfu3WrTpk2x7cnJydq9e3e59/PMM8+oR48eio6OVnR0tFJSUvThhx/6ny8oKND48ePVpEkTRUZG6pprrlFGRkaxWoYNG6bw8HA1a9ZM999/vwoLA3/x/+STT9S7d285HA61b99eixYtKlbL/Pnz1bp1a4WGhqpfv37c6LoK+W4QfaTAo/xCb5CrAQAAAGqPSgWyZs2a6fvvvy+2/bvvvlOTJk3KvZ+kpCQ9+uij2rBhg77++mtdcskluvLKK7Vp0yZJ0qRJk/Tee+/pzTff1Jo1a7R//35dffXV/td7PB4NGzZMLpdL69at08svv6xFixZp6tSp/jE7duzQsGHDdPHFF2vjxo2aOHGibrvtNn300Uf+MYsXL9bkyZM1bdo0ffPNN+rZs6fS0tJ08ODBynw8OE24zaLGjqJrx/axSgYAAAD4VSqQ3XDDDbr77ru1evVqeTweeTwerVq1Svfcc4+uv/76cu/n8ssv12WXXaYOHTronHPO0d/+9jdFRkbq888/1/Hjx/XCCy9o9uzZuuSSS9SnTx+99NJLWrdunT7//HNJ0vLly/XTTz/ptddeU69evTR06FA99NBDmj9/vlwulyRp4cKFatOmjZ544gl17txZEyZM0LXXXqs5c+b465g9e7bGjh2r0aNHq0uXLlq4cKHCw8P14osvVubjQQl8py1yHRkAAABwUqW6LD700EPauXOnBg0apJCQol14vV7dcsstlb6GzOPx6M0331Rubq5SUlK0YcMGud1upaam+sd06tRJrVq10vr169W/f3+tX79e3bt3V3x8vH9MWlqaxo0bp02bNuncc8/V+vXrA/bhGzNx4kRJksvl0oYNGzRlyhT/8xaLRampqVq/fv0Z63U6nXI6nf7HWVlZkiS32y23u+TQ4dt+pufrs+ahFv0gaU+2S263PdjlBF1Dngs4iXkAH+YCJOYBTmIu1H0V+dpVKpDZ7XYtXrxYDz30kL777juFhYWpe/fuSk5OrvC+fvjhB6WkpKigoECRkZF666231KVLF23cuFF2u12xsbEB4+Pj45Weni5JSk9PDwhjvud9z5U2JisrS/n5+Tp27Jg8Hk+JYzZv3nzGuh955BHNmDGj2Pbly5crPDy81Pe8YsWKUp+vj5whYVJib+3LcWnpBx/KkBnskmqFhjgXUBzzAD7MBUjMA5zEXKi78vLyyj22UoHM55xzztE555xzNrtQx44dtXHjRh0/flz/+c9/NHLkSK1Zs+as9lkTpkyZosmTJ/sfZ2VlqWXLlhoyZIiio6NLfI3b7daKFSs0ePBg2Wy2miq1VjBNUws2Z6tAVvUeOFjNw89q6tV5DXku4CTmAXyYC5CYBziJuVD3+c6eK49K/Vbs8Xi0aNEirVy5UgcPHpTXG9g5b9WqVeXel91uV/v27SVJffr00VdffaV58+ZpxIgRcrlcyszMDFgly8jIUEJCgiQpISGhWDdEXxfGU8ec3pkxIyND0dHRCgsLk9VqldVqLXGMbx8lcTgccjgcxbbbbLYyv3HKM6Y+ahERou1ZbqU7pVYxDe/9l6ShzgUEYh7Ah7kAiXmAk5gLdVdFvm6Vaupxzz336J577pHH41G3bt3Us2fPgD9nw+v1yul0qk+fPrLZbFq5cqX/uS1btmj37t1KSUmRJKWkpOiHH34I6Ia4YsUKRUdHq0uXLv4xp+7DN8a3D7vdrj59+gSM8Xq9WrlypX8MqkYSN4gGAAAAAlRqheyNN97QkiVLdNlll53VwadMmaKhQ4eqVatWys7O1uuvv65PPvlEH330kWJiYjRmzBhNnjxZjRs3VnR0tO666y6lpKSof//+kqQhQ4aoS5cuuvnmmzVr1iylp6frwQcf1Pjx4/2rV3fccYeefvppPfDAA7r11lu1atUqLVmyREuXLvXXMXnyZI0cOVJ9+/bV+eefr7lz5yo3N1ejR48+q/eHQEmRRYFsb45bpmnKMIwgVwQAAAAEV6WbevhOMzwbBw8e1C233KIDBw4oJiZGPXr00EcffaTBgwdLkubMmSOLxaJrrrlGTqdTaWlpWrBggf/1VqtV77//vsaNG6eUlBRFRERo5MiRmjlzpn9MmzZttHTpUk2aNEnz5s1TUlKS/vnPfyotLc0/ZsSIETp06JCmTp2q9PR09erVS8uWLSvW6ANnJyE8RBZDyi00ddzlVeyJe5MBAAAADVWlAtm9996refPm6emnnz6rVY4XXnih1OdDQ0M1f/58zZ8//4xjkpOT9cEHH5S6n4EDB+rbb78tdcyECRM0YcKEUsfg7NgshhLCQrQ/r1B7c90EMgAAADR4lQpkn376qVavXq0PP/xQXbt2LXbR2n//+98qKQ71T1KkrSiQ5RSqW+NgVwMAAAAEV6UCWWxsrIYPH17VtaABaBFRNOVo7AEAAABUMpC99NJLVV0HGghfp8VDBR4VFHoVGlKpRp8AAABAvVDp34YLCwv18ccf69lnn1V2drYkaf/+/crJyamy4lD/RNgsirUXTbv9eYVBrgYAAAAIrkqtkO3atUuXXnqpdu/eLafTqcGDBysqKkqPPfaYnE6nFi5cWNV1oh5JirQp86hTe3PcahttD3Y5AAAAQNBU+sbQffv21bFjxxQWFubfPnz48GI3YQZO5zttcW8uK2QAAABo2Cq1Qva///1P69atk90euLrRunVr7du3r0oKQ/3la+xxIM8tj2nKyg2iAQAA0EBVaoXM6/XK4/EU2753715FRUWddVGo35qGWuWwGnJ7pYP5rJIBAACg4apUIBsyZIjmzp3rf2wYhnJycjRt2jRddtllVVUb6inDMPyrZHtzCGQAAABouCoVyJ544gl99tln6tKliwoKCvSHP/zBf7riY489VtU1oh7yXUfG/cgAAADQkFXqGrKkpCR99913euONN/T9998rJydH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qmnTpkpLSyvxfXi9Xs2cOVNJSUlyOBzq1auXli1b5n/eMAxt2LBBM2fOlGEYmj59eon7GT9+vOx2u5YvX67f/va3atWqlYYOHaqPP/5Y+/bt01/+8hf/2NatW+uhhx7SLbfcoujoaN1+++2Sik5RbNWqlcLDwzV8+PASV9beeecd9e7dW6GhoWrbtq1mzJihwsLCgHqfeeYZXXHFFYqIiNDf/vY3HTt2TDfeeKPi4uIUFhamDh06lPiZAwDKh0AGAKhWVqtVf//73/XUU09p7969Z7WvVatWaf/+/Vq7dq1mz56tadOm6Xe/+50aNWqkL774QnfccYf++Mc/FjvO/fffr3vvvVfffvutUlJSdPnll/sDSmZmpi655BKde+65+vrrr7Vs2TJlZGTouuuuC9jHyy+/LLvdrs8++0wLFy4ssb558+bpiSee0OOPP67vv/9eaWlpuuKKK7R161ZJ0oEDB9S1a1fde++9OnDggO67775i+zh69Kg++ugj3XnnnQoLCwt4LiEhQTfeeKMWL14s0zT92x9//HH17NlT3377rf7617/qiy++0JgxYzRhwgRt3LhRF198sR5++OGAff3vf//TLbfconvuuUc//fSTnn32WS1atEh/+9vfAsZNnz5dw4cP1w8//KBbb71Vf/3rX/XTTz/pww8/1M8//6xnnnlGTZs2Le3LBgAojQkAQDUZOXKkeeWVV5qmaZr9+/c3b731VtM0TfOtt94yT/1f0LRp08yePXsGvHbOnDlmcnJywL6Sk5NNj8fj39axY0fzwgsv9D8uLCw0IyIizH//+9+maZrmjh07TEnmo48+6h/jdrvNpKQk87HHHjNN0zQfeughc8iQIQHH3rNnjynJ3LJli2mapvnb3/7WPPfcc8t8v4mJiebf/va3gG3nnXeeeeedd/of9+zZ05w2bdoZ9/H555+bksy33nqrxOdnz55tSjIzMjJM0zTN5ORk86qrrgoYc8MNN5iXXXZZwLYRI0aYMTEx/seDBg0y//73vweMefXVV83mzZv7H0syJ06cGDDm8ssvN0ePHn3G+gEAFcMKGQCgRjz22GN6+eWX9fPPP1d6H127dpXFcvJ/XfHx8erevbv/sdVqVZMmTXTw4MGA16WkpPj/HhISor59+/rr+O6777R69WpFRkb6/3Tq1ElS0fVePn369Cm1tqysLO3fv18XXHBBwPYLLrigUu/ZPGUFrCx9+/YNePzzzz+rX79+AdtO/Qykovc9c+bMgPc9duxYHThwQHl5eWfc97hx4/TGG2+oV69eeuCBB7Ru3bpy1wkAKC4k2AUAABqGiy66SGlpaZoyZYpGjRoV8JzFYikWQEpqIGGz2QIeG4ZR4jav11vuunJycnT55ZfrscceK/Zc8+bN/X+PiIgo9z7PRvv27WUYhn7++WcNHz682PM///yzGjVqpLi4uLOqLScnRzNmzNDVV19d7LnQ0NAz7nvo0KHatWuXPvjgA61YsUKDBg3S+PHj9fjjj1e4BgAA15ABAGrQo48+qvfee0/r168P2B4XF6f09PSAUFaV9w77/PPP/X8vLCzUhg0b1LlzZ0lS7969tWnTJrVu3Vrt27cP+FORoBMdHa3ExER99tlnAds/++wzdenSpdz7adKkiQYPHqwFCxYoPz8/4Ln09HT961//0ogRI0q9bUDnzp31xRdfBGw79TOQit73li1bir3n9u3bB6xCliQuLk4jR47Ua6+9prlz5+q5554r9/sDAAQikAEAakz37t1144036sknnwzYPnDgQB06dEizZs3S9u3bNX/+fH344YdVdtz58+frrbfe0ubNmzV+/HgdO3ZMt956q6SijoZHjx7VDTfcoK+++krbt2/XRx99pNGjR8vj8VToOPfff78ee+wxLV68WFu2bNGf/vQnbdy4Uffcc0+F9vP000/L6XQqLS1Na9eu1Z49e7Rs2TINHjxYLVq0KNZ443R33323li1bpscff1xbt27V008/HdDtUZKmTp2qV155RTNmzNCmTZv0888/64033tCDDz5Y6r6nTp2qd955R9u2bdOmTZv0/vvv+8MtAKDiCGQAgBo1c+bMYqcUdu7cWQsWLND8+fPVs2dPffnllyV2IKysRx99VI8++qh69uypTz/9VO+++66/M6BvVcvj8WjIkCHq3r27Jk6cqNjY2DJXik539913a/Lkybr33nvVvXt3LVu2TO+++646dOhQof106NBBX3/9tdq2bavrrrtO7dq10+23366LL75Y69evV+PGjUt9ff/+/fX8889r3rx56tmzp5YvX14saKWlpen999/X8uXLdd5556l///6aM2eOkpOTS9233W7XlClT1KNHD1100UWyWq164403KvT+AAAnGWZFrhoGAAAAAFQZVsgAAAAAIEgIZAAAAAAQJAQyAAAAAAgSAhkAAAAABAmBDAAAAACChEAGAAAAAEFCIAMAAACAICGQAQAAAECQEMgAAAAAIEgIZAAAAAAQJAQyAAAAAAiS/w9FRJ4Uf7IlEgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "df_instacart_orders \n",
    "\n",
    "# Calculate number of orders per customer (user)\n",
    "orders_per_customer = df_instacart_orders.groupby('user_id')['order_id'].nunique()\n",
    "\n",
    "# Plotting the line graph\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(orders_per_customer.value_counts().sort_index().index, orders_per_customer.value_counts().sort_index().values, marker='o', linestyle='-', color='skyblue')\n",
    "plt.title('Distribution of Number of Orders per Customer')\n",
    "plt.xlabel('Number of Orders')\n",
    "plt.ylabel('Frequency')\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56ebc4ef",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v3</b>\n",
    "\n",
    "\n",
    "The same issue here. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2eff7d5",
   "metadata": {},
   "source": [
    "Calculate number of orders per customer (user), .groupby('user_id')['order_id'].nunique()\n",
    "Plotting the line graph"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a3ee52e",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v4</b>\n",
    "\n",
    "Well done! "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54a0319c",
   "metadata": {},
   "source": [
    "### [B3] What are the top 20 popular products (display their id and name)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "universal-facial",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Read products and order_products data\n",
    "df_instacart_products \n",
    "df_instacart_order_products \n",
    "\n",
    "# Step 2: Merge products data with order_products to get product names\n",
    "merged_df = pd.merge(df_instacart_order_products, df_instacart_products, on='product_id')\n",
    "\n",
    "# Step 3: Count occurrences of each product and sort to get top 20\n",
    "top_products = merged_df['product_name'].value_counts().head(20)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "bbcdd20b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top 20 Popular Products:\n",
      "1. Product ID: 24852, Name: Banana\n",
      "2. Product ID: 13176, Name: Bag of Organic Bananas\n",
      "3. Product ID: 21137, Name: Organic Strawberries\n",
      "4. Product ID: 21903, Name: Organic Baby Spinach\n",
      "5. Product ID: 47209, Name: Organic Hass Avocado\n",
      "6. Product ID: 47766, Name: Organic Avocado\n",
      "7. Product ID: 47626, Name: Large Lemon\n",
      "8. Product ID: 16797, Name: Strawberries\n",
      "9. Product ID: 26209, Name: Limes\n",
      "10. Product ID: 27845, Name: Organic Whole Milk\n",
      "11. Product ID: 27966, Name: Organic Raspberries\n",
      "12. Product ID: 22935, Name: Organic Yellow Onion\n",
      "13. Product ID: 24964, Name: Organic Garlic\n",
      "14. Product ID: 45007, Name: Organic Zucchini\n",
      "15. Product ID: 39275, Name: Organic Blueberries\n",
      "16. Product ID: 49683, Name: Cucumber Kirby\n",
      "17. Product ID: 28204, Name: Organic Fuji Apple\n",
      "18. Product ID: 5876, Name: Organic Lemon\n",
      "19. Product ID: 8277, Name: Apple Honeycrisp Organic\n",
      "20. Product ID: 40706, Name: Organic Grape Tomatoes\n"
     ]
    }
   ],
   "source": [
    "# Display the top 20 popular products (ID and Name)\n",
    "print(\"Top 20 Popular Products:\")\n",
    "for idx, (product_name, count) in enumerate(top_products.iteritems(), 1):\n",
    "    print(f\"{idx}. Product ID: {merged_df.loc[merged_df['product_name'] == product_name, 'product_id'].iloc[0]}, Name: {product_name}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "92ecfe2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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GoVatWoV6WfGjBmIiIiAra0tNm7ciC1btggj04V69eoFBQUF9OrVS+Z+FMfDwwP/+9//4OnpCQsLC/Tr1w9WVlY4cuQIFBT+75Xxffv2xYsXL9C0aVOMGDEC/v7+wqvbPsaQIUPw448/okePHmjWrBkePnyI4cOHy7Tp168fFi9ejJCQEDRo0AAdO3ZESkrKR5+TiIiIiIgIqAKrl5eXQYMG4dq1azh16lRFh1Kh0tLSYGpqitjY2E/+kQF4s3q5vb29zHu4K4PClQ25ejkRUeXA1cuJiKi0q5crlFhDMoKCguDu7g41NTUcPHgQGzZsQEhISEWHVWFev36Nhw8f4tdffxVeJUZERERERESymHSX0oULF7BgwQI8ffoU9erVw9KlS4u86qoqiYmJgZubGywsLIR3XRMREREREZEsJt2ltG3btooO4avi6upapnefl1Z0dPRn75OIiIiIiKiiMOkm+oLG2unw9WFERERERFVIlVi9nIiIiIiIiKgiMOkmIiIiIiIiKidMuomIiIiIiIjKCZNuIiIiIiIionLChdSIvqDghIdQVn9V0WEQEX01JjnUrOgQiIiIyhVHuomIiIiIiIjKCZNuIiIiIiIionLCpJuIiIiIiIionDDp/gqkpaVBJBJBIpFUdCj0/xkbG2Px4sUVHQYREREREX3jKn3SnZGRAV9fX+jr60NRURFGRkbw9/fHw4cPKzo0gYGBATIzM9GwYcOPOv59SburqytGjx79aQF+on/++QeKiooffX1ERERERETfqkqddN+8eROOjo5ISUnBli1bcOPGDaxcuRJRUVFo0aIFHj16VOKxr159uRWm5eXlIRaLoaBQOReTDwsLQ/fu3ZGdnY3z589XdDhERERERERfTKVOukeMGAFFRUUcOXIELi4uMDQ0RPv27REZGYk7d+5gypQpQltjY2PMnDkTffv2haamJgYPHgwACA0NhYGBAVRVVeHl5YXg4GBoa2sLx6WmpqJz586oXbs21NXV0aRJE0RGRsrEYWxsjDlz5sDX1xcaGhowNDTE6tWrhfriRqqvXr2Kjh07QlNTExoaGnB2dkZqauon35NNmzbB0dERGhoaEIvF6N27N+7fvy/UP378GN7e3tDV1YWKigrMzc2xfv16AG9+iPDz84Oenh6UlZVhZGSEuXPnvvd8UqkU69evR58+fdC7d2+s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HpV47KtXX27la3l5eYjFYigofNoi9+np6Thz5gz8/Pywbt26zxQdERERERHR149JdwUYMWIEFBUVceTIEbi4uMDQ0BDt27dHZGQk7ty5gylTpghtjY2NMXPmTPTt2xeampoYPHgwACA0NBQGBgZQVVWFl5cXgoODoa2tLRyXmpqKzp07o3bt2lBXV0eTJk0QGRkpE4exsTHmzJkDX19faGhowNDQEKtXrxbqi5tefvXqVXTs2BGamprQ0NCAs7MzUlNT33u969evR8eOHTFs2DBs2bIFL168AABcv34dIpEI165dk2m/aNEimJqaCvsnTpxA06ZNoaSkBD09PUyaNAl5eXlCfUFBARYsWAAzMzMoKSnB0NAQs2fPFuonTpwICwsLqKqqol69eggMDMTr169lzjlv3jzUrl0bGhoaGDBgAF6+fClTX1BQgN9++w1169aFkpIS7O3tcejQofdeNxEREREREZPuL+zRo0c4fPgwhg8fDhUVFZk6sVgMb29vbN26FVKpVCgPCgqCnZ0d4uPjERgYiJiYGAwdOhT+/v6QSCRwd3eXSTIBICcnBx06dEBUVBTi4+PRrl07eHp6Ij09XabdwoUL4ejoiPj4eAwfPhzDhg1DcnJysbHfuXMHrVu3hpKSEo4dO4aLFy/C19dXJgF+l1Qqxfr16/Hzzz/DysoKZmZm2LFjBwDAwsICjo6OCA8PlzkmPDwcvXv3Fs7ZoUMHNGnSBAkJCVixYgXWrl2LWbNmCe0nT56MefPmITAwEImJidi8eTNq164t1GtoaCAsLAyJiYlYsmQJQkNDsWjRIqF+27ZtmD59OubMmYO4uDjo6ekhJCREJqYlS5Zg4cKFCAoKwuXLl+Hh4YFOnTohJSWl2OvOzc1Fdna2zEZERERERFWPSPp2dkfl7vz582jevDl27dqFLl26FKlftGgRxo4di3///Re1atWCsbExHBwcsGvXLqFNz549kZOTg3379gllP//8M/bt24cnT56UeO6GDRti6NCh8PPzA/BmpNvZ2RmbNm0C8CZBFovFmDFjBoYOHYq0tDSYmJggPj4e9vb2+OWXXxAREYHk5GRUq1atVNd79OhReHt74+7du1BQUMDixYuxe/duREdHAwAWL16M5cuX48aNGwDejH5bWloiKSkJVlZWmDJlCv766y8kJSVBJBIBAEJCQjBx4kRk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UlLExdHRESNHjhQ/877VfQqFApmZmTA2NubfWh3VrVu3cq++vHLlClq0aAGA30capNqeyY2ovgsLCxPU1dWF7du3C5cuXRImTpwo6OnpKc0iSm/OgwcPhOTkZCE5OVkAIISEhAjJycnCn3/+KQjCs1d06OnpCT///LPwxx9/CAMHDqzwFR0dOnQQfvvtN+HMmTOClZWV0is6cnNzBSMjI+GTTz4RLly4IISFhQlaWlrlXtHRuHFjITg4WEhLSxMWLFjAV3RUYvLkyYKurq4QExOj9EqcR48eiXUmTZokmJmZCdHR0UJiYqLg7OwsODs7i+Wlr8T58MMPhZSUFCEiIkIwNDSs8JU4s2bNEtLS0oQ1a9ZU+Eoc/r1WzZw5c4RTp04J169fF/744w9hzpw5gkQiEY4fPy4IAu/Zu+L52csFgfetLpo5c6YQExMjXL9+XYiLixP69OkjNG3aVLhz544gCLxndVF8fLzQuHFjYenSpUJGRoawa9cuQUtLS/jf//4n1uH3kYaFSTfRW/D9998LZmZmgpqamuDk5CScO3eutkOqt06ePCkAKLeMGTNGEIRnr+mYP3++YGRkJKirqwu9e/cW0tPTldq4d++eMHz4cEEqlQoymUwYO3as8ODBA6U6qampwgcffCCoq6sLzZs3F5YvX14ulr179wrW1taCmpqa0LZtW+HIkSM1dt7vsoruFwBh27ZtYp3Hjx8Lfn5+gr6+vqClpSV4eXkJ2dnZSu3cuHFD8PDwEDQ1NYWmTZsKM2fOFIqKipTqnDx5Umjfvr2gpqYmWFhYKB2jFP9eq8bX11do0aKFoKamJhgaGgq9e/cWE25B4D17V5RNunnf6p6hQ4cKxsbGgpqamtC8eXNh6NChSu975j2rm3755RehXbt2grq6utC6dWth48aNSuX8PtKwSARBEGqnj52IiIiIiIiofuMz3UREREREREQ1hEk3ERERERERUQ1h0k1ERERERERUQ5h0ExEREREREdUQJt1ERERERERENYRJNxEREREREVENYdJNREREREREVEOYdBMRERERERHVECbdRERERERERDWESTcRERHVCz4+PpBIJOWWq1ev1nZoRETUgDWu7QCIiIiI3pS+ffti27ZtStsMDQ2V1gsLC6GmpvY2wyIiogaMPd1ERERUb6irq0MulystvXv3hr+/P6ZNm4amTZvC3d0dAHDhwgV4eHhAKpXCyMgIn3zyCf7991+xrYcPH2L06NGQSqUwNjbGypUr0aNHD0ybNk2sI5FIcPDgQaUY9PT0sH37dnE9KysL3t7e0NPTQ5MmTTBw4EDcuHFDLPfx8cGgQYMQHBwMY2NjGBgYYMqUKSgqKhLrFBQUYPbs2TA1NYW6ujosLS2xZcsWCIIAS0tLBAcHK8WQkpLCXn4iojqCSTcRERHVe6GhoVBTU0NcXBzWr1+P3Nxc9OrVCx06dEBiYiIiIiLwzz//wNvbW9xn1qxZOHXqFH7++WccP34cMTEx+P3336t13KKiIri7u0NHRwexsbGIi4uDVCpF3759UVhYKNY7efIkMjMzcfLkSYSGhmL79u1Kifvo0aOxe/durFq1CmlpadiwYQOkUikkEgl8fX3L9e5v27YN3bt3h6Wl5atdMCIiemM4vJyIiIjqjcOHD0MqlYrrHh4eAAArKyusWLFC3L5kyRJ06NABy5YtE7dt3boVpqamuHLlCkxMTLBlyxb873//Q+/evQE8S9zfe++9asWzZ88elJSUYPPmzZBIJACeJcR6enqIiYnBhx9+CADQ19fH6tWroaKigtatW6N///6IiorChAkTcOXKFezduxcnTpxAnz59AAAWFhbiMXx8fPDll18iPj4eTk5OKCoqwg8//FCu95uIiGoHk24iIiKqN3r27Il169aJ69ra2hg+fDg6deqkVC81NRUnT55UStBLZWZm4vHjxygsLESXLl3E7U2aNIGNjU214klNTcXVq1eho6OjtP3JkyfIzMwU19u2bQsVFRVx3djYGOfPnwfwbKi4iooKXF1dKzyGiYkJ+vfvj61bt8LJyQm//PILCgoKMGTIkGrFSkRENYNJNxEREdUb2traFQ6p1tbWVlpXKBTw9PTEf//733J1jY2Nq/wstEQigSAIStuefxZboVCgU6dO2LVrV7l9n5/gTVVVtVy7JSUlAABNTc2XxjF+/Hh88skn+Oabb7Bt2zYMHToUWlpaVToHIiKqWUy6iYiIqMHp2LEj9u3bB3NzczRuXP7rUKtWraCqqorffvsNZmZmAID79+/jypUrSj3OhoaGyM7OFtczMjLw6NEjpePs2bMHzZo1g0wme6VY7ezsUFJSglOnTonDy8vq168ftLW1sW7dOkREROD06dOvdCwiInrzOJEaERERNThTpkxBTk4Ohg8fjoSEBGRmZuLYsWMYO3Ysnj59CqlUinHjxmHWrFmIjo7GhQsX4OPjg0aNlL869erVC6tXr0ZycjISExMxadIkpV7rkSNHomnTphg4cCBiY2Nx/fp1xMTE4LPPPsNff/1VpVjNzc0xZswY+Pr64uDBg2Ibe/fuFeuoqKjAx8cHc+fOhZWVFZydnd/MhSIiotfGpJuIiIgaHBMTE8TFxeHp06f48MMPYWdnh2nTpkFPT09MrL/++mu4uLjA09MTffr0wQcffFDu2fCVK1fC1NQULi4uGDFiBAIDA5WGdWtpaeH06dMwMzPDRx99BFtbW4wbNw5PnjypVs/3unXrMHjwYPj5+aF169aYMGECHj58qFRn3LhxKCwsxNixY1/jyhAR0ZsmEco+iEREREREFerRowfat2+Pb7/9trZDKSc2Nha9e/dGVlYWjIyMajscIiL6//GZbiIiIqJ3WEFBAe7evYuFCxdiyJAhTLiJiOoYDi8nIiIieoft3r0bLVq0QG5urtK7yImIqG7g8HIiIiIiIiKiGsKebiIiIiIiIqIawqSbiIiIiIiIqIYw6SYiIiIiIiKqIUy6iYiIiIiIiGoIk24iIiIiIiKiGsKkm4iIiIiIiKiGMOkmIiIiIiIiqiFMuomIiIiIiIhqCJNuIiIiIiIiohry/wGB8GFryA1JfgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Step 1: Read products and order_products data\n",
    "df_instacart_products \n",
    "df_instacart_order_products \n",
    "\n",
    "# Step 2: Merge products data with order_products to get product names\n",
    "merged_df = pd.merge(df_instacart_order_products, df_instacart_products, on='product_id')\n",
    "\n",
    "# Step 3: Count occurrences of each product and sort to get top 20\n",
    "top_products = merged_df['product_name'].value_counts().head(20)\n",
    "\n",
    "# Plotting the results\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.barh(top_products.index, top_products.values, color='skyblue')\n",
    "plt.xlabel('Frequency')\n",
    "plt.ylabel('Product Name')\n",
    "plt.title('Top 20 Products by Frequency')\n",
    "plt.gca().invert_yaxis()  # To have the first product on top\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7df00f47",
   "metadata": {},
   "source": [
    "Step 1: Read products and order_products data.\n",
    "Step 2: Merge products data with order_products to get product names\n",
    "Step 3: Count occurrences of each product and sort to get top 20\n",
    "Display the top 20 popular products (ID and Name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1bcc8fb9",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Additionally, you could plot the results on this query in the following way: \n",
    "\n",
    "```\n",
    "plt.figure(figsize=(10,6))\n",
    "plt.barh(top_20_popular['product_name'], top_20_popular['product_id'], color='skyblue')\n",
    "plt.xlabel('Product ID')\n",
    "plt.ylabel('Product Name')\n",
    "plt.title('Barplot of Product IDs against Product Names')\n",
    "plt.gca().invert_yaxis()  # To have the first product on top\n",
    "plt.tight_layout()\n",
    "plt.show()   \n",
    "```\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "gross-theme",
   "metadata": {},
   "source": [
    "# [C] Hard (must complete at least two to pass)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "romantic-deposit",
   "metadata": {},
   "source": [
    "### [C1] How many items do people typically buy in one order? What does the distribution look like?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "sensitive-breathing",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "# Assuming df_instacart_order_products is already loaded\n",
    "\n",
    "# Create a pivot table to count the number of items per order\n",
    "pivot_table = df_instacart_order_products.pivot_table(index='order_id', values='product_id', aggfunc='count')\n",
    "\n",
    "# Rename the 'product_id' column to 'num_items'\n",
    "pivot_table.rename(columns={'product_id': 'num_items'}, inplace=True)\n",
    "\n",
    "# Calculate the mean number of items per order\n",
    "mean_num_items = pivot_table['num_items'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "completed-frank",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2QAAAIjCAYAAABswtioAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAACKQklEQVR4nOzdeXxTVf7/8XfSJunesrZga6mAbKIgzmAVFaVSkK8LOu4LIurowIyA48LoKOiMuAwoKorLCG6Mgj9RRxQoiyKKG8uoIBUQWaRlL93btLm/P0IioVvaptn6ej4ePC65Obn3c3NSyKfn3M8xGYZhCAAAAADgd+ZABwAAAAAArRUJGQAAAAAECAkZAAAAAAQICRkAAAAABAgJGQAAAAAECAkZAAAAAAQICRkAAAAABAgJGQAAAAAECAkZAAAAAAQICRmAsDN58mSZTCa/nGvw4MEaPHiw+/Enn3wik8mkd955xy/nv/HGG9WlSxe/nKupiouLdfPNNyslJUUmk0njx48PdEhNMnjwYJ100kmBDsNrr7/+unr27CmLxaKkpKRAhwMfc/1b88knnwQ6FADNREIGIKjNmTNHJpPJ/ScqKkqdO3dWdna2nn76aRUVFfnkPLt379bkyZO1fv16nxzPl4I5Nm888sgjmjNnjm6//Xa9/vrruv766+ts26VLF5lMJv35z3+u8Zy/k91QtmnTJt14443q2rWrXnrpJb344ot1tnX9AmP//v3ufXPnztVTTz3lh0jDl2EYev3113X22WcrKSlJMTEx6tu3rx566CGVlJQEOjwAQSQy0AEAgDceeughZWRkyG63Kz8/X5988onGjx+v6dOn64MPPtDJJ5/sbnv//ffr3nvvbdTxd+/erSlTpqhLly7q16+f169bsmRJo87TFPXF9tJLL8nhcLR4DM2xfPlynX766XrwwQe9fs1LL72kSZMmqXPnzi0YWfj65JNP5HA4NGPGDHXr1q3Rr587d65++OGHkB3NDLTq6mpdc801mjdvns466yxNnjxZMTEx+uyzzzRlyhTNnz9fS5cuVXJycqBDBRAEGCEDEBKGDx+u6667TqNHj9akSZO0ePFiLV26VHv37tVFF12ksrIyd9vIyEhFRUW1aDylpaWSJKvVKqvV2qLnqo/FYpHNZgvY+b2xd+/eRk2Z69Onj6qrq/Xoo4+2XFBByuFwqLy8vNnH2bt3ryQxVbGFNNRPjz/+uObNm6e//vWvWrlypcaPH69bb71Vr7/+ut577z1t3LhRN954Y73nMAzD49+1lsaoHRA4JGQAQtZ5552nv//979q+fbveeOMN9/7a7iHLycnRoEGDlJSUpLi4OPXo0UN/+9vfJDlHE373u99JkkaPHu2eHjlnzhxJv907tGbNGp199tmKiYlxv/bYe8hcqqur9be//U0pKSmKjY3VRRddpJ07d3q06dKlS61fyo4+ZkOx1XYPWUlJie68806lpaXJZrOpR48e+te//iXDMDzamUwmjRs3Tu+9955OOukk2Ww29enTR4sWLar9DT/G3r17NWbMGCUnJysqKkqnnHKKXn31VffzrimG27Zt08KFC92x//LLL/Uet0uXLrrhhhv00ksvaffu3fW2reseuto+A67rnT9/vnr37q3o6GhlZmbq+++/lyS98MIL6tatm6KiojR48OA641yzZo3OOOMMRUdHKyMjQ7NmzarRpqKiQg8++KC6desmm82mtLQ03X333aqoqKg1pjfffFN9+vSRzWZr8P1/7rnn3G07d+6ssWPHqqCgwP18ly5d3KORHTp0kMlk0uTJk+s95tEGDx6shQsXavv27e4+O/o9buy1NfX93rx5sy677DKlpKQoKipKqampuuqqq3T48OEG43f9vAain8rKyvTEE0/oxBNP1NSpU2s8f+GFF2rUqFFatGiRvvzyS/f+Ll266P/+7/+0ePFinXbaaYqOjtYLL7wgSdq1a5cuueQSxcbGqmPHjpowYUKNGF2++uorDRs2TImJiYqJidE555yjzz//3KON6+dj48aNuuaaa9SmTRsNGjSo3vcVQMthyiKAkHb99dfrb3/7m5YsWaJbbrml1jYbNmzQ//3f/+nkk0/WQw89JJvNpi1btri/pPTq1UsPPfSQHnjgAd16660666yzJElnnHGG+xgHDhzQ8OHDddVVV+m6665rcKrRP//5T5lMJt1zzz3au3evnnrqKWVlZWn9+vWKjo72+vq8ie1ohmHooosu0ooVKzRmzBj169dPixcv1l133aVff/1VTz75pEf7VatW6d1339Wf/vQnxcfH6+mnn9Zll12mHTt2qF27dnXGVVZWpsGDB2vLli0aN26cMjIyNH/+fN14440qKCjQHXfcoV69eun111/XhAkTlJqaqjvvvFOSM0loyH333afXXntNjz76qJ5++mlv364GffbZZ/rggw80duxYSdLUqVP1f//3f7r77rv13HPP6U9/+pMOHTqkxx9/XDfddJOWL1/u8fpDhw7pggsu0BVXXKGrr75a8+bN0+233y6r1aqbbrpJknP05KKLLtKqVat06623qlevXvr+++/15JNP6qefftJ7773ncczly5dr3rx5GjdunNq3b19vkZbJkydrypQpysrK0u23367c3Fw9//zz+uabb/T555/LYrHoqaee0muvvaYFCxbo+eefV1xcnMeU3obcd999Onz4sHbt2uX+vMTFxTXp2pr6fldWVio7O1sVFRX685//rJSUFP3666/68MMPVVBQoMTExHqvIZD9tGrVKh06dEh33HGHIiNr/5p1ww03aPbs2frwww91+umnu/fn5ubq6quv1h//+Efdcsst6tGjh8rKyjRkyBDt2LFDf/nLX9S5c2e9/vrrNT6brhiHDx+uAQMG6MEHH5TZbNbs2bN13nnn6bPPPtPvf/97j/aXX365unfvrkceeaTGL2wA+JEBAEFs9uzZhiTjm2++qbNNYmKi0b9/f/fjBx980Dj6n7cnn3zSkGTs27evzmN88803hiRj9uzZNZ4755xzDEnGrFmzan3unHPOcT9esWKFIck47rjjjMLCQvf+efPmGZKMGTNmuPelp6cbo0aNavCY9cU2atQoIz093f34vffeMyQZ//jHPzza/eEPfzBMJpOxZcsW9z5JhtVq9dj3v//9z5BkPPPMMzXOdbSnnnrKkGS88cYb7n2VlZVGZmamERcX53Ht6enpxogRI+o9Xm1tR48ebURFRRm7d+82DOO393b+/Pl1Xr/LsZ8B1/XabDZj27Zt7n0vvPCCIclISUnxiHnSpEmGJI+2rs/BtGnT3PsqKiqMfv36GR07djQqKysNwzCM119/3TCbzcZnn33mcf5Zs2YZkozPP//cIyaz2Wxs2LChwfdm7969htVqNYYOHWpUV1e79z/77LOGJOOVV16pcf31febraztixIha39fGXltT3+9169bV6GtvBbqfXD8bCxYsqLPNwYMHDUnGpZde6t6Xnp5uSDIWLVpU6/HmzZvn3ldSUmJ069bNkGSsWLHCMAzDcDgcRvfu3Y3s7GzD4XC425aWlhoZGRnG+eef797n6vOrr766wesB0PKYsggg5MXFxdVbbdF1H83777/f5AIYNptNo0eP9rr9DTfcoPj4ePfjP/zhD+rUqZM++uijJp3fWx999JEiIiL0l7/8xWP/nXfeKcMw9PHHH3vsz8rKUteuXd2PTz75ZCUkJOjnn39u8DwpKSm6+uqr3fssFov+8pe/qLi4WJ9++mmzr+X+++9XVVWVT+8lGzJkiMfIxsCBAyVJl112mUd/ufYf+z5ERkbqj3/8o/ux1WrVH//4R+3du1dr1qyRJM2fP1+9evVSz549tX//fvef8847T5K0YsUKj2Oec8456t27d4OxL126VJWVlRo/frzM5t/++77llluUkJCghQsXevMWNEtjr62p77drBGzx4sXu+zUbI5D95Pq36OjrO5brucLCQo/9GRkZys7O9tj30UcfqVOnTvrDH/7g3hcTE6Nbb73Vo9369eu1efNmXXPNNTpw4ID7ekpKSjRkyBCtXLmyxr9/t912W4PXA6DlkZABCHnFxcX1fvm58sordeaZZ+rmm29WcnKyrrrqKs2bN69Rydlxxx3XqOId3bt393hsMpnUrVu3Bu+faq7t27erc+fONd6PXr16uZ8/2vHHH1/jGG3atNGhQ4caPE/37t09EoP6ztMUJ5xwgq6//nq9+OKLysvLa/bxpJrX6/rin5aWVuv+Y9+Hzp07KzY21mPfiSeeKEnuvt28ebM2bNigDh06ePxxtXMV3HDJyMjwKnbXe9qjRw+P/VarVSeccIJP3vOGNPbamvp+Z2RkaOLEiXr55ZfVvn17ZWdna+bMmQ3eP+YSyH5y/ezV90uiupK22s6xfft2devWrcY9kcd+DjZv3ixJGjVqVI1revnll1VRUVHj/fP2mgC0LO4hAxDSdu3apcOHD9db2js6OlorV67UihUrtHDhQi1atEhvv/22zjvvPC1ZskQRERENnqcx9315q67Fq6urq72KyRfqOo8RJPeT3HfffXr99df12GOP6ZJLLqnxfH3vYW3qul5fvg8Oh0N9+/bV9OnTa33+2GSkJT5bLaWx19ac93vatGm68cYb9f7772vJkiX6y1/+oqlTp+rLL79UampqE6/gNy3VT65fSnz33Xe1fmZdz0mqMeLWnM+C6xdMTzzxRJ1Ld7juBfTF+QD4DgkZgJD2+uuvS1KNaT7HMpvNGjJkiIYMGaLp06frkUce0X333acVK1YoKyurzi/2TeX6bbWLYRjasmWLR3GFNm3aeFTHc9m+fbtOOOEE9+PGxJaenq6lS5eqqKjI47fvmzZtcj/vC+np6fruu+/kcDg8Rsl8fZ6uXbvquuuu0wsvvOCe1na0+t7DlrB7926VlJR4jL789NNPkuSemte1a1f973//05AhQ3z6uXK9p7m5uR6fj8rKSm3btk1ZWVk+O1ddcbfUtdWlb9++6tu3r+6//3598cUXOvPMMzVr1iz94x//qPd1gewnVzXXuXPn6r777qs1+XzttdckSf/3f//X4PHS09P1ww8/yDAMjzhzc3M92rmmHickJPj0swCg5TFlEUDIWr58uR5++GFlZGTo2muvrbPdwYMHa+xz/QbZVTra9cWtti/3TfHaa695TFl65513lJeXp+HDh7v3de3aVV9++aUqKyvd+z788MMa5fEbE9sFF1yg6upqPfvssx77n3zySZlMJo/zN8cFF1yg/Px8vf322+59VVVVeuaZZxQXF6dzzjnHJ+eRnPeS2e12Pf744zWe69q1qw4fPuwecZCkvLw8LViwwGfnP1pVVZW7FLnkTIZeeOEFdejQQQMGDJAkXXHFFfr111/10ksv1Xh9WVlZk9d7ysrKktVq1dNPP+0xkvTvf/9bhw8f1ogRI5p03NrExsbWOj2wpa7tWIWFhaqqqvLY17dvX5nN5jrLvR8tkP0UExOjv/71r8rNzdV9991X4/mFCxdqzpw5ys7O9qiwWJcLLrhAu3fv1jvvvOPeV1paqhdffNGj3YABA9S1a1f961//UnFxcY3j7Nu3rwlXA8AfGCEDEBI+/vhjbdq0SVVVVdqzZ4+WL1+unJwcpaen64MPPqh3IeiHHnpIK1eu1IgRI5Senq69e/fqueeeU2pqqnvtna5duyopKUmzZs1SfHy8YmNjNXDgwCbfY9G2bVsNGjRIo0eP1p49e/TUU0+pW7duHqX5b775Zr3zzjsaNmyYrrjiCm3dulVvvPGGR5GNxsZ24YUX6txzz9V9992nX375RaeccoqWLFmi999/X+PHj69x7Ka69dZb9cILL+jGG2/UmjVr1KVLF73zzjv6/PPP9dRTT9V7T19juUbJjl7jzOWqq67SPffco5EjR+ovf/mLSktL9fzzz+vEE0/U2rVrfRaDS+fOnfXYY4/pl19+0Yknnqi3335b69ev14svviiLxSLJuRTDvHnzdNttt2nFihU688wzVV1drU2bNmnevHnudaYaq0OHDpo0aZKmTJmiYcOG6aKLLlJubq6ee+45/e53v9N1113ns+scMGCA3n77bU2cOFG/+93vFBcXpwsvvLDFru1Yy5cv17hx43T55ZfrxBNPVFVVlV5//XVFRETosssua/D1gewnSbr33nu1bt06PfbYY1q9erUuu+wyRUdHa9WqVXrjjTfUq1evWj/Ptbnlllv07LPP6oYbbtCaNWvUqVMnvf7664qJifFoZzab9fLLL2v48OHq06ePRo8ereOOO06//vqrVqxYoYSEBP33v/9t0vUAaGEBrPAIAA1ylb13/bFarUZKSopx/vnnGzNmzPAone1ybMnzZcuWGRdffLHRuXNnw2q1Gp07dzauvvpq46effvJ43fvvv2/07t3biIyM9Cgzf8455xh9+vSpNb66yt7/5z//MSZNmmR07NjRiI6ONkaMGGFs3769xuunTZtmHHfccYbNZjPOPPNM49tvv61xzPpiq63se1FRkTFhwgSjc+fOhsViMbp372488cQTHqWwDcNZynvs2LE1YqqrHP+x9uzZY4wePdpo3769YbVajb59+9Zamr+pZe+PtnnzZiMiIqLWUuhLliwxTjrpJMNqtRo9evQw3njjjTrL3h97vdu2bTMkGU888YTH/tpK7Ls+B99++62RmZlpREVFGenp6cazzz5bI97KykrjscceM/r06WPYbDajTZs2xoABA4wpU6YYhw8frjemhjz77LNGz549DYvFYiQnJxu33367cejQIY82zS17X1xcbFxzzTVGUlKSIcnjM9aca/P2/f7555+Nm266yejatasRFRVltG3b1jj33HONpUuXNng9wdJP1dXVxuzZs40zzzzTSEhIMKKioow+ffoYU6ZMMYqLi2u0r+/nZPv27cZFF11kxMTEGO3btzfuuOMOY9GiRR5l713WrVtnXHrppUa7du0Mm81mpKenG1dccYWxbNkyd5vGfD4AtDyTYQTJndsAAADNNHjwYO3fv18//PBDoEMBAK9wDxkAAAAABAgJGQAAAAAECAkZAAAAAAQI95ABAAAAQIAwQgYAAAAAAUJCBgAAAAABwsLQPuJwOLR7927Fx8fLZDIFOhwAAAAAAWIYhoqKitS5c2eZzfWPgZGQ+cju3buVlpYW6DAA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AAAIEBKyEDZz5kx16dJFUVFRGjhwoL7++utAh4RaTJ06Vb/73e8UHx+vjh076pJLLlFubq5Hm/Lyco0dO1bt2rVTXFycLrvsMu3ZsydAEaMujz76qEwmk8aPH+/eR98Ft19//VXXXXed2rVrp+joaPXt21fffvut+3nDMPTAAw+oU6dOio6OVlZWljZv3hzAiOFSXV2tv//978rIyFB0dLS6du2qhx9+WEfXIqP/gsfKlSt14YUXqnPnzjKZTHrvvfc8nvemrw4ePKhrr71WCQkJSkpK0pgxY1RcXOzHq2i96us/u92ue+65R3379lVsbKw6d+6sG264Qbt37/Y4Bv3XdCRkIertt9/WxIkT9eCDD2rt2rU65ZRTlJ2drb179wY6NBzj008/1dixY/Xll18qJydHdrtdQ4cOVUlJibvNhAkT9N///lfz58/Xp59+qt27d+vSSy8NYNQ41jfffKMXXnhBJ598ssd++i54HTp0SGeeeaYsFos+/vhjbdy4UdOmTVObNm3cbR5//HE9/fTTmjVrlr766ivFxsYqOztb5eXlAYwckvTYY4/p+eef17PPPqsff/xRjz32mB5//HE988wz7jb0X/AoKSnRKaecopkzZ9b6vDd9de2112rDhg3KycnRhx9+qJUrV+rWW2/11yW0avX1X2lpqdauXau///3vWrt2rd59913l5ubqoosu8mhH/zWDgZD0+9//3hg7dqz7cXV1tdG5c2dj6tSpAYwK3ti7d68hyfj0008NwzCMgoICw2KxGPPnz3e3+fHHHw1JxurVqwMVJo5SVFRkdO/e3cjJyTHOOecc44477jAMg74Ldvfcc48xaNCgOp93OBxGSkqK8cQTT7j3FRQUGDabzfjPf/7jjxBRjxEjRhg33XSTx75LL73UuPbaaw3DoP+CmSRjwYIF7sfe9NXGjRsNScY333zjbvPxxx8bJpPJ+PXXX/0WO2r2X22+/vprQ5Kxfft2wzDov+ZihCwEVVZWas2aNcrKynLvM5vNysrK0urVqwMYGbxx+PBhSVLbtm0lSWvWrJHdbvfoz549e+r444+nP4PE2LFjNWLECI8+kui7YPfBBx/otNNO0+WXX66OHTuqf//+eumll9zPb9u2Tfn5+R79l5iYqIEDB9J/QeCMM87QsmXL9NNPP0mS/ve//2nVqlUaPny4JPovlHjTV6tXr1ZSUpJOO+00d5usrCyZzWZ99dVXfo8Z9Tt8+LBMJpOSkpIk0X/NFRnoANB4+/fvV3V1tZKTkz32Jycna9OmTQGKCt5wOBwaP368zjzzTJ100kmSpPz8fFmtVvc/ai7JycnKz88PQJQ42ltvvaW1a9fqm2++qfEcfRfcfv75Zz3//POaOHGi/va3v+mbb77RX/7yF1mtVo0aNcrdR7X9W0r/Bd69996rwsJC9ezZUxEREaqurtY///lPXXvttZJE/4UQb/oqPz9fHTt29Hg+MjJSbdu2pT+DTHl5ue655x5dffXVSkhIkET/NRcJGeBHY8eO1Q8//KBVq1YFOhR4YefOnbrjjjuUk5OjqKioQIeDRnI4HDrttNP0yCOPSJL69++vH374QbNmzdKoUaMCHB0aMm/ePL355puaO3eu+vTpo/Xr12v8+PHq3Lkz/QcEiN1u1xVXXCHDMPT8888HOpywwZTFENS+fXtFRETUqOS2Z88epaSkBCgqNGTcuHH68MMPtWLFCqWmprr3p6SkqLKyUgUFBR7t6c/AW7Nmjfbu3atTTz1VkZGRioyM1Keffqqnn35akZGRSk5Opu+CWKdOndS7d2+Pfb169dKOHTskyd1H/FsanO666y7de++9uuqqq9S3b19df/31mjBhgqZOnSqJ/gsl3vRVSkpKjcJkVVVVOnjwIP0ZJFzJ2Pbt25WTk+MeHZPov+YiIQtBVqtVAwYM0LJly9z7HA6Hli1bpszMzABGhtoYhqFx48ZpwYIFWr58uTIyMjyeHzBggCwWi0d/5ubmaseOHfRngA0ZMkTff/+91q9f7/5z2mmn6dprr3X/nb4LXmeeeWaNJSZ++uknpaenS5IyMjKUkpLi0X+FhYX66quv6L8gUFpaKrPZ82tKRESEHA6HJPovlHjTV5mZmSooKNCaNWvcbZYvXy6Hw6GBAwf6PWZ4ciVjmzdv1tKlS9WuXTuP5+m/Zgp0VRE0zVtvvWXYbDZjzpw5xsaNG41bb73VSEpKMvLz8wMdGo5x++23G4mJicYnn3xi5OXluf+Ulpa629x2223G8ccfbyxfvtz49ttvjczMTCMzMzOAUaMuR1dZNAz6Lph9/fXXRmRkpPHPf/7T2Lx5s/Hmm28aMTExxhtvvOFu8+ijjxpJSUnG+++/b3z33XfGxRdfbGRkZBhlZWUBjByGYRijRo0yjjvuOOPDDz80tm3bZrz77rtG+/btjbvvvtvdhv4LHkVFRca6deuMdevWGZKM6dOnG+vWrXNX4fOmr4YNG2b079/f+Oqrr4xVq1YZ3bt3N66++upAXVKrUl//VVZWGhdddJGRmppqrF+/3uO7TEVFhfsY9F/TkZCFsGeeecY4/vjjDavVavz+9783vvzyy0CHhFpIqvXP7Nmz3W3KysqMP/3pT0abNm2MmJgYY+TIkUZeXl7ggkadjk3I6Lvg9t///tc46aSTDJvNZvTs2dN48cUXPZ53OBzG3//+dyM5Odmw2WzGkCFDjNzc3ABFi6MVFhYad9xxh3H88ccbUVFRxgknnGDcd999Hl8A6b/gsWLFilr/rxs1apRhGN711YEDB4yrr77aiIuLMxISEozRo0cbRUVFAbia1qe+/tu2bVud32VWrFjhPgb913QmwzhqyXsAAAAAgN9wDxkAAAAABAgJGQAAAAAECAkZAAAAAAQICRkAAAAABAgJGQAAAAAECAkZAAAAAAQICRkAAAAABAgJGQAAAAAECAkZAKDV+OWXX2QymbR+/fpAh+K2adMmnX766YqKilK/fv0CHQ4AwM9IyAAAfnPjjTfKZDLp0Ucf9dj/3nvvyWQyBSiqwHrwwQcVGxur3NxcLVu2rNY2N954oy655BL348GDB2v8+PH+CRAA0KJIyAAAfhUVFaXHHntMhw4dCnQoPlNZWdnk127dulWDBg1Senq62rVr58OoAAChgIQMAOBXWVlZSklJ0dSpU+tsM3ny5BrT95566il16dLF/dg1avTII48oOTlZSUlJeuihh1RVVaW77rpLbdu2VWpqqmbPnl3j+Js2bdIZZ5yhqKgonXTSSfr00089nv/hhx80fPhwxcXFKTk5Wddff73279/vfn7w4MEaN26cxo8fr/bt2ys7O7vW63A4HHrooYeUmpoqm82mfv36adGiRe7nTSaT1qxZo4ceekgmk0mTJ0+u55377bo//fRTzZgxQyaTSSaTSb/88ovXcf/5z3/W+PHj1aZNGyUnJ+ull15SSUmJRo8erfj4eHXr1k0ff/yx+zWHDh3Stddeqw4dOig6Olrdu3ev9T0FADQNCRkAwK8iIiL0yCOP6JlnntGuXbuadazly5dr9+7dWrlypaZPn64HH3xQ//d//6c2bdroq6++0m233aY//vGPNc5z11136c4779S6deuUmZmpCy+8UAcOHJAkFRQU6LzzzlP//v317bffatGiRdqzZ4+uuOIKj2O8+uqrslqt+vzzzzVr1qxa45sxY4amTZumf/3rX/ruu++UnZ2tiy66SJs3b5Yk5eXlqU+fPrrzzjuVl5env/71rw1e84wZM5SZmalbbrlFeXl5ysvLU1paWqPibt++vb7++mv9+c9/1u23367LL79cZ5xxhtauXauhQ4fq+uuvV2lpqSTp73//uzZu3KiPP/5YP/74o55//nm1b9/euw4CADTMAADAT0aNGmVcfPHFhmEYxumnn27cdNNNhmEYxoIFC4yj/0t68MEHjVNOOcXjtU8++aSRnp7ucaz09HSjurrava9Hjx7GWWed5X5cVVVlxMbGGv/5z38MwzCMbdu2GZKMRx991N3GbrcbqampxmOPPWYYhmE8/PDDxtChQz3OvXPnTkOSkZubaxiGYZxzzjlG//79G7zezp07G//85z899v3ud78z/vSnP7kfn3LKKcaDDz5Y73GOft9c57/jjjs82ngb96BBg9zPu96f66+/3r0vLy/PkGSsXr3aMAzDuPDCC43Ro0c3eK0AgKZhhAwAEBCPPfaYXn31Vf34449NPkafPn1kNv/2X1lycrL69u3rfhwREaF27dpp7969Hq/LzMx0/z3y/7d37y6tbAEUh5dG0yhiE0SrFAomkETULhAEQbHwDxALH50MqPjCNBZWiViIEAtri1iJUUSxsDE+EbQIKBhQCxEUBbHTxFtckuNczz0nh+Q4hb8PBiZ7YLNmd4uZ2SkpUXNzczbH2dmZdnZ2VF5enj3q6+sl/fu9V0ZTU9Mvsz0/P+v29lZ+v9807vf787rn/5Nrbq/Xmz3PrM/HNauqqpKk7JoNDAwoGo2qoaFBExMT2tvbK3h2APjOSqwOAAD4ngKBgNrb2xUMBtXb22u6VlxcrPf3d9PY6+vrpzlKS0tNv4uKin46lk6nc8718vKizs5OhcPhT9eqq6uz52VlZTnP+RVyzf27NcvsdplZs46ODl1fX2tjY0Pb29tqbW2VYRianZ39G7cBAN8OT8gAAJYJhUJaW1vT/v6+adzhcOju7s5Uygr532EHBwfZ87e3N52cnMjlckmSGhsblUgk5HQ6VVtbazr+pIRVVFSopqZG8XjcNB6Px+V2u/PKb7fblUqlTGOFyv0zDodDPT09Wlpa0tzcnBYXF/OaDwDwA4UMAGAZj8ej7u5uzc/Pm8ZbWlp0f3+vmZkZJZNJRSIR085/+YpEIlpZWdH5+bkMw9DT05P6+/slSYZh6PHxUV1dXTo+PlYymdTW1pb6+vo+laDfGR8fVzgc1vLysi4uLjQ5OanT01MNDQ3lld/pdOrw8FBXV1d6eHhQOp0uaO6PpqamtLq6qsvLSyUSCa2vr2fLKwAgfxQyAIClpqenP71S6HK5tLCwoEgkIp/Pp6Ojo5x2IMxVKBRSKBSSz+fT7u6uYrFYdufAzFOtVCqltrY2eTweDQ8Pq7Ky0vS9Wi4GBwc1MjKi0dFReTwebW5uKhaLqa6uLq/8Y2Njstlscrvdcjgcurm5KWjuj+x2u4LBoLxerwKBgGw2m6LRaF75AQA/FL3/9yV9AAAAAMCX4AkZAAAAAFiEQgYAAAAAFqGQAQAAAIBFKGQAAAAAYBEKGQAAAABYhEIGAAAAABahkAEAAACARShkAAAAAGARChkAAAAAWIRCBgAAAAAWoZABAAAAgEX+AfPRzEyFiQbmAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the distribution of the number of items per order\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(pivot_table['num_items'].value_counts().sort_index().index, pivot_table['num_items'].value_counts().sort_index().values, marker='o', linestyle='-', color='skyblue')\n",
    "plt.axvline(mean_num_items, color='red', linestyle='dashed', linewidth=1, label='Mean')\n",
    "plt.title('Distribution of Number of Items per Order')\n",
    "plt.xlabel('Number of Items')\n",
    "plt.ylabel('Frequency')\n",
    "plt.legend()\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ffbcf32",
   "metadata": {},
   "source": [
    "Decided to use a pivot table to get a better representation of the data vs a bar graph or histogram. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9461d702",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Using `axvline` can be very helpful in this context. It allows you to draw a vertical line on the plot at a specified x-value. For instance:\n",
    "\n",
    "You can use it to mark the mean of the data, giving a visual representation of where the average lies.\n",
    "    \n",
    "Adding these lines can provide additional insight into the distribution of the data, making it easier to understand the typical behavior (like where the central tendency of the data is) and variability (how spread out the data points are).\n",
    "\n",
    "If you choose to use axvline, here's a quick example for the `mean`:\n",
    "```\n",
    "plt.hist(items_per_order, bins=range(1, 52), alpha=0.7)\n",
    "plt.axvline(items_per_order.mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')\n",
    "plt.legend()\n",
    "plt.xlabel('Number of items')\n",
    "plt.ylabel('Number of orders')\n",
    "plt.title('Distribution of items per order')\n",
    "plt.show()\n",
    "```\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e6b5537",
   "metadata": {},
   "source": [
    "### [C2] What are the top 20 items that are reordered most frequently (display their names and product IDs)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "9374e55a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Step 1: RLoadorder_products and products data\n",
    "df_instacart_order_products \n",
    "df_instacart_products\n",
    "\n",
    "# Step 2: Calculate reorder frequencies\n",
    "reorder_frequencies = df_instacart_order_products.groupby('product_id')['reordered'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "possible-change",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Step 3: Sort and select top 20 reorders\n",
    "top_reorders = reorder_frequencies.sort_values(ascending=False).head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "professional-surfing",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Step 4: Merge with product names\n",
    "top_reorders = pd.merge(top_reorders, df_instacart_products[['product_id', 'product_name']], on='product_id', how='left')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "48dd3658",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top 20 Items Reordered Most Frequently:\n",
      "    product_id                                       product_name\n",
      "0        14721                            Bone Strength Take Care\n",
      "1        20949                           Vanilla Sandwich Cookies\n",
      "2         6723                                   Palmiers- Petite\n",
      "3         6732                  Naturally Sparkling Mineral Water\n",
      "4        45088  California Dill Pollen & Garlic Goat Cheese & ...\n",
      "5        45078                                       Pomegranatea\n",
      "6        21016       Parchment Lined 8 in x 3.75 in x 2.5 in Pans\n",
      "7        21005                        Peanut Butter Pie Ice Cream\n",
      "8        35192                         Chocolate Soy Milk Singles\n",
      "9        35197  Mocha Chocolate Chip  Organic Non-Dairy Frozen...\n",
      "10        6810                        Raspberry Goji Paleo Prints\n",
      "11       45040                                 Head Lock Mega Gel\n",
      "12       45035                               Coffee Flavor Yogurt\n",
      "13       27373                                     Meat Loaf Meal\n",
      "14       30748                           Cheese & Garlic Croutons\n",
      "15       45031                 Sugar Free Hazelnut Coffee Creamer\n",
      "16       35137  Superior Preference Fade-Defying Color + Shine...\n",
      "17       30747                   Dentotape® Unflavored Waxed Tape\n",
      "18       35228                       Marvelous Muffins Baking Mix\n",
      "19       35229                             Bean & Cheese Burritos\n"
     ]
    }
   ],
   "source": [
    "# Step 5: Display results\n",
    "print(\"Top 20 Items Reordered Most Frequently:\")\n",
    "print(top_reorders[['product_id', 'product_name']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80e70c74",
   "metadata": {},
   "source": [
    "Step 1: Read order_products and products data\n",
    "Step 2: Calculate reorder frequencies\n",
    "Step 3: Sort and select top 20 reorders\n",
    "Step 4: Merge with product names\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21e0c81f",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "You got correct results. You could create a graph with this information. I left an example of how to do that above.\n",
    "    \n",
    "PS: in many cases it is helpful to support your results with a plot (barchart in that case). "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d312b14",
   "metadata": {},
   "source": [
    "### [C3] For each product, what proportion of its orders are reorders?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "103e7fe1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Read order_products and products data\n",
    "df_instacart_orders \n",
    "df_instacart_order_products \n",
    "df_instacart_products \n",
    "\n",
    "# Step 2: Calculate reorder proportions\n",
    "reorder_proportions = df_instacart_order_products.groupby('product_id')['reordered'].mean().reset_index()\n",
    "reorder_proportions.rename(columns={'reordered': 'reorder_proportion'}, inplace=True)\n",
    "\n",
    "# Step 3: Merge with product names\n",
    "reorder_proportions = pd.merge(reorder_proportions, df_instacart_products[['product_id', 'product_name']], on='product_id', how='left')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "social-individual",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Orders that are Reorders by Product:\n",
      "       product_id                                       product_name  \\\n",
      "0               1                         Chocolate Sandwich Cookies   \n",
      "1               2                                   All-Seasons Salt   \n",
      "2               3               Robust Golden Unsweetened Oolong Tea   \n",
      "3               4  Smart Ones Classic Favorites Mini Rigatoni Wit...   \n",
      "4               7                     Pure Coconut Water With Orange   \n",
      "...           ...                                                ...   \n",
      "45568       49690                      HIGH PERFORMANCE ENERGY DRINK   \n",
      "45569       49691                      ORIGINAL PANCAKE & WAFFLE MIX   \n",
      "45570       49692    ORGANIC INSTANT OATMEAL LIGHT MAPLE BROWN SUGAR   \n",
      "45571       49693                             SPRING WATER BODY WASH   \n",
      "45572       49694                            BURRITO- STEAK & CHEESE   \n",
      "\n",
      "       reorder_proportion  \n",
      "0                0.564286  \n",
      "1                0.000000  \n",
      "2                0.738095  \n",
      "3                0.510204  \n",
      "4                0.500000  \n",
      "...                   ...  \n",
      "45568            0.800000  \n",
      "45569            0.430556  \n",
      "45570            0.416667  \n",
      "45571            0.440000  \n",
      "45572            0.333333  \n",
      "\n",
      "[45573 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "# Step 4: Display results\n",
    "print(\"Proportion of Orders that are Reorders by Product:\")\n",
    "print(reorder_proportions[['product_id', 'product_name', 'reorder_proportion']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "subject-boxing",
   "metadata": {},
   "source": [
    "### [C4] For each customer, what proportion of their products ordered are reorders?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "medical-couple",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "# Load datasets\n",
    "df_instacart_orders \n",
    "df_instacart_order_products \n",
    "df_instacart_products \n",
    "\n",
    "# Merge orders and order products on order_id\n",
    "df_merged = pd.merge(df_instacart_orders, df_instacart_order_products, on='order_id')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "8892e4b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   user_id  product_id  reordered  reorder_proportion\n",
      "0        2          26          1            0.038462\n",
      "1        4           2          0            0.000000\n",
      "2        5          12          8            0.666667\n",
      "3        6           4          0            0.000000\n",
      "4        7          14         13            0.928571\n"
     ]
    }
   ],
   "source": [
    "# Calculate total orders and reorders per customer\n",
    "customer_reorder_stats = df_merged.groupby(['user_id']).agg({\n",
    "    'product_id': 'count',                   # Total products ordered by user\n",
    "    'reordered': 'sum'                       # Total products that are reorders\n",
    "}).reset_index()\n",
    "\n",
    "# Calculate proportion of reordered products per customer\n",
    "customer_reorder_stats['reorder_proportion'] = customer_reorder_stats['reordered'] / customer_reorder_stats['product_id']\n",
    "\n",
    "# Merge with customer information (if available) to include customer details\n",
    "# customer_info = pd.merge(customer_reorder_stats, df_customer_info, on='user_id')\n",
    "\n",
    "# Display results or further analysis\n",
    "print(customer_reorder_stats.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac4c7ec7",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Everything is correct here. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92d35137",
   "metadata": {},
   "source": [
    "### [C5] What are the top 20 items that people put in their carts first? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "0ae57274",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top 20 items that people put in their carts first:\n",
      "Banana                         15562\n",
      "Bag of Organic Bananas         11026\n",
      "Organic Whole Milk              4363\n",
      "Organic Strawberries            3946\n",
      "Organic Hass Avocado            3390\n",
      "Organic Baby Spinach            3336\n",
      "Organic Avocado                 3044\n",
      "Spring Water                    2336\n",
      "Strawberries                    2308\n",
      "Organic Raspberries             2024\n",
      "Sparkling Water Grapefruit      1914\n",
      "Organic Half & Half             1797\n",
      "Large Lemon                     1737\n",
      "Soda                            1733\n",
      "Organic Reduced Fat Milk        1397\n",
      "Limes                           1370\n",
      "Hass Avocados                   1340\n",
      "Organic Reduced Fat 2% Milk     1310\n",
      "Half & Half                     1309\n",
      "Organic Yellow Onion            1246\n",
      "Name: product_name, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Read df_order_products & df_products \n",
    "df_instacart_order_products \n",
    "df_instacart_products\n",
    "\n",
    "# Merge order_products with products to get product names\n",
    "df_merged = pd.merge(df_instacart_order_products, df_instacart_products, on='product_id')\n",
    "\n",
    "# Filter for products added first (add_to_cart_order == 1) and count occurrences\n",
    "top_first_items = df_merged[df_merged['add_to_cart_order'] == 1]['product_name'].value_counts().head(20)\n",
    "\n",
    "# Display the top 20 items\n",
    "print(\"Top 20 items that people put in their carts first:\")\n",
    "print(top_first_items)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28ce9872",
   "metadata": {},
   "source": [
    "Read df_order_products & df_products \n",
    "Merge order_products with products to get product names\n",
    "Filter for products added first (add_to_cart_order == 1) and count occurrences\n",
    "Display the top 20 items"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4372b36",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Well done! "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d798e74",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Reviewer's comment v3</b>\n",
    " \n",
    "Additionally, it could be super useful to have short overall conclusions."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "272fab55",
   "metadata": {},
   "source": [
    "Conclusion: This analysis reveals various insights into customers' shopping behaviors on Instacart. We observed that the majority of orders are placed during mid-day hours and that Wednesdays and Saturdays show different ordering patterns. Customers generally have a consistent pattern of reordering, with certain products and items frequently reordered or placed first in the cart. Understanding these trends can help in inventory management and improving customer satisfaction."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e257433",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-success\">\n",
    "<b>Reviewer's comment v4</b>\n",
    " \n",
    "Thank you for making all additional changes in the project. "
   ]
  }
 ],
 "metadata": {
  "ExecuteTimeLog": [
   {
    "duration": 448,
    "start_time": "2024-07-01T03:52:45.981Z"
   },
   {
    "duration": 1090,
    "start_time": "2024-07-01T03:54:11.301Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-01T03:54:12.786Z"
   },
   {
    "duration": 142,
    "start_time": "2024-07-01T03:55:33.017Z"
   },
   {
    "duration": 131,
    "start_time": "2024-07-01T03:56:23.399Z"
   },
   {
    "duration": 126,
    "start_time": "2024-07-01T03:58:36.060Z"
   },
   {
    "duration": 770,
    "start_time": "2024-07-01T04:06:18.644Z"
   },
   {
    "duration": 765,
    "start_time": "2024-07-01T04:06:40.280Z"
   },
   {
    "duration": 122,
    "start_time": "2024-07-01T04:08:01.832Z"
   },
   {
    "duration": 187,
    "start_time": "2024-07-01T04:50:07.745Z"
   },
   {
    "duration": 246,
    "start_time": "2024-07-01T04:50:23.107Z"
   },
   {
    "duration": 127,
    "start_time": "2024-07-01T04:50:28.132Z"
   },
   {
    "duration": 24,
    "start_time": "2024-07-01T04:51:02.260Z"
   },
   {
    "duration": 534,
    "start_time": "2024-07-01T05:07:49.306Z"
   },
   {
    "duration": 847,
    "start_time": "2024-07-01T05:09:11.962Z"
   },
   {
    "duration": 77,
    "start_time": "2024-07-01T05:13:22.857Z"
   },
   {
    "duration": 514,
    "start_time": "2024-07-01T05:15:37.105Z"
   },
   {
    "duration": 314,
    "start_time": "2024-07-01T05:32:58.428Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.746Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.749Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.751Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.754Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.756Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.758Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.761Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.763Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.765Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.768Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.770Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.812Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.814Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.817Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.819Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.821Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.824Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.826Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.828Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.833Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.835Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.839Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.841Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:32:58.843Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-01T05:33:17.993Z"
   },
   {
    "duration": 20,
    "start_time": "2024-07-01T05:33:30.903Z"
   },
   {
    "duration": 546,
    "start_time": "2024-07-01T05:33:42.714Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T05:34:07.279Z"
   },
   {
    "duration": 216,
    "start_time": "2024-07-01T05:34:21.399Z"
   },
   {
    "duration": 93,
    "start_time": "2024-07-01T05:34:36.606Z"
   },
   {
    "duration": 1369,
    "start_time": "2024-07-01T05:34:43.798Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T05:34:51.700Z"
   },
   {
    "duration": 768,
    "start_time": "2024-07-01T05:35:02.988Z"
   },
   {
    "duration": 120,
    "start_time": "2024-07-01T05:35:18.748Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T05:35:29.459Z"
   },
   {
    "duration": 832,
    "start_time": "2024-07-01T05:35:34.501Z"
   },
   {
    "duration": 609,
    "start_time": "2024-07-01T05:35:49.366Z"
   },
   {
    "duration": 67,
    "start_time": "2024-07-01T05:35:49.978Z"
   },
   {
    "duration": 1277,
    "start_time": "2024-07-01T05:35:50.048Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T05:35:51.327Z"
   },
   {
    "duration": 1081,
    "start_time": "2024-07-01T05:35:51.341Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.426Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.429Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.431Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.434Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.436Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.439Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.440Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.442Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.444Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.447Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.448Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.451Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.454Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.456Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.458Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.513Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.515Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.517Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.519Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T05:35:52.521Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T05:36:19.995Z"
   },
   {
    "duration": 194,
    "start_time": "2024-07-01T05:36:34.318Z"
   },
   {
    "duration": 51,
    "start_time": "2024-07-01T05:36:36.280Z"
   },
   {
    "duration": 1254,
    "start_time": "2024-07-01T05:36:36.961Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T05:36:38.218Z"
   },
   {
    "duration": 182,
    "start_time": "2024-07-01T05:37:52.575Z"
   },
   {
    "duration": 51,
    "start_time": "2024-07-01T05:37:53.465Z"
   },
   {
    "duration": 1246,
    "start_time": "2024-07-01T05:37:53.999Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T05:37:55.248Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T05:39:44.374Z"
   },
   {
    "duration": 473,
    "start_time": "2024-07-01T05:39:56.502Z"
   },
   {
    "duration": 843,
    "start_time": "2024-07-01T05:40:04.044Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-01T05:41:43.877Z"
   },
   {
    "duration": 343,
    "start_time": "2024-07-01T05:43:51.339Z"
   },
   {
    "duration": 23,
    "start_time": "2024-07-01T05:45:04.387Z"
   },
   {
    "duration": 154,
    "start_time": "2024-07-01T05:46:09.978Z"
   },
   {
    "duration": 92,
    "start_time": "2024-07-01T05:47:11.815Z"
   },
   {
    "duration": 54,
    "start_time": "2024-07-01T05:49:20.085Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T05:50:12.649Z"
   },
   {
    "duration": 61,
    "start_time": "2024-07-01T05:52:43.337Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-01T05:53:25.026Z"
   },
   {
    "duration": 24,
    "start_time": "2024-07-01T05:55:05.672Z"
   },
   {
    "duration": 1240,
    "start_time": "2024-07-01T05:59:56.860Z"
   },
   {
    "duration": 2546,
    "start_time": "2024-07-01T06:00:58.327Z"
   },
   {
    "duration": 1307,
    "start_time": "2024-07-01T06:02:19.935Z"
   },
   {
    "duration": 2587,
    "start_time": "2024-07-01T06:08:16.142Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T08:33:53.102Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T08:34:19.518Z"
   },
   {
    "duration": 6,
    "start_time": "2024-07-01T08:36:00.551Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T08:36:17.842Z"
   },
   {
    "duration": 96,
    "start_time": "2024-07-01T08:38:53.620Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T08:41:29.778Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T08:43:03.834Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T08:45:42.599Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T08:46:31.478Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T08:47:55.602Z"
   },
   {
    "duration": 859,
    "start_time": "2024-07-01T08:49:42.266Z"
   },
   {
    "duration": 102,
    "start_time": "2024-07-01T08:53:43.088Z"
   },
   {
    "duration": 1241,
    "start_time": "2024-07-01T08:59:18.997Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T08:59:34.923Z"
   },
   {
    "duration": 101,
    "start_time": "2024-07-01T08:59:42.245Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T09:03:42.359Z"
   },
   {
    "duration": 128,
    "start_time": "2024-07-01T09:05:49.962Z"
   },
   {
    "duration": 111,
    "start_time": "2024-07-01T09:10:37.682Z"
   },
   {
    "duration": 107,
    "start_time": "2024-07-01T09:10:56.240Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-01T09:12:01.834Z"
   },
   {
    "duration": 28,
    "start_time": "2024-07-01T09:12:43.256Z"
   },
   {
    "duration": 185,
    "start_time": "2024-07-01T09:15:33.492Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T09:15:35.916Z"
   },
   {
    "duration": 4657,
    "start_time": "2024-07-01T09:17:18.093Z"
   },
   {
    "duration": 688,
    "start_time": "2024-07-01T09:18:11.038Z"
   },
   {
    "duration": 229,
    "start_time": "2024-07-01T09:18:24.156Z"
   },
   {
    "duration": 715,
    "start_time": "2024-07-01T09:18:35.007Z"
   },
   {
    "duration": 596,
    "start_time": "2024-07-01T09:21:54.713Z"
   },
   {
    "duration": 822,
    "start_time": "2024-07-01T09:23:52.579Z"
   },
   {
    "duration": 173,
    "start_time": "2024-07-01T09:26:39.416Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-01T09:26:40.446Z"
   },
   {
    "duration": 199,
    "start_time": "2024-07-01T09:27:24.395Z"
   },
   {
    "duration": 360,
    "start_time": "2024-07-01T09:27:31.045Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T09:28:44.431Z"
   },
   {
    "duration": 198,
    "start_time": "2024-07-01T09:28:49.139Z"
   },
   {
    "duration": 520,
    "start_time": "2024-07-01T09:30:19.354Z"
   },
   {
    "duration": 1299,
    "start_time": "2024-07-01T09:32:50.329Z"
   },
   {
    "duration": 1383,
    "start_time": "2024-07-01T09:32:51.631Z"
   },
   {
    "duration": 6304,
    "start_time": "2024-07-01T09:32:53.017Z"
   },
   {
    "duration": 1706,
    "start_time": "2024-07-01T09:34:43.725Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-01T09:34:45.434Z"
   },
   {
    "duration": 314,
    "start_time": "2024-07-01T09:35:17.456Z"
   },
   {
    "duration": 1472,
    "start_time": "2024-07-01T09:37:42.415Z"
   },
   {
    "duration": 1480,
    "start_time": "2024-07-01T09:38:32.475Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T09:38:33.964Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-01T09:38:34.958Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T09:38:36.129Z"
   },
   {
    "duration": 1330,
    "start_time": "2024-07-01T09:40:31.204Z"
   },
   {
    "duration": 185,
    "start_time": "2024-07-01T09:40:32.753Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T09:40:33.584Z"
   },
   {
    "duration": 1272,
    "start_time": "2024-07-01T09:41:42.465Z"
   },
   {
    "duration": 1297,
    "start_time": "2024-07-01T09:42:41.881Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T09:42:43.181Z"
   },
   {
    "duration": 1277,
    "start_time": "2024-07-01T09:42:53.929Z"
   },
   {
    "duration": 23,
    "start_time": "2024-07-01T09:45:53.975Z"
   },
   {
    "duration": 1468,
    "start_time": "2024-07-01T09:48:21.759Z"
   },
   {
    "duration": 160,
    "start_time": "2024-07-01T09:48:24.626Z"
   },
   {
    "duration": 1414,
    "start_time": "2024-07-01T09:49:16.193Z"
   },
   {
    "duration": 2929,
    "start_time": "2024-07-01T09:53:47.921Z"
   },
   {
    "duration": 226,
    "start_time": "2024-07-01T09:54:03.208Z"
   },
   {
    "duration": 3158,
    "start_time": "2024-07-01T09:56:17.895Z"
   },
   {
    "duration": 738,
    "start_time": "2024-07-01T09:57:08.212Z"
   },
   {
    "duration": 64,
    "start_time": "2024-07-01T09:57:08.956Z"
   },
   {
    "duration": 1272,
    "start_time": "2024-07-01T09:57:09.023Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T09:57:10.300Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T09:57:10.319Z"
   },
   {
    "duration": 542,
    "start_time": "2024-07-01T09:57:10.337Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T09:57:10.882Z"
   },
   {
    "duration": 367,
    "start_time": "2024-07-01T09:57:10.912Z"
   },
   {
    "duration": 173,
    "start_time": "2024-07-01T09:57:11.282Z"
   },
   {
    "duration": 109,
    "start_time": "2024-07-01T09:57:11.461Z"
   },
   {
    "duration": 72,
    "start_time": "2024-07-01T09:57:11.572Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T09:57:11.647Z"
   },
   {
    "duration": 72,
    "start_time": "2024-07-01T09:57:11.661Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-01T09:57:11.736Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-01T09:57:11.767Z"
   },
   {
    "duration": 40,
    "start_time": "2024-07-01T09:57:11.773Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T09:57:11.815Z"
   },
   {
    "duration": 6,
    "start_time": "2024-07-01T09:57:11.823Z"
   },
   {
    "duration": 2639,
    "start_time": "2024-07-01T09:57:11.832Z"
   },
   {
    "duration": 2638,
    "start_time": "2024-07-01T09:57:14.474Z"
   },
   {
    "duration": 51,
    "start_time": "2024-07-01T09:57:17.115Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T09:57:17.169Z"
   },
   {
    "duration": 30,
    "start_time": "2024-07-01T09:57:17.188Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T09:57:17.222Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T09:57:17.234Z"
   },
   {
    "duration": 228,
    "start_time": "2024-07-01T09:57:17.252Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T09:57:17.483Z"
   },
   {
    "duration": 1256,
    "start_time": "2024-07-01T09:57:17.512Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T09:57:18.772Z"
   },
   {
    "duration": 39,
    "start_time": "2024-07-01T09:57:18.787Z"
   },
   {
    "duration": 122,
    "start_time": "2024-07-01T09:57:18.830Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-01T09:57:18.955Z"
   },
   {
    "duration": 200,
    "start_time": "2024-07-01T09:57:18.994Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T09:57:19.198Z"
   },
   {
    "duration": 1001,
    "start_time": "2024-07-01T09:57:19.215Z"
   },
   {
    "duration": 621,
    "start_time": "2024-07-01T09:57:20.220Z"
   },
   {
    "duration": 813,
    "start_time": "2024-07-01T09:57:20.844Z"
   },
   {
    "duration": 184,
    "start_time": "2024-07-01T09:57:21.660Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T09:57:21.847Z"
   },
   {
    "duration": 221,
    "start_time": "2024-07-01T09:57:21.866Z"
   },
   {
    "duration": 320,
    "start_time": "2024-07-01T09:57:22.093Z"
   },
   {
    "duration": 530,
    "start_time": "2024-07-01T09:57:22.416Z"
   },
   {
    "duration": 1324,
    "start_time": "2024-07-01T09:57:22.950Z"
   },
   {
    "duration": 1580,
    "start_time": "2024-07-01T09:57:24.277Z"
   },
   {
    "duration": 7065,
    "start_time": "2024-07-01T09:57:25.860Z"
   },
   {
    "duration": 1900,
    "start_time": "2024-07-01T09:57:32.928Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-01T09:57:34.831Z"
   },
   {
    "duration": 341,
    "start_time": "2024-07-01T09:57:34.859Z"
   },
   {
    "duration": 1461,
    "start_time": "2024-07-01T09:57:35.202Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T09:57:36.666Z"
   },
   {
    "duration": 35,
    "start_time": "2024-07-01T09:57:36.677Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T09:57:36.716Z"
   },
   {
    "duration": 1495,
    "start_time": "2024-07-01T09:57:36.729Z"
   },
   {
    "duration": 194,
    "start_time": "2024-07-01T09:57:38.228Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T09:57:38.425Z"
   },
   {
    "duration": 3151,
    "start_time": "2024-07-01T09:57:38.441Z"
   },
   {
    "duration": 228,
    "start_time": "2024-07-01T09:57:41.595Z"
   },
   {
    "duration": 2544,
    "start_time": "2024-07-01T09:57:41.826Z"
   },
   {
    "duration": 177,
    "start_time": "2024-07-01T09:58:04.805Z"
   },
   {
    "duration": 50,
    "start_time": "2024-07-01T09:58:05.849Z"
   },
   {
    "duration": 1238,
    "start_time": "2024-07-01T09:58:06.400Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T09:58:07.641Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T09:58:07.651Z"
   },
   {
    "duration": 424,
    "start_time": "2024-07-01T09:58:15.732Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T09:58:35.206Z"
   },
   {
    "duration": 280,
    "start_time": "2024-07-01T09:58:37.774Z"
   },
   {
    "duration": 135,
    "start_time": "2024-07-01T09:58:45.069Z"
   },
   {
    "duration": 76,
    "start_time": "2024-07-01T09:58:48.095Z"
   },
   {
    "duration": 56,
    "start_time": "2024-07-01T09:59:02.105Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T09:59:04.249Z"
   },
   {
    "duration": 1241,
    "start_time": "2024-07-01T10:06:14.100Z"
   },
   {
    "duration": 254,
    "start_time": "2024-07-01T10:06:58.235Z"
   },
   {
    "duration": 709,
    "start_time": "2024-07-01T10:07:53.344Z"
   },
   {
    "duration": 628,
    "start_time": "2024-07-01T10:08:09.071Z"
   },
   {
    "duration": 60,
    "start_time": "2024-07-01T10:08:09.702Z"
   },
   {
    "duration": 1264,
    "start_time": "2024-07-01T10:08:09.765Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T10:08:11.034Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T10:08:11.045Z"
   },
   {
    "duration": 588,
    "start_time": "2024-07-01T10:08:11.055Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T10:08:11.646Z"
   },
   {
    "duration": 393,
    "start_time": "2024-07-01T10:08:11.664Z"
   },
   {
    "duration": 180,
    "start_time": "2024-07-01T10:08:12.060Z"
   },
   {
    "duration": 109,
    "start_time": "2024-07-01T10:08:12.246Z"
   },
   {
    "duration": 72,
    "start_time": "2024-07-01T10:08:12.359Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T10:08:12.434Z"
   },
   {
    "duration": 73,
    "start_time": "2024-07-01T10:08:12.449Z"
   },
   {
    "duration": 26,
    "start_time": "2024-07-01T10:08:12.525Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-01T10:08:12.554Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T10:08:12.562Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T10:08:12.571Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T10:08:12.614Z"
   },
   {
    "duration": 2682,
    "start_time": "2024-07-01T10:08:12.625Z"
   },
   {
    "duration": 2599,
    "start_time": "2024-07-01T10:08:15.314Z"
   },
   {
    "duration": 60,
    "start_time": "2024-07-01T10:08:17.916Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T10:08:17.979Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T10:08:18.013Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T10:08:18.027Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T10:08:18.039Z"
   },
   {
    "duration": 222,
    "start_time": "2024-07-01T10:08:18.056Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T10:08:18.280Z"
   },
   {
    "duration": 1232,
    "start_time": "2024-07-01T10:08:18.297Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T10:08:19.531Z"
   },
   {
    "duration": 23,
    "start_time": "2024-07-01T10:08:19.545Z"
   },
   {
    "duration": 136,
    "start_time": "2024-07-01T10:08:19.570Z"
   },
   {
    "duration": 38,
    "start_time": "2024-07-01T10:08:19.713Z"
   },
   {
    "duration": 194,
    "start_time": "2024-07-01T10:08:19.753Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T10:08:19.950Z"
   },
   {
    "duration": 980,
    "start_time": "2024-07-01T10:08:19.963Z"
   },
   {
    "duration": 651,
    "start_time": "2024-07-01T10:08:20.946Z"
   },
   {
    "duration": 826,
    "start_time": "2024-07-01T10:08:21.600Z"
   },
   {
    "duration": 195,
    "start_time": "2024-07-01T10:08:22.430Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T10:08:22.627Z"
   },
   {
    "duration": 218,
    "start_time": "2024-07-01T10:08:22.646Z"
   },
   {
    "duration": 355,
    "start_time": "2024-07-01T10:08:22.867Z"
   },
   {
    "duration": 663,
    "start_time": "2024-07-01T10:08:23.226Z"
   },
   {
    "duration": 1297,
    "start_time": "2024-07-01T10:08:23.892Z"
   },
   {
    "duration": 1443,
    "start_time": "2024-07-01T10:08:25.192Z"
   },
   {
    "duration": 6489,
    "start_time": "2024-07-01T10:08:26.638Z"
   },
   {
    "duration": 1770,
    "start_time": "2024-07-01T10:08:33.129Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-01T10:08:34.901Z"
   },
   {
    "duration": 326,
    "start_time": "2024-07-01T10:08:34.934Z"
   },
   {
    "duration": 1438,
    "start_time": "2024-07-01T10:08:35.264Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T10:08:36.705Z"
   },
   {
    "duration": 18,
    "start_time": "2024-07-01T10:08:36.722Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T10:08:36.742Z"
   },
   {
    "duration": 1496,
    "start_time": "2024-07-01T10:08:36.753Z"
   },
   {
    "duration": 188,
    "start_time": "2024-07-01T10:08:38.253Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T10:08:38.443Z"
   },
   {
    "duration": 3060,
    "start_time": "2024-07-01T10:08:38.461Z"
   },
   {
    "duration": 236,
    "start_time": "2024-07-01T10:08:41.525Z"
   },
   {
    "duration": 2522,
    "start_time": "2024-07-01T10:08:46.923Z"
   },
   {
    "duration": 370,
    "start_time": "2024-07-01T10:37:30.329Z"
   },
   {
    "duration": 1243,
    "start_time": "2024-07-01T10:39:56.659Z"
   },
   {
    "duration": 437,
    "start_time": "2024-07-01T10:39:57.912Z"
   },
   {
    "duration": 1457,
    "start_time": "2024-07-01T10:40:01.330Z"
   },
   {
    "duration": 1211,
    "start_time": "2024-07-01T10:41:34.169Z"
   },
   {
    "duration": 491,
    "start_time": "2024-07-01T10:41:35.383Z"
   },
   {
    "duration": 319,
    "start_time": "2024-07-01T10:41:35.877Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T10:43:06.856Z"
   },
   {
    "duration": 373,
    "start_time": "2024-07-01T10:49:10.770Z"
   },
   {
    "duration": 26,
    "start_time": "2024-07-01T10:51:12.205Z"
   },
   {
    "duration": 709,
    "start_time": "2024-07-01T10:52:08.531Z"
   },
   {
    "duration": 984,
    "start_time": "2024-07-01T10:54:45.028Z"
   },
   {
    "duration": 25,
    "start_time": "2024-07-01T10:59:22.326Z"
   },
   {
    "duration": 624,
    "start_time": "2024-07-01T11:01:08.073Z"
   },
   {
    "duration": 1047,
    "start_time": "2024-07-01T11:04:54.488Z"
   },
   {
    "duration": 269,
    "start_time": "2024-07-01T11:05:35.296Z"
   },
   {
    "duration": 257,
    "start_time": "2024-07-01T11:08:01.891Z"
   },
   {
    "duration": 669,
    "start_time": "2024-07-01T11:08:30.129Z"
   },
   {
    "duration": 60,
    "start_time": "2024-07-01T11:08:30.802Z"
   },
   {
    "duration": 1274,
    "start_time": "2024-07-01T11:08:30.866Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T11:08:32.143Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T11:08:32.157Z"
   },
   {
    "duration": 546,
    "start_time": "2024-07-01T11:08:32.169Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T11:08:32.718Z"
   },
   {
    "duration": 400,
    "start_time": "2024-07-01T11:08:32.736Z"
   },
   {
    "duration": 181,
    "start_time": "2024-07-01T11:08:33.140Z"
   },
   {
    "duration": 109,
    "start_time": "2024-07-01T11:08:33.324Z"
   },
   {
    "duration": 57,
    "start_time": "2024-07-01T11:08:33.437Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T11:08:33.512Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-01T11:08:33.528Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-01T11:08:33.612Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T11:08:33.648Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T11:08:33.656Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T11:08:33.670Z"
   },
   {
    "duration": 42,
    "start_time": "2024-07-01T11:08:33.677Z"
   },
   {
    "duration": 2590,
    "start_time": "2024-07-01T11:08:33.722Z"
   },
   {
    "duration": 2660,
    "start_time": "2024-07-01T11:08:36.315Z"
   },
   {
    "duration": 63,
    "start_time": "2024-07-01T11:08:38.978Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T11:08:39.043Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T11:08:39.062Z"
   },
   {
    "duration": 38,
    "start_time": "2024-07-01T11:08:39.075Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T11:08:39.116Z"
   },
   {
    "duration": 205,
    "start_time": "2024-07-01T11:08:39.133Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T11:08:39.340Z"
   },
   {
    "duration": 1261,
    "start_time": "2024-07-01T11:08:39.353Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T11:08:40.617Z"
   },
   {
    "duration": 24,
    "start_time": "2024-07-01T11:08:40.631Z"
   },
   {
    "duration": 145,
    "start_time": "2024-07-01T11:08:40.659Z"
   },
   {
    "duration": 37,
    "start_time": "2024-07-01T11:08:40.807Z"
   },
   {
    "duration": 202,
    "start_time": "2024-07-01T11:08:40.847Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T11:08:41.052Z"
   },
   {
    "duration": 1026,
    "start_time": "2024-07-01T11:08:41.064Z"
   },
   {
    "duration": 604,
    "start_time": "2024-07-01T11:08:42.093Z"
   },
   {
    "duration": 847,
    "start_time": "2024-07-01T11:08:42.700Z"
   },
   {
    "duration": 1004,
    "start_time": "2024-07-01T11:08:43.551Z"
   },
   {
    "duration": 549,
    "start_time": "2024-07-01T11:08:44.559Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.113Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.115Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.116Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.118Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.120Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.121Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.123Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.124Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.125Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.127Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.129Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.130Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.132Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.136Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.139Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T11:08:45.141Z"
   },
   {
    "duration": 1,
    "start_time": "2024-07-01T11:08:45.143Z"
   },
   {
    "duration": 211,
    "start_time": "2024-07-01T11:09:02.109Z"
   },
   {
    "duration": 563,
    "start_time": "2024-07-01T11:10:56.574Z"
   },
   {
    "duration": 853,
    "start_time": "2024-07-01T11:13:17.080Z"
   },
   {
    "duration": 235,
    "start_time": "2024-07-01T11:16:11.482Z"
   },
   {
    "duration": 218,
    "start_time": "2024-07-01T11:17:47.920Z"
   },
   {
    "duration": 710,
    "start_time": "2024-07-01T13:08:03.880Z"
   },
   {
    "duration": 91,
    "start_time": "2024-07-01T13:08:04.639Z"
   },
   {
    "duration": 1385,
    "start_time": "2024-07-01T13:08:05.199Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T13:08:07.475Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T13:08:08.198Z"
   },
   {
    "duration": 588,
    "start_time": "2024-07-01T13:08:14.752Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-01T13:08:24.507Z"
   },
   {
    "duration": 350,
    "start_time": "2024-07-01T13:08:34.015Z"
   },
   {
    "duration": 172,
    "start_time": "2024-07-01T13:08:52.684Z"
   },
   {
    "duration": 93,
    "start_time": "2024-07-01T13:08:57.433Z"
   },
   {
    "duration": 55,
    "start_time": "2024-07-01T13:09:06.388Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T13:09:12.167Z"
   },
   {
    "duration": 47,
    "start_time": "2024-07-01T13:09:13.697Z"
   },
   {
    "duration": 4622,
    "start_time": "2024-07-01T13:11:10.999Z"
   },
   {
    "duration": 632,
    "start_time": "2024-07-01T13:13:30.508Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T13:14:44.611Z"
   },
   {
    "duration": 637,
    "start_time": "2024-07-01T13:15:00.669Z"
   },
   {
    "duration": 734,
    "start_time": "2024-07-01T13:16:49.948Z"
   },
   {
    "duration": 1275,
    "start_time": "2024-07-01T13:17:10.436Z"
   },
   {
    "duration": 1497,
    "start_time": "2024-07-01T13:17:11.716Z"
   },
   {
    "duration": 6402,
    "start_time": "2024-07-01T13:17:13.216Z"
   },
   {
    "duration": 1228,
    "start_time": "2024-07-01T13:17:30.019Z"
   },
   {
    "duration": 478,
    "start_time": "2024-07-01T13:17:31.430Z"
   },
   {
    "duration": 318,
    "start_time": "2024-07-01T13:17:32.599Z"
   },
   {
    "duration": 1466,
    "start_time": "2024-07-01T13:18:10.603Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T13:18:12.074Z"
   },
   {
    "duration": 20,
    "start_time": "2024-07-01T13:18:12.087Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T13:18:12.580Z"
   },
   {
    "duration": 1445,
    "start_time": "2024-07-01T13:18:29.264Z"
   },
   {
    "duration": 174,
    "start_time": "2024-07-01T13:18:30.713Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-01T13:18:30.891Z"
   },
   {
    "duration": 2984,
    "start_time": "2024-07-01T13:18:46.267Z"
   },
   {
    "duration": 231,
    "start_time": "2024-07-01T13:18:49.254Z"
   },
   {
    "duration": 2642,
    "start_time": "2024-07-01T13:19:21.489Z"
   },
   {
    "duration": 1243,
    "start_time": "2024-07-01T14:33:48.404Z"
   },
   {
    "duration": 502,
    "start_time": "2024-07-01T14:33:49.946Z"
   },
   {
    "duration": 291,
    "start_time": "2024-07-01T14:33:51.728Z"
   },
   {
    "duration": 634,
    "start_time": "2024-07-01T15:26:53.088Z"
   },
   {
    "duration": 56,
    "start_time": "2024-07-01T15:26:53.731Z"
   },
   {
    "duration": 1272,
    "start_time": "2024-07-01T15:26:53.790Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T15:26:55.065Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T15:26:55.077Z"
   },
   {
    "duration": 18,
    "start_time": "2024-07-01T15:26:55.088Z"
   },
   {
    "duration": 545,
    "start_time": "2024-07-01T15:26:55.133Z"
   },
   {
    "duration": 352,
    "start_time": "2024-07-01T15:26:55.681Z"
   },
   {
    "duration": 171,
    "start_time": "2024-07-01T15:26:56.037Z"
   },
   {
    "duration": 124,
    "start_time": "2024-07-01T15:26:56.210Z"
   },
   {
    "duration": 67,
    "start_time": "2024-07-01T15:26:56.337Z"
   },
   {
    "duration": 26,
    "start_time": "2024-07-01T15:26:56.408Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-01T15:26:56.438Z"
   },
   {
    "duration": 51,
    "start_time": "2024-07-01T15:26:56.493Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T15:26:56.547Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T15:26:56.554Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-01T15:26:56.566Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T15:26:56.573Z"
   },
   {
    "duration": 2594,
    "start_time": "2024-07-01T15:26:56.583Z"
   },
   {
    "duration": 2642,
    "start_time": "2024-07-01T15:26:59.180Z"
   },
   {
    "duration": 55,
    "start_time": "2024-07-01T15:27:01.824Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-01T15:27:01.881Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-01T15:27:01.899Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T15:27:01.934Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T15:27:01.946Z"
   },
   {
    "duration": 232,
    "start_time": "2024-07-01T15:27:01.966Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T15:27:02.202Z"
   },
   {
    "duration": 1303,
    "start_time": "2024-07-01T15:27:02.231Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T15:27:03.537Z"
   },
   {
    "duration": 23,
    "start_time": "2024-07-01T15:27:03.552Z"
   },
   {
    "duration": 145,
    "start_time": "2024-07-01T15:27:03.578Z"
   },
   {
    "duration": 37,
    "start_time": "2024-07-01T15:27:03.730Z"
   },
   {
    "duration": 225,
    "start_time": "2024-07-01T15:27:03.770Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T15:27:03.998Z"
   },
   {
    "duration": 1043,
    "start_time": "2024-07-01T15:27:04.010Z"
   },
   {
    "duration": 662,
    "start_time": "2024-07-01T15:27:05.059Z"
   },
   {
    "duration": 832,
    "start_time": "2024-07-01T15:27:05.723Z"
   },
   {
    "duration": 809,
    "start_time": "2024-07-01T15:27:06.562Z"
   },
   {
    "duration": 580,
    "start_time": "2024-07-01T15:27:07.374Z"
   },
   {
    "duration": 605,
    "start_time": "2024-07-01T15:27:07.957Z"
   },
   {
    "duration": 1271,
    "start_time": "2024-07-01T15:27:08.571Z"
   },
   {
    "duration": 1446,
    "start_time": "2024-07-01T15:27:09.844Z"
   },
   {
    "duration": 6503,
    "start_time": "2024-07-01T15:27:11.292Z"
   },
   {
    "duration": 1248,
    "start_time": "2024-07-01T15:27:17.798Z"
   },
   {
    "duration": 539,
    "start_time": "2024-07-01T15:27:19.049Z"
   },
   {
    "duration": 261,
    "start_time": "2024-07-01T15:27:19.591Z"
   },
   {
    "duration": 1479,
    "start_time": "2024-07-01T15:27:19.856Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T15:27:21.338Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-01T15:27:21.350Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T15:27:21.369Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T15:27:21.381Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T15:27:21.430Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T15:27:21.432Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T15:27:21.436Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T15:27:21.438Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T15:27:21.440Z"
   },
   {
    "duration": 695,
    "start_time": "2024-07-01T19:27:56.488Z"
   },
   {
    "duration": 85,
    "start_time": "2024-07-01T19:27:57.187Z"
   },
   {
    "duration": 1328,
    "start_time": "2024-07-01T19:27:57.275Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T19:27:58.608Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-01T19:27:58.620Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-01T19:27:58.640Z"
   },
   {
    "duration": 592,
    "start_time": "2024-07-01T19:27:58.662Z"
   },
   {
    "duration": 347,
    "start_time": "2024-07-01T19:27:59.257Z"
   },
   {
    "duration": 172,
    "start_time": "2024-07-01T19:27:59.606Z"
   },
   {
    "duration": 109,
    "start_time": "2024-07-01T19:27:59.786Z"
   },
   {
    "duration": 64,
    "start_time": "2024-07-01T19:27:59.898Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T19:27:59.965Z"
   },
   {
    "duration": 68,
    "start_time": "2024-07-01T19:27:59.978Z"
   },
   {
    "duration": 31,
    "start_time": "2024-07-01T19:28:00.048Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-01T19:28:00.083Z"
   },
   {
    "duration": 42,
    "start_time": "2024-07-01T19:28:00.089Z"
   },
   {
    "duration": 5,
    "start_time": "2024-07-01T19:28:00.135Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-01T19:28:00.144Z"
   },
   {
    "duration": 2619,
    "start_time": "2024-07-01T19:28:00.155Z"
   },
   {
    "duration": 2612,
    "start_time": "2024-07-01T19:28:02.777Z"
   },
   {
    "duration": 63,
    "start_time": "2024-07-01T19:28:05.392Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-01T19:28:05.458Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T19:28:05.481Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-01T19:28:05.496Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T19:28:05.535Z"
   },
   {
    "duration": 245,
    "start_time": "2024-07-01T19:28:05.551Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T19:28:05.803Z"
   },
   {
    "duration": 1222,
    "start_time": "2024-07-01T19:28:05.835Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T19:28:07.061Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-01T19:28:07.077Z"
   },
   {
    "duration": 146,
    "start_time": "2024-07-01T19:28:07.102Z"
   },
   {
    "duration": 37,
    "start_time": "2024-07-01T19:28:07.252Z"
   },
   {
    "duration": 192,
    "start_time": "2024-07-01T19:28:07.292Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T19:28:07.487Z"
   },
   {
    "duration": 4711,
    "start_time": "2024-07-01T19:28:07.501Z"
   },
   {
    "duration": 688,
    "start_time": "2024-07-01T19:28:12.215Z"
   },
   {
    "duration": 863,
    "start_time": "2024-07-01T19:28:12.906Z"
   },
   {
    "duration": 782,
    "start_time": "2024-07-01T19:28:13.772Z"
   },
   {
    "duration": 561,
    "start_time": "2024-07-01T19:28:14.556Z"
   },
   {
    "duration": 597,
    "start_time": "2024-07-01T19:28:15.120Z"
   },
   {
    "duration": 1325,
    "start_time": "2024-07-01T19:28:15.720Z"
   },
   {
    "duration": 1554,
    "start_time": "2024-07-01T19:28:17.050Z"
   },
   {
    "duration": 7090,
    "start_time": "2024-07-01T19:28:18.607Z"
   },
   {
    "duration": 1671,
    "start_time": "2024-07-01T19:28:25.700Z"
   },
   {
    "duration": 658,
    "start_time": "2024-07-01T19:28:27.374Z"
   },
   {
    "duration": 274,
    "start_time": "2024-07-01T19:28:28.046Z"
   },
   {
    "duration": 1885,
    "start_time": "2024-07-01T19:28:28.322Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-01T19:28:30.216Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-01T19:28:30.238Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T19:28:30.269Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T19:28:30.295Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T19:28:30.320Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T19:28:30.324Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T19:28:30.331Z"
   },
   {
    "duration": 1,
    "start_time": "2024-07-01T19:28:30.333Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T19:28:30.339Z"
   },
   {
    "duration": 1000,
    "start_time": "2024-07-01T22:54:28.015Z"
   },
   {
    "duration": 26,
    "start_time": "2024-07-01T23:10:14.149Z"
   },
   {
    "duration": 784,
    "start_time": "2024-07-01T23:11:47.129Z"
   },
   {
    "duration": 25,
    "start_time": "2024-07-01T23:15:10.529Z"
   },
   {
    "duration": 91,
    "start_time": "2024-07-01T23:15:59.657Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-01T23:16:02.179Z"
   },
   {
    "duration": 351,
    "start_time": "2024-07-01T23:17:46.574Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.932Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.934Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.936Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.938Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.940Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.942Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.944Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.946Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.948Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.950Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.952Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.954Z"
   },
   {
    "duration": 1,
    "start_time": "2024-07-01T23:17:46.959Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:46.962Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.012Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.014Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.016Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.018Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.022Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.025Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.027Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.029Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.031Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.033Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.036Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.038Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.040Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.044Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.049Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.051Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.053Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.055Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.113Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.116Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.118Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.120Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.122Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.126Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.129Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.131Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.134Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.136Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.138Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.141Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.143Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.145Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.148Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.150Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.213Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-01T23:17:47.215Z"
   },
   {
    "duration": 656,
    "start_time": "2024-07-01T23:19:14.484Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-01T23:19:21.164Z"
   },
   {
    "duration": 691,
    "start_time": "2024-07-01T23:19:32.713Z"
   },
   {
    "duration": 633,
    "start_time": "2024-07-01T23:23:14.736Z"
   },
   {
    "duration": 339,
    "start_time": "2024-07-01T23:27:28.668Z"
   },
   {
    "duration": 142,
    "start_time": "2024-07-01T23:27:32.689Z"
   },
   {
    "duration": 89,
    "start_time": "2024-07-01T23:27:38.454Z"
   },
   {
    "duration": 71,
    "start_time": "2024-07-01T23:27:52.067Z"
   },
   {
    "duration": 109,
    "start_time": "2024-07-01T23:28:01.473Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T23:28:09.158Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-01T23:28:18.090Z"
   },
   {
    "duration": 25,
    "start_time": "2024-07-01T23:28:38.741Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-01T23:28:49.785Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T23:28:50.441Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-01T23:28:55.995Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-01T23:28:56.721Z"
   },
   {
    "duration": 2711,
    "start_time": "2024-07-01T23:29:00.071Z"
   },
   {
    "duration": 2644,
    "start_time": "2024-07-01T23:29:09.723Z"
   },
   {
    "duration": 2608,
    "start_time": "2024-07-01T23:29:44.739Z"
   },
   {
    "duration": 49,
    "start_time": "2024-07-01T23:29:55.872Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-01T23:29:57.362Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T23:30:06.155Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-01T23:30:11.028Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-01T23:30:16.593Z"
   },
   {
    "duration": 175,
    "start_time": "2024-07-01T23:30:29.316Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-01T23:30:30.994Z"
   },
   {
    "duration": 1246,
    "start_time": "2024-07-01T23:30:43.742Z"
   },
   {
    "duration": 24,
    "start_time": "2024-07-01T23:30:44.991Z"
   },
   {
    "duration": 23,
    "start_time": "2024-07-01T23:30:47.238Z"
   },
   {
    "duration": 110,
    "start_time": "2024-07-01T23:30:55.781Z"
   },
   {
    "duration": 35,
    "start_time": "2024-07-01T23:31:00.119Z"
   },
   {
    "duration": 183,
    "start_time": "2024-07-01T23:31:30.856Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-01T23:31:32.115Z"
   },
   {
    "duration": 4720,
    "start_time": "2024-07-01T23:31:41.852Z"
   },
   {
    "duration": 645,
    "start_time": "2024-07-01T23:31:53.268Z"
   },
   {
    "duration": 783,
    "start_time": "2024-07-01T23:31:59.148Z"
   },
   {
    "duration": 822,
    "start_time": "2024-07-01T23:32:25.321Z"
   },
   {
    "duration": 555,
    "start_time": "2024-07-01T23:32:41.099Z"
   },
   {
    "duration": 586,
    "start_time": "2024-07-01T23:32:56.469Z"
   },
   {
    "duration": 1287,
    "start_time": "2024-07-01T23:33:06.090Z"
   },
   {
    "duration": 1439,
    "start_time": "2024-07-01T23:33:07.380Z"
   },
   {
    "duration": 6457,
    "start_time": "2024-07-01T23:33:08.823Z"
   },
   {
    "duration": 1214,
    "start_time": "2024-07-01T23:33:28.525Z"
   },
   {
    "duration": 501,
    "start_time": "2024-07-01T23:33:30.759Z"
   },
   {
    "duration": 275,
    "start_time": "2024-07-01T23:33:32.769Z"
   },
   {
    "duration": 699,
    "start_time": "2024-07-02T07:34:18.089Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-02T07:34:18.791Z"
   },
   {
    "duration": 655,
    "start_time": "2024-07-02T07:34:18.813Z"
   },
   {
    "duration": 317,
    "start_time": "2024-07-02T07:34:19.473Z"
   },
   {
    "duration": 166,
    "start_time": "2024-07-02T07:34:19.793Z"
   },
   {
    "duration": 113,
    "start_time": "2024-07-02T07:34:19.963Z"
   },
   {
    "duration": 127,
    "start_time": "2024-07-02T07:34:20.078Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-02T07:34:20.208Z"
   },
   {
    "duration": 49,
    "start_time": "2024-07-02T07:34:20.233Z"
   },
   {
    "duration": 47,
    "start_time": "2024-07-02T07:34:20.287Z"
   },
   {
    "duration": 3,
    "start_time": "2024-07-02T07:34:20.337Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T07:34:20.343Z"
   },
   {
    "duration": 4,
    "start_time": "2024-07-02T07:34:20.355Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T07:34:20.361Z"
   },
   {
    "duration": 3497,
    "start_time": "2024-07-02T07:34:20.373Z"
   },
   {
    "duration": 3344,
    "start_time": "2024-07-02T07:34:23.874Z"
   },
   {
    "duration": 78,
    "start_time": "2024-07-02T07:34:27.221Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T07:34:27.301Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-02T07:34:27.320Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-02T07:34:27.337Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T07:34:27.351Z"
   },
   {
    "duration": 219,
    "start_time": "2024-07-02T07:34:27.371Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T07:34:27.592Z"
   },
   {
    "duration": 1298,
    "start_time": "2024-07-02T07:34:27.604Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T07:34:28.904Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-02T07:34:28.919Z"
   },
   {
    "duration": 128,
    "start_time": "2024-07-02T07:34:28.953Z"
   },
   {
    "duration": 47,
    "start_time": "2024-07-02T07:34:29.089Z"
   },
   {
    "duration": 192,
    "start_time": "2024-07-02T07:34:29.139Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T07:34:29.334Z"
   },
   {
    "duration": 1002,
    "start_time": "2024-07-02T07:34:29.346Z"
   },
   {
    "duration": 598,
    "start_time": "2024-07-02T07:34:30.351Z"
   },
   {
    "duration": 798,
    "start_time": "2024-07-02T07:34:30.952Z"
   },
   {
    "duration": 804,
    "start_time": "2024-07-02T07:34:31.753Z"
   },
   {
    "duration": 570,
    "start_time": "2024-07-02T07:34:32.560Z"
   },
   {
    "duration": 596,
    "start_time": "2024-07-02T07:34:33.134Z"
   },
   {
    "duration": 1282,
    "start_time": "2024-07-02T07:34:33.734Z"
   },
   {
    "duration": 346,
    "start_time": "2024-07-02T08:15:56.207Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-02T08:17:17.012Z"
   },
   {
    "duration": 702,
    "start_time": "2024-07-02T08:18:15.594Z"
   },
   {
    "duration": 70,
    "start_time": "2024-07-02T08:18:19.224Z"
   },
   {
    "duration": 96,
    "start_time": "2024-07-02T08:20:25.202Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-02T08:20:29.096Z"
   },
   {
    "duration": 59,
    "start_time": "2024-07-02T08:20:56.604Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-02T08:21:05.173Z"
   },
   {
    "duration": 70,
    "start_time": "2024-07-02T08:21:27.607Z"
   },
   {
    "duration": 41,
    "start_time": "2024-07-02T08:21:33.350Z"
   },
   {
    "duration": 287,
    "start_time": "2024-07-02T08:29:12.898Z"
   },
   {
    "duration": 72,
    "start_time": "2024-07-02T08:29:13.629Z"
   },
   {
    "duration": 1697,
    "start_time": "2024-07-02T08:29:14.191Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-02T08:29:15.893Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T08:29:15.907Z"
   },
   {
    "duration": 1167,
    "start_time": "2024-07-02T08:29:30.660Z"
   },
   {
    "duration": 78,
    "start_time": "2024-07-02T08:30:04.230Z"
   },
   {
    "duration": 22,
    "start_time": "2024-07-02T08:31:56.514Z"
   },
   {
    "duration": 77,
    "start_time": "2024-07-02T08:32:05.256Z"
   },
   {
    "duration": 108,
    "start_time": "2024-07-02T08:33:29.517Z"
   },
   {
    "duration": 200,
    "start_time": "2024-07-02T08:33:58.793Z"
   },
   {
    "duration": 53,
    "start_time": "2024-07-02T08:33:59.551Z"
   },
   {
    "duration": 1248,
    "start_time": "2024-07-02T08:34:00.042Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-02T08:34:01.294Z"
   },
   {
    "duration": 209,
    "start_time": "2024-07-02T08:35:30.826Z"
   },
   {
    "duration": 58,
    "start_time": "2024-07-02T08:35:31.386Z"
   },
   {
    "duration": 1423,
    "start_time": "2024-07-02T08:35:31.814Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-02T08:35:33.244Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T08:35:33.262Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-02T08:35:36.060Z"
   },
   {
    "duration": 468,
    "start_time": "2024-07-02T08:36:16.545Z"
   },
   {
    "duration": 465,
    "start_time": "2024-07-02T08:36:28.307Z"
   },
   {
    "duration": 324,
    "start_time": "2024-07-02T08:36:43.218Z"
   },
   {
    "duration": 149,
    "start_time": "2024-07-02T08:36:52.187Z"
   },
   {
    "duration": 103,
    "start_time": "2024-07-02T08:36:58.321Z"
   },
   {
    "duration": 54,
    "start_time": "2024-07-02T08:37:18.653Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T08:37:29.638Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-02T08:37:39.291Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-02T08:38:56.875Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-02T08:39:05.786Z"
   },
   {
    "duration": 1419,
    "start_time": "2024-07-02T08:39:35.781Z"
   },
   {
    "duration": 2497,
    "start_time": "2024-07-02T08:39:46.063Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-02T08:40:07.569Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T08:40:21.231Z"
   },
   {
    "duration": 35,
    "start_time": "2024-07-02T08:40:31.290Z"
   },
   {
    "duration": 34,
    "start_time": "2024-07-02T08:41:37.223Z"
   },
   {
    "duration": 25,
    "start_time": "2024-07-02T08:42:58.268Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-02T08:43:28.403Z"
   },
   {
    "duration": 28,
    "start_time": "2024-07-02T08:44:47.185Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T08:45:23.004Z"
   },
   {
    "duration": 25,
    "start_time": "2024-07-02T08:45:37.267Z"
   },
   {
    "duration": 25,
    "start_time": "2024-07-02T08:47:27.886Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T08:50:11.049Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-02T08:50:37.829Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-02T08:51:44.870Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-02T08:52:45.504Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T08:53:49.107Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T08:54:00.092Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-02T08:54:29.097Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-02T08:54:51.501Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-02T08:55:16.550Z"
   },
   {
    "duration": 18,
    "start_time": "2024-07-02T08:55:26.869Z"
   },
   {
    "duration": 142,
    "start_time": "2024-07-02T08:55:32.589Z"
   },
   {
    "duration": 44,
    "start_time": "2024-07-02T08:55:40.481Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-02T08:56:12.235Z"
   },
   {
    "duration": 4626,
    "start_time": "2024-07-02T08:56:35.728Z"
   },
   {
    "duration": 873,
    "start_time": "2024-07-02T08:56:53.237Z"
   },
   {
    "duration": 537,
    "start_time": "2024-07-02T08:57:25.464Z"
   },
   {
    "duration": 657,
    "start_time": "2024-07-02T08:57:53.806Z"
   },
   {
    "duration": 1038,
    "start_time": "2024-07-02T08:58:24.695Z"
   },
   {
    "duration": 702,
    "start_time": "2024-07-02T08:58:31.057Z"
   },
   {
    "duration": 576,
    "start_time": "2024-07-02T08:58:47.690Z"
   },
   {
    "duration": 543,
    "start_time": "2024-07-02T08:59:27.890Z"
   },
   {
    "duration": 374,
    "start_time": "2024-07-02T09:00:02.952Z"
   },
   {
    "duration": 622,
    "start_time": "2024-07-02T09:01:04.067Z"
   },
   {
    "duration": 50,
    "start_time": "2024-07-02T09:02:41.839Z"
   },
   {
    "duration": 1819,
    "start_time": "2024-07-02T09:03:18.678Z"
   },
   {
    "duration": 6685,
    "start_time": "2024-07-02T09:03:31.506Z"
   },
   {
    "duration": 732,
    "start_time": "2024-07-02T09:05:02.719Z"
   },
   {
    "duration": 328,
    "start_time": "2024-07-02T09:05:05.225Z"
   },
   {
    "duration": 225,
    "start_time": "2024-07-02T09:06:25.042Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-02T09:06:26.038Z"
   },
   {
    "duration": 31,
    "start_time": "2024-07-02T09:06:26.754Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T09:06:29.366Z"
   },
   {
    "duration": 149,
    "start_time": "2024-07-02T09:07:51.053Z"
   },
   {
    "duration": 214,
    "start_time": "2024-07-02T09:08:07.583Z"
   },
   {
    "duration": 254,
    "start_time": "2024-07-02T09:08:25.495Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-02T09:08:28.628Z"
   },
   {
    "duration": 30,
    "start_time": "2024-07-02T09:09:27.824Z"
   },
   {
    "duration": 1375,
    "start_time": "2024-07-02T09:09:45.637Z"
   },
   {
    "duration": 247,
    "start_time": "2024-07-02T09:10:00.857Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-02T09:11:07.201Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-02T09:11:28.262Z"
   },
   {
    "duration": 1606,
    "start_time": "2024-07-02T09:11:43.027Z"
   },
   {
    "duration": 740,
    "start_time": "2024-07-02T09:12:05.588Z"
   },
   {
    "duration": 60,
    "start_time": "2024-07-02T09:12:06.332Z"
   },
   {
    "duration": 1316,
    "start_time": "2024-07-02T09:12:06.395Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T09:12:07.716Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-02T09:12:07.737Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T09:12:07.748Z"
   },
   {
    "duration": 595,
    "start_time": "2024-07-02T09:12:07.769Z"
   },
   {
    "duration": 385,
    "start_time": "2024-07-02T09:12:08.368Z"
   },
   {
    "duration": 186,
    "start_time": "2024-07-02T09:12:08.757Z"
   },
   {
    "duration": 132,
    "start_time": "2024-07-02T09:12:08.950Z"
   },
   {
    "duration": 76,
    "start_time": "2024-07-02T09:12:09.086Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T09:12:09.166Z"
   },
   {
    "duration": 77,
    "start_time": "2024-07-02T09:12:09.182Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-02T09:12:09.265Z"
   },
   {
    "duration": 1419,
    "start_time": "2024-07-02T09:12:09.297Z"
   },
   {
    "duration": 2823,
    "start_time": "2024-07-02T09:12:10.719Z"
   },
   {
    "duration": 18,
    "start_time": "2024-07-02T09:12:13.545Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T09:12:13.567Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T09:12:13.582Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-02T09:12:13.634Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T09:12:13.654Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-02T09:12:13.666Z"
   },
   {
    "duration": 60,
    "start_time": "2024-07-02T09:12:13.682Z"
   },
   {
    "duration": 123,
    "start_time": "2024-07-02T09:12:13.745Z"
   },
   {
    "duration": 39,
    "start_time": "2024-07-02T09:12:13.871Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-02T09:12:13.913Z"
   },
   {
    "duration": 906,
    "start_time": "2024-07-02T09:12:13.945Z"
   },
   {
    "duration": 460,
    "start_time": "2024-07-02T09:12:14.860Z"
   },
   {
    "duration": 671,
    "start_time": "2024-07-02T09:12:15.323Z"
   },
   {
    "duration": 379,
    "start_time": "2024-07-02T09:12:16.000Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.382Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.383Z"
   },
   {
    "duration": 1,
    "start_time": "2024-07-02T09:12:16.386Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.389Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.392Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.394Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.396Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.398Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.400Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.433Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.435Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.437Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.440Z"
   },
   {
    "duration": 1,
    "start_time": "2024-07-02T09:12:16.441Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T09:12:16.444Z"
   },
   {
    "duration": 1894,
    "start_time": "2024-07-02T09:12:46.167Z"
   },
   {
    "duration": 689,
    "start_time": "2024-07-02T19:15:53.902Z"
   },
   {
    "duration": 87,
    "start_time": "2024-07-02T19:15:54.595Z"
   },
   {
    "duration": 1341,
    "start_time": "2024-07-02T19:15:54.685Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T19:15:56.028Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T19:15:56.043Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-02T19:15:56.055Z"
   },
   {
    "duration": 558,
    "start_time": "2024-07-02T19:15:56.076Z"
   },
   {
    "duration": 333,
    "start_time": "2024-07-02T19:15:56.637Z"
   },
   {
    "duration": 169,
    "start_time": "2024-07-02T19:15:56.975Z"
   },
   {
    "duration": 103,
    "start_time": "2024-07-02T19:15:57.147Z"
   },
   {
    "duration": 53,
    "start_time": "2024-07-02T19:15:57.254Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-02T19:15:57.310Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-02T19:15:57.339Z"
   },
   {
    "duration": 55,
    "start_time": "2024-07-02T19:15:57.395Z"
   },
   {
    "duration": 1321,
    "start_time": "2024-07-02T19:15:57.454Z"
   },
   {
    "duration": 2621,
    "start_time": "2024-07-02T19:15:58.778Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-02T19:16:01.401Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T19:16:01.433Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T19:16:01.448Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-02T19:16:01.460Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T19:16:01.478Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T19:16:01.532Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-02T19:16:01.547Z"
   },
   {
    "duration": 149,
    "start_time": "2024-07-02T19:16:01.563Z"
   },
   {
    "duration": 41,
    "start_time": "2024-07-02T19:16:01.715Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-02T19:16:01.759Z"
   },
   {
    "duration": 4478,
    "start_time": "2024-07-02T19:16:01.778Z"
   },
   {
    "duration": 443,
    "start_time": "2024-07-02T19:16:06.260Z"
   },
   {
    "duration": 641,
    "start_time": "2024-07-02T19:16:06.707Z"
   },
   {
    "duration": 434,
    "start_time": "2024-07-02T19:16:07.351Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.789Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.792Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.793Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.795Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.797Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.799Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.800Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.803Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.805Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.831Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.833Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.835Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.837Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.839Z"
   },
   {
    "duration": 0,
    "start_time": "2024-07-02T19:16:07.841Z"
   },
   {
    "duration": 49,
    "start_time": "2024-07-02T19:20:57.030Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-02T19:21:01.807Z"
   },
   {
    "duration": 38,
    "start_time": "2024-07-02T19:22:01.232Z"
   },
   {
    "duration": 30,
    "start_time": "2024-07-02T19:22:08.995Z"
   },
   {
    "duration": 1925,
    "start_time": "2024-07-02T19:22:10.163Z"
   },
   {
    "duration": 6889,
    "start_time": "2024-07-02T19:22:12.092Z"
   },
   {
    "duration": 634,
    "start_time": "2024-07-02T19:22:18.985Z"
   },
   {
    "duration": 285,
    "start_time": "2024-07-02T19:22:19.622Z"
   },
   {
    "duration": 206,
    "start_time": "2024-07-02T19:22:19.912Z"
   },
   {
    "duration": 31,
    "start_time": "2024-07-02T19:22:20.122Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-02T19:22:20.160Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T19:22:20.185Z"
   },
   {
    "duration": 235,
    "start_time": "2024-07-02T19:22:20.197Z"
   },
   {
    "duration": 16,
    "start_time": "2024-07-02T19:22:20.435Z"
   },
   {
    "duration": 1448,
    "start_time": "2024-07-02T19:22:20.462Z"
   },
   {
    "duration": 295,
    "start_time": "2024-07-02T19:22:21.913Z"
   },
   {
    "duration": 1593,
    "start_time": "2024-07-02T19:22:22.211Z"
   },
   {
    "duration": 4585,
    "start_time": "2024-07-02T23:02:46.074Z"
   },
   {
    "duration": 37,
    "start_time": "2024-07-02T23:03:55.986Z"
   },
   {
    "duration": 30,
    "start_time": "2024-07-02T23:06:05.517Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-02T23:07:35.353Z"
   },
   {
    "duration": 31,
    "start_time": "2024-07-02T23:08:02.808Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-02T23:10:52.049Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-02T23:13:28.204Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-02T23:14:46.424Z"
   },
   {
    "duration": 323,
    "start_time": "2024-07-02T23:15:41.832Z"
   },
   {
    "duration": 911,
    "start_time": "2024-07-02T23:17:20.290Z"
   },
   {
    "duration": 655,
    "start_time": "2024-07-02T23:17:37.730Z"
   },
   {
    "duration": 570,
    "start_time": "2024-07-02T23:19:15.126Z"
   },
   {
    "duration": 385,
    "start_time": "2024-07-02T23:19:26.704Z"
   },
   {
    "duration": 451,
    "start_time": "2024-07-02T23:19:46.144Z"
   },
   {
    "duration": 27,
    "start_time": "2024-07-02T23:23:14.254Z"
   },
   {
    "duration": 30,
    "start_time": "2024-07-02T23:24:23.836Z"
   },
   {
    "duration": 680,
    "start_time": "2024-07-02T23:26:59.350Z"
   },
   {
    "duration": 93,
    "start_time": "2024-07-02T23:27:00.035Z"
   },
   {
    "duration": 1422,
    "start_time": "2024-07-02T23:27:00.130Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T23:27:01.556Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-02T23:27:01.569Z"
   },
   {
    "duration": 18,
    "start_time": "2024-07-02T23:27:01.586Z"
   },
   {
    "duration": 584,
    "start_time": "2024-07-02T23:27:01.606Z"
   },
   {
    "duration": 359,
    "start_time": "2024-07-02T23:27:02.194Z"
   },
   {
    "duration": 175,
    "start_time": "2024-07-02T23:27:02.556Z"
   },
   {
    "duration": 101,
    "start_time": "2024-07-02T23:27:02.738Z"
   },
   {
    "duration": 56,
    "start_time": "2024-07-02T23:27:02.842Z"
   },
   {
    "duration": 35,
    "start_time": "2024-07-02T23:27:02.901Z"
   },
   {
    "duration": 49,
    "start_time": "2024-07-02T23:27:02.939Z"
   },
   {
    "duration": 52,
    "start_time": "2024-07-02T23:27:02.991Z"
   },
   {
    "duration": 1329,
    "start_time": "2024-07-02T23:27:03.048Z"
   },
   {
    "duration": 2632,
    "start_time": "2024-07-02T23:27:04.381Z"
   },
   {
    "duration": 23,
    "start_time": "2024-07-02T23:27:07.016Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T23:27:07.042Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T23:27:07.058Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-02T23:27:07.070Z"
   },
   {
    "duration": 53,
    "start_time": "2024-07-02T23:27:07.088Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-02T23:27:07.144Z"
   },
   {
    "duration": 19,
    "start_time": "2024-07-02T23:27:07.161Z"
   },
   {
    "duration": 147,
    "start_time": "2024-07-02T23:27:07.183Z"
   },
   {
    "duration": 40,
    "start_time": "2024-07-02T23:27:07.338Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-02T23:27:07.380Z"
   },
   {
    "duration": 857,
    "start_time": "2024-07-02T23:27:07.397Z"
   },
   {
    "duration": 471,
    "start_time": "2024-07-02T23:27:08.263Z"
   },
   {
    "duration": 617,
    "start_time": "2024-07-02T23:27:08.737Z"
   },
   {
    "duration": 616,
    "start_time": "2024-07-02T23:27:09.359Z"
   },
   {
    "duration": 389,
    "start_time": "2024-07-02T23:27:09.978Z"
   },
   {
    "duration": 444,
    "start_time": "2024-07-02T23:27:10.370Z"
   },
   {
    "duration": 1837,
    "start_time": "2024-07-02T23:27:10.818Z"
   },
   {
    "duration": 6588,
    "start_time": "2024-07-02T23:27:12.658Z"
   },
   {
    "duration": 615,
    "start_time": "2024-07-02T23:27:19.248Z"
   },
   {
    "duration": 258,
    "start_time": "2024-07-02T23:27:19.866Z"
   },
   {
    "duration": 192,
    "start_time": "2024-07-02T23:27:20.132Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-02T23:27:20.327Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T23:27:20.342Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T23:27:20.362Z"
   },
   {
    "duration": 234,
    "start_time": "2024-07-02T23:27:20.374Z"
   },
   {
    "duration": 21,
    "start_time": "2024-07-02T23:27:20.611Z"
   },
   {
    "duration": 1357,
    "start_time": "2024-07-02T23:27:20.635Z"
   },
   {
    "duration": 252,
    "start_time": "2024-07-02T23:27:21.995Z"
   },
   {
    "duration": 1540,
    "start_time": "2024-07-02T23:27:22.250Z"
   },
   {
    "duration": 447,
    "start_time": "2024-07-02T23:31:09.474Z"
   },
   {
    "duration": 615,
    "start_time": "2024-07-02T23:32:15.954Z"
   },
   {
    "duration": 1984,
    "start_time": "2024-07-02T23:35:23.095Z"
   },
   {
    "duration": 104,
    "start_time": "2024-07-02T23:40:46.897Z"
   },
   {
    "duration": 256,
    "start_time": "2024-07-02T23:42:04.586Z"
   },
   {
    "duration": 211,
    "start_time": "2024-07-02T23:42:36.943Z"
   },
   {
    "duration": 491,
    "start_time": "2024-07-02T23:49:35.067Z"
   },
   {
    "duration": 1565,
    "start_time": "2024-07-02T23:51:32.737Z"
   },
   {
    "duration": 7,
    "start_time": "2024-07-02T23:52:06.354Z"
   },
   {
    "duration": 238,
    "start_time": "2024-07-02T23:53:01.666Z"
   },
   {
    "duration": 323,
    "start_time": "2024-07-02T23:55:09.543Z"
   },
   {
    "duration": 557,
    "start_time": "2024-07-02T23:55:13.201Z"
   },
   {
    "duration": 352,
    "start_time": "2024-07-02T23:55:15.169Z"
   },
   {
    "duration": 648,
    "start_time": "2024-07-02T23:55:48.589Z"
   },
   {
    "duration": 57,
    "start_time": "2024-07-02T23:55:49.241Z"
   },
   {
    "duration": 1268,
    "start_time": "2024-07-02T23:55:49.301Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T23:55:50.574Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T23:55:50.586Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-02T23:55:50.599Z"
   },
   {
    "duration": 537,
    "start_time": "2024-07-02T23:55:50.639Z"
   },
   {
    "duration": 381,
    "start_time": "2024-07-02T23:55:51.178Z"
   },
   {
    "duration": 172,
    "start_time": "2024-07-02T23:55:51.562Z"
   },
   {
    "duration": 103,
    "start_time": "2024-07-02T23:55:51.745Z"
   },
   {
    "duration": 55,
    "start_time": "2024-07-02T23:55:51.851Z"
   },
   {
    "duration": 32,
    "start_time": "2024-07-02T23:55:51.909Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-02T23:55:51.945Z"
   },
   {
    "duration": 46,
    "start_time": "2024-07-02T23:55:51.996Z"
   },
   {
    "duration": 1431,
    "start_time": "2024-07-02T23:55:52.045Z"
   },
   {
    "duration": 2932,
    "start_time": "2024-07-02T23:55:53.479Z"
   },
   {
    "duration": 20,
    "start_time": "2024-07-02T23:55:56.424Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-02T23:55:56.447Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-02T23:55:56.462Z"
   },
   {
    "duration": 17,
    "start_time": "2024-07-02T23:55:56.475Z"
   },
   {
    "duration": 39,
    "start_time": "2024-07-02T23:55:56.495Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-02T23:55:56.537Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-02T23:55:56.553Z"
   },
   {
    "duration": 155,
    "start_time": "2024-07-02T23:55:56.571Z"
   },
   {
    "duration": 42,
    "start_time": "2024-07-02T23:55:56.735Z"
   },
   {
    "duration": 11,
    "start_time": "2024-07-02T23:55:56.780Z"
   },
   {
    "duration": 1138,
    "start_time": "2024-07-02T23:55:56.795Z"
   },
   {
    "duration": 726,
    "start_time": "2024-07-02T23:55:57.949Z"
   },
   {
    "duration": 938,
    "start_time": "2024-07-02T23:55:58.678Z"
   },
   {
    "duration": 688,
    "start_time": "2024-07-02T23:55:59.619Z"
   },
   {
    "duration": 459,
    "start_time": "2024-07-02T23:56:00.310Z"
   },
   {
    "duration": 540,
    "start_time": "2024-07-02T23:56:00.773Z"
   },
   {
    "duration": 2146,
    "start_time": "2024-07-02T23:56:01.317Z"
   },
   {
    "duration": 7019,
    "start_time": "2024-07-02T23:56:03.469Z"
   },
   {
    "duration": 2306,
    "start_time": "2024-07-02T23:56:10.492Z"
   },
   {
    "duration": 603,
    "start_time": "2024-07-02T23:56:12.800Z"
   },
   {
    "duration": 401,
    "start_time": "2024-07-02T23:56:13.406Z"
   },
   {
    "duration": 193,
    "start_time": "2024-07-02T23:56:13.810Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-02T23:56:14.007Z"
   },
   {
    "duration": 29,
    "start_time": "2024-07-02T23:56:14.019Z"
   },
   {
    "duration": 8,
    "start_time": "2024-07-02T23:56:14.050Z"
   },
   {
    "duration": 232,
    "start_time": "2024-07-02T23:56:14.062Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-02T23:56:14.297Z"
   },
   {
    "duration": 1364,
    "start_time": "2024-07-02T23:56:14.313Z"
   },
   {
    "duration": 261,
    "start_time": "2024-07-02T23:56:15.680Z"
   },
   {
    "duration": 1550,
    "start_time": "2024-07-02T23:56:15.945Z"
   },
   {
    "duration": 690,
    "start_time": "2024-07-03T06:51:59.521Z"
   },
   {
    "duration": 88,
    "start_time": "2024-07-03T06:52:00.215Z"
   },
   {
    "duration": 1331,
    "start_time": "2024-07-03T06:52:00.306Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-03T06:52:01.643Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-03T06:52:01.655Z"
   },
   {
    "duration": 39,
    "start_time": "2024-07-03T06:52:01.669Z"
   },
   {
    "duration": 552,
    "start_time": "2024-07-03T06:52:01.711Z"
   },
   {
    "duration": 349,
    "start_time": "2024-07-03T06:52:02.267Z"
   },
   {
    "duration": 169,
    "start_time": "2024-07-03T06:52:02.619Z"
   },
   {
    "duration": 106,
    "start_time": "2024-07-03T06:52:02.800Z"
   },
   {
    "duration": 56,
    "start_time": "2024-07-03T06:52:02.909Z"
   },
   {
    "duration": 35,
    "start_time": "2024-07-03T06:52:02.968Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-03T06:52:03.005Z"
   },
   {
    "duration": 50,
    "start_time": "2024-07-03T06:52:03.056Z"
   },
   {
    "duration": 1350,
    "start_time": "2024-07-03T06:52:03.109Z"
   },
   {
    "duration": 2668,
    "start_time": "2024-07-03T06:52:04.463Z"
   },
   {
    "duration": 15,
    "start_time": "2024-07-03T06:52:07.137Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-03T06:52:07.155Z"
   },
   {
    "duration": 36,
    "start_time": "2024-07-03T06:52:07.172Z"
   },
   {
    "duration": 18,
    "start_time": "2024-07-03T06:52:07.214Z"
   },
   {
    "duration": 12,
    "start_time": "2024-07-03T06:52:07.236Z"
   },
   {
    "duration": 51,
    "start_time": "2024-07-03T06:52:07.251Z"
   },
   {
    "duration": 14,
    "start_time": "2024-07-03T06:52:07.305Z"
   },
   {
    "duration": 134,
    "start_time": "2024-07-03T06:52:07.322Z"
   },
   {
    "duration": 48,
    "start_time": "2024-07-03T06:52:07.459Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-03T06:52:07.511Z"
   },
   {
    "duration": 835,
    "start_time": "2024-07-03T06:52:07.524Z"
   },
   {
    "duration": 400,
    "start_time": "2024-07-03T06:52:08.366Z"
   },
   {
    "duration": 658,
    "start_time": "2024-07-03T06:52:08.770Z"
   },
   {
    "duration": 607,
    "start_time": "2024-07-03T06:52:09.431Z"
   },
   {
    "duration": 388,
    "start_time": "2024-07-03T06:52:10.041Z"
   },
   {
    "duration": 443,
    "start_time": "2024-07-03T06:52:10.433Z"
   },
   {
    "duration": 1825,
    "start_time": "2024-07-03T06:52:10.879Z"
   },
   {
    "duration": 6706,
    "start_time": "2024-07-03T06:52:12.706Z"
   },
   {
    "duration": 2394,
    "start_time": "2024-07-03T06:52:19.415Z"
   },
   {
    "duration": 654,
    "start_time": "2024-07-03T06:52:21.812Z"
   },
   {
    "duration": 406,
    "start_time": "2024-07-03T06:52:22.469Z"
   },
   {
    "duration": 193,
    "start_time": "2024-07-03T06:52:22.878Z"
   },
   {
    "duration": 10,
    "start_time": "2024-07-03T06:52:23.073Z"
   },
   {
    "duration": 31,
    "start_time": "2024-07-03T06:52:23.086Z"
   },
   {
    "duration": 9,
    "start_time": "2024-07-03T06:52:23.120Z"
   },
   {
    "duration": 237,
    "start_time": "2024-07-03T06:52:23.132Z"
   },
   {
    "duration": 13,
    "start_time": "2024-07-03T06:52:23.372Z"
   },
   {
    "duration": 1531,
    "start_time": "2024-07-03T06:52:23.402Z"
   },
   {
    "duration": 272,
    "start_time": "2024-07-03T06:52:24.936Z"
   },
   {
    "duration": 1644,
    "start_time": "2024-07-03T06:52:25.212Z"
   }
  ],
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.19"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": true,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "vscode": {
   "interpreter": {
    "hash": "01a7be9ec63e704a62cefc5fe7a4756944464ee731be31632bdf42a4cb4688cf"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
