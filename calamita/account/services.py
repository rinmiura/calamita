from django.core.mail import send_mail
from calamita.settings import EMAIL_HOST_USER

from Crypto.PublicKey import RSA
from Crypto import Random


def get_pair():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    public, private = key.public_key().export_key('PEM'), key.export_key('PEM')

    return private.decode(), public.decode()


def send_private_key_to_mail(pk, user_email):
    send_mail(
        'Вы зарегистрировались на Каламита',
        f'Ваш приватный ключ от кошелька: {pk}',
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False
    )
