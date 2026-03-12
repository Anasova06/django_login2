from django.urls import path
from .views import home, about ,ismim, familiyam, yoshim , university      
urlpatterns =[
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('ismim/', ismim, name='ismim'),
    path('familiyam/', familiyam, name='familiyam'),
    path('yoshim/', yoshim, name='yoshim'),
    path('university/', university, name='university'),
]