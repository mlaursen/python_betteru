from django import template

from utils.util import HtmlTag, display_unit
from meals.models import MealPartsView

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
def as_dropdown(name, choices, error, label=False, d=0, onclick='selectItemDropdown'):
    h  = "<div class=\"input-append\">\n"
    h += "  <div class=\"btn-group\">\n"
    h += "  <button id=\"%s_button\" class=\"btn dropdown-toggle\" data-toggle=\"dropdown\">" % name
    h += "%s" % choices[d][1]
    h += " <span class=\"caret\"></span></button>\n"
    h += "  <input type=\"hidden\" name=\"%s\" value=\"%s\" />\n" % (name, choices[d][0])
    h += "  <ul class=\"dropdown-menu\" id=\"%s_choices\">\n" % name
    for c in choices:
        h += "    <li><a href=\"#\""
        if onclick:
            h += " id=\"id_%s\" onclick=\"%s(this)\"" % (c[0], onclick)
        h += ">%s</a></li>\n" % c[1]
        if "Select" in c[1]:
            h += "    <li class=\"divider\"></li>\n"
    h += "  </ul>\n"
    h += "  </div>\n"
    h += "</div>"
    return as_controls(name, label, h, error)


@register.simple_tag
def as_submit(value, primary='primary', disable=False):
    h  = "<div class=\"control-group\">\n"
    h += "  <div class=\"controls\">\n"
    h += "    <button type=\"submit\" class=\"btn"
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


@register.simple_tag
def as_meal_divs(meals):
    h  = "<div class=\"meals\">\n"
    for meal in meals:
        h += "<div class=\"meal\">\n"
        h += "   <div class=\"meal-name\">%s</div>\n" % meal.name
        h += "    <hr />\n"
        h += "    <div class=\"meal-description\">%s</div>\n" % meal.description
        h += "    <div class=\"nutritional-facts\">\n"
        h += "      <div class=\"header\">Nutritional facts</div>\n"
        h += "      Calories: %s<br />\n" % meal.total_calories
        h += "      Fat: %s<br />\n" % meal.total_fat
        h += "      Carbs: %s <br />\n" % meal.total_carbohydrates
        h += "      Protein: %s\n" % meal.total_protein
        h += "    </div>\n"
        h += "</div>\n"
    h += "</div>\n"
    return h

@register.simple_tag
def ingredient_list(mealid):
    meal_parts = MealPartsView.objects.filter(mealid=mealid)
    h  = "<ul>\n"
    for meal_part in meal_parts:
        ing_name = meal_part.ingredient_name
        ing_amt  = meal_part.amount
        ing_unit = display_unit(meal_part.serving_unit, ing_amt, ing_name)
        h += "<li>%s - %s %s</li>\n" % (ing_name, ing_amt, ing_unit)
    return h + "</ul>\n"

@register.simple_tag
def another_row(counter, amt=5):
    if (counter-1) % amt == 0:
        return "</div>\n<div class=\"row-fluid\">\n"
    else:
        return ""

@register.simple_tag
def as_hidden(name, value=0):
    return "<input type=\"hidden\" name=\"%s\" id=\"id_%s\" value=\"%s\" />\n" % (name, name, value)

