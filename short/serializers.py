from rest_framework.serializers import(
    ModelSerializer,
    ValidationError,
    )

from short.models import(
	URL,
	)

class URLShortSerializer(ModelSerializer):
	class Meta:
		model = URL
		fields = '__all__'