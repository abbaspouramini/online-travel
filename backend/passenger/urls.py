from django.urls import path
from .views import PassengerList, PassengerDetail

urlpatterns = [
      path('api/create/', PassengerList.as_view()),
      path('api/<int:pk>/', PassengerDetail.as_view()),
]