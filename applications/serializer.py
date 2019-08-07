from rest_flex_fields import FlexFieldsModelSerializer
from good.serializer import GoodSerializer
from user.serializer import UserSerializer
from .models import Application



class ApplicationSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Application
        exclude = ['date']

    expandable_fields = {
        'goods': (GoodSerializer, {'many': True}),
        'user': (UserSerializer, {})
    }
