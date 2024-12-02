from django.db import models

# Create your models here.
class Exchange(models.Model):
    cur_unit = models.CharField(max_length=100)
    cur_nm = models.CharField(max_length=100)
    ttb = models.CharField(max_length=100)
    tts = models.CharField(max_length=100)
    deal_bas_r = models.CharField(max_length=100)
    bkpr = models.CharField(max_length=100)
    yy_efee_r = models.CharField(max_length=100)
    ten_dd_efee_r =models.CharField(max_length=100)
    kftc_deal_bas_r = models.CharField(max_length=100)
    kftc_bkpr = models.CharField(max_length=100)
    sell=models.FloatField(default=-1)
    buy=models.FloatField(default=-1)
    date=models.DateField(auto_now_add=True)