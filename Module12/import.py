import psycopg2
import json

# Connect to database
conn = psycopg2.connect("dbname= user= password= ")

# Open the connection
current = conn.cursor()

# Read the JSON file
with open('JSON Filename goes here', 'r') as file:
    data = json.load(file)

# Iterate through JSON
for item in data:
    current.execute("INSERT INTO table name (colmun1, column2, column3) VALUES (%s, %s, %s)",
                    (item['column1'], item['column2'], item['column3']))
    
# Commit Changes
conn.commit()

# Close Connection
current.close()
conn.close()