from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.myView, name='fun'),
    
    # Class Based View
    
    path('cl/', views.MyView.as_view(), name='cl'),
    path('clwn/', views.MyViewWithName.as_view(), name='clwn'),
    # path('clwn/', views.MyViewWithName.as_view(name="shivaay"), name='clwn'),
    path('child/', views.MyViewChild.as_view(), name='child'),
    
    # template url
    path('home/', views.Home.as_view(), name='home'),
    path('contactfun/', views.contact, name='contactfun'),
    path('contactcl/', views.Contact.as_view(), name='contactcl'),
    
]
