from django.core.management.base import BaseCommand
from common.models import DataSetIndex

class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open('data_index.txt', 'r')
        
        while True:
            line = f.readline()
            if not line: break
            informations = line.strip().split(' ')
            DataSetIndex.objects.get_or_create(
                area_id=informations[0],
                area_name=informations[1],
                crop_id=informations[2],
                crop_name=informations[3],
                crop_specific=informations[4],
            )
            print(informations)
        f.close()
