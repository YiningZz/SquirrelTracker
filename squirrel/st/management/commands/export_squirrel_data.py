# st/management/commands/export_squirrel_data.py

from django.core.management.base import BaseCommand, CommandError
from st.models import Squirrel as sq

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('args',nargs='+',type=str)

    #getattr(instance, field.name)
    
    def handle(self,*args,**options):
        if not args:
            raise CommandError("Invalid Innovation.")

        path = args[0]
        fields = sq._meta.fields 

        with open(path,'w',newline='') as f:
            for obj in sq.objects.all():
                row = ""
                for field in fields:
                    # print(getattr(obj, field.name))
                    row += str(getattr(obj, field.name))+',' 
                    #print(row)
                print(row,file=f)

        f.close()
