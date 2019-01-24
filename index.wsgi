# encoding=utf8
'''
@author:zhangfan
@email:zf083415@gmail.com
@code_upload_website:


 
 　　　　　　　 ┏┓       ┏┓+ +
 　　　　　　　┏┛┻━━━━━━━┛┻┓ + +
 　　　　　　　┃　　　　　　 ┃
 　　　　　　　┃　　　━　　　┃ ++ + + +
 　　　　　　 █████━█████  ┃+
 　　　　　　　┃　　　　　　 ┃ +
 　　　　　　　┃　　　┻　　　┃
 　　　　　　　┃　　　　　　 ┃ + +
 　　　　　　　┗━━┓　　　 ┏━┛
                  ┃　　  ┃
 　　　　　　　　　┃　　  ┃ + + + +
 　　　　　　　　　┃　　　┃　Code is far away from bug with the animal protecting
 　　　　　　　　　┃　　　┃ + 　　　　         神兽保佑,代码无bug
 　　　　　　　　　┃　　　┃
 　　　　　　　　　┃　　　┃　　+
 　　　　　　　　　┃　 　 ┗━━━┓ + +
 　　　　　　　　　┃ 　　　　　┣┓
 　　　　　　　　　┃ 　　　　　┏┛
 　　　　　　　　　┗┓┓┏━━━┳┓┏┛ + + + +
 　　　　　　　　　 ┃┫┫　 ┃┫┫
 　　　　　　　　　 ┗┻┛　 ┗┻┛+ + + +
'''


'''导入用到的相关模块'''
import sae,numpy,math
import sae.kvdb
import time,datetime
import urllib2
import re
#导入Bottle中的功能模块
from bottle import Bottle,route, run, template, request, response,  post, get,static_file,debug
app=Bottle()
debug(True)  #打开debug功能
import matplotlib.pyplot as plt
from io import BytesIO
import base64


kv = sae.kvdb.Client()  #引入一个kvdb客户端



###############################################
################函数功能块区####################
###############################################
'''线性回归方程计算输入页面函数'''
def linear_input():
    page='''<html>
    <head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
    <br/>
    <title>线性回归方程求解</title>
    </head>
    <body>
    <center><h1><font  color="red">线性回归方程求解</font></h1></center>'''
    page=page+'''
    <h4><font  color="green">友情链接</font></h4>
    <div id="navfirst">
<ul id="menu"><h4>
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="blue">十九大报告中英文全文</font></a></li>
<li id="ho"><a href="http://1.liuwen.applinzi.com/login"><font  color="blue">我的云笔记</font></a></li></h4>
</ul>
</div>
<center><p><font  color="red">各个数据之间用英文逗号隔开</font></p></center>
    <form method = "POST" id="form">
    <h3><font  color="red">请输x内容</font>
    <input name="x" style='width:95%;background: #F0F8FF;' /></h3>
    <h3><font  color="red">请输y内容</font>
    <input name="y" style='width:95%;background: #F0F8FF;' /></h3><h3>
    <label>
    <input type="radio"  name ="log" value="yes" >取对数
    </label>
    <label>
　　<input type="radio"  name ="log" value="no" checked>不取对数
  	</label></h3>
    <h3><br/>
    <input type='submit' style='background: #F0F8FF;' value='确定' /></h3>
  	</form>
    </body> </html><!--'''
    return page


'''登陆页面函数'''
def log_in():
    page='''<form method = "POST" id="login">
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>'''
    page=page+'''<br/>
    <br/>'''
    page=page+'''<br/><br/><br/>
    <h1><font  color="green">密码</font>
    <input name="psd" type='password' style='font-size:80px;background: #F0F8FF;' size=18/></h1>
   <br/><br/><br/>
    <input type='submit' style='font-size:80px;background: #F0F8FF;' value='登陆' /></h3>
  	</form><!--'''
    return page


'''线性回归方程计算函数'''
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


'''线性回归方程绘图及post页面生成函数'''
def linear_plot():
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
            return '''<br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <center><p><font  color="red">x，y个数不相等，请检查后重新输入</font></p></center>
    <center><p><font  color="red">x，y个数不相等，请检查后重新输入</font></p></center><!--'''
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
           	return '''<br/>
    <br/><br/><br/><br/><br/><br/>
    <center><p><font  color="red">可能的错误原因</font></p></center>
    <p><font  color="blue">1、在取对数的情况下，x,y输入中有小于或等于0的数</font></p>
    <p><font  color="blue">2、数据之间的的符号不符合规范（必须是英文逗号“,”）</font></p>
    <p><font  color="blue">3、x，y数据个数不相等</font></p>
    <p><font  color="blue">4、服务器内部错误（概率特别低，除非我充的money已经没有了。或者很不巧，你使用那会我正在调试这部分程序的代码）</font></p><!--'''
    else:
        return '<h1>您的输入为空，请重新输入<h1><!--'


