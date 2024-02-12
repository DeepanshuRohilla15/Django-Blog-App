from django.apps import AppConfig

# this file is interact with database
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
