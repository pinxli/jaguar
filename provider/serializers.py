from rest_framework import serializers
from provider.models import Provider
from gametype.models import GameType
from gametype.serializers import GameTypeSerializer


class ProviderSerializer(serializers.ModelSerializer):
    '''
    @class ProviderSerializer
    @brief
        Serializer class for Provider
    '''

    def __init__(self, *args, **kwargs):
        '''
        '''

        super(ProviderSerializer, self).__init__(*args, **kwargs)
        if 'request' in self.context:
            opt_fields = self.context['request'].query_params.get('opt_fields')
            if opt_fields:
                opt_fields = opt_fields.split(',')
                # Remove not specified fields
                to_show = set(opt_fields)
                default = set(self.fields.keys())
                for field in default - to_show:
                    self.fields.pop(field)

    provider = serializers.IntegerField(source='id')
    name = serializers.CharField(max_length=255)
    status = serializers.IntegerField(default=1)
    gametypes = GameTypeSerializer(many=True)

    class Meta:
        model = Provider
        fields = ('provider', 'name', 'status', 'gametypes')
