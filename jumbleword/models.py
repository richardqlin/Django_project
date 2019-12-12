from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=50)

    def __str(self):
        return '%s' %( self.word )



