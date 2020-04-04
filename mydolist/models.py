from django.db import models as md


# Create your models here.

class todolists(md.Model):
    description = md.CharField(max_length=150)
    status= md.CharField(max_length=10,default="red")

    def __str__(self):
        return '{}'.format(self.description.title())
    class Meta:
        verbose_name_plural = 'To do List'
        ordering = ('id',)