'''我的私人云笔记页面生成函数'''    
def cloud_note():   
    page='''<html>
    <head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
    <br/>
    <title>我的云笔记</title>
    </head>
    <body>
    <center><h1><font  color="red">我的云笔记</font></h1></center>
    <br/>
    <h4><font  color="green">友情链接</font></h4>
    <div id="navfirst">
<ul id="menu"><h4>
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
<li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
<li id="h"><a href="/english" title="英语阅读练习"><font  color="#0d47a1">共享英语阅读</font></a></li><br/>
<li id="h"><a href="/learn" title="学习网站推荐"><font  color="#0d47a1">学习网站推荐</font></a></li><br/>
<li id="h"><a href="/update_article" title="更新文章"><font  color="#0d47a1">更新文章</font></a></li><br/>
<li id="o"><a href="http://1.liuwen.applinzi.com/update_data" title="上传数据" target="_blank"><font  color="green">上传文章</font></a></li><br/>
<li id="ho"><a href="http://1.liuwen.applinzi.com/note"><font  color="#0d47a1">共享云笔记</font></a></li><br/>
<li id="ho"><a href="/"><font  color="#0d47a1">网站网页导航页面</font></a></li></h4>
</ul>
</div>'''
    page=page+'''
<br/>
    <center><h2><font  color="blue">笔记内容</font></h2></center>
    <br/>
'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    n=1
    for i in data:
        text=kv.get(i)
        if '######' in text:
            title=text.split('######')[0]
            content=text.split('######')[1]
            page=page+'<h3><font  color="red"><center>&nbsp;&diams;&nbsp;&nbsp;'+str(n)+'、'+title+'</center></font></h3>'+'<center><font ><p>上传日期：&nbsp;'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i)))).replace(' ','&nbsp;')+'</p></font></center>'
            page=page+'<p style="width:100%; word-wrap:break-word;">'
            page=page+'<font >&nbsp;&nbsp;&nbsp;&nbsp;'+content
            page=page+'</font></p>'
            n=n+1     
    page=page+'</body> </html><!--'
    return page


'''我的私人云日记页面生成函数'''    
def diary(): #get_data1()
    page='''<html>
    <head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
    <br/>
    <title>我的云笔记</title>
    </head>
    <body>
    <center><h1><font  color="red">我的每日记录</font></h1></center>
    <br/>
    <h4><font  color="green">友情链接</font></h4>
    <div id="navfirst"><h4>
<ul id="menu"><h4>
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
<li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
<li id="h"><a href="/english" title="英语阅读练习"><font  color="#0d47a1">共享英语阅读</font></a></li><br/>
<li id="h"><a href="/learn" title="学习网站推荐"><font  color="#0d47a1">学习网站推荐</font></a></li><br/>
<li id="h"><a href="/update_article" title="更新文章"><font  color="#0d47a1">更新文章</font></a></li><br/>
<li id="o"><a href="http://1.liuwen.applinzi.com/update_data" title="上传数据" target="_blank"><font  color="green">上传文章</font></a></li><br/>
<li id="ho"><a href="http://1.liuwen.applinzi.com/note"><font  color="#0d47a1">共享云笔记</font></a></li><br/>
<li id="ho"><a href="/"><font  color="#0d47a1">网站网页导航页面</font></a></li></h4>

</ul>
</div>
'''
    page=page+'''
<br/>
    <center><h2><font  color="blue">记录详情</font></h2></center>
    <br/>
'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    n=1
    for i in data:
        text=kv.get(i)
        if '******' in text:
            title=text.split('******')[0]
            content=text.split('******')[1]
            page=page+'<h3><font color="red"><center>&nbsp;&diams;&nbsp;&nbsp;'+str(n)+'、'+title+'</center></font></h3>'+'<center><font ><p>上传日期：&nbsp;'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i)))).replace(' ','&nbsp;')+'</p></font></center>'
            page=page+'<p style="width:100%; word-wrap:break-word;">'
            page=page+'<font >&nbsp;&nbsp;&nbsp;&nbsp;'+content
            page=page+'</font></p>'
            n=n+1   
    page=page+'</body> </html><!--'
    return page


