from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import RUser,Teacher


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
def achievement_1(request):
    teacher1 = Teacher.objects.filter(name='罗永龙')
    return render(request, 'ahnuapp/achievement_1.html', {'teacher1': teacher1})


@login_required
def achievement_2(request):
    teacher2 = Teacher.objects.filter(name='方群')
    return render(request, 'ahnuapp/achievement_2.html', {'teacher2': teacher2})


@login_required
def achievement_3(request):
    teacher3 = Teacher.objects.filter(name='陈付龙')
    return render(request, 'ahnuapp/achievement_3.html', {'teacher3': teacher3})


@login_required
def achievement_4(request):
    teacher4 = Teacher.objects.filter(name='何昕')
    return render(request, 'ahnuapp/achievement_4.html', {'teacher4': teacher4})


@login_required
def achievement_5(request):
    teacher5 = Teacher.objects.filter(name='许勇')
    return render(request, 'ahnuapp/achievement_5.html', {'teacher5': teacher5})


@login_required
def achievement_6(request):
    teacher6 = Teacher.objects.filter(name='王杨')
    return render(request, 'ahnuapp/achievement_6.html', {'teacher6': teacher6})


@login_required
def achievement_7(request):
    teacher7 = Teacher.objects.filter(name='张佩云')
    return render(request, 'ahnuapp/achievement_7.html', {'teacher7': teacher7})


@login_required
def achievement_8(request):
    teacher8 = Teacher.objects.filter(name='郑孝遥')
    return render(request, 'ahnuapp/achievement_8.html', {'teacher8': teacher8})

@login_required
def achievement_9(request):
    teacher9 = Teacher.objects.filter(name='章一磊')
    return render(request, 'ahnuapp/achievement_9.html', {'teacher9': teacher9})


@login_required
def achievement_10(request):
    teacher10 = Teacher.objects.filter(name='程桂花')
    return render(request, 'ahnuapp/achievement_10.html', {'teacher10': teacher10})


@login_required
def achievement_11(request):
    teacher11 = Teacher.objects.filter(name='俞庆英')
    return render(request, 'ahnuapp/achievement_11.html', {'teacher11': teacher11})


@login_required
def achievement_12(request):
    teacher12 = Teacher.objects.filter(name='卞维新')
    return render(request, 'ahnuapp/achievement_12.html', {'teacher12': teacher12})


@login_required
def achievement_13(request):
    teacher13 = Teacher.objects.filter(name='陈传明')
    return render(request, 'ahnuapp/achievement_13.html', {'teacher13': teacher13})


@login_required
def achievement_14(request):
    teacher14 = Teacher.objects.filter(name='丁新涛')
    return render(request, 'ahnuapp/achievement_14.html', {'teacher14': teacher14})


@login_required
def achievement_15(request):
    teacher15 = Teacher.objects.filter(name='郭良敏')
    return render(request, 'ahnuapp/achievement_15.html', {'teacher15': teacher15})


@login_required
def achievement_16(request):
    teacher16 = Teacher.objects.filter(name='杭后俊')
    return render(request, 'ahnuapp/achievement_16.html', {'teacher16': teacher16})


@login_required
def achievement_17(request):
    teacher17 = Teacher.objects.filter(name='接标')
    return render(request, 'ahnuapp/achievement_17.html', {'teacher17': teacher17})


@login_required
def achievement_18(request):
    teacher18 = Teacher.objects.filter(name='齐学梅')
    return render(request, 'ahnuapp/achievement_18.html', {'teacher18': teacher18})


@login_required
def achievement_19(request):
    teacher19 = Teacher.objects.filter(name='孙丽萍')
    return render(request, 'ahnuapp/achievement_19.html', {'teacher19': teacher19})


@login_required
def achievement_20(request):
    teacher20 = Teacher.objects.filter(name='王涛春')
    return render(request, 'ahnuapp/achievement_20.html', {'teacher20': teacher20})


@login_required
def achievement_21(request):
    teacher21 = Teacher.objects.filter(name='赵传信')
    return render(request, 'ahnuapp/achievement_21.html', {'teacher21': teacher21})


@login_required
def achievement_22(request):
    teacher22 = Teacher.objects.filter(name='左开中')
    return render(request, 'ahnuapp/achievement_22.html', {'teacher22': teacher22})


@login_required
def achievement_23(request):
    teacher23 = Teacher.objects.filter(name='汪小寒')
    return render(request, 'ahnuapp/achievement_23.html', {'teacher23': teacher23})


@login_required
def achievement_24(request):
    teacher24 = Teacher.objects.filter(name='李汪根')
    return render(request, 'ahnuapp/achievement_24.html', {'teacher24': teacher24})


@login_required
def achievement_25(request):
    teacher25 = Teacher.objects.filter(name='孙道清')
    return render(request, 'ahnuapp/achievement_25.html', {'teacher25': teacher25})



@csrf_exempt
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/index')
    else:
        return HttpResponseRedirect('/index')