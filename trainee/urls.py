
from .views import alltrainee, updateTrainee,insertTrainee,deleteTrainee
from django.urls import path


urlpatterns = [
    path("alltrainees/", alltrainee,name="alltrainees"),
    path('Update/<int:id>/',updateTrainee,name="updatetrainee"),
    path('delete/<int:id>/', deleteTrainee, name="deletetrainee"),
    path('Insert/',insertTrainee,name='inserttrainee'),
    # path("register/", views.register, name="login"),







]
