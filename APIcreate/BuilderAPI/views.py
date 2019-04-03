from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class employeeList(APIView):

    def get(self, request):
        employee1= employee.objects.all()
        serializer=employeeSerializer(employee1, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer = employeeSerializer(data=request.POST)
        return Response(serializer.data)
