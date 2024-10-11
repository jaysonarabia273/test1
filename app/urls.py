from django.urls import path
from .views import HomepageView, AboutpageView


urlpatterns = [
    path('', HomepageView.as_view(), name= 'Home'),
    path('About/', AboutpageView.as_view(), name= 'About'),
]