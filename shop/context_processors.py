from .models import Category


def categories_context(request,):
    categories = Category.objects.filter(parent=None)
    return {'categories_context': categories}

