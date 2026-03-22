#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class xinlizixunshi(BaseModel):
    __doc__ = u'''xinlizixunshi'''
    __tablename__ = 'xinlizixunshi'

    __loginUser__='zixunshizhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zixunshizhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='是'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zixunshizhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='咨询师账号' )
    zixunshixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='咨询师姓名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    gerenjianjie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='个人简介' )
    '''
    zixunshizhanghao=VARCHAR
    zixunshixingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    lianxifangshi=VARCHAR
    zhaopian=Text
    gerenjianjie=VARCHAR
    '''
    class Meta:
        db_table = 'xinlizixunshi'
        verbose_name = verbose_name_plural = '心理咨询师'
class yuyuezixun(BaseModel):
    __doc__ = u'''yuyuezixun'''
    __tablename__ = 'yuyuezixun'



    __authTables__={'zixunshizhanghao':'xinlizixunshi','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    biaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标题' )
    yuyueneirong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='预约内容' )
    yuyueshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='预约时间' )
    zixunshizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='咨询师账号' )
    zixunshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='咨询师姓名' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    biaoti=VARCHAR
    yuyueneirong=VARCHAR
    yuyueshijian=DateTime
    zixunshizhanghao=VARCHAR
    zixunshixingming=VARCHAR
    zhaopian=Text
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'yuyuezixun'
        verbose_name = verbose_name_plural = '预约咨询'
class cepingjieguofenxi(BaseModel):
    __doc__ = u'''cepingjieguofenxi'''
    __tablename__ = 'cepingjieguofenxi'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    cepingjieguo=models.TextField   (  null=True, unique=False, verbose_name='测评结果' )
    cepingfenxi=models.TextField   (  null=True, unique=False, verbose_name='测评分析' )
    cepingriqi=models.DateField   (  null=True, unique=False, verbose_name='测评日期' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    touxiang=Text
    cepingjieguo=Text
    cepingfenxi=Text
    cepingriqi=Date
    '''
    class Meta:
        db_table = 'cepingjieguofenxi'
        verbose_name = verbose_name_plural = '测评结果分析'
class zixunxiaoguopinggu(BaseModel):
    __doc__ = u'''zixunxiaoguopinggu'''
    __tablename__ = 'zixunxiaoguopinggu'



    __authTables__={'zixunshizhanghao':'xinlizixunshi','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zixunpinggu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='咨询评估' )
    pingguneirong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='评估内容' )
    pinggushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='评估时间' )
    zixunshizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='咨询师账号' )
    zixunshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='咨询师姓名' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    '''
    zixunpinggu=VARCHAR
    pingguneirong=VARCHAR
    pinggushijian=DateTime
    zixunshizhanghao=VARCHAR
    zixunshixingming=VARCHAR
    zhaopian=Text
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    '''
    class Meta:
        db_table = 'zixunxiaoguopinggu'
        verbose_name = verbose_name_plural = '咨询效果评估'
class fudaokecheng(BaseModel):
    __doc__ = u'''fudaokecheng'''
    __tablename__ = 'fudaokecheng'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    kechengjianjie=models.TextField   (  null=True, unique=False, verbose_name='课程简介' )
    kechengtupian=models.TextField   (  null=True, unique=False, verbose_name='课程图片' )
    kechengneirong=models.TextField   (  null=True, unique=False, verbose_name='课程内容' )
    fabushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发布时间' )
    '''
    kechengmingcheng=VARCHAR
    kechengjianjie=Text
    kechengtupian=Text
    kechengneirong=Text
    fabushijian=DateTime
    '''
    class Meta:
        db_table = 'fudaokecheng'
        verbose_name = verbose_name_plural = '辅导课程'
class fudaofangan(BaseModel):
    __doc__ = u'''fudaofangan'''
    __tablename__ = 'fudaofangan'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    cepingjieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='测评结果' )
    fudaofangan=models.TextField   (  null=True, unique=False, verbose_name='辅导方案' )
    zhidingshijian=models.DateField   (  null=True, unique=False, verbose_name='制定时间' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    touxiang=Text
    cepingjieguo=VARCHAR
    fudaofangan=Text
    zhidingshijian=Date
    '''
    class Meta:
        db_table = 'fudaofangan'
        verbose_name = verbose_name_plural = '辅导方案'
class fudaojilu(BaseModel):
    __doc__ = u'''fudaojilu'''
    __tablename__ = 'fudaojilu'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    cepingjieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='测评结果' )
    fudaofangan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='辅导方案' )
    kechengneirong=models.TextField   (  null=True, unique=False, verbose_name='课程内容' )
    xueshengbiaoxian=models.TextField   (  null=True, unique=False, verbose_name='学生表现' )
    jilushijian=models.DateField   (  null=True, unique=False, verbose_name='记录时间' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    touxiang=Text
    cepingjieguo=VARCHAR
    fudaofangan=VARCHAR
    kechengneirong=Text
    xueshengbiaoxian=Text
    jilushijian=Date
    '''
    class Meta:
        db_table = 'fudaojilu'
        verbose_name = verbose_name_plural = '辅导记录'
class fudaoxiaoguopinggu(BaseModel):
    __doc__ = u'''fudaoxiaoguopinggu'''
    __tablename__ = 'fudaoxiaoguopinggu'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    cepingjieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='测评结果' )
    fudaofangan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='辅导方案' )
    xiaoguopinggu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='效果评估' )
    pingguneirong=models.TextField   (  null=True, unique=False, verbose_name='评估内容' )
    pinggushijian=models.DateField   (  null=True, unique=False, verbose_name='评估时间' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    touxiang=Text
    cepingjieguo=VARCHAR
    fudaofangan=VARCHAR
    xiaoguopinggu=VARCHAR
    pingguneirong=Text
    pinggushijian=Date
    '''
    class Meta:
        db_table = 'fudaoxiaoguopinggu'
        verbose_name = verbose_name_plural = '辅导效果评估'
class shujutongji(BaseModel):
    __doc__ = u'''shujutongji'''
    __tablename__ = 'shujutongji'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tongjiriqi=models.DateField   (  null=True, unique=False, verbose_name='统计日期' )
    yonghuliang=models.IntegerField  (  null=True, unique=False, verbose_name='用户量' )
    zixunshuliang=models.IntegerField  (  null=True, unique=False, verbose_name='咨询数量' )
    kechengshuliang=models.IntegerField  (  null=True, unique=False, verbose_name='课程数量' )
    '''
    tongjiriqi=Date
    yonghuliang=Integer
    zixunshuliang=Integer
    kechengshuliang=Integer
    '''
    class Meta:
        db_table = 'shujutongji'
        verbose_name = verbose_name_plural = '数据统计'
class exampaper(BaseModel):
    __doc__ = u'''exampaper'''
    __tablename__ = 'exampaper'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='心理测评名称' )
    time=models.IntegerField  ( null=False, unique=False, verbose_name='心理测试时长(分钟)' )
    status=models.IntegerField  ( null=False, unique=False,default='0', verbose_name='心理测评状态' )
    '''
    name=VARCHAR
    time=Integer
    status=Integer
    '''
    class Meta:
        db_table = 'exampaper'
        verbose_name = verbose_name_plural = '心理测评表'
