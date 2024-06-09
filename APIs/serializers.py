from rest_framework.serializers import ModelSerializer
from .models import Profile, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile(user=user)
        profile.save()
        return user


class UserSerializerforProfile(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('email',)


class ProfileSerializer(ModelSerializer):
    user = UserSerializerforProfile()

    class Meta:
        model = Profile
        exclude = ('friend_requests', 'friends',)
