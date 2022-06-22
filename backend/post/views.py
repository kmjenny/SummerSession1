from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def ListPost(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data)
