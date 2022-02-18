from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username', 'password', 'type', 'is_active']
        # extra_kwargs = {'type': {'required': False},
        #                 'profile': {'required': False}}

    def create(self, validated_data):
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=username, email=email, password=password, is_active=False)

        return user