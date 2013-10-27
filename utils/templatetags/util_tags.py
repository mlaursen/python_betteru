from django import template

register = template.Library()

@register.simple_tag
def example(a1):
    return "string a1: %s" % a1
