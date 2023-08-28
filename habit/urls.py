from habit.apps import HabitConfig
from rest_framework.routers import DefaultRouter
# from django.urls import path
from habit.views import HabitViewSet

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habits')

urlpatterns = [

              ] + router.urls
