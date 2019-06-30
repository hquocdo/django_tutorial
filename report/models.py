from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Post(models.Model) :
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,blank=False)
	mark = models.IntegerField(validators=[MinValueValidator(0),
											MaxValueValidator(10)], null=True )
	def __str__ (self) :
		return self.title
class Author (models.Model) :
	name = models.CharField(max_length=255)
	birthday = models.DateField(null=True, blank=True)

	def age(self) :
		import dateime
		return int((dateime.date.today()- self.birthday).days/ 365.25)
# Create your models here.
