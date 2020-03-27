import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj_two.settings')

import django
django.setup()

from app_two.models import User
from faker import Faker
import random

f = Faker()
# print(f.first_name())

def populate(N=10):

    # for a in range(N):

    fake_fname = f.first_name()
    fake_lname = f.last_name()
    fake_email = f.email()

    info = User.objects.get_or_create(fname = fake_fname , lname = fake_lname, emails = fake_email)[0]



if __name__ == '__main__':
    print("Filling Data !!")
    populate(20)
    print("Filling Done")
