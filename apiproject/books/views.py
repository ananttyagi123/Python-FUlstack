# from django.shortcuts import render
# from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# class BookViewset(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

@api_view(['GET','POST','DELETE','PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE','PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def book_list_auth(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error":"Book not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial=True)  # <- Note partial=True
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

