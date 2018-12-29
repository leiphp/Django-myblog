from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    # return HttpResponse('Hello, World!')
    # return render(request, 'blog/index.html',{'hello':'Hello，Blog!'})

    article=models.Article.objects.get(pk=1)#传递article对象
    return render(request, 'blog/index.html',{'article':article})
