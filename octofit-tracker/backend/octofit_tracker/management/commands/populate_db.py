
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard, UserProfile

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Smazat existující data
        # Mazat závislé objekty jako první
        UserProfile.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Týmy
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Uživatelé

        users = []
        user_data = [
            ('ironman@marvel.com', 'ironman', marvel),
            ('captain@marvel.com', 'captain', marvel),
            ('batman@dc.com', 'batman', dc),
            ('superman@dc.com', 'superman', dc),
        ]
        for email, username, team in user_data:
            user = User(email=email, username=username)
            user.set_password('test1234')
            user.save()
            UserProfile.objects.create(user=user, team=team)
            users.append(user)

        # Aktivity
        Activity.objects.create(user=users[0], type='run', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='cycle', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='swim', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='walk', duration=20, calories=100)

        # Workouty
        Workout.objects.create(name='Morning Cardio', description='Run and cycle', suggested_for=marvel)
        Workout.objects.create(name='Strength', description='Pushups and squats', suggested_for=dc)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
