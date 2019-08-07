from .models import User
from rest_flex_fields import FlexFieldsModelSerializer


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        exclude = ['email', 'first_name', 'last_name']
