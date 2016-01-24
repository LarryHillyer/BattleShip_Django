from django.conf.urls import url
from . import views
from battleship.views import index

urlpatterns = [ 
    url(r'^$', index.as_view(), name='index'), 
    ]
