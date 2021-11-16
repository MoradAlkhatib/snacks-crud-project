from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('',SnackListView.as_view(),name='all'),
    path('<int:pk>/',SnackDetailView.as_view(),name='details'),
    path('create/',SnackCreateView.as_view(),name='create'),
    path('<int:pk>/update/',SnackUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(),name='delete'),

]