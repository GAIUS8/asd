from django.core.management.base import BaseCommand
from django.conf import settings

from bs4 import BeautifulSoup
import requests
import datetime

from common.models import CropEnvironment
from decimal import Decimal


class Command(BaseCommand):
    def handle(self, *args, **options):
        base_url = 'http://newsky2.kma.go.kr/service/ProductingAreaInfoService/DayStats' \
                   '?ServiceKey={service_key}&' \
                   'ST_YMD={start_date}&' \
                   'ED_YMD={end_date}&' \
                   'AREA_ID={area_id}&' \
                   'PA_CROP_SPE_ID={crop_id}&' \
        
        last_date = datetime.date(year=2018, month=1, day=31)
        date = datetime.date(year=2001, month=1, day=1)
        
        print(date)
        
        prams = dict(
            service_key=settings.API_SERVICE_KEY,
            start_date='20010101',
            end_date='20010110',
            area_id='4215000002',
            crop_id='PA020101',
        )
        
        url = base_url.format(**prams)
        
        response = requests.get(url)
        print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('item')
        
        db_prams = dict()
        for daily_data in items:
            print(daily_data)
            date_local = daily_data.find('ymd').text.split(' ')[0]
            area_id = daily_data.find('areaid').text
            area_name = daily_data.find('areaname').text
            crop_id = daily_data.find('pacropspeid').text
            crop_name = daily_data.find('pacropname').text
            crop_specific = daily_data.find('pacropspename').text
            daily_temp_max = Decimal(daily_data.find('daymaxta').text)
            daily_temp_avg = Decimal(daily_data.find('dayavgta').text)
            daily_temp_min = Decimal(daily_data.find('dayminta').text)
            daily_rmh_avg = Decimal(daily_data.find('dayavgrhm').text)
            daily_rmh_min = Decimal(daily_data.find('dayminrhm').text)
            daily_precipitation = Decimal(daily_data.find('daysumrn').text)
            daily_wind_speed_avg = Decimal(daily_data.find('dayavgws').text)
            daily_accumulated_sunset = Decimal(daily_data.find('daysumss').text)
            
            db_prams.update(
                date_local=date_local,
                area_id=area_id,
                area_name=area_name,
                crop_id=crop_id,
                crop_name=crop_name,
                crop_specific=crop_specific,
                daily_temp_max=daily_temp_max,
                daily_temp_avg=daily_temp_avg,
                daily_temp_min=daily_temp_min,
                daily_rmh_avg=daily_rmh_avg,
                daily_rmh_min=daily_rmh_min,
                daily_precipitation=daily_precipitation,
                daily_wind_speed_avg=daily_wind_speed_avg,
                daily_accumulated_sunset=daily_accumulated_sunset
            )
            
            CropEnvironment.objects.get_or_create(**db_prams)