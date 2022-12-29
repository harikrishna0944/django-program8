from django.urls import path
from app2.views import *

urlpatterns=[
    path("jinja_print2/",jinja_print2,name="jinja_print2")
]