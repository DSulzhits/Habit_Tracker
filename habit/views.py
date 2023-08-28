from rest_framework.viewsets import ModelViewSet
from habit.models import Habit
from habit.serializers.habit_serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from habit.paginators import HabitPaginator


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator
