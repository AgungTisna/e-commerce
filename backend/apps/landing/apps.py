from django.apps import AppConfig

class LandingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.landing'   # <-- Should match folder structure
