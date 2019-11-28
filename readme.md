環境建置:
pip install virtualenv

virtualenv mysite

cd mysite

Scripts\activate

git clone 此專案

cd 專案 

pip install -r requirements.txt

python manage.py runserver

專案架構:

root:[.]
|--.spyproject
|--cart
|      |--admin.py                          #註冊model到後台
|      |--apps.py
|      |--cart.py                           #建立一個購物車class 購物車裡的商品是用session存放
|      |--forms.py                          #新增數量 還有updata按鈕
|      |--migrations
|      |      |--__init__.py
|      |      |--__pycache__
|      |      |      |--__init__.cpython-36.pyc
|      |--models.py             
|      |--templates
|      |      |--cart
|      |      |      |--detail.html         #購物車頁面
|      |--tests.py
|      |--urls.py
|      |--views.py                          #藉由不同的url呼叫cart class function
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
|      |--forms.py                           #登入 和 註冊表單
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
|      |      |--login                        #登入 登出 註冊 頁面
|      |      |      |--confirm.html
|      |      |      |--index.html
|      |      |      |--login.html
|      |      |      |--login2.html
|      |      |      |--register.html
|      |--tests.py
|      |--views.py                             #目前實作登入 登出 註冊(會確認你填的信箱是否有效)
|      |--__init__.py
|      |--__pycache__
|      |      |--admin.cpython-36.pyc
|      |      |--forms.cpython-36.pyc
|      |      |--models.cpython-36.pyc
|      |      |--views.cpython-36.pyc
|      |      |--__init__.cpython-36.pyc
|--manage.py
|--media                                      #存放商品圖片
|      |--products
|      |      |--2019
|      |      |      |--11
|      |      |      |      |--25
|      |      |      |      |      |--c1ddc16c7a7685b184a47825c9491c6f.png
|      |      |      |      |      |--卡比獸.JPEG
|      |      |      |      |      |--卡比獸_foruRtA.JPEG
|      |      |      |      |      |--卡比獸_GlpoFso.JPEG
|      |      |      |      |      |--卡比獸_gp2H17s.JPEG
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
|      |      |--shop                 #商店頁面
|      |      |      |--base.html
|      |      |      |--product
|      |      |      |      |--detail.html           #點連結看商品詳細內容
|      |      |      |      |--list.html             #顯示所有商品
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
|--templates                                         #測試用的東西
|      |--base.html
|      |--home.html
|
