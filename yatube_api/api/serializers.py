from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ("id", "text", "post", "author", "created")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("title",)


class PostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False
    )
    comment = CommentSerializer(many=True, required=False)
    author = serializers.StringRelatedField(read_only=True)

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
