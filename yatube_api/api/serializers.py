from rest_framework import serializers
from .models import CommentPost
from posts.models import Post, Group, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, required=False)

    class Meta:
        model = Comment
        fields = ("id", "text", "post", "author", "created")

    # def get_author(self, obj):
    #   return obj.author


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("title", "slug")


# class PostSerializer(serializers.ModelSerializer):
#   class Meta:
#       fields = ("id", "text", "author", "image", "pub_date")
# укажите поля, доступные только для чтения
#       author = serializers.PrimaryKeyRelatedField(read_only=True)
#      model = Post


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field="slug", queryset=Group.objects.all(), required=False
    )
    comment = CommentSerializer(many=True, required=False)
    author = serializers.StringRelatedField(read_only=True, required=False)

    class Meta:
        fields = (
            "id",
            "text",
            "author",
            "image",
            "pub_date",
            "group",
            "comment",
        )
        model = Post
