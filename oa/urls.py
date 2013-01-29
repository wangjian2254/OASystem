#coding=utf-8
'''
Created on 2011-3-19

@author: 王健
'''
from django.conf.urls.defaults import patterns
from OASystem.oa.flexviews import oaGateway

urlpatterns = patterns('^oa/$',
#                       (r'^tiaozheng', tiaozhengOrderBB),
                       (r'^geteway/', oaGateway
                           ),
                       )