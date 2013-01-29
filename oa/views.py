#coding=utf-8
# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required
def index(request):
    url='http://'+request.META['HTTP_HOST']+'/static/swf/'
    return render_to_response('oa/index.html',{'url':url,'p':datetime.now()})