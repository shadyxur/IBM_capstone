#Collecting job data using API

#Import required libraries
import pandas as pd
import requests

#access data using API url
api_url = "http://127.0.0.1:5000/data"

# List of locations and technologies
locations = ["Los Angeles", "New York", "San Francisco", "Washington DC", "Seattle", "Austin", "Detroit"]
technologies = ['C', 'C++', 'Java', 'C#', 'Python', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB', 'JavaScript']

def get_number_of_jobs(location, technology):
    response = requests.get(api_url, params={"Location": location, "Key Skills": technology})
    data = response.json()
    return len(data)

results = {}

# Collect number of jobs for each technology in each location
for location in locations:
    results[location] = {}
    for tech in technologies:
        num_jobs = get_number_of_jobs(location, tech)
        results[location][tech] = num_jobs

# Create a DataFrame from the results
df = pd.DataFrame(results).transpose()

# Save the DataFrame to an Excel file
df.to_excel("job-postings.xlsx", sheet_name="Job Postings")

# Print the results
print("Results saved to job-postings.xlsx")





