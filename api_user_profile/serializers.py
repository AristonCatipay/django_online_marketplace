from rest_framework import serializers
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'location']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context['request'].user

        # Check if the old password matches the user's current password
        if not user.check_password(data.get('old_password')):
            raise serializers.ValidationError('Old password is incorrect.')

        # Check if the new password matches the confirmed new password
        if data.get('new_password') != data.get('confirm_new_password'):
            raise serializers.ValidationError('New password and confirmation do not match.')

        # Validate the new password using Django's validators
        try:
            validate_password(data.get('new_password'), user=user)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e)

        return data