# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewset


# router = DefaultRouter()
# router.register(r'books',BookViewset)


# urlpatterns =  [
#     path('',include(router.urls)),
# ] 

from django.urls import path
from .views import book_list_create , book_list_auth

urlpatterns = [
    path('books/', book_list_create, name='book-list-create'),
    path('bookauth/<int:pk>', book_list_auth, name='book_list_auth'),
]