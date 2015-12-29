from django.core.management.base import BaseCommand, CommandError
from app.models import *

class Command(BaseCommand):
    help = 'Set club to athlete'


    def handle(self, *args, **options):
        #participation_attr = AttributeItem.objects.get(pk=3)        
        club = Club.objects.get(pk=1)

        for athlete in Athlete.objects.all():
            athlete.club = club
            athlete.save()    
            #participation = Attribute.objects.create(result=result, attribute_item=participation_attr)
            
                        

            #participation.save()
            

            self.stdout.write('Saved athlete: %s' % athlete)