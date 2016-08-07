from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponseServerError
from rest_framework import viewsets
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from rest_framework.decorators import list_route
from mimoney import settings
import models, serializers
import json

# Create your views here.
def home(request):
	context = {
		"static": settings.STATIC_URL
	}
	context.update(csrf(request))

	return render(request, "login.html", context)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = []
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer

	@list_route(methods=['post'])
	def login(self, request):
		user = authenticate(username=request.data['user'], password=request.data['password'])
		if user is not None:
			# the password verified for the user
			if user.is_active:
				#print("User is valid, active and authenticated")
				return Response({'user': serializers.UserSerializer(user).data})
			else:
				#print("The password is valid, but the account has been disabled!")
				return  HttpResponseServerError(json.dumps({'title': "Cuenta deshabilitada", 'message': "Los datos son validos, pero tu cuenta no esta habilitada."}), content_type="application/json")
		else:
			# the authentication system was unable to verify the username and password
			#print("The username and password were incorrect.")
			return  HttpResponseServerError(json.dumps({'title': "Login incorrecto", 'message': "El usuario o la contrasena introducidos son incorrectos."}), content_type="application/json")

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = []
	queryset = models.Account.objects.all()
	serializer_class = serializers.AccountSerializer

	@list_route(methods=['post'])
	def getAccount(self,request):
		user = request.data['user']
		acc = models.Account.objects.get(user__id=user)
		return Response({'account': serializers.AccountSerializer(acc).data})