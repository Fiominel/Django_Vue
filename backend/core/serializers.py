from rest_framework import serializers
from .models import *


class FilterReviewListSerializer(serializers.ListSerializer):

  def to_representation(self, data):
    data = data.filter(parent=None)
    return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

  def to_representation(self, value):
    serializer = self.parent.parent.__class__(value, context=self.context)
    return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

  children = RecursiveSerializer(many=True)

  class Meta:
    list_serializer_class = FilterReviewListSerializer
    model = Review
    fields = ("name", "text", "children")


class DeveloperListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Developer
    fields = "__all__"


class DeveloperDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Developer
    fields = ("name", "description", "logo")


class GameListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Game
    fields = "__all__"

class GenreListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Genre
    fields = "__all__"

class PlatformListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Platform
    fields = "__all__"


class GameDetailSerializer(serializers.ModelSerializer):

  genre = GenreListSerializer(read_only=True, many=True)
  developer = DeveloperListSerializer(read_only=True, many=True)
  publisher = DeveloperListSerializer(read_only=True, many=True)
  platform = PlatformListSerializer(read_only=True, many=True)
  reviews = ReviewSerializer(many=True)

  class Meta:
    model = Game
    fields = ('id', 'title', 'description', 'genre', 'developer', 'publisher', 'platform', 'release_date', 'site', 'trailer', 'url', 'poster', 'reviews')
