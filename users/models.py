from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string


class CustomUser(AbstractUser):
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def generate_confirmation_code(self):
        return ''.join(random.choices(string.digits, k=6))


CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_set'


