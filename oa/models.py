#coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SystemSetting(models.Model):
    rtx_host=models.URLField(verbose_name=u'腾讯通IP网址')

class Dept(models.Model):
    name=models.CharField(max_length=30,verbose_name=u'部门名称')
    desc=models.CharField(max_length=200,verbose_name=u'部门简介')
    parent_dept=models.ForeignKey("Dept",blank=True,null=True,verbose_name=u'父级部门')
    is_del=models.BooleanField(default=False,verbose_name=u'是否废弃')

class DownloadFile(models.Model):
    name=models.CharField(max_length=30,verbose_name=u'文件名称')
    file=models.FileField(upload_to='upload/',verbose_name=u'存储文件')
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')


class Role(models.Model):

    class Meta:
        permissions=(
            ('user_change',u'用户管理'),

            ('add_Project',u'添加项目'),
            ('modify_Project',u'修改项目'),
            ('del_Project',u'删除项目'),
            ('close_Project',u'关闭项目'),
            ('open_Project',u'开始项目'),

            ('add_Task',u'添加任务'),
            ('modify_Task',u'修改任务'),
            ('del_Task',u'删除任务'),
            ('open_Task',u'开始任务'),
            ('close_Task',u'关闭任务'),

            ('add_Daily_Check',u'添加日自检'),
            ('modify_Daily_Check',u'修改日自检'),
            ('del_Daily_Check',u'删除日自检'),
            ('right_Daily_Check',u'审核日自检'),

            ('add_Weekly_Check',u'添加周自检'),
            ('modify_Weekly_Check',u'修改周自检'),
            ('del_Weekly_Check',u'删除周自检'),
            ('right_Weekly_Check',u'审核周自检'),

            ('add_Monthly_Check',u'添加月自检'),
            ('modify_Monthly_Check',u'修改月自检'),
            ('del_Monthly_Check',u'删除月自检'),
            ('right_Monthly_Check',u'审核月自检'),

            ('add_Yearly_Check',u'添加年自检'),
            ('modify_Yearly_Check',u'修改年自检'),
            ('del_Yearly_Check',u'删除年自检'),
            ('right_Yearly_Check',u'审核年自检'),
            )

class Person(models.Model):
    #用户个人信息
    user=models.OneToOneField(User,verbose_name=u'登录账户')
    dept=models.ManyToManyField(Dept,verbose_name=u'隶属部门')
    rtx_user=models.CharField(max_length=10,blank=True,null=True,verbose_name=u'腾讯通账号')
    svn_user=models.CharField(max_length=10,blank=True,null=True,verbose_name=u'svn账号')
    svn_pwd=models.CharField(max_length=10,blank=True,null=True,verbose_name=u'svn密码')


class Project(models.Model):
    #项目
    name=models.CharField(max_length=30,verbose_name=u'项目名')
    desc=models.CharField(max_length=500,verbose_name=u'项目描述')
    code=models.CharField(max_length=30,unique=True,verbose_name=u'项目代码',help_text=u'IDE中的项目名')
    start_date=models.DateField(verbose_name=u'开始日期')
    end_date=models.DateField(verbose_name=u'预计结束日期')
    real_end_date=models.DateField(verbose_name=u'实际结束日期')
    status=models.IntegerField(default=1,verbose_name=u'状态',help_text=u'未开始、进行中、结束')
    to_user=models.ForeignKey(User,related_name='topersion',blank=True,null=True,verbose_name=u'指定给')
    team_Name=models.CharField(max_length=30,verbose_name=u'团队名称')

class SVNProject(models.Model):
    project=models.ForeignKey(Project,verbose_name=u'隶属项目')
    svnName=models.CharField(max_length=30,verbose_name=u'svn项目名(源代码)')
    svnPath=models.CharField(max_length=200,verbose_name=u'svn路径(源代码)')
    svnNameTest=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'svn项目名(测试机)')
    svnPathTest=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'svn路径(测试机)')
    svnNameProduct=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'svn项目名(产品)')
    svnPathProduct=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'svn路径(产品)')

class SVNLog(models.Model):
    project=models.ForeignKey(Project,verbose_name=u'隶属项目')
    type=models.IntegerField(default=1,verbose_name=u'提交日志类型',help_text=u'源代码提交、测试机提交、产品机提交')
    create_date=models.DateTimeField(auto_created=True)
    log=models.CharField(max_length=500,verbose_name=u'日志内容')
    user=models.ForeignKey(User,verbose_name=u'提交人')
    number=models.IntegerField(verbose_name=u'svn版本号')

class TaskType(models.Model):
    name=models.CharField(max_length=10,verbose_name=u'类型',help_text=u'设计、开发、测试、研究、')
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')

class Task(models.Model):
    #任务
    name=models.CharField(max_length=100,verbose_name=u'任务名称')
    desc=models.CharField(max_length=500,verbose_name=u'任务描述')
    to_user=models.ForeignKey(User,related_name='to',blank=True,null=True,verbose_name=u'指定给')
    creat_user=models.ForeignKey(User,related_name='create',blank=True,null=True,verbose_name=u'创建者')
    finish_user=models.ForeignKey(User,related_name='finish',blank=True,null=True,verbose_name=u'完成者')
    jb=models.IntegerField(default=3,verbose_name=u'优先级')
    yuji_time=models.IntegerField(verbose_name=u'预计工时')
    start_date=models.DateField(verbose_name=u'开始日期')
    end_date=models.DateField(verbose_name=u'结束日期')
    type=models.ForeignKey(TaskType,verbose_name=u'任务类型')
    other_user=models.ForeignKey(User,blank=True,null=True,related_name='other',verbose_name=u'配合人员')
    files=models.ManyToManyField(DownloadFile,blank=True,null=True,verbose_name=u'附件')


