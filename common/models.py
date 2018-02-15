from django.db import models


class DataSetIndex(models.Model):
    area_id = models.CharField(max_length=100, blank=True, null=True)
    area_name = models.CharField(max_length=100, blank=True, null=True)
    crop_id = models.CharField(max_length=100, blank=True, null=True)
    crop_name = models.CharField(max_length=100, blank=True, null=True)
    crop_specific = models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'dataset_index'
        verbose_name = 'Data Index'
        verbose_name_plural = verbose_name


class CropEnvironment(models.Model):
    date_local = models.DateField(blank=True, null=True)
    area_id = models.CharField(max_length=100, blank=True, null=True)
    area_name = models.CharField(max_length=100, blank=True, null=True)
    crop_id = models.CharField(max_length=100, blank=True, null=True)
    crop_name = models.CharField(max_length=100, blank=True, null=True)
    crop_specific = models.CharField(max_length=100, blank=True, null=True)
    daily_temp_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 최고기온')
    daily_temp_avg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 평균기온')
    daily_temp_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 최저기온')
    daily_rmh_avg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 평균 상대습도')
    daily_rmh_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 최저 상대습도')
    daily_precipitation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 강수량')
    daily_wind_speed_avg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 평균 풍속')
    daily_accumulated_sunset = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='일 누적 일조시간')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'crop_environment'
        verbose_name = '작물별 환경'
        verbose_name_plural = verbose_name
        
        index_together = ['date_local', 'area_id', 'crop_id']
        

class KamisIndex(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    kind_name = models.CharField(max_length=100, blank=True, null=True)
    quality_name = models.CharField(max_length=100, blank=True, null=True)
    category_code = models.CharField(max_length=100, blank=True, null=True)
    item_code = models.CharField(max_length=100, blank=True, null=True)
    kind_code = models.CharField(max_length=100, blank=True, null=True)
    quality_code = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'kamis_index'
        verbose_name = 'Kamis Index'
        verbose_name_plural = verbose_name


class KamisPriceInfo(models.Model):
    date_local = models.DateField(blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='대분류')
    item_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='품명')
    kind_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='세부 품명')
    quality_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='등급')
    category_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='대분류 코드')
    item_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='품명 코드')
    kind_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='세부 품명')
    quality_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='등급 코드')
    market_class = models.CharField(max_length=100, blank=True, null=True, verbose_name='도소매 구분', help_text='01:retail, 02:wholesale')
    place_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='지역명')
    market_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='시장명')
    
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, verbose_name='단위당 가격')
    unit = models.CharField(max_length=100, blank=True, null=True, verbose_name='단위')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'kamis_price_info'
        verbose_name = 'Kamis_Price_Info'
        verbose_name_plural = verbose_name
    
        index_together = ['date_local', 'category_code', 'item_code', 'kind_code', 'quality_code']