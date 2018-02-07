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
