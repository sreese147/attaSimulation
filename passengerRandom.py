import random
from faker import Faker

# Create a Faker object to generate fake data
fake = Faker()

# Define the schema for the table
schema = {
    "id": "text",
    "ff_number": "text",
    "first_name": "text",
    "last_name": "text",
    "gender": "text",
    "nationality": "text",
    "no_fly_status": "text"
}

# Generate a random SQL query to insert data into the table
query = f"INSERT INTO passengers ({','.join(schema.keys())}) VALUES ()"
values = [f"'{fake.uuid4()}'", f"'{fake.uuid4()}'", f"'{fake.first_name()}'", f"'{fake.last_name()}'", f"'{random.choice(['M', 'F'])}'", f"'{fake.country()}'", f"'{random.choice(['Yes', 'No'])}')"]
query += ','.join(values)

print(query)