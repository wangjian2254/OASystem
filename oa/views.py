#coding=utf-8
# Create your views here.
from datetime import datetime
from xml.dom.minidom import Document
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response


@login_required
def index(request):
    url='http://'+request.META['HTTP_HOST']+'/static/swf/'
    return render_to_response('oa/index.html',{'url':url,'p':datetime.now()})

def menu(request):
    '''
    flex 获取菜单列表
     xml=Document()
        datas=xml.createElement('datas')
        #datas.setAttribute('time','%s' %time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#        datas.setAttribute('type','infoall')
        xml.appendChild(datas)
    '''
    menu_xml=Document()
    root=menu_xml.createElement('root')
    menu_xml.appendChild(root)
    menu1=menu_xml.createElement('menu')
    menu1.setAttribute('label',u'基础管理')
    menu1.setAttribute('mod',u'settings')
    root.appendChild(menu1)
    menuitem1=menu_xml.createElement('menuitem')
    menuitem1.setAttribute('label',u'部门管理')
    menuitem1.setAttribute('mod',u'dept')
    menu1.appendChild(menuitem1)
    menuitem2=menu_xml.createElement('menuitem')
    menuitem2.setAttribute('label',u'人员管理')
    menuitem2.setAttribute('mod',u'people')
    menu1.appendChild(menuitem2)

    menu2=menu_xml.createElement('menu')
    menu2.setAttribute('label',u'项目视图')
    menu2.setAttribute('mod',u'project')
    root.appendChild(menu2)
    menuitem1=menu_xml.createElement('menuitem')
    menuitem1.setAttribute('label',u'新建项目')
    menuitem1.setAttribute('mod',u'addproject')
    menu2.appendChild(menuitem1)
    menuitem2=menu_xml.createElement('menuitem')
    menuitem2.setAttribute('label',u'项目列表')
    menuitem2.setAttribute('mod',u'projectlist')
    menu2.appendChild(menuitem2)
    menuitem3=menu_xml.createElement('menuitem')
    menuitem3.setAttribute('label',u'版本日志')
    menuitem3.setAttribute('mod',u'svnlog')
    menu2.appendChild(menuitem3)
    menuitem4=menu_xml.createElement('menuitem')
    menuitem4.setAttribute('label',u'新建任务')
    menuitem4.setAttribute('mod',u'addtask')
    menu2.appendChild(menuitem4)
    menuitem5=menu_xml.createElement('menuitem')
    menuitem5.setAttribute('label',u'任务列表')
    menuitem5.setAttribute('mod',u'tasklist')
    menu2.appendChild(menuitem5)

    menu3=menu_xml.createElement('menu')
    menu3.setAttribute('label',u'我的自检')
    menu3.setAttribute('mod',u'myzijian')
    root.appendChild(menu3)
    menuitem1=menu_xml.createElement('menuitem')
    menuitem1.setAttribute('label',u'日自检')
    menuitem1.setAttribute('mod',u'daily')
    menu3.appendChild(menuitem1)
    menuitem2=menu_xml.createElement('menuitem')
    menuitem2.setAttribute('label',u'周自检')
    menuitem2.setAttribute('mod',u'weekly')
    menu3.appendChild(menuitem2)
    menuitem3=menu_xml.createElement('menuitem')
    menuitem3.setAttribute('label',u'月自检')
    menuitem3.setAttribute('mod',u'monthly')
    menu3.appendChild(menuitem3)
    menuitem4=menu_xml.createElement('menuitem')
    menuitem4.setAttribute('label',u'年自检')
    menuitem4.setAttribute('mod',u'yearly')
    menu3.appendChild(menuitem4)

    menu4=menu_xml.createElement('menu')
    menu4.setAttribute('label',u'假期申请')
    menu4.setAttribute('mod',u'jiaqishenq')
    root.appendChild(menu4)
    menuitem1=menu_xml.createElement('menuitem')
    menuitem1.setAttribute('label',u'请假')
    menuitem1.setAttribute('mod',u'day')
    menu4.appendChild(menuitem1)
    menuitem2=menu_xml.createElement('menuitem')
    menuitem2.setAttribute('label',u'申请')
    menuitem2.setAttribute('mod',u'aply')
    menu4.appendChild(menuitem2)

    return HttpResponse(menu_xml.toxml('utf-8'))
