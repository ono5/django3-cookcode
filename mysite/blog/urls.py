from django.urls import path
from . import views

# application namespace
app_name = 'blog'

# https://docs.djangoproject.com/en/3.0/topics/http/urls/#path-converters
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
