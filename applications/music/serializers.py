from rest_framework import serializers

from applications.music.models import Category, Music


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'year')


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

    def to_representation(self, instance):
        representasion = super().to_representation(instance)
        representasion.pop('id')
        representasion['category'] = CategorySerializer(Category.objects.get(music=instance.id)).data
        return representasion

