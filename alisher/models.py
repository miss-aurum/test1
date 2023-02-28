from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    discription = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    # images = models.ImageField(verbose_name='Картинки')
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Categories(models.Model):
    name = models.CharField(max_length=200,verbose_name='Катигории')
    

    def __str__(self):
        return self.name
    

    
    

