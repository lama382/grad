from django.apps import AppConfig
class CaloriesConfig(AppConfig):
    name = 'Fityfeed'
    def ready(self): #new
        import Fityfeed.signals #new
