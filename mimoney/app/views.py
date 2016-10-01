from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponseServerError
from rest_framework import viewsets
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from rest_framework.decorators import list_route
from django.db.models import Q, Sum
from django.db import transaction
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
	def getBalance(self,request):
		try:
			user = request.data['user']
			balance = dict()
			mv = models.Movement.objects.filter(user__id=user, done=False).exclude(contribution='O') | models.Movement.objects.filter(done=False).exclude(user__id=user).exclude(contribution='M')
			if mv.count() > 0:
				balance['out'] = -mv.aggregate(out=Sum('amount'))['out']
			else:
				balance['out'] = 0
			mv = models.Movement.objects.filter(user__id=user, done=False, contribution='O') | models.Movement.objects.filter(done=False, contribution='M').exclude(user__id=user)
			if mv.count() > 0:
				balance['in'] = mv.aggregate(inn=Sum('amount'))['inn']
			else:
				balance['in'] = 0
			return Response({'balance': balance})
		except Exception as e:
			return  HttpResponseServerError(json.dumps({'title': 'Error al acceder a la cuenta de usuario', 'message': str(e.message)}), content_type="application/json")

	@list_route(methods=['post'])
	def getMovements(self,request):
		try:
			user = request.data['user']
			mv = models.Movement.objects.filter(user__id=user).exclude(contribution='O') | models.Movement.objects.exclude(user__id=user).exclude(contribution='M')
			return Response({'movements': serializers.MovementSerializer(mv, many=True).data})
		except Exception as e:
			return  HttpResponseServerError(json.dumps({'title': 'Error al acceder a la cuenta de usuario', 'message': str(e.message)}), content_type="application/json")

	@list_route(methods=['post'])
	def completeMovement(self,request):
		try:
			movement = request.data['movement']
			with transaction.atomic():
				mv = models.Movement.objects.get(id=movement)
				mv.done = True
				mv.save()
				return Response({'ok': True})
		except Exception as e:
			return  HttpResponseServerError(json.dumps({'title': 'Error al acceder a la cuenta de usuario', 'message': str(e.message)}), content_type="application/json")

	@list_route(methods=['post'])
	def liquidation(self,request):
		try:
			with transaction.atomic():
				mv = models.Movement.objects.filter(done=False).update(done=True)
				return Response({'ok': True})
		except Exception as e:
			return  HttpResponseServerError(json.dumps({'title': 'Error al acceder a la cuenta de usuario', 'message': str(e.message)}), content_type="application/json")


