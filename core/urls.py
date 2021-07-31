from django.urls import path
from .views import home, user_lists

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('user_lists/', user_lists, name='user_lists'),
]
