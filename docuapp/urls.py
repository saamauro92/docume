from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('explore/', views.DocPostList.as_view(), name='explore'),
    path('docs/<slug:slug>', views.DocPostDetail.as_view(), name='docpost_detail'),
    path('view-profile', views.ProfileView.as_view(), name='view_profile'),
    path('public-profile/<str:username>/', views.PublicProfileView.as_view(), name='public_profile'),
    path('docs', views.ProfileDocsView.as_view(), name='docs'),
    path('delete_docpost/<int:pk>', views.DeleteDocPost.as_view(), name='delete_docpost'),
    path('update_profile/<int:pk>', views.UpdateProfile.as_view(), name='update_profile'),
    path('create_post/', views.CreateDocPost.as_view(), name='create_post'),
    path('update_docpost/<int:pk>', views.UpdateDocPost.as_view(), name='update_docpost'),
    path("docs/like/<slug:slug>", views.DocPostLike.as_view(), name="docpost_like"),
    path('add_to_favorites/<int:docpost_id>/', views.AddToFavoritesView.as_view(), name='add_to_favorites'),
    path('remove-from-favorites/<int:docpost_id>/', views.RemoveFromFavoritesView.as_view(), name='remove_from_favorites'),
    path('favourites/', views.ProfileFavouritesView.as_view(), name='favourites'),
    path('custom-login/', views.CustomLoginView.as_view(), name='custom_login'),
]