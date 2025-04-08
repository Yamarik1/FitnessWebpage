from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("file/", views.file_select),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/file', views.present_data, name='present_data')
    
]
