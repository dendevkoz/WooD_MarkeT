from django.shortcuts import render
from .models import ShoplistProduct, Category, Gallery
from django.http import Http404



# def index(request):
#     products = ShoplistProduct.objects.all()
#     category = Category.objects.all()
#     context = {'products': products, 'category': category}
#     return render(request, 'catalog.html', context)

def detail(request, product_id):
    try:
        products = ShoplistProduct.objects.get(pk=product_id)
    except ShoplistProduct.DoesNotExist:
        raise Http404("Product does not exist")
    cat = products.product_category
    related = ShoplistProduct.objects.filter(product_category=cat)[:4]
    color_product = products.add_color.all()
    size_product = products.add_size.all()
    return render(request, 'detail_sp.html', {'product': products, 'related': related, 'color_product': color_product, 'size_product': size_product})


def product_category(request, category_id=None):
    if category_id:
        categories = Category.objects.get(pk=category_id)
        products = ShoplistProduct.objects.filter(product_category=categories)
    else:
        products = ShoplistProduct.objects.all()
        # big_img = products.get_big_image()


    context = {'categories': Category.objects.all(), 'products': products}
    return render(request, 'catalog.html', context)


def gallery_product(request, image_id=1):
    # if image_id:
    #     gp = Gallery.objects.get(pk=image_id)
    # else:
    gp = Gallery.objects.get(image_id)
    context = {'gp': gp}
    return render(request, 'detail_sp.html', context)