'''上传数据功能函数【数据包括日记、笔记、文章等】'''
def upload_data():  #updata
    page='''<html>
    <head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
    <br/>
    <title>数据上传页面</title>
    </head>
    <body>
    <center><h1><font  color="#01579b">数据上传</font></h1></center>
    <br/>
    <h4><font color="green">其他链接</font></h4>
    <div id="navfirst">
<ul id="menu"><h4>
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
<li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
<li id="h"><a href="/english" title="英语阅读练习"><font  color="#0d47a1">共享英语阅读</font></a></li><br/>
<li id="h"><a href="/learn" title="学习网站推荐"><font  color="#0d47a1">学习网站推荐</font></a></li><br/>
<li id="h"><a href="/update_article" title="更新文章"><font  color="#0d47a1">更新文章</font></a></li><br/>
<li id="o"><a href="http://1.liuwen.applinzi.com/update_data" title="上传数据" target="_blank"><font  color="green">上传文章</font></a></li><br/>
<li id="ho"><a href="http://1.liuwen.applinzi.com/note"><font  color="#0d47a1">共享云笔记</font></a></li><br/>
<li id="ho"><a href="/"><font  color="#0d47a1">网站网页导航页面</font></a></li></h4>

</ul>
</div>
    <form method = "POST" id="form">
    <br/><br/><br/>
    <center><h3><font  color="green">请输入保存数据权限码</font></h3></center>
   <center> <input name="psd" style="width:100%;background: #F0F8FF;" placeholder="请输入保存数据权限码[必填项]"/></center>
   <center><h3><font  color="green">请输入标题</font></h3></center>
   <center> <input name="title" style="width:95%;background:#F0F8FF;" placeholder="请输入标题[必填项]" /></center>
    <br/>
    <center><button type="submit"  form="form"><h1>提交<br></h1></button></center>
    <br/> <br/>
    <center><h3><font  color="red">请输入内容</font></h3></center>
		<center><textarea name="note" style="width:100%;background: #F0F8FF;" placeholder="请输入要保存的文章或者笔记内容[非空]" cols="45" rows="20"></textarea></center>
	</form>
 <br/> <br/>
	'''
    page=page+'</body> </html><!--'
    return page


'''更新文章选择页面函数'''
def choose_to_update():
    page='''<html>
    <head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
        <br/>
    <title>文章更新页面</title>
    </head>
    <body>
    <center><h1><font  color="red">文章更新管理页面</font></h1></center>
    <br/>
    <h5><font  color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="blue">十九大报告中英文全文</font></a></li>
</ul>
</div>
    <form method = "POST" id="form">
    <font  ><p>
    <label><p>
    <input type="radio"  name ="log" value="1" checked>国际新闻类文章</p>
    </label>
    <label><p>
　　<input type="radio"  name ="log" value="2" >商业经济类文章</p>
  	</label>
    <label><p>
    <input type="radio"  name ="log" value="3" >科技类文章</p>
    </label>
    <label><p>
　　<input type="radio"  name ="log" value="4" >教育类文章</p>
  	</label>
    <label><p>
    <input type="radio"  name ="log" value="5" >文化类文章</p>
    </label>
    <label><p>
　　<input type="radio"  name ="log" value="6" >科学类文章</p>
  	</label>
    <label><p>
　　<input type="radio"  name ="log" value="7" >观点类文章</p>
  	</label></p>
    <label><p>
　　<input type="radio"  name ="log" value="8" >健康类文章</p>
  	</label>
    <label><p>
　　<input type="radio"  name ="log" value="9" >旅游类文章</p>
  	</label></p>
    </font>
    <h1><input type='submit' style='background: #F0F8FF;' value='确认更新选定的文章' /></h1>
	</form>
    </body> </html><!--'''
    return page


