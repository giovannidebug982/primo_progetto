from django.urls import path
from .views import es_if, if_else_elif , es_for, index_secondo
app_name="seconda_app"
urlpatterns=[
    
    path('es_if',es_if,name="es_if"),
    path('if_else_elif',if_else_elif,name="if_else_elif"),
    path('es_for',es_for,name="es_for"),
    path('index_secondo',index_secondo,name="index_secondo"),

]