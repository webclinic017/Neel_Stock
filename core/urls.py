from django.urls import path
from .views import home, user_lists, user_buckets, watch_lists, delete_userlist, delete_bucket, delete_watchlist, update_userlist, update_bucket, get_ajax

app_name = 'core'

urlpatterns = [
    # dashboard
    path('', home, name='home'),
    # create and list views
    path('user_lists/', user_lists, name='user_lists'),
    path('user_buckets/', user_buckets, name='user_buckets'),
    path('watch_list/', watch_lists, name='watch_list'),
    # edit views
    path('update_user/<int:pk>/', update_userlist.as_view(), name='update_user'),
    path('update_bucket/<int:pk>/', update_bucket.as_view(), name='update_bucket'),

    # delete views
    path('delete_userlist/<int:pk>/', delete_userlist, name='delete_userlist'),
    path('delete_bucket/<int:pk>/', delete_bucket, name='delete_bucket'),
    path('delete_watchlist/<int:pk>/', delete_watchlist, name='delete_watchlist'),

    # ltp view
    path('ltp/', get_ajax, name='get_ltp'),
]
