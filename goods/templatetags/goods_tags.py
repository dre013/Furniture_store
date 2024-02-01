from django import template

from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    """
    Returns all categories using the simple tag decorator.
    """
    return Categories.objects.all()