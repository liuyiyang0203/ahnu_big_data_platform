from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password_again = request.POST.get('password_again', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if password == password_again:
                auth_login(request, user)
                return HttpResponseRedirect('/teachers')
            else:
                error_msg = '两次输入密码不一致'
                return render(request, 'ahnuapp/index.html', {'error_msg': error_msg})
        else:
            #
            error_msg = '请输入正确的用户名和密码'
            return render(request, 'ahnuapp/index.html', {'error_msg': error_msg})
    return render(request, 'ahnuapp/index.html')


@login_required
def teachers(request):
    return render(request, 'ahnuapp/teachers.html')


@login_required
def achievements(request):
    return render(request, 'ahnuapp/achievements.html')

@csrf_exempt
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/index')