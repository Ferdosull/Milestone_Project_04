from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


# Update on save function using the receiver decorator
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    Receives post_save signal from OrderLineItem model
    """
    instance.order.update_total()


# Update on delete function using the receiver decorator
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    Receives post_delete signal from OrderLineItem model
    """
    instance.order.update_total()
