from django.core.management.base import BaseCommand
from monitor.models import CrowdData

class Command(BaseCommand):
    help = 'Delete all data from CrowdData'

    def handle(self, *args, **kwargs):
        CrowdData.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all data from CrowdData'))
