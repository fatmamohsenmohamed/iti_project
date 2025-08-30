from .views import *
from django.urls import path
url_pattern=[
    path("alltracks/",allTracks,name="alltracks"),
    path("get_track/",getTrackById,name="get_track"),
    path("updatetrack/",updateTrack,name="updatetrack"),
    path("addtrack/",addTrack,name="addtrack"),
    path("deletetrack/", deleteTrack, name="deletetrack"),
]