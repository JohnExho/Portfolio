from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    middle_name = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if self.first_name and self.last_name:
            parts = [self.first_name, self.middle_name, self.last_name]
            self.username = "_".join(p.lower() for p in parts if p)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class System(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class UserSystemRole(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('user', 'system')

    def __str__(self):
        return f"{self.user.username} - {self.system.name} ({self.role})"
