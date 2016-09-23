from django.db import models


# Create your models here.
class Data(models.Model):
    CPU_usage = models.FloatField()
    SWAP_usage = models.FloatField()

    def __str__(self):
        return 'CPU: ' + self.CPU_usage.__str__() + '%, SWAP: ' + self.SWAP_usage.__str__() + '%'
