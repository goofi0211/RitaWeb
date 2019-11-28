from django.shortcuts import render

# Create your views here.
def index(request):
    print('request',request.session.get('is_login', None))
    is_login=request.session.get('is_login', None)
    return render(request, 'index/index.html',locals())
