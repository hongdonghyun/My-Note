from django.db import models

__all__ = [
    'TimeMixinStamp'
]


class TimeMixinStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
