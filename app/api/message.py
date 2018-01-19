from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..models import Message
from ..serializers import Serializer
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .common import *


class Messages():
    """
    List all snippets, or create a new snippet.
    """
    @api_view(['POST'])
    def getsa(self):

        message = Message.objects.all()
        serializer = Serializer(message, many=True)
        response = addCrossDomainHeader(JsonResponse(serializer.data, safe=False))
        return response

    @api_view(['POST'])
    def post(self, request, format=None):
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def messages_list(request):
        """
            List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            message = Message.objects.all()
            serializer = Serializer(message, many=True)
            print(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = Serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def messages_list(request):
    """
                        List all code snippets, or create a new snippet.
                    """
    if request.method == 'GET':
        message = Message.objects.all()
        serializer = Serializer(message, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# class UserDetail(generics.RetrieveAPIView):
#     model = User
#     serializer_class = UserSerializer
#     lookup_field = 'username'
#
#
# class PostList(generics.ListCreateAPIView):
#     model = Post
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     model = Post
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#
# class UserPostList(generics.ListAPIView):
#     model = Post
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         queryset = super(UserPostList, self).get_queryset()
#         return queryset.filter(author__username=self.kwargs.get('username'))
#
#
# class PhotoList(generics.ListCreateAPIView):
#     model = Photo
#     serializer_class = PhotoSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#
# class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
#     model = Photo
#     serializer_class = PhotoSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#
# class PostPhotoList(generics.ListAPIView):
#     model = Photo
#     serializer_class = PhotoSerializer
#
#     def get_queryset(self):
#         queryset = super(PostPhotoList, self).get_queryset()
#         return queryset.filter(post__pk=self.kwargs.get('pk'))




# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#        Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)