from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer) :
	class Meta :
		fields = ('id','title','content','date_posted',)
		model = models.Post