from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def home_list(request):
    categories = Category.objects.filter(parent=None)
    new_categories = []
    for category_id in categories:
        if category_id.children.all():
            new_categories.append(category_id)
        else:
            continue
    return render(request, 'shop/index.html', locals())


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(parent=None)
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        children = category.children.all()
    return render(request, 'shop/shop-left-sidebar.html', locals())


def get_all_products(request):
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/all-products.html', locals())


def get_all_category(request):
    categories = Category.objects.filter(parent=None)
    paginator = Paginator(categories, 9)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request, 'shop/all-category.html', locals())


def get_product_by_category(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    if request.GET.get('sort-by'):
        sort = request.GET.get('sort-by')
        if sort == 'desc':
            products = products.order_by('-cost')
        elif sort == 'asc':
            products = products.order_by('cost')
    return render(request, 'shop/get_product_by_category.html', locals())


@csrf_protect
def contact(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        message_name = request.POST.get['message_name']
        message_email = request.POST.get['message_email']
        message = request.POST.get['message']

        send_mail(message_name, message, message_email, ['vitaemarketmail@gmail.com'])
        return render(request, 'shop/contact.html', {'message_name': message_name})
    else:
        return render(request, 'shop/all-category.html')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'shop/single-product.html', {'product': product})


def contact_list(request):
    return render(request, 'shop/contact.html')


def base_list(request):
    return render(request, 'shop/base.html')


def wholesalers_list(request):
    return render(request, 'shop/wholesalers.html')
