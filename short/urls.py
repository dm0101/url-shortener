from rest_framework.routers import DefaultRouter
from short.views import(
	URLShortView,
	ShortURLView,
	SearchView,
	)
from django.urls import path

app_name = 'short'

router = DefaultRouter()
router.register('short',URLShortView,basename='short')

urlpatterns = [
	path('<str:pk>',ShortURLView.as_view(), name='short-url'),
	path('search/',SearchView.as_view(), name='search'),
]

urlpatterns += router.urls