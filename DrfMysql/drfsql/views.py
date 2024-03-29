from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import StudentSerializer

from .forms import ImageUploadForm


# Create your views here.
def home(request):
    return render(request, "home.html")


# API JSON VIEW
class StudentDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            student = Student.objects.get(id=1)
            seriliazer = StudentSerializer(student)
            return render(seriliazer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student with id=1 not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# SIMPLE DATA RETRIEVE
def student_detail_view(request):
    try:
        student = Student.objects.get(id=2)
        seriliazer = StudentSerializer(student)
        return render(
            request,
            "home.html",
            {
                "firstName": seriliazer.data["firstName"],
                "lastName": seriliazer.data["lastName"],
            },
        )
    except Student.DoesNotExist:
        return render(request, "home.html", {"error": "Student with id=1 not found"})


# IMAGE UPLOAD IN ADMIN
def imageUpload(request):
    images = ImageUpload.objects.all()
    return render(request, "home.html", {"images": images})


# IMAGE UPLOAD FROM FORMS
def formUpload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("formUpload")
    else:
        form = ImageUploadForm()

    images = ImageUpload.objects.all()
    return render(request, "home.html", {"form": form, "images": images})
