from django.shortcuts import render
from short.models import(
	URL,
	Click,
	)
from rest_framework.viewsets import(
	ViewSet,
	)
from short.serializers import(
	URLShortSerializer,
	)
from hashlib import md5
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta

class URLShortView(ViewSet):

	def create(self,request):
		full_url = request.data['full_url']
		current_site = get_current_site(request)
		md5_hash = md5(full_url.encode()).hexdigest()[:5]
		url_hash = current_site.domain + '/' + md5_hash
		serializer = URLShortSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save(url_hash = url_hash)
			return Response({
				'message': 'Short URL created',
				'url':serializer.data['url_hash']
				})
		else:
			return Response(serializer.errors)

	def list(self,request):
		queryset = URL.objects.all()
		serializer = URLShortSerializer(queryset,many=True)
		return Response(serializer.data)

class ShortURLView(APIView):

	def get(self,request,pk=None):
		current_site = get_current_site(request)
		url_hash = current_site.domain + '/' + pk
		qs = URL.objects.get(url_hash=url_hash)
		click = Click.objects.create(url_hash = qs)
		click_count = Click.objects.filter(url_hash=qs).count()
		time_threshold = datetime.now() - timedelta(hours=5)
		clicks_last_hour = Click.objects.filter(timestamp__lte = time_threshold).count()
		return Response({'total clicks':click_count,'clicks in last one hour':clicks_last_hour})

class SearchView(APIView):

	def post(self,request,format=None):
		search_term = request.data.get('search_term')
		queryset = URL.objects.filter(full_url__icontains = search_term)
		serializer = URLShortSerializer(queryset,many=True)
		return Response(serializer.data) 