from django import template

register = template.Library()


@register.simple_tag
def generate_url(search_content, dept, page=1):
    return "?page={}&dept=string:{}&search_content={}".format(page, dept, search_content)
