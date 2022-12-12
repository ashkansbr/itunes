from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerizlier


class UserSerializers(BaseUserSerizlier):
    class Meta(BaseUserSerizlier.Meta):
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserCreateSerializers(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('username', 'password', 'email', 'first_name', 'last_name')