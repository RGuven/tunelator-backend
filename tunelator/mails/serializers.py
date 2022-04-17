from rest_framework import serializers
from mails.models import UserMail
from mails.validators import UserMailAliasValidator

class UserMailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserMail
        fields = ["user", "name", "mail_user", "redirect_enabled"]

class UserMailRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMail
        fields = ["id", "name", "mail", "redirect_enabled", "plan_enabled", "created_at", "updated_at"]

mail_user_validator = UserMailAliasValidator()

class UserMailVerifySerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=25, validators=[mail_user_validator])
