from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model) :
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__ (self) :
		return self.title
class Author (models.Model) :
	name = models.CharField(max_length=255)
	birthday = models.DateField(null=True, blank=True)

	def age(self) :
		import dateime
		return int((dateime.date.today()- self.birthday).days/ 365.25)
# Create your models here.
