from django.conf import settings
from django.db import models

# Create your models here.
class Helloworld(models.Model):
    title = models.CharField('単語', max_length=128)
    code = models.CharField('読み仮名', blank=False)
    description = models.TextField('語釈', blank=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name='投稿者',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
    click_count = models.PositiveIntegerField("クリック数",default=0)
    def __str__(self):
        return self.title