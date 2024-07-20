import os
import django

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arun_redis.settings')

# Initialize Django
django.setup()

from redis_app.models import EmployeesData
from faker import Faker
import random


roles = ['developer', 'tester', 'accountant',
         'sales', 'marketing', 'hr', 'manager', 'tl']
salary_amt = [30000, 35000, 40000, 50000, 55000, 60000]


def generate_mobile_no():
    start_digits = random.randint(7,9)
    mobile_no = f"{start_digits}{random.randint(100000000, 999999999)}"
    return mobile_no

def populate_employees(n):
    fake = Faker()
    for _ in range(n):
        name = fake.name()
        role = random.choice(roles)
        mobile = generate_mobile_no()
        city = fake.city()
        salary = random.choice(salary_amt)
        joined_date = fake.date_time()
        EmployeesData.objects.create(
            name=name, role=role, mobile=mobile, city=city, salary=salary, joined_date=joined_date
        )


if __name__ == "__main__":
    populate_employees(1000)  # Change the number to add more or fewer records
