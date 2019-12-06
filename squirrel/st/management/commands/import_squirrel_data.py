# /st/management/commands/import_squirrel_data.py

import csv
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from st.models import Squirrel as sq


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args',nargs='+',type=str)
    
    def handle(self,*args,**options):
    
        if not args:
            raise CommandError ("Invalid Invocation.")
        path = args[0]
        with open(path) as f:
            reader = csv.DictReader(f)
            data = list(reader)
            for row in data:
                try:
                    s  = sq(
                        Latitude = row['Y'],
                        Longitude = row['X'],
                        S_ID = row['Unique Squirrel ID'],
                        Shift = row['Shift'],
                        Date = datetime.strptime(row['Date'],'%m%d%Y').date(),
                        Age = row['Age'],
                        Fur = row['Primary Fur Color'],
                        Location = row['Location'],
                        S_location = row['Specific Location'],
                        Run = row['Running'].capitalize(),
                        Chase = row['Chasing'].capitalize(),
                        Climb = row['Climbing'].capitalize(),
                        Eat = row['Eating'].capitalize(),
                        Forage = row['Foraging'].capitalize(),
                        Other_a = row['Other Activities'],
                        Kuks = row['Kuks'].capitalize(),
                        Quaas = row['Quaas'].capitalize(),
                        Moans = row['Moans'].capitalize(),
                        T_flag = row['Tail flags'].capitalize(),
                        T_twitch = row['Tail twitches'].capitalize(),
                        Approach = row['Approaches'].capitalize(),
                        Indifferent = row['Indifferent'].capitalize(),
                        Run_from = row['Runs from'].capitalize(),)
                    s.save()
                except:
                    print(f"Primary key collision: {row['Unique Squirrel ID']}")
            print("Import Successfully!!Congratulations!!")
