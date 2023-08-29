from django.apps import AppConfig


class NomuraCorporationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nomura_corporation_app'

    def ready(self):
    	import nomura_corporation_app.signals
