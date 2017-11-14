from django.conf.urls import url, include
# from rest_framework import routers
from accounts.views import TaskViewSet, PartyViewSet, TaskView

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view



schema_view = get_swagger_view(title='Demo API')




router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'tasks_filter', TaskView)


urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]