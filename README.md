# Django-myblog
Django入门与实践--Python制作个人博客网站，一个Python的高级Web框架，功能非常强大。

## 开发环境
1.Python  
2.Django   
3.编辑器  

## 搭建环境
Python一般在系统里面有默认的，不需要安装。当然如果你想升级Python3.x话也是可以的，但是Django同时支持2.x和3.x，为减少不必要的麻烦，建议使用默认的版本即可。

Django的安装，可以使用pip install Django==2.0（为什么我要选2.0版，因为我python是3.7.0版），也可以使用源码安装，从GitHub下载源码，然后通过python setup.py install安装。不同的Django对应不同的python版本，下面是Django官网版本对应参考。  
What Python version can I use with Django?  
Django version	Python versions  
1.11	2.7, 3.4, 3.5, 3.6, 3.7 (added in 1.11.17)  
2.0	3.4, 3.5, 3.6, 3.7  
2.1, 2.2	3.5, 3.6, 3.7  

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
