from django.core.mail import send_mail
from django.conf import settings


def send_habit_email(email):
    send_mail(
        subject='Новая привычка',
        message='Поздравляем! Вы добавили себе новую полезную привычку! Так держать!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
