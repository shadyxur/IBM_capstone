#Web information scraping

import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table')

# Extract the header
headers = ['Language name', 'Created By', 'Annual average salary', 'Learning Difficulty']

# Extract the rows
rows = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    language_name = cols[1].text.strip()
    created_by = cols[2].text.strip()
    average_salary = cols[3].text.strip()
    learning_difficulty = cols[4].text.strip()
    rows.append([language_name, created_by, average_salary, learning_difficulty])

# Write the data to a CSV file
with open('popular-languages.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(rows)

print('Data has been successfully scraped and saved to popular-languages.csv')
