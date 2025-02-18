# Data statistical exploration

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pointbiserialr

pd.set_option('display.max_columns', None)  # Show all the columns on the screen

# Download the data and convert to dataframe
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/Capstone_edX/Module%203/Survey_data.csv"
data = pd.read_csv(url)

# Plot the distribution curve for 'ConvertedComp'
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.kdeplot(data['ConvertedComp'].dropna(), fill=True)
plt.title('Distribution Curve for Converted Compensation')
plt.xlabel('Converted Compensation')
plt.ylabel('Density')
plt.show()

# Plot the histogram for 'ConvertedComp'
plt.figure(figsize=(10, 6))
plt.hist(data['ConvertedComp'].dropna(), bins=30, edgecolor='k')
plt.title('Histogram of Converted Compensation')
plt.xlabel('Converted Compensation')
plt.ylabel('Frequency')
plt.show()

# Calculate the Median of 'ConvertedComp'
median_comp = data['ConvertedComp'].median()
print(f"Median of Converted Compensation: {median_comp}")

# Count how many responders are men
num_men = data[data['Gender'] == 'Man'].shape[0]
print(f"Number of responders identified as Man: {num_men}")

# Count how many responders are women
num_women = data[data['Gender'] == 'Woman'].shape[0]
print(f"Number of responders identified as Woman: {num_women}")

# Calculate the Median 'ConvertedComp' for women
median_comp_women = data[data['Gender'] == 'Woman']['ConvertedComp'].median()
print(f"Median Converted Compensation for Women: {median_comp_women}")

# Calculate the Median 'ConvertedComp' for men
median_comp_men = data[data['Gender'] == 'Man']['ConvertedComp'].median()
print(f"Median Converted Compensation for Men: {median_comp_men}")

# Describe 5-number summary for 'Age'
age_summary = data['Age'].describe(percentiles=[.25, .5, .75])
age_five_number_summary = {
    'min': age_summary['min'],
    'q1': age_summary['25%'],
    'median': age_summary['50%'],
    'q3': age_summary['75%'],
    'max': age_summary['max']
}
print(f"Five Number Summary for Age: {age_five_number_summary}")

# Plot histogram for 'Age'
plt.figure(figsize=(10, 6))
plt.hist(data['Age'].dropna(), bins=30, edgecolor='k')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Detect outliers in 'ConvertedComp'
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['ConvertedComp'].dropna())
plt.title('Box Plot of Converted Compensation')
plt.xlabel('Converted Compensation')
plt.show()

# Calculating the IQR
q1 = data['ConvertedComp'].quantile(0.25)
q3 = data['ConvertedComp'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Identifying outliers
outliers = data[(data['ConvertedComp'] < lower_bound) | (data['ConvertedComp'] > upper_bound)]
num_outliers = outliers.shape[0]
print(f"Number of outliers in Converted Compensation: {num_outliers}")

# Removing outliers
data_no_outliers = data[~((data['ConvertedComp'] < lower_bound) | (data['ConvertedComp'] > upper_bound))]

# Calculate median and mean of 'ConvertedComp' after removing outliers
median_comp_no_outliers = data_no_outliers['ConvertedComp'].median()
mean_comp_no_outliers = data_no_outliers['ConvertedComp'].mean()
print(f"Median Converted Compensation after removing outliers: {median_comp_no_outliers}")
print(f"Mean Converted Compensation after removing outliers: {mean_comp_no_outliers}")

# Find correlation between 'Age' and other numerical columns
# Convert columns to numeric, setting errors='coerce' to convert non-numeric to NaN
data_numeric = data.apply(pd.to_numeric, errors='coerce')

# Calculate the correlation matrix
correlation_matrix = data_numeric.corr()

# Get the correlation of 'Age' with other numerical columns
age_correlation = correlation_matrix['Age']
print(f"Correlation between Age and other numerical columns:\n{age_correlation}")

# Find correlation between responder's gender and salary
# Encode Gender column: 'Man' -> 0, 'Woman' -> 1
data['Gender_encoded'] = data['Gender'].map({'Man': 0, 'Woman': 1})

# Drop rows with NaN values in 'ConvertedComp' or 'Gender_encoded'
filtered_data = data.dropna(subset=['ConvertedComp', 'Gender_encoded'])

# Calculate point-biserial correlation
correlation, p_value = pointbiserialr(filtered_data['Gender_encoded'], filtered_data['ConvertedComp'])
print(f"Point-Biserial Correlation between Gender and Converted Compensation: {correlation}")
print(f"P-value: {p_value}")

# Create a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='ConvertedComp', data=filtered_data)
plt.title('Box Plot of Converted Compensation by Gender')
plt.xlabel('Gender')
plt.ylabel('Converted Compensation')
plt.show()

# Saving results to a DataFrame
# Create a DataFrame for the five number summary of Age
age_summary_df = pd.DataFrame(list(age_five_number_summary.items()), columns=['Metric', 'Value'])

# Create a DataFrame for the correlation with Age
age_correlation_df = pd.DataFrame(age_correlation).reset_index()
age_correlation_df.columns = ['Metric', 'Value']
age_correlation_df['Metric'] = 'Correlation with Age: ' + age_correlation_df['Metric']

# Create a DataFrame with the results
results = pd.DataFrame({
    'Metric': [
        'Median Converted Compensation',
        'Number of Men',
        'Number of Women',
        'Median Converted Compensation for Women',
        'Median Converted Compensation for Men',
        'ConvertedComp IQR', 'Lower Bound', 'Upper Bound',
        'Number of Outliers',
        'Point-Biserial Correlation between Gender and Converted Compensation',
        'P-value',
        'Median Converted Compensation after removing outliers',
        'Mean Converted Compensation after removing outliers'
    ],
    'Value': [
        median_comp,
        num_men,
        num_women,
        median_comp_women,
        median_comp_men,
        iqr,
        lower_bound,
        upper_bound,
        num_outliers,
        correlation,
        p_value,
        median_comp_no_outliers,
        mean_comp_no_outliers
    ]
})

# Concatenate all results
final_results = pd.concat([results, age_summary_df, age_correlation_df], ignore_index=True)

# Save the DataFrame to an Excel file
final_results.to_excel('data_analysis_results.xlsx', index=False)

print("Results saved to 'data_analysis_results.xlsx'")



