from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created =  models.DateTimeField(auto_now_add=False)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'PostModel'
        verbose_name_plural = 'PostModel'
        # ordering = ('-date_created')
    
    def __str__(self) -> str:
        return self.title 
