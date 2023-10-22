import smtplib
import ssl


def send_email(subject, body_text):
    """
    Send an email
    """

    smtp_server = "smtp.gmail.com"
    port = 465   # для SSL подключения
    sender_email = "esperansa.stitch@gmail.com"  # Емайл отправителя
    receiver_email = "visteria09@yandex.ru"  # Емайл получателя
    password = input("Введите пароль и нажмите Enter: ")

    # Создание безопасного контекста SSL
    context = ssl.create_default_context()

    message = '\r\n'.join((
        f'From: {sender_email}',
        f'To: {receiver_email}',
        f'Subject: {subject}',
        '',
        body_text))

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode('UTF-8'))


subject = 'Тестирование'
body_text = '''Сотрудники Фонда «Второе дыхание» посетили праздник урожая в
Кадыйском психоневрологическом интернате и провели выдачу вещевой помощи для
проживающих и сотрудников'''

send_email(subject, body_text)
