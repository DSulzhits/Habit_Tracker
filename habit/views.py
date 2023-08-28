from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from habit.models import Habit
from habit.serializers.habit_serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from habit.paginators import HabitPaginator
from users.models import UserRoles


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitIsPublicListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(public=True)
