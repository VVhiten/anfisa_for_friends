from django.urls import path

from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.proposal, name='create'),
    path('list/', views.proposal_list, name='list'),
    # Добавьте сюда новые маршруты для редактирования и удаления заявок.
]