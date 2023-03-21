from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from rest_framework import status
from .models import Student

class TestView(APIView):
    
    def get(self,request):
        if request.version == '1.0':
            
            test = "Hello World !!"
            print(request.version)
            return Response(test)
        else:
            return Response("Please Specifiy Your Version..")

class StudentView(APIView):
    # pagination_class = LimitOffsetPagination

    def get(self, request, pk, format=None):

    #user = request.user
        student = Student.objects.all()
        student1 = student.get_student_items().all()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(student1, request)
        serializer = StudentSerializer(result_page, many=True, context={'request':request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response