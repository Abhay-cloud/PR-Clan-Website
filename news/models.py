from django.db import models

# Create your models here.
class News(models.Model):
    sno1 = models.AutoField(primary_key=True)
    headLine = models.CharField(max_length=500)

    def __str__(self):
        return f"News {self.sno1}"