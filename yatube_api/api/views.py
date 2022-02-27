from urllib import response
from django.shortcuts import render

from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        super(PostViewSet, self).perform_destroy(serializer)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, serializer):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        super(CommentsViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        super(CommentsViewSet, self).perform_destroy(serializer)

    def get_queryset(self):
        # Получаем post_id
        post_id = self.kwargs.get("post_id")
        # И отбираем только нужные комментарии
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset
