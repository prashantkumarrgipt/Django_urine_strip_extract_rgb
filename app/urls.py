from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .views import show_image

urlpatterns = [
    path('', views.show_image, name="show_image"),
    path('upload-image/', show_image, name='upload_image'),
    

]


