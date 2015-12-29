from django.core.management.base import BaseCommand, CommandError
from app.models import Results, Attribute, AttributeItem

class Command(BaseCommand):
    help = 'Create an atttribute from victories and rewards'


    def handle(self, *args, **options):
        victory_attr = AttributeItem.objects.get(pk=1)
        place_attr = AttributeItem.objects.get(pk=2)

        for result in Results.objects.all():
            if result.category.pk in [1,2,3,4]:
                victory = Attribute.objects.create(result=result, value=result.victories, attribute_item=victory_attr)
                place = Attribute.objects.create(result=result, value=result.score, attribute_item=place_attr)
                            

                victory.save()
                place.save()

                self.stdout.write('Successfully created the attribute "%s"' % victory)
                self.stdout.write('Successfully created the attribute "%s"' % place)
            else:
                self.stdout.write('"%s" is not the correct category!' % result.category)                
