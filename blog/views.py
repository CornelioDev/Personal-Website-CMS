from django.shortcuts import render
from .models import Article, Category

# Create your views here.
def list(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title':'Todos los artículos',
        'articles':articles
    })

def category(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, 'categories/category.html', {
        'title':category,
        'category':category
    })
