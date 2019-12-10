from django.urls import path
from .views import HomePageView, AddDogView, EidtDogView, DeleteDogView
from . import views
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('addDog', AddDogView.as_view(), name="addDog"),
    path('<int:pk>/editDog', EidtDogView.as_view(), name="editDog"),
    path('<int:pk>/deleteDog', DeleteDogView.as_view(), name="deleteDog"),
    path('<int:dog_id>/', views.detail, name='detail'),
    path('<int:dog_id>/like', views.like, name='like'),
]