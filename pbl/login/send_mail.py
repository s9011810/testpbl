import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'pbl.settings'

if __name__ == '__main__':   

    send_mail(
        'test'
    )