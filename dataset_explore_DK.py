#Dataset exploration

import pandas as pd

# URL of the dataset
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/Capstone_edX/Module%201/survey_results_public_2020.csv'

# Read the dataset
df = pd.read_csv(url)

# Display the top 5 rows and columns
top_5 = df.head()
print("Top 5 rows and columns:")
print(top_5)

# Print the number of rows in the dataset
num_rows = df.shape[0]
print(f"\nNumber of rows in the dataset: {num_rows}")

# Print the number of columns in the dataset
num_columns = df.shape[1]
print(f"Number of columns in the dataset: {num_columns}")

# Adjust pandas display settings to show all columns
pd.set_option('display.max_columns', None)

# Print the datatype of all columns
datatypes = df.dtypes
print("\nDatatypes of all columns:")
print(datatypes)

# Print the mean age of the survey participants
mean_age = round(df['Age'].mean(), 3)
print(f"\nMean age of the survey participants: {mean_age}")

# Print how many unique countries are there in the 'Country' column
unique_countries = df['Country'].nunique()
print(f"\nNumber of unique countries in the 'Country' column: {unique_countries}")

unique_resp = df['Respondent'].nunique()
print(f"\nNumber of unique crespondents in the 'Respondent' column: {unique_resp}")