class examquestion(BaseModel):
    __doc__ = u'''examquestion'''
    __tablename__ = 'examquestion'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    paperid=models.BigIntegerField  ( null=False, unique=False, verbose_name='所属心理测评id（外键）' )
    papername=models.CharField ( max_length=255,null=False, unique=False, verbose_name='心理测评名称' )
    questionname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='测试试题名称' )
    options=models.TextField   (  null=True, unique=False, verbose_name='选项，json字符串' )
    score=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='分值' )
    answer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='正确答案' )
    analysis=models.TextField   (  null=True, unique=False, verbose_name='答案解析' )
    type=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='测试试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）4:主观题' )
    sequence=models.BigIntegerField  (  null=True, unique=False,default='100', verbose_name='测试试题排序，值越大排越前面' )
    '''
    paperid=BigInteger
    papername=VARCHAR
    questionname=VARCHAR
    options=Text
    score=BigInteger
    answer=VARCHAR
    analysis=Text
    type=BigInteger
    sequence=BigInteger
    '''
    class Meta:
        db_table = 'examquestion'
        verbose_name = verbose_name_plural = '测试试题'
class examquestionbank(BaseModel):
    __doc__ = u'''examquestionbank'''
    __tablename__ = 'examquestionbank'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    questionname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='测试试题名称' )
    options=models.TextField   (  null=True, unique=False, verbose_name='选项，json字符串' )
    score=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='分值' )
    answer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='正确答案' )
    analysis=models.TextField   (  null=True, unique=False, verbose_name='答案解析' )
    type=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='测试试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空） 4:主观题' )
    sequence=models.BigIntegerField  (  null=True, unique=False,default='100', verbose_name='测试试题排序，值越大排越前面' )
    '''
    questionname=VARCHAR
    options=Text
    score=BigInteger
    answer=VARCHAR
    analysis=Text
    type=BigInteger
    sequence=BigInteger
    '''
    class Meta:
        db_table = 'examquestionbank'
        verbose_name = verbose_name_plural = '测试试题'
class examrecord(BaseModel):
    __doc__ = u'''examrecord'''
    __tablename__ = 'examrecord'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __examinationPaper__='是'#[examinationPaper:是/否]后台生成普通试卷功能
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    paperid=models.BigIntegerField  ( null=False, unique=False, verbose_name='心理测评id（外键）' )
    papername=models.CharField ( max_length=255,null=False, unique=False, verbose_name='心理测评名称' )
    questionid=models.BigIntegerField  ( null=False, unique=False, verbose_name='测试试题id（外键）' )
    questionname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='测试试题名称' )
    options=models.TextField   (  null=True, unique=False, verbose_name='选项，json字符串' )
    score=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='分值' )
    answer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='正确答案' )
    analysis=models.TextField   (  null=True, unique=False, verbose_name='答案解析' )
    ismark=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='是否批卷' )
    type=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='测试试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空） 4:主观题' )
    myscore=models.BigIntegerField  ( null=False, unique=False,default='0', verbose_name='测试试题得分' )
    myanswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='考生答案' )
    '''
    userid=BigInteger
    username=VARCHAR
    paperid=BigInteger
    papername=VARCHAR
    questionid=BigInteger
    questionname=VARCHAR
    options=Text
    score=BigInteger
    answer=VARCHAR
    analysis=Text
    ismark=BigInteger
    type=BigInteger
    myscore=BigInteger
    myanswer=VARCHAR
    '''
    class Meta:
        db_table = 'examrecord'
        verbose_name = verbose_name_plural = '心理测试记录表'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '通知公告分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '通知公告'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
