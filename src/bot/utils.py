import smtplib
import ssl

from core.settings import settings


def send_email(subject, body_text):
    '''
    Отправляет сообщение на электронную почту.
    '''
    # Создание безопасного контекста SSL
    context = ssl.create_default_context()

    message = '\r\n'.join((
        f'From: {settings.sender_email}',
        f'To: {settings.receiver_email}',
        f'Subject: {subject}',
        '',
        body_text))

    with smtplib.SMTP_SSL(settings.smtp_server,
                          settings.port,
                          context=context) as server:
        server.login(settings.sender_email, settings.password_email)
        server.sendmail(settings.sender_email,
                        settings.receiver_email,
                        message.encode('UTF-8'))


subject = 'Тестирование'
body_text = '''Ненужная одежда — огромный ресурс и катализатор изменений. Она
важна для того, чтобы бездомный не замёрз на улице, а девушка из нуждающейся
семьи пошла на свой первый в жизни выпускной бал красивой. Одежда не только
помогает людям, но и создает рабочие места и даже может вернуться в нашу жизнь
в качестве набивки для дивана. '''

send_email(subject, body_text)
