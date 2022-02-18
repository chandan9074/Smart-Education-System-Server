from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.core.mail import EmailMessage


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.id) + text_type(timestamp) + text_type(user.is_active))


activation_token = AppTokenGenerator()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
