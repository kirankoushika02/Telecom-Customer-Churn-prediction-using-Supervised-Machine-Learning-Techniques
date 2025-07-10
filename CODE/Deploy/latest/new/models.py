from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    TENURE_IN_MONTHS = models.CharField(max_length=100)
    OFFERS = models.CharField(max_length=100)
    INTERNET_TYPE = models.CharField(max_length=100)
    AVERAGE_MONTHLY_GB_DOWNLOAD = models.CharField(max_length=100)
    UNLIMITED_DATA = models.CharField(max_length=100)
    CONTRACT = models.CharField(max_length=100)
    PAYMENT_METHOD = models.CharField(max_length=100)
    MONTHLY_CHARGE = models.CharField(max_length=100)
    TOTAL_CHARGES = models.CharField(max_length=100)
    TOTAL_EXTRA_DATA_CHARGES = models.CharField(max_length=100)
    Customer_Status = models.CharField(max_length=100)


def __str__(self):
    return self.TENURE_IN_MONTHS, self.OFFERS,self.INTERNET_TYPE,self.AVERAGE_MONTHLY_GB_DOWNLOAD,self.UNLIMITED_DATA,self.CONTRACT,self.PAYMENT_METHOD,self.MONTHLY_CHARGE,self.TOTAL_CHARGES,self.TOTAL_EXTRA_DATA_CHARGES

class FeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)