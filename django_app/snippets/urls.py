from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'snippet'
urlpatterns = [
    url(r'^$', views.SnippetList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
