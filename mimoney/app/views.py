from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from rest_framework.decorators import list_route
from mimoney import settings
import models, serializers

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
				return Response({'user': "The password is valid, but the account has been disabled!"})
		else:
			# the authentication system was unable to verify the username and password
			#print("The username and password were incorrect.")
			return Response({'user': "The username and password were incorrect."})
