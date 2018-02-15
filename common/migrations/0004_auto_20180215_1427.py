# Generated by Django 2.0.2 on 2018-02-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_kamisindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='KamisPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_local', models.DateField(blank=True, null=True)),
                ('category_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='대분류')),
                ('item_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='품명')),
                ('kind_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='세부 품명')),
                ('quality_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='등급')),
                ('category_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='대분류 코드')),
                ('item_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='품명 코드')),
                ('kind_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='세부 품명')),
                ('quality_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='등급 코드')),
                ('market_class', models.CharField(blank=True, help_text='01:retail, 02:wholesale', max_length=100, null=True, verbose_name='도소매 구분')),
                ('place_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='지역명')),
                ('market_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='시장명')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='단위당 가격')),
                ('unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='단위')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Kamis_Price_Info',
                'verbose_name_plural': 'Kamis_Price_Info',
                'db_table': 'kamis_price_info',
            },
        ),
        migrations.AlterModelOptions(
            name='kamisindex',
            options={'verbose_name': 'Kamis Index', 'verbose_name_plural': 'Kamis Index'},
        ),
        migrations.AlterIndexTogether(
            name='kamispriceinfo',
            index_together={('date_local', 'category_code', 'item_code', 'kind_code', 'quality_code')},
        ),
    ]