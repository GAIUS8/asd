import datetime
from pprint import pprint
from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from common.models import KamisIndex, KamisPriceInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        base_url = 'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&' \
                   'p_productclscode={p_productclscode}&' \
                   'p_startday={p_startday}&' \
                   'p_endday={p_endday}&' \
                   'p_itemcategorycode={p_itemcategorycode}&' \
                   'p_itemcode={p_itemcode}&' \
                   'p_kindcode={p_kindcode}&' \
                   'p_productrankcode={p_productrankcode}&' \
                   'p_countrycode=&' \
                   'p_convert_kg_yn=Y&' \
                   'p_cert_key={p_cert_key}&' \
                   'p_cert_id={p_cert_id}&' \
                   'p_returntype=json'

        market_class = '02'

        first_date = datetime.date(year=2001, month=1, day=1)
        last_date = datetime.date(year=2018, month=1, day=31)

        indexs = KamisIndex.objects.all()
        
        for index in indexs:
            category_code = index.category_code
            item_code = index.item_code
            kind_code = index.kind_code
            quality_code = index.quality_code
            category_name = index.category_name
            item_name = index.item_name
            kind_name = index.kind_name
            quality_name = index.quality_name
            
            start_date = first_date
            while start_date < last_date:
                if KamisPriceInfo.objects.filter(date_local=start_date, category_code=category_code, item_code=item_code, kind_code=kind_code, quality_code=quality_code).exists():
                    start_date = start_date + datetime.timedelta(days=1)
                    print('{}-{}-{}-{} / pass'.format(item_name, kind_name, quality_name, start_date))
                else:
                    print('{}-{}-{}-{}'.format(item_name, kind_name, quality_name, start_date))
                    
                    start_date = datetime.date(year=2018, month=1, day=5)
                    
                    end_date = start_date

                    start_date_text = start_date.strftime('%Y-%m-%d')
                    end_date_text = end_date.strftime('%Y-%m-%d')

                    params = dict()
                    params.update(
                        p_cert_key=settings.KAMIS_SERVICE_KEY,
                        p_cert_id=settings.KAMIS_ID,
                        p_productclscode=market_class,
                        p_startday=start_date_text,
                        p_endday=end_date_text,
                        p_itemcategorycode=category_code,
                        p_itemcode=item_code,
                        p_kindcode=kind_code,
                        p_productrankcode=quality_code,
                    )
        
                    url = base_url.format(**params)
                    print(url)
                    response = requests.get(url)
                    print(response)
                    if response.status_code == 200:
                        plain_text = response.json()
                        items = plain_text.get('data').get('item')
                        if items is None:
                            pass  # target 날짜에 해당하는 데이터 없음
                        else:
                            for data in items:
                                if data.get('countyname') in ['평균', '평년']:
                                    pass
                                else:
                                    pass  # create
                    else:
                        print('요청에 실패했습니다.')