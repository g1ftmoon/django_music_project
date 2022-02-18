from django.urls import path
from applications.music.views import MusiclistView

urlpatterns = [
    path('music-list/', MusiclistView.as_view()),
]
