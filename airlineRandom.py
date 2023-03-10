import random
from faker import Faker

# Create a Faker object to generate fake data
fake = Faker()

# Define the schema for the table
schema = {
    "ein": "text",
}

# Generate a random SQL query to insert data into the table
query = f"INSERT INTO airlines ({','.join(schema.keys())}) VALUES ()"
values = [f"'{fake.uuid4()}'"]
query += ','.join(values)

print(query)