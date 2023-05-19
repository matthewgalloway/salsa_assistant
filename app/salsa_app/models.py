from typing import Any
from django.db import models
from .variable_utils import BASE_MOVES, HOLDS, DIFFICULTY_LEVELS, MEMORY_DIFFICULTY,default_date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, password, **extra_fields):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="salsa_app_user_set",
        related_query_name="salsa_app_user",
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="salsa_app_user_set",
        related_query_name="salsa_app_user",
        verbose_name=_('user permissions')
    )
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD='email'





class Position(models.Model):
    name = models.CharField(max_length=255)
    moves = models.ManyToManyField('Move', related_name='positions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
        
    def __str__(self):
        return self.name
    
class Move(models.Model):
    name = models.CharField(max_length=255)
    # Remove the line below
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    entry_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)
    exit_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)

    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    video_link = models.CharField(max_length=255,null=True, blank=True)
    notes = models.CharField(max_length=255,null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Combo(models.Model):
    name = models.CharField(max_length=255)
    Move = models.ManyToManyField(Move)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    video_link = models.CharField(max_length=255,null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ComboHistory(models.Model):
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, default=0)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.combo}" #{self.user}"
    
class PositionHistory(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, default=0)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.combo}" #{self.user}"
    
class MoveHistory(models.Model):
    move = models.ForeignKey(Move, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.move}" #{self.user}"

class Shine(models.Model):
    name = models.CharField(max_length=255)
    # Remove the line below
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    entry_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)
    exit_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)

    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    video_link = models.CharField(max_length=255,null=True, blank=True)
    notes = models.CharField(max_length=255,null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class ShineHistory(models.Model):
    move = models.ForeignKey(Shine, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.move}" #{self.user}"