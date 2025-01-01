from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.urls import path
from .views import HomepageView, AboutpageView
from.views import (
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,

)

urlpatterns = [
    path('', HomepageView.as_view(), name= 'Home'),
    path('About/', AboutpageView.as_view(), name= 'About'),

    path('client/', ClientListView.as_view(), name='Client'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client/', ClientListView.as_view(), name='client_list'),

]