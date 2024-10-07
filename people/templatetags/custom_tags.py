import datetime
from django import template

register = template.Library()

@register.simple_tag
def greeting(user):
    name = user.username
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return f"Good Morning, {name.title()}"
    elif 12 <= current_hour < 18:
        return f"Good Afternoon, {name.title()}"
    else:
        return f"Good Evening, {name.title()}"