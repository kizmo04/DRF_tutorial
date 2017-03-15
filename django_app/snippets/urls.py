from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import cbv

snippet_list = cbv.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

snippet_detail = cbv.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

snippet_highlight = cbv.SnippetViewSet.as_view({
    'get': 'highlight',
})

app_name = 'snippets'
urlpatterns = [
    url(r'^$', snippet_list, name='snippets-list'),
    url(r'^(?P<pk>[0-9]+)/$', snippet_detail, name='snippets-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippets-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
