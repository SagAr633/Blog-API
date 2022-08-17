from rest_framework.serializers import ModelSerializer
from api.models import Blog
from rest_framework import serializers

class BlogSerializer(ModelSerializer):
    author = serializers.CharField(read_only=True)
    liked_by = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    depth = 2
    class Meta:
        model = Blog
        exclude = ('date',)

    def create(self, validated_data):
        user = self.context.get('user')
        return Blog.objects.create(**validated_data,author=user)


