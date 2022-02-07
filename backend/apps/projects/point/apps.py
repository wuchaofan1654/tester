from django.apps import AppConfig


class PointConfig(AppConfig):
    name = 'apps.projects.point'

    def ready(self):
        from apps.projects.point.signals import point_init_callback
        from apps.projects.point.signals import point_received_signal_callback_check
        from apps.projects.point.signals import point_received_signal_callback_save
        pass
