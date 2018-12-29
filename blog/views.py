from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    # return HttpResponse('Hello, World!')
    # return render(request, 'blog/index.html',{'hello':'Hello，Blog!'})

    # article=models.Article.objects.get(pk=1)#传递article对象,id=1
    articles=models.Article.objects.all()#传递article对象,所有
    return render(request, 'blog/index.html',{'articles':articles})

def article_page(request, article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html',{'article':article})
