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
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                try:
                     _, created = sq.objects.get_or_create(
                        Latittude = row[0],
                        Longitude = row[1],
                        S_ID = row[2],
                        Shift = row[4],
                        Date = datetime.strptime(row[5],'%m%d%Y').date(),
                        Age = row[7],
                        Fur = row[8],
                        Location = row[12],
                        S_location = row[14],
                        Run = row[15].capitalize(),
                        Chase = row[16].capitalize(),
                        Climb = row[17].capitalize(),
                        Eat = row[18].capitalize(),
                        Forage = row[19].capitalize(),
                        Other_a = row[20],
                        Kuks = row[21].capitalize(),
                        Quaas = row[22].capitalize(),
                        Moans = row[23].capitalize(),
                        T_flag = row[24].capitalize(),
                        T_twitch = row[25].capitalize(),
                        Approach = row[26].capitalize(),
                        Indifferent = row[27].capitalize(),
                        Run_from = row[28].capitalize(),
                    )
                except:
                    print(f'Primary key collision: {row[2]}')
