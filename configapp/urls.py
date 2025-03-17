from django.urls import path, include
from configapp.views import *

urlpatterns = [
    path('index/', index, name='home'),
    path('category/<int:category_id>/', category_new, name='category_new'),
    path('', loginPage, name='login'),
    path('add-news/', add_news, name='add_news'),
    path('/delete/<int:news_id>/', delete_news, name='delete_news'),
]