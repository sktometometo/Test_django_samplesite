from django.conf import settings
from django.db import models

from datetime import datetime

# Create your models here.

class Part(models.Model):

    class Meta:
        db_table = 'partlist'

    part_name = models.CharField(
            max_length=200,
            verbose_name='部品名'
            )
    part_number = models.CharField(
            max_length=20,
            verbose_name='部品番号',
            unique=True
            )
    part_amount = models.FloatField(
            verbose_name='数量',
            default=0
            )
    part_unit = models.CharField(
            verbose_name='単位',
            max_length=200
            )
    part_place = models.CharField(
            verbose_name='保管場所',
            max_length=200
            )
    part_supplier = models.URLField(
            verbose_name='調達先',
            blank=True
            )
    part_remark = models.TextField(
            verbose_name='備考',
            blank=True
            )

    def __str__(self):
        return self.part_name


class Transaction(models.Model):

    class Meta:
        db_table = 'transactions'

    transaction_date = models.DateTimeField(
            verbose_name='日付',
            default=datetime.now
            )
    # transaction_user = models.ForeignKey(
    #         settings.AUTH_USER_MODEL,
    #         verbose_name='担当者',
    #         on_delete=models.PROTECT
    #         )
    transaction_part = models.ForeignKey(
            Part,
            on_delete = models.PROTECT,
            verbose_name='部品名'
            )
    transaction_diff = models.FloatField(
            verbose_name='変更量',
            default=0
            )
    transaction_remark = models.TextField(
            verbose_name='備考',
            blank=True
            )

    def __str__(self):
        return str(self.transaction_date) + ',' + str(self.transaction_part)
