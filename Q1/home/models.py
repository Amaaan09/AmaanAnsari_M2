from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Tasks'        
