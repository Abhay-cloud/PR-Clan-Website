from django.db import models
from django.utils.timezone import now

# Create your models here.
class DailyResult(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # description = models.TextField()
    desc = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130) 
    isPinned = models.BooleanField(default=False)
    timeStamp = models.DateTimeField(blank=True)
 
    def __str__(self):
        return f"{self.title}"