from django.shortcuts import render,redirect
from .models import Track
# Create your views here.
def allTracks(request):
    alltracks = Track.objects.all()
    return render(request,'tracks/alltracks.html',{'alltracks':alltracks})
def getTrackById(request,id):
    track = Track.objects.get(id= id)
    return render(request,'tracks/track_info.html',{'track':track})
def updateTrack(request,id):
    track_to_update = Track.objects.get(id= id)
    if request.method =='POST':
        track_to_update.name = request.POST['name']
        track_to_update.save()
        return redirect("alltrackes")
    return render(request,'tracks/update.html',{'track':track_to_update})
def addTrack(request):
    if request.method == 'POST':
        track_name = request.POST.get('name')
        new_track = Track.objects.create(name=track_name) #create a new object and also save the name to the database bt3ml record gdid brdo
        return redirect('alltracks')
    return render(request, 'tracks/addtrack.html')



