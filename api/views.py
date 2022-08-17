from django.shortcuts import render
from api.serializers import BlogSerializer
from api.models import Blog
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action

class BlogViewSet(ModelViewSet):
    model = Blog
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    @action(["GET"],detail=True)
    def get_likes(self, request, *args, **kwargs):
        post = self.get.objects()
        data = post.liked_by.all()
        serializer = BlogSerializer(data,many=True)
        return Response(serializer.data)

    @action(["GET"],detail=True)
    def add_like(self,request, *args, **kwargs):
        user = self.request.user
        post = self.get_object(kwargs.get("pk"))
        post.liked_by.add(user)
        post.save()
        return Response({"msg":"ok"})

    @action(["GET"],detail=False)
    def all_post(self,request, *args, **kwargs):
        qs = Blog.objects.all()
        serializer = BlogSerializer(qs,many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
