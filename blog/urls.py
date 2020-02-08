from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('',views.post_list, name='post_list'), # url for post_list view
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'), # url for post_detail view
]
