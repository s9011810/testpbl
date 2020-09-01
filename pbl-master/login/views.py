from django.shortcuts import render
from . import form
# Create your views here.
from login import models
from django.shortcuts import redirect

# Create your views here.
from .models import Group


def index(request):
    class_id = 0
    if 'class_id' not in request.session:
        print('1223')
    else:
        class_id = request.session['class_id']
    test_class = models.CreateClass.objects.all()
    context = {'create_class': test_class, 'class_id': class_id}
    return render(request, 'index.html', context)


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('index')
    if request.method == 'POST':
        login_form = form.UserForm(request.POST)
        message = '請檢查內容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            identify = login_form.cleaned_data.get('identify')

            c_name = login_form.cleaned_data.get('c_name')
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用戶不存在！'
                return render(request, 'login_base.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_identify'] = user.identify
                request.session['c_name'] = user.c_name
                return redirect('index')
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
            identify = register_form.cleaned_data.get('identify')
            c_name = register_form.cleaned_data.get('c_name')
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
                new_user.identify = identify
                new_user.c_name = c_name
                new_user.save()

                return redirect('login')
        else:
            return render(request, 'register_base.html', locals())
    register_form = form.RegisterForm()
    return render(request, 'register_base.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('index')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("index")


def create_class(request):
    # if request.session['user_identify'] == 'teacher':
        if request.method == 'POST':
            class_form = form.ClassForm(request.POST)
            if class_form.is_valid():
                obj = class_form.save()
                request.session['class_id'] = obj.id

                return redirect('index')
        else:
            class_form = form.ClassForm()
        context = {
            'class_form': class_form,
        }
        return render(request, 'create_class.html', context)


def create_activate(request):
    class_c = models.CreateClass.objects.all()
    if request.method == 'POST':
        activate = form.ActivateForm(request.POST)
        if activate.is_valid():
            activate.save()
            return redirect('index')
    else:
        activate = form.ActivateForm()
    context = {
        'class_c': class_c,
        'activate': activate,
    }
    return render(request, 'create_activate.html', context)


def view_activate(request, pk):
    group_a = models.Group.objects.filter(group_user=request.session['user_id'])
    activte_a = models.CreateActivate.objects.filter(class_id=pk)
    if 'class_id' not in request.session:
        class_id = 0
    else:
        class_id = request.session['class_id']
    context = {
        'activate_a': activte_a,
        'pk': pk,
        'group_a': group_a,
        'class_id': class_id
    }
    return render(request, 'view_activate.html', context)


def view_group(request, pk):
    activate_a = models.CreateActivate.objects.filter(id=pk)
    group_a = models.Group.objects.filter(activate=pk)
    context = {
        'activate_a': activate_a,
        'group_a': group_a,
        'pk': pk
    }
    return render(request, 'view_group.html', context)


def create_group(request, pk):
    activate_a = models.CreateActivate.objects.filter(id=pk)
    user_a = models.User.objects.all()
    if request.method == 'POST':
        group = form.CreateGroup(request.POST)
        tests = request.POST.getlist('check_box_list')
        # activate_id = request.POST.get('activate_id')
        if group.is_valid():
            obj: Group()
            obj = group.save()
            for t in tests:
                obj.group_user.add(t)
                obj.save()
            return redirect('index')
    else:
        group = form.CreateGroup()
    context = {
        'user_a': user_a,
        'activate_a': activate_a,
        'group': group
    }
    return render(request, 'create_group.html', context)


def check_group(request):
    group = Group.objects.all()
    activate = models.CreateActivate.objects.all()
    context = {
        'group': group,
        'activate': activate
    }
    return render(request, 'check_group.html', context)


def delete_group(request, pk):
    pk = pk
    if request.method == "POST":
        group = Group.objects.get(pk=pk)
        group.delete()
    return redirect('index')


def edit_group(request, pk):
    group = Group.objects.get(id=pk)
    groupform = form.CreateGroup(request.POST or None, instance=group)
    group_member = group.group_user.all()
    user_a = models.User.objects.all()
    user_c = []
    member_c = []
    user_b = []
    user_e = []
    for user_a1 in user_a:
        user_c.append(user_a1.id)
        user_e.append(user_a1.id)
    for group_member1 in group_member:
        member_c.append(group_member1.id)
    for i in user_c:
        for j in member_c:
            if i == j:
                user_b.append(i)
                user_e.remove(i)
    context = {
        'groupform': groupform,
        'group': group,
        'user_a': user_a,
        'user_b': user_b,
        'user_e': user_e
    }
    tests = request.POST.getlist('check_box_list')
    if groupform.is_valid():
        obj: Group()
        obj = groupform.save()
        for t in tests:
            obj.group_user.add(t)
            obj.save()
        return redirect('index')
    else:
        groupform = form.CreateGroup()
    return render(request, 'edit_group.html', context)
