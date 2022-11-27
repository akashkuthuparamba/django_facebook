from . import views
from django.urls import path


urlpatterns=[
    path('login/home/',views.home),
    path('login/',views.login),
    path('',views.create),
    path('profile/<str:username>/',views.profile),
    path('profile/create/<int:id>',views.create_profile)
]