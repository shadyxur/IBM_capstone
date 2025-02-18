#Data wrangling

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None) #show all the columns on the screen

# URL of the dataset
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/Capstone_edX/Module%201/survey_results_public_2020.csv'

# Read the dataset
df = pd.read_csv(url)

# Count the missing values in the 'Hobbyist' column
missing_hobbyist_count = df['Hobbyist'].isna().sum()
print(f'Missing rows in the "Hobbyist" column: {missing_hobbyist_count}')

# Find the median for the column 'Age' before any modifications
original_median_age = df['Age'].median()
print(f'Original median age: {original_median_age}')

# Find how many duplicate rows exist in the dataframe
duplicate_count = df.duplicated().sum()
print(f'Number of duplicate rows: {duplicate_count}')

# Remove the duplicate rows from the dataframe
df = df.drop_duplicates()

# Verify if duplicates were actually dropped
duplicate_count_after = df.duplicated().sum()
print(f'Number of duplicate rows after removal: {duplicate_count_after}')

# Impute the median value to 'Age' column
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# Verify the median age after imputation
median_age_after_imputation = df['Age'].median()
print(f'Median age after imputation: {median_age_after_imputation}')

# Impute missing values for numerical columns with the mean
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    if col != 'Age':  # 'Age' column already imputed
        df[col] = df[col].fillna(df[col].mean())

# Impute missing values for categorical columns with the mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Identify the value that is most frequent (majority) in the 'Country' column
majority_country = df['Country'].mode()[0]
print(f'\nMost frequent country: {majority_country}')

# List out the various categories in the column 'CompFreq'
compfreq_categories = df['CompFreq'].unique()
print('\nCategories in the column "CompFreq":')
print(compfreq_categories)

# Filter out unrealistic values in CompTotal and replace them with values from ConvertedComp
threshold = 1e10  # Example threshold
df.loc[df['CompTotal'] > threshold, 'CompTotal'] = np.nan
df['CompTotal'] = df['CompTotal'].fillna(df['ConvertedComp'])

# Verify if the values have been corrected
print('\nFirst few rows of CompTotal and ConvertedComp columns after correction:')
print(df[['CompTotal', 'ConvertedComp']].head())

# Check if CompTotal and ConvertedComp columns are still identical after correction
are_identical_after_correction = df['CompTotal'].equals(df['ConvertedComp'])
print(f'\nAre CompTotal and ConvertedComp columns identical after correction? {are_identical_after_correction}')

# Create a new column called 'NormalizedAnnualCompensation'
def normalize_compensation(row):
    if row['CompFreq'] == 'Yearly':
        return row['CompTotal']
    elif row['CompFreq'] == 'Monthly':
        return row['CompTotal'] * 12
    elif row['CompFreq'] == 'Weekly':
        return row['CompTotal'] * 52
    else:
        return None

df['NormalizedAnnualCompensation'] = df.apply(normalize_compensation, axis=1)

print('\nNormalized Annual Compensation has been calculated.')

# Check for any remaining NaN values
remaining_nans = df.isnull().sum()
print('\nRemaining NaN values in the dataframe:')
print(remaining_nans)

# Verify the median age after processing
final_median_age = df['Age'].median()
print(f'Final median age: {final_median_age}')

# Calculate and print the median NormalizedAnnualCompensation
median_normalized_compensation = df['NormalizedAnnualCompensation'].median()
print(f'\nMedian NormalizedAnnualCompensation: {median_normalized_compensation}')

# Display the first few rows of the updated dataframe
print(df.head())









