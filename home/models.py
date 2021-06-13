from django.db import models

# Create your models here.
from django.utils.timezone import now

class Application(models.Model):
    sno1 = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    Why_do_you_think_you_should_become_a_mod = models.TextField()
    How_long_can_you_be_active_on_the_server_everyday = models.CharField(max_length=255)
    past_experience = models.TextField()
    What_would_you_do_if_you_are_the_only_Mod_online_and_see_some_of_your_teammates_bullying_someone = models.TextField()
    What_would_you_do_if_someone_breaks_the_rules = models.TextField()
    What_would_you_do_if_someone_uses_N_word = models.TextField()
    What_would_you_do_if_someone_pinging_mods_for_no_reason = models.TextField()
    What_would_you_do_if_someone_starts_unnecessary_drama = models.TextField()

    def __str__(self):
        return f"{self.username}"