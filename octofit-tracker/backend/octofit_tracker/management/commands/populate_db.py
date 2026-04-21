from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		# Delete children before parents to avoid Djongo PK issues

		# Use pymongo to drop collections directly
		from django.db import connections
		db = connections['default'].connection
		if db:
			db.drop_collection('octofit_tracker_activity')
			db.drop_collection('octofit_tracker_leaderboard')
			db.drop_collection('octofit_tracker_workout')
			db.drop_collection('octofit_tracker_user')
			db.drop_collection('octofit_tracker_team')

		# Create Teams
		marvel = Team.objects.create(name='Marvel')
		dc = Team.objects.create(name='DC')

		# Create Users
		spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
		ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
		wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
		batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

		# Create Workouts
		run = Workout.objects.create(name='Running', description='Run at a steady pace')
		swim = Workout.objects.create(name='Swimming', description='Swim laps in the pool')
		lift = Workout.objects.create(name='Weight Lifting', description='Strength training')

		# Create Activities
		Activity.objects.create(user=spiderman, workout=run, duration=30, date=date.today())
		Activity.objects.create(user=ironman, workout=swim, duration=45, date=date.today())
		Activity.objects.create(user=wonderwoman, workout=lift, duration=60, date=date.today())
		Activity.objects.create(user=batman, workout=run, duration=25, date=date.today())

		# Create Leaderboard
		Leaderboard.objects.create(team=marvel, points=75)
		Leaderboard.objects.create(team=dc, points=85)

		self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
