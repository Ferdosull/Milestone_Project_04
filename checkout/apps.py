from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Import signals when the ready function is called
        """
        import checkout.signals
