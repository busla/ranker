from django.core.management.base import BaseCommand, CommandError
from app.models import *

class Command(BaseCommand):
    help = 'Create an atttribute from victories and rewards'


    def handle(self, *args, **options):
        poomsae_attribute_item = AttributeItem.objects.get(pk=1)
        sparring_attribute_item = AttributeItem.objects.get(pk=4)
        

        #place_attr = AttributeItem.objects.get(pk=2)

        for result in Results.objects.all():
            if result.category.pk == 1:

                for attribute in result.attribute_set.all():
                    #self.stdout.write('Found victory "%s"' % attribute.attribute_item.pk)
                    #self.stdout.write('Lookup: "%s"' % poomsae_attribute_item.pk)
                    """
                    if attribute.attribute_item.pk == sparring_attribute_item.pk:
                        self.stdout.write('Found sparring "%s"' % attribute)
                    """

                    if attribute.attribute_item.pk == poomsae_attribute_item.pk:
                        self.stdout.write('Found poomsae "%s"' % attribute)
                        #won_fight = Attribute.objects.create(result=result, value=attribute.value, attribute_item=sparring_attribute_item)
                        
                        self.stdout.write('Deleting victory: "%s"' % attribute)
                        attribute.delete()
