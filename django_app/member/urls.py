from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
