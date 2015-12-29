from django.core.management.base import BaseCommand, CommandError
from app.models import ScoreItem

class Command(BaseCommand):
    help = 'Copy int field values to float field'


    def handle(self, *args, **options):
        
        for item in ScoreItem.objects.all():
            item.value = item.points
            item.save()

            self.stdout.write('Successfully copied "%s" to the values field' % item.value)