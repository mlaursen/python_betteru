from django import template

from utils.util import HtmlTag

register = template.Library()


@register.simple_tag
def as_controls(name, label, input, error, d=False):
    h  = "<div class=\"control-group\">\n"
    if label:
        h += "  <label class=\"control-label\" for=\"%s\">%s</label>\n" % (name, label)
    h += "  <div class=\"controls\">\n"
    h += "    %s\n" % input
    h += "    <span class=\"error help-inline\" id=\"%s_help\">%s</span>\n" % (name, error)
    h += "  </div>\n"
    h += "</div>\n"
    return h

@register.simple_tag
def as_dropdown(name, choices, error, onclick=False, d=0, label=False):
    h  = "<div class=\"input-append\">\n"
    h += "  <div class=\"btn-group\">\n"
    h += "  <button id=\"%s_button\" class=\"btn dropdown-toggle\" data-toggle=\"dropdown\">" % name
    h += "%s" % choices[d][1]
    h += " <span class=\"caret\"></span></button>\n"
    h += "  <input type=\"hidden\" name=\"%s\" value=\"%s\" />\n" % (name, choices[d][0])
    h += "  <ul class=\"dropdown-menu\">\n"
    for c in choices:
        if "Select" in c[1]:
            h += "    <li><a href=\"#\""
            if onclick:
                h += " id=\"id_%s\" onclick=\"%s\"" % (c[0], onclick)
            h += ">%s</a></li>\n" % c[1]
            h += "    <li class=\"divider\"></li>\n"
        else:
            h += "    <li><a href=\"#\""
            if onclick:
                h += " id=\"id_%s\" onclick=\"%s\"" % (c[0], onclick)
            h += ">%s</a></li>\n" % c[1]
    h += "  </ul>\n"
    h += "  </div>\n"
    h += "</div>"
    return as_controls(name, label, h, error)


@register.simple_tag
def as_submit(value, primary=True, disable=False):
    h  = "<div class=\"control-group\">\n"
    h += "  <div class=\"controls\">\n"
    h += "    <button type=\"submit\" class=\"btn"
    if primary:
        if primary is True:
            h += " btn-primary"
        else:
            h += " btn-%s" % primary
    
    h += "\" name=\"submit\""
    if disable:
        h += " disabled"
    h += ">%s</button>\n" % value
    h += "  </div>\n"
    h += "</div>\n"
    return h


@register.simple_tag
def display_error(field):
    h  = "  <div class=\"row-fluid\">\n"
    h += "    <div class=\"span6 offset2 alert alert-error\">\n"
    h += "      %s<br />\n" % field
    h += "    </div>\n"
    h += "  </div>\n"
    return h

@register.simple_tag
def display_success(text):
    h  = "  <div class=\"row-fluid\">\n"
    h += "    <div class=\"alert alert-success\">\n"
    h += "      %s\n" % text
    h += "    <a href=\"#\" class=\"close\" data-dismiss=\"alert\">x</a>\n"
    h += "    </div>\n"
    h += "  </div>\n"
    return h

@register.simple_tag
def as_text_action(name, itms, error, label=False, func=False):
    h  = "<div class=\"input-append\">\n"
    h += "  <input type=\"text\" id=\"%s\" name=\"%s\" placeholder=\"%s\" class=\"span7\">\n" % (name, name, label)
    h += "  <div class=\"btn-group\">\n"
    h += "    <button id=\"%s_button\" class=\"btn dropdown-toggle\" data-toggle=\"dropdown\">%s <span class=\"caret\"></span></button>\n" % (name, itms[0])
    h += "    <ul class=\"dropdown-menu\">\n"
    divider = True
    for i in itms:
        h += "      <li><a href=\"#\""
        if func:
            h += " onclick=\"%s('%s', '%s')\"" % (func, i, name)
        h += ">%s</a></li>\n" % i
        if divider:
            h += "      <li class=\"divider\"></li>\n"
        divider = False

    h += "    </ul>\n"
    h += "  </div>\n"
    h += "</div>\n"
    return as_controls(name, label, h, error)

