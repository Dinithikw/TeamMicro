from django.db import models

# Create your models here.
class Kyc_Info(models.Model):
    full_name = models.CharField(max_length=200)
    name_init = models.CharField(max_length=100)
    id_type = models.CharField(max_length=50)
    nics_no = models.CharField(max_length=50)

    """company_name = models.CharField(max_length=50)
    address_full = models.CharField(max_length=250)
    email_add = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=12)
    long_text = models.TextField(max_length=255)"""


    def __str__(self):
        return self.full_name