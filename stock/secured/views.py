from django.shortcuts import render

# Create your views here.

from django.http.response import Http404
# import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import User,Stocks
from .serializers import StudentSerializer,StockSerializer
from requests.auth import HTTPBasicAuth

class StudentView(APIView):

    def get_student(self, pk):
        try:
            student = User.objects.get(user_id=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = User.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Added Successfully", safe=False)
        return JsonResponse("Failed to Add User", safe=False)


    def delete(self, request, pk):
        student_to_delete = User.objects.get(user_id=pk)
        student_to_delete.delete()
        return JsonResponse("User Deleted Successfully", safe=False)


def stock():
    basic = HTTPBasicAuth('username', 'password')
    print(basic)
    username=User.objects.get(email=basic['username'])
    if username!=None and username.password==basic['pasword']:
        if username.is_admin==True:
            data=Stocks.objects.all()
            serializer = StockSerializer(data, many=True)
            return Response(serializer.data)

        elif username.group=='bulk':
            data=Stocks.objects.filter(group='bulk').all()
            serializer = StockSerializer(data, many=True)
            return Response(serializer.data)

        elif username.group=='tanker':
            data = Stocks.objects.filter(group='tanker').all()
            serializer = StockSerializer(data, many=True)
            return Response(serializer.data)

        return "There is no data in stocks right now!"

    return "username and password is incorrect"




