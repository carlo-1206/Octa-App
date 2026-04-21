from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard
from datetime import date

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=10, date=date.today())
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.duration, 10)
        self.assertEqual(self.activity.user, self.user)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
        self.assertEqual(self.leaderboard.team, self.team)
