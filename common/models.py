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