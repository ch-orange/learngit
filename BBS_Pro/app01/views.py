#coding=utf-8
from django.shortcuts import render,render_to_response
from django  import forms
from django.http  import HttpResponse
from django.http import  HttpResponseRedirect
#from django.template  import RequestContext
from django.contrib  import auth
from django.contrib  import comments
import models
import logging
#from django.conf import settings
#def global_setting(request):
  #  return  {
  #  'SITE_NAME'=settings.SITE_NAME,
  #'SITE_DESC'=settings.SITE_DESC
  #  }
logger=logging.getLogger('app01.views')
def index1(request):
    try:
        file1=open('ddd.txt','r')
    except Exception as e:
        logger.error(e)
    return render(request,'index1.html',locals())

def acc_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    print username,password
    if user is not None:
        auth.login(request,user)
        content='''
        welcome  %s !!!
        <a href='/logout/'>Logout</a>
        '''%user.username
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
def logout_view(request):
    user=request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b>logged  out!<br/><a href='/'>Re-login</a>"%user)

def login(request):
    return render_to_response('login.html')
        
                              
# Create your views here.
def index(request):
    bbs_list=models.BBS.objects.all()
    bbs_categories=models.Category.objects.all()
    index_id=True
    return render_to_response('index.html',{
        'bbs_list':bbs_list,
        'user':request.user,
        'bbs_category':bbs_categories,
        'index_id':index_id
        })


def category(request,cata_id):
    bbs_list=models.BBS.objects.filter(category__id=cata_id)
    bbs_categories=models.Category.objects.all()
    return render_to_response('index.html',{
        'bbs_list':bbs_list,
        'user':request.user,
        'bbs_category':bbs_categories,
        'cata_id':int(cata_id)})

def bbs_detail(request,bbs_id):
    bbs=models.BBS.objects.get(id=bbs_id)
    category=models.Category.objects.all()
    return render_to_response('bbs_detail.html',{
        'bbs_obj':bbs,
        'user':request.user,
        'bbs_category':category})


def sub_comment(request):
    print request.POST
    bbs_id=request.POST.get('bbs_id')
    comment=request.POST.get('comment_content')
    comments.models.Comment.objects.create(
            content_type_id=7,
            object_pk=bbs_id,
            site_id=1,
            user=request.user,
            comment=comment,
        )
    return HttpResponseRedirect('/detail/%s/'%bbs_id)

def bbs_sub(request):
    #print ',--->', request.POST.get('content')
    content=request.POST.get('content')
    author=models.BBS_user.objects.get(user__username=request.user)
    models.BBS.objects.create(
        title='TEST TITLE',
        summary='HAHA',
        content=content,
        author=author,
        view_count=1,
        ranking=1,
        )
    return HttpResponse('yes.')

def bbs_pub(request):
    return render_to_response('bbs_pub.html')


'''
#虫师
#定义表单模型
class UserForm(forms.Form):
    username=forms.CharField(label='用户名:',max_length=100)
    password=forms.CharField(label='密码:',widget=forms.PasswordInput())
    email=forms.EmailField(label='电子邮件：')

#创建视图
def register(request):
    if request.method=="POST":
        uf=UserForm(request.POST)
        if uf_is_valid():
            #获取表单信息
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            email=uf.cleaned_data['email']
            #将表单写入数据库
            user=BBS_user
            user.username=username
            user.password=password
            user.email=email
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username})
    else:
        uf=UserForm()
    return render_to_response('register.html',{'uf':uf})

    '''
