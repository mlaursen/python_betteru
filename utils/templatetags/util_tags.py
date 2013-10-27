from django import template

from utils.util import HtmlTag

register = template.Library()

@register.simple_tag
def tag(name, content='', tclass=False, tid=False, other=False):
    return HtmlTag(name, content, tclass, tid, other).print()

@register.simple_tag
def submit(init='Submit'):
    return tag( 'button', init, 'btn', False, {'type': 'submit'}, True)

