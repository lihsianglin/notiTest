from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
	email = models.CharField(max_length=30)
	nickname = models.CharField(max_length=10)
	gender = models.DecimalField(max_digits=1, decimal_places=1)
	birthdate = models.DateField()

class Song(models.Model):
	singer = models.CharField(max_length=10)
	composer = models.CharField(max_length=10, blank=True)
	lyricist = models.CharField(max_length=10, blank=True)
	title = models.CharField(max_length=20)
	videoURL = models.CharField(max_length=15)
	uploadTime = models.DateTimeField(auto_now_add=True)
	viewNumber = models.DecimalField(max_digits=20, decimal_places=10)
	uploader = models.ForeignKey(User)

class Viewlist(models.Model):
	viewTimes = models.PositiveIntegerField()
	username = models.ForeignKey(User)
	song = models.ForeignKey(Song)

class Favorite(models.Model):
	username = models.ForeignKey(User)
	song = models.ForeignKey(Song)

class Follow(models.Model):
	follower = models.ForeignKey(User, related_name="follower")
	followee = models.ForeignKey(User, related_name="followee")


class Lyrics(models.Model):
	start_time = models.DecimalField(max_digits=20, decimal_places=5)
	end_time = models.DecimalField(max_digits=20, decimal_places=5)
	text = models.CharField(max_length=50)
	textCH = models.CharField(max_length=50, blank=True)
	textEN  = models.CharField(max_length=50, blank=True)
	textJP = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=50, blank=True)
	song = models.ForeignKey(Song)

class Comment(models.Model):
	content = models.TextField(blank=True)
	commentTime = models.DateTimeField(auto_now_add=True)
	username = models.ForeignKey(User)
	song = models.ForeignKey(Song)

class Rating(models.Model):
	grade = models.DecimalField(max_digits=1, decimal_places=1)
	username = models.ForeignKey(User)
	song = models.ForeignKey(Song)