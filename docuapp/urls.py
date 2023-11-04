from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name="home" ),
    path('explore/', views.DocPostList.as_view(), name='explore'),

]