from django.core.management.base import BaseCommand
from common.models import KamisIndex


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open('kamis_index.csv', 'r')
        
        while True:
            line = f.readline()
            if not line: break
            datas = line.strip().split(',')
            KamisIndex.objects.get_or_create(
                category_name=datas[0],
                item_name=datas[1],
                kind_name=datas[2],
                quality_name=datas[3],
                category_code=datas[4],
                item_code=datas[5],
                kind_code=datas[6],
                quality_code=datas[7],
            )
            print(datas)
        f.close()
