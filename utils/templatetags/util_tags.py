from django import template

from utils.util import HtmlTag

register = template.Library()

@register.simple_tag
def tag(name, content='', tclass=False, tid=False, other=False):
    return HtmlTag(name, content, tclass, tid, other).print()

@register.simple_tag
def submit(init='Submit'):
    return tag( 'button', init, 'btn', False, {'type': 'submit'}, True)


@register.simple_tag
def print_goal_table(table):
    h  = "<h4>%s</h4>\n" % table.day
    h += "<table class='table table-striped table-condensed'>\n"
    h += "<tr>\n"
    h += "<th></th>\n"
    for meal in table.meals:
        h += "<th>%s</th>\n" % meal
    h += "<th>Expected Total</th>\n"
    h += "<th>My Total</th>\n"
    h += "<th>Remaining Total</th>\n"
    h += "</tr>\n"
    h += goal_table_row(table.calories, table.day)
    h += goal_table_row(table.fat, table.day)
    h += goal_table_row(table.carbs, table.day)
    h += goal_table_row(table.protein, table.day)
    h += "</table>\n"
    return h


def goal_table_row(row, day):
    h  = "<tr>\n"
    h += "<th>%s</th>\n" % row['name']

    rowvals = []
    for v in row['values']:
        rowvals.append(v)

    for v in rowvals:
        h += "<td>%02d</td>\n" % v

    expect = row['expected']
    total = sum(rowvals)
    rem = expect - total
    h += "<td>%02d</td>\n" % expect
    h += "<td>%02d</td>\n" % total
    h += "<td>%02d</td>\n" % rem
    h += "</tr>\n"
    return h




@register.simple_tag
def as_controls(name, label, input, error):
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
def as_dropdown(name, choices, error, onclick=False):
    h  = "<div class=\"input-append\">\n"
    h += "  <div class=\"btn-group\">\n"
    h += "  <button id=\"%s_button\" class=\"btn dropdown-toggle\" data-toggle=\"dropdown\">" % name
    h += "%s <span class=\"caret\"></span></button>\n" % choices[0][1]
    h += "  <input type=\"hidden\" name=\"%s\" value=\"%s\" />\n" % (name, choices[0][0])
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
    return as_controls(name, False, h, error)


@register.simple_tag
def as_submit(value, primary=True):
    h  = "<div class=\"control-group\">\n"
    h += "  <div class=\"controls\">\n"
    h += "    <button type=\"submit\" class=\"btn"
    if primary:
        if primary is True:
            h += " btn-primary"
        else:
            h += " btn-%s" % primary
    
    h += "\" name=\"submit\">%s</button>\n" % value
    h += "  </div>\n"
    h += "</div>\n"
    return h



