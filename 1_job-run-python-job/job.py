import csv
import random
import faker

# Create a Faker instance
fake = faker.Faker()

# Number of rows you want to generate
num_rows = 100

# Define the CSV file name
csv_file = 'generated_data.csv'
csv_file = os.path.join(folder_path, 'generated_data.csv')

# Generate data
data = []
for _ in range(num_rows):
    text_col1 = fake.name()
    text_col2 = fake.city()
    text_col3 = fake.company()
    num_col1 = random.randint(1, 100)  # Random integer between 1 and 100
    num_col2 = random.uniform(1.0, 100.0)  # Random float between 1.0 and 100.0
    data.append([text_col1, text_col2, text_col3, num_col1, num_col2])

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Name', 'City', 'Company', 'Integer Column', 'Float Column'])
    # Write data rows
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created with {num_rows} rows.")
