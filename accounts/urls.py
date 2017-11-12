from django.conf.urls import url
from rest_framework import routers
from accounts.views import TaskViewSet, PartyViewSet, TaskView

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'tasks_filter', TaskView)

urlpatterns = router.urls