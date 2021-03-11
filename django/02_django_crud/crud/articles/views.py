from django.shortcuts import render, redirect
from .models import Article


def index(request):
    # 1.DB에 있는 순서를 파이썬이 변경
    # articles = Article.objects.all()[::-1]
    # 2. 처음부터 DB가 변경
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 
    article = Article(title=title, content=content)
    # 데이터 검증
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)
    context = {
        'title': title,
        'content': content,
    }

    # return redirect(f'/articles/{article.pk}/')
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    # 몇 번 글을 조회할건지 가져와야함.
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
    
