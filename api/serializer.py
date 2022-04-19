from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    customer_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'password', 'customer_id')
        extra_kwargs = {'password': {'write_only': True}}

    def get_customer_id(self, obj):
        customer_id = self.context["customer_id"]
        return customer_id

    def create(self, validated_data):
        customer_id = self.context.get('customer_id')
        return User.objects.create(email=validated_data['email'], password=validated_data['password'],
                                   customer_id=customer_id)
