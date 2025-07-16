
# from django.urls import path
# from . import views
# urlpatterns = [
    
#     path('data/',views.data,name="data"),
#     path('main/', views.mainpage, name="mainpage"),
#     path('about/', views.about, name="about"),
#     path('register/', views.register, name="register"),
#     path('login/', views.login, name="login"),
#     path('services/', views.services, name="services"),
#     path('appointment/', views.appointment, name="appointment"),
#     path('consultation/', views.consultation, name="consultation"),
#     path("persons/",views.person_list,name="person_list"),
#     path("add/",views.add_person,name="add_person"),
#     path('update/<int:pk>/', views.update_person, name='update_person'),
#     path('delete/<int:pk>/', views.delete_person, name='delete_person'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewset


router = DefaultRouter()
router.register(r'appointment',TaskViewset)

urlpatterns = [
    path('', include(router.urls)),
]


