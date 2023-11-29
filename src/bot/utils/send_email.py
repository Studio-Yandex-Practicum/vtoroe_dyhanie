import smtplib
import ssl

from ..core.settings import settings


def send_email(subject, body_text):
    '''
    Отправляет сообщение на электронную почту.
    '''
    # Создание безопасного контекста SSL
    context = ssl.create_default_context()

    message = '\r\n'.join(
        (
            f'From: {settings.sender_email}',
            f'To: {settings.receiver_email}',
            f'Subject: {subject}',
            '',
            body_text,
        )
    )

    with smtplib.SMTP_SSL(
        settings.smtp_server, settings.port, context=context
    ) as server:
        server.login(settings.sender_email, settings.password_email)
        server.sendmail(
            settings.sender_email,
            settings.receiver_email,
            message.encode('UTF-8'),
        )


# def send_email(subject, body_text):
#     print(f'Заглушка посылки письма {subject=} {body_text=}')
