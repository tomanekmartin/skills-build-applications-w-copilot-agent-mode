from rest_framework import serializers
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Workout, Leaderboard, UserProfile

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'team']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'calories']

class WorkoutSerializer(serializers.ModelSerializer):
    suggested_for = TeamSerializer(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']
