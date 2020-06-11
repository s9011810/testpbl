from django.shortcuts import render
from . import form
# Create your views here.
from login import models
from django.shortcuts import redirect

# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = form.UserForm(request.POST)
        message = '請檢查內容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用戶不存在！'
                return render(request, 'login_base.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密碼不正確！'
                return render(request, 'login_base.html', locals())
        else:
            return render(request, 'login_base.html', locals())

    login_form = form.UserForm()
    return render(request, 'login_base.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = form.RegisterForm(request.POST)
        message = "請檢查填寫內容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'register_base.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'register_base.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'email已存在！'
                    return render(request, 'register_base.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'register_base.html', locals())
    register_form = form.RegisterForm()
    return render(request, 'register_base.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")
