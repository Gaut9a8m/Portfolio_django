
from django.conf.urls import url
from . import views

urlpatterns = [
    url('< int : blog_id >/', views.detail , name='detail'),
    url('blog/', views.allblogs , name='allblogs'),
    
] 
