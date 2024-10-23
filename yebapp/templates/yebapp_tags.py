# yebapp/templatetags/yebapp_tags.py
from django import template
from yebapp.models import UserDetails, YebOffers

register = template.Library()

@register.filter
def get_user_detail(user_key, field_name):
    try:
        user_detail = UserDetails.objects.get(u_key=user_key)
        return getattr(user_detail, field_name, "")
    except UserDetails.DoesNotExist:
        return ""

@register.filter
def get_yeb_offer(yeb_key):
    try:
        offer = YebOffers.objects.get(yeb_key=yeb_key)
        return offer.short_desc
    except YebOffers.DoesNotExist:
        return ""
