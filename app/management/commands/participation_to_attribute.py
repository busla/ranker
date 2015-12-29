from django.core.management.base import BaseCommand, CommandError
from app.models import Results, Attribute, AttributeItem

class Command(BaseCommand):
    help = 'Create an atttribute from participation'


    def handle(self, *args, **options):
        #participation_attr = AttributeItem.objects.get(pk=3)        

        for result in Results.objects.exclude(category__pk__in=[6,7,9]):
            
            result.save()   
            #participation = Attribute.objects.create(result=result, attribute_item=participation_attr)
            
                        

            #participation.save()
            

            self.stdout.write('Saved attribute: %s' % result)