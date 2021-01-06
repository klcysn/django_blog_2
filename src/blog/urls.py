from django.urls import path
from .views import post_list, post_create, post_detail

app_name = "blog"
urlpatterns = [
    path('', post_list, name="post-list" ),
    path('create/', post_create, name="create" ),
    path('<slug:slug>/', post_detail, name="detail" ),
]