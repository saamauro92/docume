from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('explore/', views.DocPostList.as_view(), name='explore'),
    path('docs/<slug:slug>', views.DocPostDetail.as_view(), name='docpost_detail'),
    path('view-profile', views.ProfileView.as_view(), name='view_profile'),
    path('delete_docpost/<int:pk>', views.DeleteDocPost.as_view(), name='delete_docpost'),
    path('update_profile/<int:pk>', views.UpdateProfile.as_view(), name='update_profile'),
]