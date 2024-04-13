from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.logins, name='logins'),
    path('signup/', views.sign, name='sign'),
    path("kyrss", views.Kyrss, name='kyrss'),
    path('logout/', views.log_out, name='log_out'),
    path("user/<slug:slug>/", views.User1.as_view(), name='user'),
    path("addkyrs/<int:pk>/", views.AddKyrs.as_view(), name='addkyrs'),
]