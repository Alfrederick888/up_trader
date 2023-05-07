from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class SubMenu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    menu = TreeForeignKey('Menu', on_delete=models.CASCADE, related_name='sub_menu', verbose_name='Категория')
    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Menu(MPTTModel):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
