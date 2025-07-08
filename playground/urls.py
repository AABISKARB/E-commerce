from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello) # Not calling but passing reference to this function
]