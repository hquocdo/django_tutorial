from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer) :
	class Meta :
		fields = ('id','title','content','author','mark')
		model = models.Post
	def validate_title(self,value):
		if len(value) < 5 :
			raise serializers.ValidationError("At least 5 characters")
		return value
	def validate_content(self,value) :
		if len(value) < 20 :
			raise serializers.ValidationError("At least 20 chars")
		return value