import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Topic, Webpage

from faker import Faker


fake = Faker()
topics = ['Search', 'News', 'Marketplace', 'Games', 'Social']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N):
    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Creating Fake access records

        access_record = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]


if __name__ == "__main__":
    print("Populating Script")
    populate(20)
    print("Population Complete")