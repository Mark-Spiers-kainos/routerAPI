from .models import Good
from user.serializer import UserSerializer
from rest_flex_fields import FlexFieldsModelSerializer


class GoodSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Good
        exclude = []

    expandable_fields = {
        'user': (UserSerializer, {})
    }
