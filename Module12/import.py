import psycopg2
import json

# Connect to database
conn = psycopg2.connect("dbname=penguins user=postgres password=postgres")

# Open the connection
current = conn.cursor()

# Read the JSON file
with open('output.json', 'r') as file:
    data = json.load(file)

# Iterate through JSON
for item in data:
    current.execute("INSERT INTO penguins (name, number, position) VALUES (%s, %s, %s)",
                    (item['name'], item['number'], item['position']))
    
# Commit Changes
conn.commit()

# Close Connection
current.close()
conn.close()