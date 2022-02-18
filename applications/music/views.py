from rest_framework import generics
from applications.music.models import Music
from applications.music.serializers import MusicSerializer


class MusiclistView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
