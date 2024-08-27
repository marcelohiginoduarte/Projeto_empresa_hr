from django.apps import AppConfig


class GestaohrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GestaoHR'

    

class MinhaAppConfig(AppConfig):
    name = 'minha_app'

    def ready(self):
        import minha_app.signals  
