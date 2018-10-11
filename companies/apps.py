from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'companies'
    verbose_name = 'Compañías'

    def ready(self):
        import companies.signals