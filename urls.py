from django.urls import path
from CherryTest import views

urlpatterns = [
    path('index', views.show, name='index'),
    path('search',views.search,name='search')
#     path('add', views.add, name='add'),
#     path('create', views.create, name='create'),
#     path('edit', views.edit, name='edit'),
#     path('update', views.update, name='update'),
#     path('delete', views.update, name='update')
    ]