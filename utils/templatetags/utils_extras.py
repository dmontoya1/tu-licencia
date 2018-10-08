from django import template
from users.models import User
from utils.models import SoftDeletionModelMixin


register = template.Library()

@register.filter(name="is_softdeletion_instance")
def is_softdeletion_instance(value):
    return isinstance(value, SoftDeletionModelMixin)


@register.filter(name="is_user_instance")
def is_user_instance(value):
    return isinstance(value, User)
