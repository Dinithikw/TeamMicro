from django.db import models
from datetime import datetime, date


# Create your models here.
class Kyc_Info(models.Model):
    full_name = models.CharField(max_length=200)
    name_init = models.CharField(max_length=100)
    id_type = models.CharField(max_length=50)
    nics_no = models.CharField(max_length=50)
    driv_lic = models.CharField(max_length=50)
    driv_exp = models.CharField(max_length=20)
    pass_no = models.CharField(max_length=50)
    pass_exp = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    nationality_other = models.CharField(max_length=50)
    date_of_birth = models.DateField('%Y-%m-%d')
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    #country = models.CharField(max_length=20)
    mob_no = models.CharField(max_length=20)
    office_num = models.CharField(max_length=20)
    home_num = models.CharField(max_length=20)
    email_add = models.CharField(max_length=50)
    occu_state = models.CharField(max_length=50)




    """company_name = models.CharField(max_length=50)
    address_full = models.CharField(max_length=250)
    email_add = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=12)
    long_text = models.TextField(max_length=255)"""


    def __str__(self):
        return self.full_name

class Kyc_Infotemp(models.Model):
    full_name_temp = models.CharField(max_length=200)
    name_init_temp = models.CharField(max_length=100)
    id_type_temp = models.CharField(max_length=50)
    nics_no_temp = models.CharField(max_length=50)
    driv_lic_temp = models.CharField(max_length=50)
    driv_exp_temp = models.CharField(max_length=20)
    pass_no_temp = models.CharField(max_length=50)
    pass_exp_temp = models.CharField(max_length=20)
    nationality_temp = models.CharField(max_length=50)
    nationality_other_temp = models.CharField(max_length=50)
    date_of_birth_temp = models.DateField('%Y-%m-%d')
    house_no_temp = models.CharField(max_length=20)
    street_temp = models.CharField(max_length=20)
    city_temp = models.CharField(max_length=20)
    #country_temp = models.CharField(max_length=20)
    mob_no_temp = models.CharField(max_length=20)
    office_num_temp = models.CharField(max_length=20)
    home_num_temp = models.CharField(max_length=20)
    email_add_temp = models.CharField(max_length=50)
    occu_state_temp = models.CharField(max_length=50)
    id_red_flag_temp = models.BooleanField(default=False)
    idname_blue_flag_temp = models.BooleanField(default=False)
    iddob_blue_flag_temp = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name_temp

class Id_Info(models.Model):
    nic_no = models.CharField(max_length=50)
    name_full = models.CharField(max_length=100)
    birth_day = models.DateField('%Y-%m-%d')
    house_num = models.CharField(max_length=20)
    street_add = models.CharField(max_length=20)
    city_ref = models.CharField(max_length=20)

    def __str__(self):
        return self.name_full