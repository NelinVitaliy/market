from django import template
from shop.models import Category

register = template.Library()


@register.simple_tag
def get_categories(n=6):
    all_categories = Category.objects.all()[0:n]
    return all_categories


