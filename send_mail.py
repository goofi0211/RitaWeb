import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':   

    send_mail(
        '還趕下來阿冰鳥',
        '喔齁齁齁齁齁齁齁齁齁齁',
        'p76081433@gs.ncku.edu.tw',
        ['gcobs2336588@gmail.com'],
    )