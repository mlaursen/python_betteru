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




