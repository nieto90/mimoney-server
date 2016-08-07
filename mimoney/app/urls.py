from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'account', views.AccountViewSet)
# router.register(r'provinces', views.ProvincesViewSet)
# router.register(r'category', views.CategoryViewSet)
# router.register(r'question', views.QuestionViewSet)
# router.register(r'stage', views.StageViewSet)
# router.register(r'round', views.RoundViewSet)
# router.register(r'ranking', views.RankingViewSet, base_name='ranking')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/home/', views.home, name='home')
#    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)