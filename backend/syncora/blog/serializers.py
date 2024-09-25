from rest_framework import serializers
from .models import Post
from departments.serializers import DepartmentSerializer

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    department = DepartmentSerializer()  # Nested department serializer

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'created_at', 'department', 'is_published']
