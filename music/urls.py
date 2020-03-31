from django.urls import path
from .import views
app_name = 'music'
urlpatterns = [
    path('',views.IndexView.as_view(),name = 'index'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    #music/album/add
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),



]