# Django-myblog
Django入门与实践--Python制作个人博客网站，一个Python的高级Web框架，功能非常强大，下面是项目预览，随便找了一套前端模板，目前只做了主页和文章页的界面。  
## 项目预览  
![项目前端](/indexshow.jpg)  
![项目文章页](/article.jpg)  
![项目后台](/adminshow.png)  
## 开发环境
1.Python  
2.Django   
3.编辑器  
## 搭建环境
Python一般在系统里面有默认的，不需要安装。当然如果你想升级Python3.x话也是可以的，但是Django同时支持2.x和3.x，为减少不必要的麻烦，建议使用默认的版本即可。

Django的安装，可以使用pip install Django==2.0（为什么我要选2.0版，因为我python是3.7.0版），也可以使用源码安装，从GitHub下载源码，然后通过python setup.py install安装。  
不同的Django对应不同的python版本，下面是Django官网版本对应参考。  
What Python version can I use with Django?  
Django version	Python versions  
1.11	2.7, 3.4, 3.5, 3.6, 3.7 (added in 1.11.17)  
2.0	  3.4, 3.5, 3.6, 3.7  
2.1,  2.2	 3.5, 3.6, 3.7  

编辑器  
Pycharm（推荐）    
Eclipse  
Sublime Text  
Atom    

## 创建项目
diango-admin startproject myblog  

## 运行项目
先切换到myblog文件夹，输入以下命令运行项目     
F:\github-project\myblog>python manage.py runserver  
Performing system checks...  

System check identified no issues (0 silenced).  

You have 14 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth,   contenttypes, sessions.  
Run 'python manage.py migrate' to apply them.  
December 27, 2018 - 00:17:11  
Django version 2.0, using settings 'myblog.settings'  
Starting development server at http://127.0.0.1:8000/  
Quit the server with CTRL-BREAK.  

浏览器输入：127.0.0.1:8000
![django界面前端](/index.png)

## 开发步骤  
**生成数据表**  
1.命令行进入manage.py同级目录
2.执行python manage.py makemigrations app名（可选，不选创建全部）    
3.再执行python manage.py migrate  （生成移植文件Django-myblog\blog\migrations\0001_initial.py）

**查看生成表的SQL语句**  
1.命令行进入manage.py同级目录  
2.执行python manage.py sqlmigrate app名 文件ID(python manage.py sqlmigrate blog 0001)

**打开数据库编辑文章数据**
下载：sqlite expert personal  
或者用其他的数据管理软件，能管理sqlite3即可

**取出数据**  
views.py编写：  
```python
from . import models  
article=models.Article.objects.get(pk=1)#传递article对象  
return render(request, 'blog/index.html',{'article':article})  
```
template/blog/index.html编写：
```html
<h1>{{article.title}}</h1>  
<h3>{{article.content}}</h3>  
```
**admin创建超级用户**   
1.命令行进入manage.py同级目录  
2.执行python manage.py createsuperuser (回车)  
3.username:admin  
4.Password:100txycom  
5.http://127.0.0.1:8000/admin/ #登录后台  
6.设置中文LANGUAGE_CODE = 'zh_Hans'  

**配置admin应用**  
1.在应用下admin.py中引入自身的models模块（或里面模型的类）    
2.编辑admin.py:admin.site.register(models.Article)  
3.在blog/admin.py编辑  
```python
from django.contrib import admin  
from  .models import Article  

admin.site.register(Article)
```
**admin后台**  
![后台界面](/admin.jpg)  

**修改Article显示的标题**  
1.python3添加__str__(self)或__unicode_(self)  
2.return self.title
