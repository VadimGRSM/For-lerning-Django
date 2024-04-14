from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def news_home(request):
    data = {
        'title': 'Новости',
        'news': Articles.objects.order_by('-data')[:20]
    }
    return render(request, 'news/news_home.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    data = {
        'title': 'Добавить запись',
        'form': ArticlesForm(),
        'error': error
    }
    return render(request, 'news/create.html', data)
