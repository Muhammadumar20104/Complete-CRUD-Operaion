from django.urls import path
from . import views
urlpatterns = [path('Create',views.Create),
               path('Read',views.Read),
               path("update/<str:data>",views.update)]