���ҫظm:
pip install virtualenv

virtualenv mysite

cd mysite

Scripts\activate

git clone ���M��

cd �M�� 

pip install -r requirements.txt

python manage.py runserver

�M�׬[�c:

root:[.]
|--.spyproject
|--cart
|      |--admin.py                          #���Umodel���x
|      |--apps.py
|      |--cart.py                           #�إߤ@���ʪ���class �ʪ����̪��ӫ~�O��session�s��
|      |--forms.py                          #�s�W�ƶq �٦�updata���s
|      |--migrations
|      |      |--__init__.py
|      |      |--__pycache__
|      |      |      |--__init__.cpython-36.pyc
|      |--models.py             
|      |--templates
|      |      |--cart
|      |      |      |--detail.html         #�ʪ�������
|      |--tests.py
|      |--urls.py
|      |--views.py                          #�ǥѤ��P��url�I�scart class function
|      |--__init__.py
|      |--__pycache__
|      |      |--admin.cpython-36.pyc
|      |      |--cart.cpython-36.pyc
|      |      |--forms.cpython-36.pyc
|      |      |--models.cpython-36.pyc
|      |      |--urls.cpython-36.pyc
|      |      |--views.cpython-36.pyc
|      |      |--__init__.cpython-36.pyc
|--db.sqlite3
|--login
|      |--admin.py
|      |--apps.py
|      |--forms.py                           #�n�J �M ���U���
|      |--migrations
|      |      |--0001_initial.py
|      |      |--0002_auto_20191124_2354.py
|      |      |--__init__.py
|      |      |--__pycache__
|      |      |      |--0001_initial.cpython-36.pyc
|      |      |      |--0002_auto_20191124_2354.cpython-36.pyc
|      |      |      |--__init__.cpython-36.pyc
|      |--models.py
|      |--static
|      |      |--login
|      |      |      |--css
|      |      |      |      |--login.css
|      |      |      |      |--register.css
|      |      |      |--image
|      |--templates
|      |      |--login                        #�n�J �n�X ���U ����
|      |      |      |--confirm.html
|      |      |      |--index.html
|      |      |      |--login.html
|      |      |      |--login2.html
|      |      |      |--register.html
|      |--tests.py
|      |--views.py                             #�ثe��@�n�J �n�X ���U(�|�T�{�A�񪺫H�c�O�_����)
|      |--__init__.py
|      |--__pycache__
|      |      |--admin.cpython-36.pyc
|      |      |--forms.cpython-36.pyc
|      |      |--models.cpython-36.pyc
|      |      |--views.cpython-36.pyc
|      |      |--__init__.cpython-36.pyc
|--manage.py
|--media                                      #�s��ӫ~�Ϥ�
|      |--products
|      |      |--2019
|      |      |      |--11
|      |      |      |      |--25
|      |      |      |      |      |--c1ddc16c7a7685b184a47825c9491c6f.png
|      |      |      |      |      |--�d���~.JPEG
|      |      |      |      |      |--�d���~_foruRtA.JPEG
|      |      |      |      |      |--�d���~_GlpoFso.JPEG
|      |      |      |      |      |--�d���~_gp2H17s.JPEG
|--mysite
|      |--settings.py
|      |--urls.py
|      |--wsgi.py
|      |--__init__.py
|      |--__pycache__
|      |      |--settings.cpython-36.pyc
|      |      |--urls.cpython-36.pyc
|      |      |--wsgi.cpython-36.pyc
|      |      |--__init__.cpython-36.pyc
|--outline.txt
|--outputOutline.py
|--requirements.txt
|--send_mail.py
|--shop
|      |--admin.py
|      |--apps.py
|      |--migrations
|      |      |--0001_initial.py
|      |      |--__init__.py
|      |      |--__pycache__
|      |      |      |--0001_initial.cpython-36.pyc
|      |      |      |--__init__.cpython-36.pyc
|      |--models.py
|      |--templates
|      |      |--shop                 #�ө�����
|      |      |      |--base.html
|      |      |      |--product
|      |      |      |      |--detail.html           #�I�s���ݰӫ~�ԲӤ��e
|      |      |      |      |--list.html             #��ܩҦ��ӫ~
|      |--tests.py
|      |--urls.py
|      |--views.py
|      |--__init__.py
|      |--__pycache__
|      |      |--admin.cpython-36.pyc
|      |      |--models.cpython-36.pyc
|      |      |--urls.cpython-36.pyc
|      |      |--views.cpython-36.pyc
|      |      |--__init__.cpython-36.pyc
|--static
|--templates                                         #���եΪ��F��
|      |--base.html
|      |--home.html
|
