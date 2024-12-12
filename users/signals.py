from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

## we are doing this to create profile for every new user
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()



@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    #instance.profile.save()
    try:
        instance.profile.save()  # This will save the profile without force_insert
    except Profile.DoesNotExist:
        # In case the profile doesn't exist yet
        profile = Profile(user=instance)
        profile.save()
