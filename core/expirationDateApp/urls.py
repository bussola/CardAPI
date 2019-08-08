from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static
from django.conf import settings
from expirationDateApp.card.viewsets import CardViewSet
from expirationDateApp.client.viewsets import ClientViewSet


schema_view = get_swagger_view(title='Cards API')
app_name = 'expirationDateApp'

router = routers.DefaultRouter()

router.register(r'valid-thru', CardViewSet, basename='cards')
router.register(r'clients', ClientViewSet, basename='clients')


api_urls = [
    url(r'^', include(router.urls)),
]


urlpatterns = [
    url(r'^', include(api_urls)),
    url(r'^swagger/$', schema_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)