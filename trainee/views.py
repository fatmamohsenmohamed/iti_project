from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def alltrainee(request):
    trainees = Trainee.objects.all().order_by("id")
    return render(request,'alltrainees.html',{'trainees':trainees})


def updateTrainee(request):
    trainee = Trainee.objects.get(id=request.POST.get("id"))  # get trainee by id

    if request.method == "POST":
        trainee.name = request.POST.get("trname")
        trainee.email = request.POST.get("tremail")
        if request.FILES.get("trimage"):
            trainee.image = request.FILES.get("trimage")
        trainee.save()
        return redirect("alltrainees")
    context = {"trainee_info": trainee}
    return render(request, "update.html", context)
def insertTrainee(request):
    if request.method == "POST":
        trainee_name = request.POST.get("trname")
        trainee_email = request.POST.get("tremail")
        trainee_image = request.FILES.get("trimage") if request.FILES.get("trimage") else None

        new_trainee = Trainee(
            name=trainee_name,
            email=trainee_email,
            image=trainee_image
        )
        new_trainee.save() #kda b insert new record in the database

        return redirect("alltrainees")
    return render(request, 'trainee/insert.html')

def deleteTrainee(request):
    Trainee.objects.filter(id=request.POST.get("id")).update(status=False)
    return redirect('alltrainee')









