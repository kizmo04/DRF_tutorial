import json

from rest_framework.test import APILiveServerTestCase, APIRequestFactory

from snippets.views import SnippetList


class SnippetListTest(APILiveServerTestCase):
    def setUp(self):
        factory = APIRequestFactory()
        self.path = '/snippets/'
        self.request = factory.get(self.path)

    def test_get_snippet_list(self):
        view = SnippetList.as_view()
        factory = APIRequestFactory()
        url = 'http://127.0.0.1:8000/snippets/'

        request = factory.get(url)
        # response = self.client.get(url)
        response = view(request)
        response.render()
        print(response.data)