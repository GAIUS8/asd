from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup

from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        base_url = 'http://newsky2.kma.go.kr/service/ProductingAreaInfoService/DayStats' \
                   '?ServiceKey={service_key}&' \
                   'ST_YMD={start_date}&' \
                   'ED_YMD={end_date}&' \
                   'AREA_ID={area_id}&' \
                   'PA_CROP_NAME={crop_name}&' \
                   'PA_CROP_SPE_ID={crop_id}&' \
                   'pageNo={page_number}&' \
                   'numOfRows={num_of_row}'
        
        prams = dict(
            service_key=settings.API_SERVICE_KEY,
            start_date='20180110',
            end_date='20180111',
            area_id='4827000001',
            crop_name='감자',
            crop_id='PA020101',
            page_number=1,
            num_of_row=10
        )
        
        url = base_url.format(**prams)
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        
        print(soup.find('dayavgws'))