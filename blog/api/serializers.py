from rest_framework import serializers
from blog import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'text')
        model = models.Post