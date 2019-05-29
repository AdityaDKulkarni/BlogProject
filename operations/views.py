from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ViewSet):

	def get_queryset(self):
		queryset = Post.objects.all()
		category = self.request.query_params.get('category', None)
		if category is not None:
			queryset = queryset.filter(category=category)
		return queryset

	def list(self, request):
		queryset = Post.objects.all()
		category = self.request.query_params.get('category', None)
		if category is not None:
			queryset = queryset.filter(category=category)
			serializer = PostSerializer(queryset, many = True)
		else:
			serializer = PostSerializer(queryset, many = True)
		return Response(serializer.data)

	def retrieve(self, request, pk = None):
		queryset = Post.objects.all()
		user = get_object_or_404(queryset, pk = pk)
		serializer = PostSerializer(user)
		return Response(serializer.data)

	def post(self, request):
		serializer = PostSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = HTTP_201_CREATED)
		return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ViewSet):

	def list(self, request):
		queryset = Category.objects.all()
		serializer = CategorySerializer(queryset, many = True)
		return Response(serializer.data)

	def retrieve(self, request, pk = None):
		queryset = Category.objects.all()
		user = get_object_or_404(queryset, pk = pk)
		serializer = CategorySerializer(user)
		return Response(serializer.data)

	def post(self, request):
		serializer = CategorySerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = HTTP_201_CREATED)
		return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
