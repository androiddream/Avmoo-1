from django.forms import widgets
from rest_framework import serializers
from api.models import avmoo_api


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = avmoo_api
        fields = (
            'id', 'indeximg', 'titileimg', 'fanhao', 'faxingshijian', 'yingpianchangdu', 'zhizaoshang', 'faxingshang',
            'xilie', 'leibie', 'artists', 'artistsimg', 'simpleimg', 'bigsimpleimg')

