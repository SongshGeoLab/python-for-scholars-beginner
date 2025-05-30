#!/usr/bin/env python3
"""
Generate two CSV files with fake user data using the Faker package.
"""

import csv
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_users1_csv(filename, num_records=100):
    """
    Generate a CSV file with username, age, address, email, and occupation.
    
    Args:
        filename (str): Path to save the CSV file
        num_records (int): Number of records to generate
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['username', 'age', 'address', 'email', 'occupation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'username': fake.user_name(),
                'age': random.randint(18, 80),
                'address': fake.address().replace('\n', ', '),
                'email': fake.email(),
                'occupation': fake.job()
            })
    
    print(f"Generated {num_records} records in {filename}")

def generate_users2_csv(filename, num_records=100):
    """
    Generate a CSV file with username, age, address, phone_number, and date_of_birth.
    
    Args:
        filename (str): Path to save the CSV file
        num_records (int): Number of records to generate
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['username', 'age', 'address', 'phone_number', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for _ in range(num_records):
            age = random.randint(18, 80)
            # Calculate birth date based on age
            birth_date = fake.date_of_birth(minimum_age=age, maximum_age=age)
            
            writer.writerow({
                'username': fake.user_name(),
                'age': age,
                'address': fake.address().replace('\n', ', '),
                'phone_number': fake.phone_number(),
                'date_of_birth': birth_date.strftime('%Y-%m-%d')
            })
    
    print(f"Generated {num_records} records in {filename}")

def main():
    """Main function to generate both CSV files."""
    users1_file = 'users1.csv'
    users2_file = 'users2.csv'
    
    print("Generating fake user data...")
    generate_users1_csv(users1_file)
    generate_users2_csv(users2_file)
    print("Done!")

if __name__ == "__main__":
    main()

