from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet

User = get_user_model()


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    detail = serializers.HyperlinkedIdentityField(
        view_name='snippets:snippet_detail',
    )
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippets:snippet_highlight',
        format='html'
    )

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'highlight', 'linenos', 'language', 'style', 'owner', 'detail')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
