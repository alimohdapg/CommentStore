from django.urls import path
from . import views

urlpatterns = [
    path('comment_list/', views.comment_list, name="comment_list"),
    path('add_comment/', views.add_comment, name="add_comment"),
]
