from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('pharmacy', 'Pharmacy'),
        ('factory', 'Factory'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='pharmacy')
    
    # Provide unique related_name attributes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',  # Use a unique related_name
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Use a unique related_name
        related_query_name='user',
    )

    def __str__(self):
        return self.username
