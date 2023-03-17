from rest_framework import serializers

from category.models import Category
from .models import Post
from comment.serializers import CommentSerializer


class PostListSerializers(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'category',
                  'preview', 'owner_username', 'category_name')


class PostCreateSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'preview')


class PostDetailSerializers(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    # comments = CommentSerializer(many=True) # 1 способ

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['comments count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance=instance.comments.all(), many=True).data
        return repr # 2 способ

