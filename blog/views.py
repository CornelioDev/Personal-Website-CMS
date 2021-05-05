from django.shortcuts import get_object_or_404, render
from .models import Article, Category

# Create your views here.
def list(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title':'Todos los artículos',
        'articles':articles
    })

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category)

    return render(request, 'categories/category.html', {
        'category':category,
        'articles':articles
    })

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article':article
    })