from django.urls import include, path
from .views import dbCreate, dbList, dbUpdate, dbDelete


urlpatterns = [
    path('create/', dbCreate.as_view(), name='create-customer'),
    path('', dbList.as_view()),
    path('update/<int:pk>/', dbUpdate.as_view(), name='update-customer')
]
