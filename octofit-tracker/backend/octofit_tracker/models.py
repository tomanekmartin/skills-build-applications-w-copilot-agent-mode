
from djongo import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    calories = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ForeignKey(Team, on_delete=models.CASCADE)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
