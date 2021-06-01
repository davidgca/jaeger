from rest_framework import routers
from star import views
from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'stars', views.StarViewSet)
schema_view = get_schema_view(title='Star Rest API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'schema', schema_view),
    url(r'^stars/$', views.StarViewSet.as_view()),
    url(r'^star/(?P<name>[a-z]+).*', views.StarDetailView.as_view()),
]