'''更新文章功能函数【实质是爬虫——爬取数据、解析数据、再按自己要求重新组装数据,然后存入kvdb】'''
def update_article():
    num=request.forms.get('log')
    url=[('http://www.qqenglish.com/bn/bn/','国际新闻类文章'),('http://www.qqenglish.com/bn/business/','商业经济类文章'),\
             ('http://www.qqenglish.com/bn/technology/','科技类文章'),('http://www.qqenglish.com/bn/education/','教育类文章'),\
             ('http://www.qqenglish.com/bn/culture/','文化类文章'),('http://www.qqenglish.com/bn/science/','科学类文章'),\
             ('http://www.qqenglish.com/bn/opinion/','观点类文章'),('http://www.qqenglish.com/bn/health/','健康类文章'),('http://www.qqenglish.com/bn/travel/','旅游类文章')]
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
            <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
            <title>'''
            m=m+url[1]+'''</title>
            </head>
            <body>
            <center><a href="/notice" title="公告"><font  color="red"><p>[置顶公告]:文章内容来自蛐蛐英语阅读网[http://qqenglish.com/]</p></font></a></center>
            <center><h3><font  color="#01579b">英语阅读练习——by zf</font></h3></center> 
            <br/><br/>
            <div id="navfirst">
            <ul id="menu"><h4>
            <li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
            <li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
            <li id="b"><a href="/business" title="商业经济类文章"><font  color="#0d47a1">商业经济类文章</font></a></li><br/>
            <li id="s"><a href="/technology" title="科技类文章"><font  color="#0d47a1">科技类文章</font></a></li><br/>
            <li id="d"><a href="/education" title="教育类文章"><font  color="#0d47a1">教育类文章</font></a></li><br/>
            <li id="x"><a href="/culture" title="文化类文章"><font  color="#0d47a1">文化类文章</font></a></li><br/>
            <li id="ws"><a href="/science" title="科学类文章"><font  color="#0d47a1">科学类文章</font></a></li><br/>
            <li id="w"><a href="/opinion" title="观点类文章"><font  color="#0d47a1">观点类文章</font></a></li><br/>
            <li id="ws"><a href="/health" title="科学类文章"><font  color="#0d47a1">健康类文章</font></a></li><br/>
            <li id="w"><a href="/tour" title="观点类文章"><font  color="#0d47a1">旅游类文章</font></a></li><br/>
            <li id="ho"><a href="/"><font  color="#0d47a1">网站网页导航页面</font></a></li></h4></h4>
            </ul>
            </div><br/><br/>'''
            for i in urls[:10]:
                try:
                    #time.sleep(random.randint(3,6))
                    #print(i[0],'http://www.qqenglish.com'+i[1])
                    req = urllib2.Request('http://www.qqenglish.com'+i[1],headers=header)
                    res = urllib2.urlopen(req)
                    text=res.read().decode("GBK").encode("utf8")
                   
                    title=re.compile('<H2>(.*?)</H2>').findall(text)[0]
                    data= re.compile(r'</script></div>(.*?)全文请访问',re.DOTALL).findall(text)[0].replace('</div>','').replace('<FONT color=#666666>“','')[:-4]
                    m=m+'<center><h3><font>第'+str(n)+'篇文章</font></h3></center>\n'
                    m=m+'<center><h3><font color="#01579b">'+str(title)+'</font></h3></center>\n'
                    m=m+'<center><p><b>日期-'+str(i[0])+'</b></p></center>\n'
                    m=m+'<font  face="arial">'
                    m=m+data
                    m=m+'</font>'
                    m=m+'\n\n'
                    n=n+1
                    
                except:
                    pass
            m=m+'</body> </html><!--'
            kv.set(str(int(time.time())),'###article###'+m)
            return '''<br/><br/><br/><br/><br/><br/><br/><br/>
    <center><h1><font  color="red">更新完成</font></h1></center>
    <center><h1><font  color="red">更新完成</font></h1></center><!--'''
    else:
        return '<center><h1>您的输入为空，请重新输入<h1></center>'


'''导航页面生成函数'''
def navigation_page():
    page='''<!doctype html>
            <html>
            <head>
            <meta charset="utf8">
            <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
            <title>网站导航页面</title>
            </head>
            <body>
            <center><h1><font  color="#01579b">网站导航页面</font></h1></center> 
            <br/><br/>
            <div id="navfirst">
            <ul id="menu"><h4>
            <li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
            <li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
            <li id="b"><a href="/business" title="商业经济类文章"><font  color="#0d47a1">商业经济类文章</font></a></li><br/>
            <li id="s"><a href="/technology" title="科技类文章"><font  color="#0d47a1">科技类文章</font></a></li><br/>
            <li id="d"><a href="/education" title="教育类文章"><font  color="#0d47a1">教育类文章</font></a></li><br/>
            <li id="x"><a href="/culture" title="文化类文章"><font  color="#0d47a1">文化类文章</font></a></li><br/>
            <li id="ws"><a href="/science" title="科学类文章"><font  color="#0d47a1">科学类文章</font></a></li><br/>
            <li id="w"><a href="/opinion" title="观点类文章"><font  color="#0d47a1">观点类文章</font></a></li><br/>
            <li id="ws"><a href="/health" title="科学类文章"><font  color="#0d47a1">健康类文章</font></a></li><br/>
            <li id="w"><a href="/tour" title="观点类文章"><font  color="#0d47a1">旅游类文章</font></a></li><br/>
            <li id="o"><a href="/learn" title="其他网站推荐" target="_blank"><font  color="#0d47a1">其他学习网站推荐</font></a></li>
            <li id="h"><a href="/english" title="英语阅读练习"><font  color="#0d47a1">共享英语阅读</font></a></li><br/>
            <li id="h"><a href="/learn" title="学习网站推荐"><font  color="#0d47a1">学习网站推荐</font></a></li><br/>
            <li id="h"><a href="/update_article" title="更新文章"><font  color="#0d47a1">更新文章</font></a></li><br/>
            <li id="o"><a href="http://1.liuwen.applinzi.com/update_data" title="上传数据" target="_blank"><font  color="green">上传数据</font></a></li><br/>
            <li id="ho"><a href="http://1.liuwen.applinzi.com/note"><font  color="#0d47a1">共享云笔记</font></a></li><br/>
            <li id="ho"><a href="http://1.liuwen.applinzi.com/login"><font  color="#0d47a1">私有云笔记</font></a></li><br/></h4>
            </ul>
            </div>
          <center><p><font>站长：zf</font></p></center></body> </html><!--'''
    return page



'''英语阅读练习页面内容生成函数'''
def get_english():
    page='''<html>
    <head>
    <meta charset="utf8">
    <br/><br/>
    <title>共享英语阅读练习</title>
     <meta name="viewport" content="width=device-width, initial-scale=1" />
    </head>
    <body>
    <center><a href="/enuse" title="共享英语阅读使用教程"><font  color="red"><p>共享英语阅读使用教程</p></font></a></center>
    <center><h1><font color="#01579b">共享英语阅读</font></h1></center>
    <br/>
    <h4><font  color="green">其他链接</font></h4>
    <div id="navfirst">
<ul id="menu"><h4>
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
<li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
<li id="h"><a href="/english" title="英语阅读练习"><font  color="#0d47a1">共享英语阅读</font></a></li><br/>
<li id="h"><a href="/learn" title="学习网站推荐"><font  color="#0d47a1">学习网站推荐</font></a></li><br/>
<li id="h"><a href="/update_article" title="更新文章"><font  color="#0d47a1">更新文章</font></a></li><br/>
<li id="o"><a href="http://1.liuwen.applinzi.com/update_data" title="上传数据" target="_blank"><font  color="green">上传文章</font></a></li><br/>
<li id="ho"><a href="http://1.liuwen.applinzi.com/note"><font  color="#0d47a1">共享云笔记</font></a></li><br/>
<li id="ho"><a href="/"><font  color="#0d47a1">网站网页导航页面</font></a></li></h4>
</ul>
</div>
'''
    page=page+'''
<br/>
    <br/>
'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    content_box=[]
    if data:
        n=1
        for i in data:
            text=kv.get(i)
            page1=''
            if '####english####' in text:
                title=text.split('####english####')[0]
                content=text.split('####english####')[1]
                page1=page1+'<h3 style="width:100%; word-wrap:break-word;"><font  color="#01579b"><center>&nbsp;&diams;&nbsp;&nbsp;<b>第'+str(n)+'篇文章</font><br/>'+title+'</center></h3>'+'<center><font ><p>上传日期：&nbsp;'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i)))).replace(' ','&nbsp;')+'</b></p></font></center>'
                page1=page1+'<p style="width:100%; word-wrap:break-word;">'
                page1=page1+'<font >&nbsp;&nbsp;&nbsp;&nbsp;'+content
                page1=page1+'</font></p>'
                content_box.append(page1)
                n=n+1
        for p in range(len(content_box)):
            page=page+content_box[len(content_box)-p-1]
        page=page+'</body> </html><!--'
        return page
    else:
        page=page+'</body> </html><!--'
        return page
    

