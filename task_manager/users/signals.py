from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser, UserProfile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        logger.info(f"Creating profile for user: {instance.username}")