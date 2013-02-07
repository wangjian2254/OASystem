#coding=utf-8
'''
Created on 2011-3-19

@author: 王健
'''
from django.conf.urls.defaults import patterns
from OASystem.oa.flexviews import oaGateway
from oa.views import menu

urlpatterns = patterns('^oa/$',
                       (r'^menu', menu),
                       (r'^geteway/', oaGateway
                           ),
                       )