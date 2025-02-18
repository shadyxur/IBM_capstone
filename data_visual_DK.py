#Data visualization 

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Download the database file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/Capstone_edX/Module%204/master.db"
r = requests.get(url)
with open("master.db", "wb") as f:
    f.write(r.content)

# Connect to the database
conn = sqlite3.connect("master.db")

# Read data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM master", conn)

# Plot a histogram of 'ConvertedComp' column
plt.figure(figsize=(10, 6))
sns.histplot(df['ConvertedComp'].dropna(), kde=True)
plt.title('Histogram of recieved Compensation')
plt.xlabel('Converted compensation (USD)')
plt.ylabel('Frequency')
plt.show()

# Plot a box plot of 'Age'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Age'].dropna())
plt.title('Box Plot of Age')
plt.xlabel('Age')
plt.show()

# Create a scatter plot of 'Age' and 'WorkWeekHrs'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='WorkWeekHrs', data=df)
plt.title('Scatter Plot of Age and Working hours')
plt.xlabel('Age')
plt.ylabel('How many hours do you work in a week')
plt.show()

# Create a bubble plot of 'WorkWeekHrs' and 'Age', use 'Age' column as bubble size
plt.figure(figsize=(10, 6))
sns.scatterplot(x='WorkWeekHrs', y='Age', size='Age', sizes=(20, 200), data=df)
plt.title('Bubble Plot of Working hours and Age')
plt.xlabel('How many hours do you work in a week')
plt.ylabel('Age')
plt.show()

# Create a pie chart of the top 5 Countries
top_5_countries = df['Country'].value_counts().nlargest(5)
plt.figure(figsize=(10, 6))
top_5_countries.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Countries in the Survey')
plt.ylabel('')
plt.show()

# Draw distribution plot for 'ConvertedComp' and plot the median
plt.figure(figsize=(10, 6))
sns.histplot(df['ConvertedComp'].dropna(), kde=True)
plt.axvline(df['ConvertedComp'].median(), color='r', linestyle='--', label='Median')
plt.title('Distribution Plot of Compensation with Median')
plt.xlabel('Converted compensation (USD)')
plt.ylabel('Density')
plt.legend()
plt.show()

# Create a horizontal bar chart using column 'MainBranch'
plt.figure(figsize=(10, 6))
df['MainBranch'].value_counts().plot.barh()
plt.title('Horizontal Bar Chart of the Nature of the job')
plt.xlabel('Number of responses')
plt.ylabel('Is programming your main job?')

# Adjust the layout to make sure the labels fit
plt.tight_layout()

plt.show()

# Close the database connection
conn.close()
