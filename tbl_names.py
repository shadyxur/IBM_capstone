#Retrieve table names

import sqlite3
import requests

# Download the database file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/Capstone_edX/Module%204/master.db"
r = requests.get(url)
with open("master.db", "wb") as f:
    f.write(r.content)

# Connect to the database
conn = sqlite3.connect("master.db")

# Create a cursor object
cursor = conn.cursor()

# Query to get the list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()

# Print the names of the tables
for table in tables:
    print(table[0])

# Close the connection
conn.close()
