from . import views
from django.urls import path
urlpatterns = [
		path('helloworld/', views.myapp_hi,name ='myapp-hi'),
		path('characters/',views.myapp_characters, name='myapp-char'),
]
