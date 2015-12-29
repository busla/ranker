from django.core.management.base import BaseCommand, CommandError
from app.models import Results, Attribute, AttributeItem

class Command(BaseCommand):
    help = 'Delete participation results'


    def handle(self, *args, **options):
        #participation_attr = AttributeItem.objects.get(pk=3)        

        for result in Results.objects.filter(category__pk__in=[6,7]):
            self.stdout.write('Deleting results: %s' % result)
            result.delete()   
            #participation = Attribute.objects.create(result=result, attribute_item=participation_attr)
            
                        

            #participation.save()
            

            