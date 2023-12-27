from django.urls import path
from drfsql import views
from .views import *

# change the views in the path if you want to show different views or some stuff
urlpatterns = [
    path("api/student/", StudentDetailView.as_view(), name="person-detail"),
    path("", student_detail_view, name="student_detail_view"),
]
