import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

##FAKE PROP script
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker
import random

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    # retrieve the topic if it already exist or else it will create one
    # [0] bceacuse of the way it is formated - it returns a tuple that contains an object and we want reference to first model instance
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top = add_topic()

        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create a Webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url =  fake_url)[0]

        # create a Access Record entry
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


if __name__ == '__main__':
    print("Populating script")
    populate(20)
