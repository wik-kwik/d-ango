# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import Post
 
# create a serializer class
class PostSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Post
        fields = ("title", "slug", "text", "imgOne", "imgTwo", "created_on")