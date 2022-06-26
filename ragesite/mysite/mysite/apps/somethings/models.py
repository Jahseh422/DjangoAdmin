from django.db import models

class Something(models.Model):

    something_title = models.CharField('Список интерфейсов', max_length = 250)
    something_text = models.TextField('Именно список')
    get_dateTime = models.DateTimeField

    def __str__(self):
        return self.something_title

class Comment(models.Model):
    comment = models.ForeignKey(Something, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length= 50)
    comment_text = models.CharField('Text', max_length= 200)

    def __str__(self):
        return self.author_name
