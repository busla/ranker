from django.core.management.base import BaseCommand, CommandError
from app.models import Results, Attribute

class Command(BaseCommand):
    help = 'Create an atttribute from victories'


    def handle(self, *args, **options):
        for result in Results.objects.all():

            a1 = Attribute(results=result, value=result.victories)
            a2 = Attribute(results=result, value=result.score)
            a1.save()
            a2.save()
                        
            a1.tags.add('victories')
            a2.tags.add('place')


            self.stdout.write('Successfully created the attribute "%s"' % a1)
            self.stdout.write('Successfully created the attribute "%s"' % a2)