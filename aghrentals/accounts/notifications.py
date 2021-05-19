from herald import registry
from herald.base import EmailNotification


class WelcomeEmail(EmailNotification):  # extend from EmailNotification for emails
    template_name = 'welcome_email'  # name of template, without extension
    subject = 'Welcome'  # subject of email

    def __init__(self, user):  # optionally customize the initialization
        self.context = {'user': user}  # set context for the template rendering
        self.to_emails = [user.email]  # set list of emails to send to

    @staticmethod
    def get_demo_args():  # define a static method to return list of args needed to initialize class for testing
        from users.models import User
        return [User.objects.order_by('?')[0]]


registry.register(WelcomeEmail)  # finally, register your notification class

# Alternatively, a class decorator can be used to register the notification:


@registry.register_decorator()
class WelcomeEmail(EmailNotification):
    cc = ['sdpaghrentals@gmail.com']
