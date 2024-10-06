from django import template
import datetime

register = template.Library()


@register.filter
def format_duration(value):
    if isinstance(value, datetime.timedelta):
        total_seconds = int(value.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        hours_part = f"{hours} год" if hours > 0 else ""
        minutes_part = f"{minutes}" if minutes > 0 else ""

        return f"{hours_part} {minutes_part}".strip()
    return value
