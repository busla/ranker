from django.core.management.base import BaseCommand, CommandError
from app.models import *

class Command(BaseCommand):
    help = 'Set club to result'


    def handle(self, *args, **options):
        #participation_attr = AttributeItem.objects.get(pk=3)        
        club = Club.objects.get(pk=1)

        for result in Results.objects.all():
            result.athlete_club = club
            result.save()    
            #participation = Attribute.objects.create(result=result, attribute_item=participation_attr)
            
                        

            #participation.save()
            

            self.stdout.write('Saved result: %s' % result)