from django.core.management.base import BaseCommand
from django.conf import settings

from bs4 import BeautifulSoup
import requests
import datetime

from common.models import DataSetIndex, CropEnvironment
from decimal import Decimal


class Command(BaseCommand):
    def handle(self, *args, **options):
        base_url = 'http://newsky2.kma.go.kr/service/ProductingAreaInfoService/DayStats' \
                   '?ServiceKey={service_key}&' \
                   'ST_YMD={start_date}&' \
                   'ED_YMD={end_date}&' \
                   'AREA_ID={area_id}&' \
                   'PA_CROP_SPE_ID={crop_id}' \
        
        first_date = datetime.date(year=2001, month=1, day=1)
        last_date = datetime.date(year=2018, month=1, day=31)
        
        indexs = DataSetIndex.objects.all()
        
        for index in indexs:
            area_id = index.area_id
            crop_id = index.crop_id
            
            start_date = first_date
            while start_date < last_date:
                if CropEnvironment.objects.filter(area_id=area_id, crop_id=crop_id, date_local=start_date).exists():
                    start_date = start_date + datetime.timedelta(days=1)
                    print('{}-{}-{} / pass'.format(area_id, crop_id, start_date))
                else:
                    print('{}-{}-{}'.format(area_id, crop_id, start_date))

                    end_date = start_date + datetime.timedelta(days=9)
                    # 10개씩밖에 못 가져옴
                    start_date_text = start_date.strftime('%Y%m%d')
                    end_date_text = end_date.strftime('%Y%m%d')
                    prams = dict(
                        service_key=settings.API_SERVICE_KEY,
                        start_date=start_date_text,
                        end_date=end_date_text,
                        area_id=area_id,
                        crop_id=crop_id,
                    )
                
                    url = base_url.format(**prams)

                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    items = soup.find_all('item')
                    if len(items) == 0:
                        print('일일 트레픽 초과')
                        print(start_date)
                        print(url)
                        return
                    else:
                        self.data_saver(items=items)
                        start_date = end_date + datetime.timedelta(days=1)
                    
    def data_saver(self, items):
        """
        DB에 저장
        :param items: xml element
        :return:
        """
        db_prams = dict()
        for daily_data in items:
            if daily_data is not None:
                date_local = daily_data.find('ymd').text.split(' ')[0]
                area_id = daily_data.find('areaid').text
                area_name = daily_data.find('areaname').text
                crop_id = daily_data.find('pacropspeid').text
                crop_name = daily_data.find('pacropname').text
                crop_specific = daily_data.find('pacropspename').text
                try:
                    daily_temp_max = Decimal(daily_data.find('daymaxta').text)
                except AttributeError:
                    daily_temp_max = 0
                
                try:
                    daily_temp_avg = Decimal(daily_data.find('dayavgta').text)
                except AttributeError:
                    daily_temp_avg = 0
                
                try:
                    daily_temp_min = Decimal(daily_data.find('dayminta').text)
                except AttributeError:
                    daily_temp_min = 0
                
                try:
                    daily_rmh_avg = Decimal(daily_data.find('dayavgrhm').text)
                except AttributeError:
                    daily_rmh_avg = 0
                
                try:
                    daily_rmh_min = Decimal(daily_data.find('dayminrhm').text)
                except AttributeError:
                    daily_rmh_min = 0
                
                try:
                    daily_precipitation = Decimal(daily_data.find('daysumrn').text)
                except AttributeError:
                    daily_precipitation = 0
                
                try:
                    daily_wind_speed_avg = Decimal(daily_data.find('dayavgws').text)
                except AttributeError:
                    daily_wind_speed_avg = 0
                
                try:
                    daily_accumulated_sunset = Decimal(daily_data.find('daysumss').text)
                except AttributeError:
                    daily_accumulated_sunset = 0
                
                
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
            else:
                print('{} data error'.format(items))
            
        return None
