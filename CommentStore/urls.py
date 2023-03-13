from django.contrib import admin
from django.urls import include, path
from register import views

urlpatterns = [
    path('commentstore/', include('commentstoreapp.urls')),
    path('register/', include('register.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
]
