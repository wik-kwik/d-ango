from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PostSerializer
 
# import the Todo model from the models file
from .models import Post

# Create your views here.

def front(request):
    context = { }
    return render(request, "index.html", context)


class PostView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = PostSerializer
 
    # define a variable and populate it
    # with the Todo list objects
    queryset = Post.objects.all()