#coding=utf-8
from django.contrib.auth.decorators import login_required
from django.db import transaction
from oa.models import Person, Dept

__author__ = u'王健'
from django.contrib.auth.models import User, Permission

def getResult(result,success=True,message=None):
    return {'result':result,'success':success,'message':message}

from pyamf.remoting.gateway.django import DjangoGateway
import pyamf
try:
    pyamf.register_class(User, 'django.contrib.auth.models.User')
except ValueError:
    print "Class already registered"
def login_required1(login=False):
    def islogin(func):
        def test(request, *args, **kwargs):
            if request.user.is_authenticated():
                return func(request, *args, **kwargs)
            else:
                return getResult(False,False,'需要登录后才能操作。')
            return test
    return islogin


def permission_required(code):
    '''
    权限验证，具有权限方可继续访问
    '''
    def permission(func):
        def test(request, *args, **kwargs):
            if request.user.has_perm(code):
                return func(request, *args, **kwargs)
            else:
                return getResult(False,False,u'权限不够,需要具有：%s 权限'%Ztperm.perm[code])
        return test
    return permission

def orderbbchange_required(code):
    '''
    具有XX权限或者其他条件方可继续
    '''
    def permission(func):
        def test(request, *args, **kwargs):
            if len(args)==1 or not args[1]:
                return func(request, *args, **kwargs)
            elif request.user.has_perm(code):
                return func(request, *args, **kwargs)
            else:
                lsh=args[1]
                if request.user.pk==OrderBBNo.objects.get(lsh=lsh).user.pk:
                    return func(request, *args, **kwargs)
                return getResult(False,False,u'权限不够,需要具有：%s 权限'%Ztperm.perm[code])
        return test
    return permission

@login_required
def getUser(request):
    return getResult(request.user)
@login_required
def getAllUser(request):
    userlist=[]
    for u in User.objects.all():
        udict={}
        udict['id']=u.pk
        udict['username']=u.username
        udict['is_active']=u.is_active
        udict['last_name']=u.last_name
        if hasattr(u,'person'):
            udict['dept']=[]
            for d in u.person.dept.all():
                udict['dept'].append(d.pk)
            udict['rtx_user']=u.person.rtx_user
            udict['svn_user']=u.person.svn_user
            udict['svn_pwd']=u.person.svn_pwd


        userlist.append(udict)
    return getResult(userlist)
    pass
@login_required
def userhaschange(request):
    if request.user.has_perm('oa.user_change'):
        return getResult(True)
    else:
        return getResult(False)
    pass

@login_required
@permission_required('oa.user_change')
@transaction.commit_on_success
def saveUser(request,obj):
    u=User()
    if obj.has_key('id'):
        u=User.objects.get(pk=obj['id'])
#        u.pk=obj['id']
        if obj.has_key('password'):
            u.set_password(obj['password'])
#        u.is_staff=User.objects.get(pk=obj['id']).is_staff

    else:
        u.set_password(obj['password'])
    u.username=obj['username']
    u.last_name=obj['last_name']
    u.is_active=obj['is_active']

#    u.first_name=obj['first_name']

#    u.is_active=True
    u.save()
    if hasattr(u,'person'):
        person=u.person
    else:
        person=None
    if not person:
        person=Person()
        person.user=u
        person.save()

    if obj.has_key('dept'):
        person.dept=Dept.objects.filter(id__in=obj['dept'])
    if obj.has_key('rtx_user'):
        person.rtx_user=obj['rtx_user']
    if obj.has_key('svn_user'):
        person.svn_user=obj['svn_user']
    if obj.has_key('svn_pwd'):
        person.svn_pwd=obj['svn_pwd']
    person.save()

#    u.user_permissions=[]
#    for p in Permission.objects.filter(codename__in=obj['permissions']):
#        u.user_permissions.add(p)
#
#    u.save()

    return getResult(True)
    pass
@login_required
@transaction.commit_on_success
def changeUserPassword(request,obj):
    u=request.user
    if u.username==obj['username']:
        if u.check_password(obj['oldpassword']):
            u.set_password(obj['password'])
            u.save()
            return getResult(True)

    return getResult(False,False,u'修改密码失败')
    pass



@login_required
def getUserById(request,id):
    return getResult(User.objects.filter(pk=id)[:1])
    pass


def saveDept(request,deptObj):
    dept=Dept()
    if deptObj.has_key('id'):
        dept=Dept.objects.get(pk=deptObj.get('id',None))
    if dept:
        if deptObj.has_key('name'):
            dept.name=deptObj.get('name',None)
        if deptObj.has_key('desc'):
            dept.desc=deptObj.get('desc',None)
        if deptObj.has_key('is_del'):
            dept.is_del=deptObj.get('is_del',None)
        if deptObj.has_key('parent_dept'):
            dept.parent_dept=Dept.objects.get(pk=deptObj.get('parent_dept',None))
        dept.save()
    return getResult(True)

def getAllDept(request):
    return getResult(Dept.objects.all())
def getAllUsedDept(request):
    return getResult(Dept.objects.filter(is_del=False))





oaGateway = DjangoGateway({
    'service.getUser': getUser,
    'service.userhaschange': userhaschange,
    'service.saveUser': saveUser,
    'service.changeUserPassword': changeUserPassword,
    'service.getAllUser': getAllUser,
    'service.getAllUsedDept': getAllUsedDept,
    'service.getAllDept': getAllDept,
    'service.getUserById': getUserById,
    'service.saveDept': saveDept,
    })

