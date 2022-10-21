from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # на гл.стр. из файла views импортир-м ф-ю index

]
