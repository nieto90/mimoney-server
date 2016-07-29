from django.shortcuts import render
from rest_framework import viewsets
from django.core.context_processors import csrf
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
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		# if user is not None:
		# 	# the password verified for the user
		# 	if user.is_active:
		# 		#print("User is valid, active and authenticated")

		# 	else:
		# 		#print("The password is valid, but the account has been disabled!")
		# else:
		# 	# the authentication system was unable to verify the username and password
		# 	#print("The username and password were incorrect.")
		return Response({'LOGIN': 'OK'})