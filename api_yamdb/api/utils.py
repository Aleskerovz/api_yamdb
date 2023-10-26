from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_code(user):
    email_body = (
        f'Приветствуем, {user.username}.'
        f'\nКод подтверждения для доступа к API: {user.confirmation_code}'
    )
    send_mail(
        subject='Код подтверждения',
        message=email_body,
        from_email=settings.EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
