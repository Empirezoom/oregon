from django.urls import path
from . import views

 
urlpatterns = [
path('',views.homepage,name='homepage'),
path('application/<str:id>/<str:slug>',views.application,name='application'),
path('payment/<str:id>/<str:slug>',views.payment,name='payment'),
path('confirmation/<str:id>/<str:slug>',views.confirmation,name='confirmation'),
path('thanks/<str:id>/<str:slug>',views.thanks,name='thanks'),
path('message',views.message,name='message'),
# path('apply',views.apply,name='apply'),

]