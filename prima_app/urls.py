from django.urls import path
from .views import homepage, welcome, lista
app_name="prima_app"
urlpatterns=[
    path('',homepage,name="homepage"),
    path('welcome',welcome,name="welcome"),
    path('lista',lista,name="lista")
]