'''共享笔记页面生成函数'''
def get_note():
    page='''<html>
    <head>
    <meta charset="utf8">
    <br/><br/>
    <title>共享笔记</title>
     <meta name="viewport" content="width=device-width, initial-scale=1" />
    </head>
    <body>
    <center><a href="/noteuse" title="共享笔记使用教程"><font  color="red"><p>共享笔记使用教程</p></font></a></center>
    <center><h1><font color="#01579b">共享笔记</font></h1></center>
    <br/>
    <h4><font  color="green">其他链接</font></h4>
    <div id="navfirst">
<ul id="menu"><h4>
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font  color="#0d47a1">十九大报告中英文全文</font></a></li><br/>
<li id="h"><a href="/bn" title="国际新闻类文章"><font  color="#0d47a1">国际新闻类文章</font></a></li><br/>
<li id="h"><a href="/english" title="英语阅读练习"><font  color="#0d47a1">共享英语阅读</font></a></li><br/>
<li id="h"><a href="/learn" title="学习网站推荐"><font  color="#0d47a1">学习网站推荐</font></a></li><br/>
<li id="h"><a href="/update_article" title="更新文章"><font  color="#0d47a1">更新文章</font></a></li><br/>
<li id="o"><a href="http://1.liuwen.applinzi.com/update_data" title="上传数据" target="_blank"><font  color="green">上传文章</font></a></li><br/>
<li id="ho"><a href="http://1.liuwen.applinzi.com/note"><font  color="#0d47a1">共享云笔记</font></a></li><br/>
<li id="ho"><a href="/"><font  color="#0d47a1">网站网页导航页面</font></a></li></h4>
</ul>
</div>
'''
    page=page+'''
<br/>
    <center><h1><font color="#01579b">笔记详情</font></h1></center>
    <br/>
'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    content_box=[]
    if data:
        n=1
        for i in data:
            text=kv.get(i)
            page1=''
            if '####note####' in text:
                title=text.split('####note####')[0]
                content=text.split('####note####')[1]
                page=page+'<h3 style="width:100%; word-wrap:break-word;"><font  color="#01579b"><center>&nbsp;&diams;&nbsp;&nbsp;第'+str(n)+'个笔记</font><br/>'+title+'</center></h3>'+'<center><font ><p><b>上传日期：&nbsp;'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i)))).replace(' ','&nbsp;')+'</b></p></font></center>'
                page=page+'<p style="width:100%; word-wrap:break-word;">'
                page=page+'<font >&nbsp;&nbsp;&nbsp;&nbsp;'+content
                page=page+'</font></p>'
                content_box.append(page)
                n=n+1
        page=page+'</body> </html><!--'
        return page
    else:
        page=page+'</body> </html><!--'
        return page


'''上传数据保存分区判断'''
def data_judgment():
    name = request.forms.get('note')
    psd=request.forms.get('psd')
    title=request.forms.get('title')
    if name!='' and psd=='****' and title!='':
        if name!='':
            kv.set(str(int(time.time())),title.replace(' ','&nbsp;')+'######'+name.replace(' ','&nbsp;').replace('\r\n','<br>'))
            return cloud_note()
    elif name!='' and psd=='*****' and title!='':
        if name!='':
            kv.set(str(int(time.time())),title.replace(' ','&nbsp;')+'******'+name.replace(' ','&nbsp;').replace('\r\n','<br>'))
            return diary()
    elif name!='' and psd=='submit' and title!='':
        if name!='':
            kv.set(str(int(time.time())),title.replace(' ','&nbsp;')+'####english####'+name.replace(' ','&nbsp;').replace('\r\n','<br>'))
            return get_english()
        
    elif name!='' and psd=='mynote' and title!='':
        if name!='':
            kv.set(str(int(time.time())),title.replace(' ','&nbsp;')+'####note####'+name.replace(' ','&nbsp;').replace('\r\n','<br>'))
            return get_note()
    elif name!='' and psd=='*****':
        if name!='':
            data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
            for i in data:
                text=kv.get(i)
                if '######' in text and name in text:
                    kv.delete(i)
        return cloud_note()
    elif name!='' and psd=='*****':
        if name!='':
            data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
            for i in data:
                text=kv.get(i)
                if '******' in text and name in text:
                    kv.delete(i)
        return diary()
    elif name!='' and psd=='delete':
        if name!='':
            data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
            for i in data:
                text=kv.get(i)
                if '####english####' in text and name in text:
                    kv.delete(i)
        return get_english()
    elif name!='' and psd=='notego':
        if name!='':
            data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
            for i in data:
                text=kv.get(i)
                if '####note####' in text and name in text:
                    kv.delete(i)
        return get_note()
    else:
        return  '''<br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <center><h1><font  color="red">您无权限保存内容</font></h1>
    </center><center><h1><font  color="red">您无权限保存内容</font></h1>
    </center><!--'''


'''私人云笔记登陆验证函数'''
def login_judgment():
    psd=request.forms.get('psd')
    if psd=='123446':
        return cloud_note()
    elif psd=='4546125':
        return diary()
    	
    else:
        return '''<br/><br/><br/><br/><br/><br/><br/>
    <center><h1><font  color="red">您无权限访问此空间</font></h1></center>
    <center><h1><font  color="red">您无权限访问此空间</font></h1></center><!--'''
    

    
'''共享笔记使用教程页面函数'''
def note_use():
    page='''<html>
    <head>
    <meta charset="utf8">
    <br/><br/>
    <title>共享笔记</title>
     <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:2%;
                margin-bottom:40px;
            }
        </style>
    </head>
    <body>
    <center><h1><font color="#01579b">共享笔记使用方法如下所示</font></h1></center>
    <br/><br/><br/>
    <p>1、打开网址http://1.liuwen.applinzi.com/note，进入共享笔记页面</p><br/>
    <center><img src="/images/note1.png" width="80%" /></center>
    <br/><br/><br/>
    <p>2、点击上部导航栏中绿色字<上传文章>，进入上传文章页面</p><br/>
    <center><img src="/images/note2.png"   width="80%"/></center>
    <br/><br/><br/>
    <p>3、输入共享笔记数据保存权限码<mynote>，笔记的标题以及笔记内容，然后点击页面中部的按钮<提交></p><br/>
    <center><img src="/images/note3.png"   width="80%"/></center>
    <br/><br/><br/>
    <p>4、点击提交按钮后会保存数据并跳转到共享笔记页面，如下图所示，笔记内容已成功保存</p><br/>
    <center><img src="/images/note4.png"  width="80%"/></center>
    <br/><br/><br/>
    <p>5、如果想要删除保存的笔记，重复布奏1、2，在保存数据的权限码中输入notego,标题一栏中不用输入，内容一栏中输入要删除的笔记的部分内容段【最好不要少于十个字，以防止误删】。然后点击提交按钮</p><br/>
    <center><img src="/images/note5.png"  width="80%" /></center>
    <br/><br/><br/>
    <p>6、如下图所示，目标笔记内容及标题已成功删除</p><br/>
    <center><img src="/images/note6.png"  width="80%" /></center>
    <center><h2>教程完</h2></center></body> </html><!--
    '''
    return page



'''共享英语阅读使用教程页面函数'''
def en_use():
    page='''<html>
    <head>
    <meta charset="utf8">
    <br/><br/>
    <title>共享笔记</title>
     <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:2%;
                margin-bottom:40px;
            }
        </style>
    </head>
    <body>
    <center><h1><font color="#01579b">共享笔记使用方法如下所示</font></h1></center>
    <br/><br/><br/>
    <p>1、打开网址http://1.liuwen.applinzi.com/english，进入共享英语阅读页面</p><br/>
    <center><img src="/images/en1.png" width="80%" /></center>
    <br/><br/><br/>
    <p>2、点击上部导航栏中绿色字<上传文章>，进入上传文章页面</p><br/>
    <center><img src="/images/en2.png"   width="80%"/></center>
    <br/><br/><br/>
    <p>3、输入共享笔记数据保存权限码<submit>，英语阅读的标题以及英语阅读内容，然后点击页面中部的按钮<提交></p><br/>
    <center><img src="/images/en3.png"   width="80%"/></center>
    <br/><br/><br/>
    <p>4、点击提交按钮后会保存数据并跳转到共享英语阅读页面，如下图所示，笔记英语阅读内容已成功保存</p><br/>
    <center><img src="/images/en4.png"  width="80%"/></center>
    <br/><br/><br/>
    <p>5、如果想要删除保存的英语阅读，重复布奏1、2，在保存数据的权限码中输入delete,标题一栏中不用输入，内容一栏中输入要删除的英语阅读的部分内容段【最好不要少于十个字或单词，以防止误删】。然后点击提交按钮</p><br/>
    <center><img src="/images/en5.png"  width="80%" /></center>
    <br/><br/><br/>
    <p>6、如下图所示，目标英语阅读内容及标题已成功删除</p><br/>
    <center><img src="/images/en6.png"  width="80%" /></center>
    <center><h2>教程完</h2></center></body> </html><!--
    '''
    return page
#################################################
###################函数功能区结束#################
#################################################




#################################################
############定义路由，即浏览器访问的地址############
#################################################


'''定义线性回归方程输入页面浏览器访问的地址'''
@app.get('/linear')
def data():
    return linear_input()

'''定义线性回归方程计算结果及生成图片页面浏览器访问的地址'''
@app.post('/linear')
def plot_data():
    return linear_plot()

'''定义国际新闻类文章页面浏览器访问的地址'''
@app.get("/bn")
def bn():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>国际新闻类文章</title>' in text:
            return text.split('###article###')[1]


'''定义商业经济类文章页面浏览器访问的地址'''
@app.get("/business")
def business():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>商业经济类文章</title>' in text:
            return text.split('###article###')[1]


'''定义科技类文章页面浏览器访问的地址'''
@app.get("/technology")
def technology():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>科技类文章</title>' in text:
            return text.split('###article###')[1]


'''定义教育类文章页面浏览器访问的地址'''
@app.get("/education")
def education():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>教育类文章</title>' in text:
            return text.split('###article###')[1]


'''定义文化类文章页面浏览器访问的地址'''
@app.get("/culture")
def culture():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>文化类文章</title>' in text:
            return text.split('###article###')[1]


'''定义科学类文章页面浏览器访问的地址'''
@app.get("/science")
def science():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>科学类文章</title>' in text:
            return text.split('###article###')[1]


'''定义观点类文章页面浏览器访问的地址'''
@app.get("/opinion")
def opinion():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>观点类文章</title>' in text:
            return text.split('###article###')[1]


'''定义健康类文章页面浏览器访问的地址'''
@app.get("/health")
def health():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>健康类文章</title>' in text:
            return text.split('###article###')[1]


'''定义旅游类文章页面浏览器访问的地址'''
@app.get("/tour")
def tour():
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        text=kv.get(i)
        if '###article###' in text and '<title>旅游类文章</title>' in text:
            return text.split('###article###')[1]


'''定义更新文章get请求页面浏览器访问的地址'''
@app.get('/update_article')
def login_form():
    return choose_to_update()


'''定义更新文章post请求页面浏览器访问的地址'''
@app.post('/update_article')
def login():
    return update_article()



'''定义置顶公告详情页面浏览器访问的地址'''
@app.get('/notice')
def notice():
    return '''<br/><br/><br/><br/><center><h2><font  color="red">公告：文章内容来自蛐蛐英语阅读网[http://qqenglish.com/] ，为了维护原网站权益，请尽量去蛐蛐英语阅读网阅读
            （备注：因为原网站手机阅读体验不佳（字体太小，看着太累），所以才建立了该网站，建立该网站的初衷是为了自用，学习英语（我还是一个学僧：)：)：)），
            而不是为了盈利，希望可以帮助到学习英语的同学）</font></h2></center><!--'''


'''定义导航页面浏览器访问的地址'''
@app.get('/')
def navigation():
    return navigation_page()


'''共享英语阅读练习页面浏览器访问的地址'''
@app.get("/english")
def english():
    return get_english()


'''共享笔记练习页面浏览器访问的地址'''
@app.get("/note")
def english():
    return get_note()


'''bottle模板引擎c测试页面浏览器访问的地址'''
@app.get("/index")
def test():
    return template("index")


'''学习类网站推荐页面浏览器访问的地址'''
@app.get("/learn")
def learn():
    return template("learn")


'''19大报告中英文页面浏览器访问的地址'''
@app.get("/19")
def party():
    return template("19")


'''图片静态资源访问路由'''
@app.get("/images/:filename")
def file_images(filename):
    return static_file(filename,root='images')


'''私人云日记及私人云笔记登陆入口页面浏览器访问的地址[get请求]'''
@app.get('/login')
def login():
    return log_in()


'''私人云日记及私人云笔记登陆入口页面浏览器访问的地址[post请求]'''
@app.post('/login')
def login():
    return login_judgment()
    

'''数据上传页面浏览器访问的地址[get请求]'''
@app.get('/update_data')
def up_date():
    return upload_data()


'''数据上传页面浏览器访问的地址[post请求]'''
@app.post('/update_data')
def up_data():
    return data_judgment()


'''页面浏览器访问的地址[post请求]'''
@app.get("/other")
def other():
    return template("other")



'''共享笔记使用教程页面浏览器访问的地址'''
@app.get('/noteuse')
def noteuse():
    return note_use()



'''共享英语阅读使用教程页面浏览器访问的地址'''
@app.get('/enuse')
def enuse():
    return en_use()


application = sae.create_wsgi_app(app)


###########END#############
