import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_exercise.settings')

import django
django.setup()

from user_list_app.models import Users
from faker import Faker
import random

fakegen = Faker()

def populate(N):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        usr = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)

if __name__ == '__main__':
    print("Populating script")
    populate(10)