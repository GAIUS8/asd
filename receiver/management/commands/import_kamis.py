import json
from pprint import pprint

from django.core.management.base import BaseCommand
from django.conf import settings

import requests


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

        params = dict()
        params.update(
            p_cert_key=settings.KAMIS_SERVICE_KEY,
            p_cert_id=settings.KAMIS_ID,
            p_productclscode='02',
            p_startday='2017-10-19',
            p_endday='2017-10-19',
            p_itemcategorycode='100',
            p_itemcode='111',
            p_kindcode='05',
            p_productrankcode='04',
        )
        
        url = base_url.format(**params)
        print(url)
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            result = response.json()
            print(len(result))
            pprint(result.get('data').get('item'))
        else:
            print(response)