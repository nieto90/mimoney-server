from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)
# router.register(r'provinces', views.ProvincesViewSet)
# router.register(r'category', views.CategoryViewSet)
# router.register(r'question', views.QuestionViewSet)
# router.register(r'stage', views.StageViewSet)
# router.register(r'round', views.RoundViewSet)
# router.register(r'ranking', views.RankingViewSet, base_name='ranking')

urlpatterns = [
    url(r'^api/', include(router.urls)),
#    url(r'^$', views.index, name='index'),
]