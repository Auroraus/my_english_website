# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:58:15 2018

@author: Administrator
"""

# encoding=utf8
import sae,numpy,math
import sae.kvdb
import time,datetime

kv = sae.kvdb.Client()

ftime=datetime.date(2018,12,22)

#导入Bottle模块
from bottle import Bottle,route, run, template, request, response,  post, get,static_file,debug
app=Bottle()
debug(True)  #打开debug功能
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def plot():
    today = datetime.date.today()
    stime=datetime.date(2018,today.month,today.day)
    t=ftime-stime
    t=str(t).split(' ')[0]
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="2" >.</font></p></center>
    <title>线性回归方程求解</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">线性回归方程求解</font></h1></center>'''
    page=page+'''<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>'''
    page=page+'''<center><p><font size="12" color="red">距离考研还有--'''+t+'''--天</font></p></center>'''
    page=page+'''<center><p><font size="2" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
<li id="ho"><a href="http://1.liuwen.applinzi.com/login"><font size="8" color="blue">我的云笔记</font></a></li>
</ul>
</div>
<center><p><font size="6" color="red">各个数据之间用英文逗号隔开</font></p></center>
    <form method = "POST" id="form">
    <h3><font size="12" color="red">请输x内容</font>
    <input name="x" style='font-size:40px;background: #F0F8FF;'size=35 /></h3>
    <h3><font size="12" color="red">请输y内容</font>
    <input name="y" style='font-size:40px;background: #F0F8FF;' size=35/></h3><h1>
    <label>
    <input type="radio" style="width:40px;height:40px" name ="log" value="yes" >取对数
    </label>
    <label>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="no" checked>不取对数
  	</label></h1>
    <h3><center><p><font size="2" >.</font></p></center>
    <input type='submit' style='font-size:80px;background: #F0F8FF;' value='确定' /></h3>
  	</form>
    </body> </html><!--'''
    return page
    
def log_in():
    today = datetime.date.today()
    stime=datetime.date(2018,today.month,today.day)
    t=ftime-stime
    t=str(t).split(' ')[0]
    page='''<form method = "POST" id="login">
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>'''
    page=page+'''<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>'''
    page=page+'''<center><p><font size="12" color="red">距离考研还有--'''+t+'''--天</font></p></center>'''
    page=page+'''<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <h1><font size="12" color="green">密码</font>
    <input name="psd" style='font-size:80px;background: #F0F8FF;' size=18/></h1>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <input type='submit' style='font-size:80px;background: #F0F8FF;' value='登陆' /></h3>
  	</form><!--'''
    return page
    
def linear(number,xstr,ystr):
    try:
        if xstr=='' or ystr=='':
            return '222333','222333'
        xtuple=eval(xstr)
        xlist=[]
        if number=='yes':
            for x in xtuple:
                if x>0:
                    xlist.append(math.log(float(x))) #这里的numpy.log(是为了金属工艺学实验而加的，后面必须去掉)变为：xlist=list(xtuple)
                else:
                    return '222333','222333'
        else:
            for i in xtuple:xlist.append(float(i))
        ytuple=eval(ystr)
        ylist=[]
        if number=='yes':
            for y in ytuple:
                if y>0:
                    ylist.append(math.log(float(y))) #这里的numpy.log(是为了金属工艺学实验而加的，后面必须去掉)变为：xlist=list(xtuple)
                else:
                    return '222333','222333'
        else:
            for i in ytuple:ylist.append(float(i))
        if len(ylist)==len(xlist):
            pass
        else:
            return '222333','222333'
        xaver=float(sum(xlist))/len(xlist)
        yaver=float(sum(ylist))/len(ylist)
        xy=[] 
        for i in xlist:
            for j in ylist:
                if xlist.index(i)==ylist.index(j):
                    a=i*j
                    xy.append(a)
        xx=[]
        for ii in xlist:
            b=ii**2
            xx.append(b)
        xyaver=float(sum(xy))/len(xy)
        xxaver=float(sum(xx))/len(xx)
        if (xaver**2-xxaver)!=0:
            para=(xaver*yaver-xyaver)/(xaver**2-xxaver)
            bbb=yaver-para*xaver
            if bbb>=0:
                if number=='yes':
                    return round((math.e)**bbb,4),round(para,4)
                else:
                    	return para,bbb
        else:
            return '222333','222333'
    except:
        return '222333','222333'
     
def get_data():
    today = datetime.date.today()
    stime=datetime.date(2018,today.month,today.day)
    t=ftime-stime
    t=str(t).split(' ')[0]
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <title>我的云笔记</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">我的云笔记</font></h1></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
<li id="h"><a href="/bn" title="国际新闻类文章"><font size="8" color="blue">国际新闻类文章</font></a></li>
<li id="he"><a href="http://1.liuwen.applinzi.com/linear"><font size="8" color="blue">线性回归方程求解</font></a></li>
<li id="o"><a href="/other" title="其他网站推荐" target="_blank"><font size="8" color="green">其他网站推荐</font></a></li>
<li id="o"><a href="http://1.liuwen.applinzi.com/updata_data" title="上传数据" target="_blank"><font size="8" color="green">上传笔记数据</font></a></li>
<li id="ho"><a href="http://1.liuwen.applinzi.com/login"><font size="8" color="blue">我的云笔记</font></a></li>
</ul>
</div>'''
    page=page+'''<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>'''
    page=page+'''<center><p><font size="12" color="red">距离考研还有--'''+t+'''--天</font></p></center>'''
    page=page+'''
<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><h1><font size="12" color="blue">笔记内容</font></h1></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>

'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    n=1
    for i in data:
        text=kv.get(i)
        if '###' in text:
            title=text.split('###')[0]
            content=text.split('###')[1]
            page=page+'<h1><font size="12" color="red"><center>&nbsp;&diams;&nbsp;&nbsp;'+str(n)+'、'+title+'</center></font></h1>'+'<center><font size="6"><p>上传日期：&nbsp;'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i)))).replace(' ','&nbsp;')+'</p></font></center>'
            texe=page+'<p style="width:965px; word-wrap:break-word;">'
            page=page+'<font size="12">&nbsp;&nbsp;&nbsp;&nbsp;'+content
            page=page+'</font></p>'
            n=n+1
         
        
    page=page+'</body> </html><!--'
    return page

def get_data1():
    today = datetime.date.today()
    stime=datetime.date(2018,today.month,today.day)
    t=ftime-stime
    t=str(t).split(' ')[0]
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <title>我的云笔记</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">我的每日记录</font></h1></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
<li id="h"><a href="/bn" title="国际新闻类文章"><font size="8" color="blue">国际新闻类文章</font></a></li>
<li id="he"><a href="http://1.liuwen.applinzi.com/linear"><font size="8" color="blue">线性回归方程求解</font></a></li>
<li id="o"><a href="/other" title="其他网站推荐" target="_blank"><font size="8" color="green">其他网站推荐</font></a></li>
<li id="o"><a href="http://1.liuwen.applinzi.com/updata_data" title="上传数据" target="_blank"><font size="8" color="green">上传笔记数据</font></a></li>
<li id="ho"><a href="http://1.liuwen.applinzi.com/login"><font size="8" color="blue">我的云笔记</font></a></li>
</ul>
</div>
'''
    page=page+'''<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>'''
    page=page+'''<center><p><font size="12" color="red">距离考研还有--'''+t+'''--天</font></p></center>'''
    page=page+'''
<center><p><font size="2" >.</font></p></center>
    <center><p><font size="2" >.</font></p></center>
    <center><h1><font size="12" color="blue">记录详情</font></h1></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>

'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    n=1
    for i in data:
        text=kv.get(i)
        if '***' in text:
            title=text.split('***')[0]
            content=text.split('***')[1]
            page=page+'<h1><font size="12" color="red"><center>&nbsp;&diams;&nbsp;&nbsp;'+str(n)+'、'+title+'</center></font></h1>'+'<center><font size="6"><p>上传日期：&nbsp;'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i)))).replace(' ','&nbsp;')+'</p></font></center>'
            texe=page+'<p style="width:965px; word-wrap:break-word;">'
            page=page+'<font size="12">&nbsp;&nbsp;&nbsp;&nbsp;'+content
            page=page+'</font></p>'
            n=n+1
        
    page=page+'</body> </html><!--'
    return page
def updata():
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <title>我的云笔记</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">我的云笔记</font></h1></center>
    <center><p><font size="1" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
<li id="h"><a href="/bn" title="国际新闻类文章"><font size="8" color="blue">国际新闻类文章</font></a></li>
<li id="he"><a href="http://1.liuwen.applinzi.com/linear"><font size="8" color="blue">线性回归方程求解</font></a></li>
<li id="o"><a href="/other" title="其他网站推荐" target="_blank"><font size="8" color="green">其他网站推荐</font></a></li>
<li id="o"><a href="http://1.liuwen.applinzi.com/login" title="回到我的笔记" target="_blank"><font size="8" color="green">回到我的笔记</font></a></li>
</ul>
</div>
    <form method = "POST" id="form">
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><h1><font size="12" color="green">请输入保存数据权限码</font></h1></center>
   <center> <input name="psd" style='font-size:40px;background: #F0F8FF;' size=15/></center>
   <center><h1><font size="20" color="green">请输入标题</font></h1></center>
   <center> <input name="title" style='font-size:40px;background: #F0F8FF;' size=30/></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><h3><font size="12" color="red">请输入内容</font></h3></center>
		<center><textarea name="note" style='font-size:40px;background: #F0F8FF;' cols="45" rows="15"></textarea></center>
	</form>
 
	<button type="submit" style="width: 200px; height: 120px;" form="form"><font size="12" >提交<br></font></button>

'''
    page=page+'</body> </html><!--'
    return page


import urllib2
import re


def update_article():
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="12" color="blue">.</font></p></center>
    <center><p><font size="12" color="blue">.</font></p></center>
    <title>文章更新页面</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">文章更新管理页面</font></h1></center>
    <center><p><font size="12" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
</ul>
</div>
    <form method = "POST" id="form">
    <font size="12" ><p>
    <label><p>
    <input type="radio" style="width:40px;height:40px" name ="log" value="1" checked>国际新闻类文章</p>
    </label>
    <label><p>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="2" >商业经济类文章</p>
  	</label>
    <label><p>
    <input type="radio" style="width:40px;height:40px" name ="log" value="3" >科技类文章</p>
    </label>
    <label><p>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="4" >教育类文章</p>
  	</label>
    <label><p>
    <input type="radio" style="width:40px;height:40px" name ="log" value="5" >文化类文章</p>
    </label>
    <label><p>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="6" >科学类文章</p>
  	</label>
    <label><p>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="7" >观点类文章</p>
  	</label></p>
    <label><p>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="8" >健康类文章</p>
  	</label>
    <label><p>
　　<input type="radio" style="width:40px;height:40px" name ="log" value="9" >旅游类文章</p>
  	</label></p>
    </font>
    <h1><input type='submit' style='font-size:60px;background: #F0F8FF;' value='确认更新选定的文章' /></h1>
	</form>
    </body> </html><!--'''
    return page
        
@app.get("/bn")
def bn():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>国际新闻类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/business")
def business():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>商业经济类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/technology")
def technology():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>科技类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/education")
def education():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>教育类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/culture")
def culture():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>文化类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/science")
def science():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>科学类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/opinion")
def opinion():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>观点类文章</title>' in text:
            return text.split('###article###')[1]
        
@app.get("/health")
def opinion():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>健康类文章</title>' in text:
            return text.split('###article###')[1]
@app.get("/tour")
def opinion():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>旅游类文章</title>' in text:
            return text.split('###article###')[1]


@app.get('/update_article')
def login_form():
    return update_article()

@app.post('/update_article')
def login():
    num=request.forms.get('log')
    url=[('http://www.qqenglish.com/bn/bn/','国际新闻类文章'),('http://www.qqenglish.com/bn/business/','商业经济类文章'),\
             ('http://www.qqenglish.com/bn/technology/','科技类文章'),('http://www.qqenglish.com/bn/education/','教育类文章'),\
             ('http://www.qqenglish.com/bn/culture/','文化类文章'),('http://www.qqenglish.com/bn/science/','科学类文章'),\
             ('http://www.qqenglish.com/bn/opinion/','观点类文章'),('http://www.qqenglish.com/bn/health/','健康类文章'),('http://www.qqenglish.com/bn/tour/','旅游类文章')]
    if num!='':
        url=url[int(num)-1]
        data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
        for i in data:
            text=kv.get(i)
            if '###article###' in text and '<title>'+url[1]+'</title>' in text:
                kv.delete(i)
        header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
        
        if 1:
            req = urllib2.Request(url[0],headers=header)
            res = urllib2.urlopen(req)
            text=res.read().decode("GBK")
            #print(text)
            urls=re.compile('<li><span>(.*?)</span><a href="(.*?)" target=_blank').findall(text)
            n=1
            m='''<!doctype html>
            <html>
            <head>
            <meta charset="utf8">
            <title>'''
            m=m+url[1]+'''</title>
            </head>
            <body>
            <center><p>.</p></center>
            <center><p>.</p></center>
            <center><p><font size="6" color="red">置顶公告：除了十九大报告，以下九个板块每个板块有20篇文章，文章是人工翻译的（不是机器翻译的，更不可能是我翻译的），所以翻译质量是有保证的。九个板块的英文材料我会平均每周更新一次</font></p></center>
            <center><a href="https://mp.weixin.qq.com/s/aXm6ZgCEFY-e6zScKeI0IA"><img src="/images/wx.jpg"   width="50%" height="50%"/></a></center>
            <center><p><font size="5">扫一扫关注我的微信公众号</font></p></center>
            <center><h1><font size="12" color="blue">英语阅读练习——by zf</font></h1></center> 
            <center><p>.</p></center>
            <center><p>.</p></center>
            <div id="navfirst">
            <ul id="menu">
            <li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
            <li id="h"><a href="/bn" title="国际新闻类文章"><font size="8" color="blue">国际新闻类文章</font></a></li>
            <li id="b"><a href="/business" title="商业经济类文章"><font size="8" color="blue">商业经济类文章</font></a></li>
            <li id="s"><a href="/technology" title="科技类文章"><font size="8" color="blue">科技类文章</font></a></li>
            <li id="d"><a href="/education" title="教育类文章"><font size="8" color="blue">教育类文章</font></a></li>
            <li id="x"><a href="/culture" title="文化类文章"><font size="8" color="blue">文化类文章</font></a></li>
            <li id="ws"><a href="/science" title="科学类文章"><font size="8" color="blue">科学类文章</font></a></li>
            <li id="w"><a href="/opinion" title="观点类文章"><font size="8" color="blue">观点类文章</font></a></li>
            <li id="o"><a href="/other" title="其他网站推荐" target="_blank"><font size="8" color="green">其他网站推荐</font></a></li>
            </ul>
            </div>'''
            for i in urls[:10]:
                try:
                    #time.sleep(random.randint(3,6))
                    #print(i[0],'http://www.qqenglish.com'+i[1])
                    req = urllib2.Request('http://www.qqenglish.com'+i[1],headers=header)
                    res = urllib2.urlopen(req)
                    text=res.read().decode("GBK").encode("utf8")
                   
                    title=re.compile('<H2>(.*?)</H2>').findall(text)[0]
                    data= re.compile(r'</script></div>(.*?)全文请访问',re.DOTALL).findall(text)[0].replace('</div>','').replace('<FONT color=#666666>“','')[:-4]
                    m=m+'<center><h1><font color="green">这是第'+str(n)+'篇文章</font></h1></center>\n'
                    m=m+'<center><h1><font color="red">文章标题-'+str(title)+'</font></h1></center>\n'
                    m=m+'<center><p>日期-'+str(i[0])+'</p></center>\n'
                    m=m+'<font size="7" face="arial">'
                    m=m+data
                    m=m+'</font>'
                    m=m+'\n\n'
                    n=n+1
                    
                except:
                    pass
            m=m+'</body> </html><!--'
            kv.set(str(int(time.time())),'###article###'+m)
            return '''<center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="12" color="red">更新完成</font></p></center>
    <center><p><font size="12" color="red">更新完成</font></p></center><!--'''
    else:
        return '<h1>您的输入为空，请重新输入<h1>'
    
@app.get('/linear')
def data():
    return plot()

@app.get('/')
def data():
    return '<h1>网址已改，请访问：http://1.liuwen.applinzi.com/linear<h1><!--'

@app.post('/linear')
def plot_data():
    try:
        xx = request.forms.get('x')
        yy = request.forms.get('y')
        d=request.forms.get('log')
    except:
        return '<h1>您的输入有误，请重新输入<h1>'
    if xx!='' and yy!='':
        para,bbb=linear(d,xx,yy)
        x=list(eval(xx))
        y=list(eval(yy))
        if len(x)!=len(y):
            return '''<center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="12" color="red">x，y个数不相等，请检查后重新输入</font></p></center>
    <center><p><font size="12" color="red">x，y个数不相等，请检查后重新输入</font></p></center><!--'''
        if para!='222333':
            if d=='yes':
                zz=numpy.arange(min(x),max(x),0.001)
                yyy=round(para,4)*(zz**(round(bbb,4)))
                plt.title('linear')  # 图名
                plt.plot(x, y, 'ro')  # 图上的点,最后一个参数为显示的模式
                plt.plot(zz,yyy,'b-',label='y='+str(para)+'x^'+str(round(bbb,4))) 
                buffer = BytesIO()
                label='y='+str(para)+'x^'+str(round(bbb,4))
                plt.savefig(buffer)  
                plot_data = buffer.getvalue()
                
                # 图像数据转化为 HTML 格式
                imb = base64.b64encode(plot_data)  
                #imb = plot_data.encode('base64')   # 对于 Python 2.7可用 
                ims = imb.decode()
                imd = "data:image/png;base64,"+ims
                iris_im = "<img src='%s'>"% imd   
                
                root = "<title>linear</title>"
                root = root + iris_im+"<center><p style='width:965px; word-wrap:break-word;'><font size='6' >x-data:&nbsp;&nbsp;"+str(xx)+"</font></p></center>"+"<center><p style='width:965px; word-wrap:break-word;'><font size='6' >y-data:&nbsp;&nbsp;"+str(yy)+"</font></p></center>"+"<center><font size='12'><p>final  result:&nbsp;&nbsp;&nbsp;&nbsp;"+label+"</p></font></center>  " 
                plt.close()
                return root
            else:
                zz=numpy.arange(min(x),max(y),0.001)
                yyy=para*zz+bbb
                plt.title('linear')  # 图名
                plt.plot(x, y, 'ro')  # 图上的点,最后一个参数为显示的模式
                plt.plot(zz,yyy,'b-',label='y='+str(round(para,4))+'x+'+str(round(bbb,4))) 
                buffer = BytesIO()
                plt.savefig(buffer)  
                plot_data = buffer.getvalue()
                label='y='+str(round(para,4))+'x+'+str(round(bbb,4))
                # 图像数据转化为 HTML 格式
                imb = base64.b64encode(plot_data)  
                #imb = plot_data.encode('base64')   # 对于 Python 2.7可用 
                ims = imb.decode()
                imd = "data:image/png;base64,"+ims
                iris_im = "<img src='%s'>" % imd 
                
                root = "<title>Iris Dataset</title>"
                root = root + iris_im+"<center><p style='width:965px; word-wrap:break-word;'><font size='6' >x-data:&nbsp;&nbsp;"+str(xx)+"</font></p></center>"+"<center><p style='width:965px; word-wrap:break-word;'><font size='6'>y-data:&nbsp;&nbsp;"+str(yy)+"</font></p></center>"+"<center><font size='12'><p> final  result:&nbsp;&nbsp;&nbsp;&nbsp;"+label+"</p></font></center>  <!--"
                plt.close()
                return root
        else:
           	return '''<center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="12" color="red">可能的错误原因</font></p></center>
    <p><font size="8" color="blue">1、在取对数的情况下，x,y输入中有小于或等于0的数</font></p>
    <p><font size="8" color="blue">2、数据之间的的符号不符合规范（必须是英文逗号“,”）</font></p>
    <p><font size="8" color="blue">3、x，y数据个数不相等</font></p>
    <p><font size="8" color="blue">4、服务器内部错误（概率特别低，除非我充的money已经没有了。或者很不巧，你使用那会我正在调试这部分程序的代码）</font></p><!--'''
    else:
        return '<h1>您的输入为空，请重新输入<h1><!--'

@app.get("/index")
def web_login():
    return template("index")


@app.get("/19")
def party():
    return template("19")

@app.get("/images/:filename")
def file_images(filename):
    return static_file(filename,root='images')

@app.get('/login')
def login():
    return log_in()

@app.post('/login')
def login():
    psd=request.forms.get('psd')
    if psd=='bhzf':
        return get_data()
    elif psd=='hfzf':
        return get_data1()
    	
    else:
        return '''<center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="12" color="red">您无权限访问此空间</font></p></center>
    <center><p><font size="12" color="red">您无权限访问此空间</font></p></center><!--'''
    
@app.get('/updata_data')
def up_date():
    return updata()

@app.post('/updata_data')
def up_data():
    name = request.forms.get('note')
    psd=request.forms.get('psd')
    title=request.forms.get('title')
    if name!='' and psd=='bh' and title!='':
        if name!='':
    			kv.set(str(int(time.time())),title.replace(' ','&nbsp;')+'###'+name.replace(' ','&nbsp;').replace('\r\n','<br>'))
    			return get_data()
    elif name!='' and psd=='hf' and title!='':
        if name!='':
    			kv.set(str(int(time.time())),title.replace(' ','&nbsp;')+'***'+name.replace(' ','&nbsp;').replace('\r\n','<br>'))
    			return get_data1()
    else:
        return  '''<center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center><center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center>
    <center><p><font size="2" color="blue">.</font></p></center><center><p><font size="12" color="red">您无权限保存内容</font></p></center><center><p><font size="12" color="red">您无权限保存内容</font></p></center><!--'''

@app.get("/other")
def other():
    return template("other")

application = sae.create_wsgi_app(app)
