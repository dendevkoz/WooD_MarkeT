from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticles, CategoryArticles
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .forms import NameForm


def index(request, key_id=None):
    dict_cat = {}
    categories = CategoryArticles.objects.all()
    articles = BlogArticles.objects.all()
    recents_post = BlogArticles.objects.order_by('pub_date')[::-1]
    for item in categories:
        dict_cat[item] = BlogArticles.objects.filter(product_category=item).count()
    if key_id:
        categories = CategoryArticles.objects.get(pk=key_id)
        articles = BlogArticles.objects.filter(product_category=categories)
    else:
        print('No articles are available.')
    context = {'articles': articles, 'categories': categories,
               'recents_post': recents_post, 'dict_cat': dict_cat}
    return render(request, 'index.html', context)


def detail(request, articles_id):
    try:
        articles = BlogArticles.objects.get(pk=articles_id)
    except BlogArticles.DoesNotExist:
        raise Http404("Article does not exist")
    cat = articles.product_category
    related = BlogArticles.objects.filter(product_category=cat)[:4]
    return render(request, 'detail.html', {'articles': articles, 'related': related})

# def detail_cat(request, cat_id):
#     categories = CategoryArticles.objects.get(pk=cat_id)
#     cat = BlogArticles.objects.filter(product_category=categories)
#     context = {'categories': cat}
#     return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('thanks/')

    else:
        form = NameForm()

    return render(request, 'contact.html', {'form': form})


def thank_you(request):
    context = {}
    return render(request, 'thank_you.html', context)