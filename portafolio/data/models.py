from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    link = models.URLField(null=True, blank=True)
    created = models.DateField(auto_now_add=True) #cada que agregas
    updated = models.DateTimeField(auto_now=True) #cada que modificas

    class Meta:
        ordering = ['title'] # - descendente; sin el - sera ascendente 

    def __str__(self):
        return self.title