from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class producto(models.Model):
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    nombre =    models.CharField(max_length=200)
    precio =    models.DecimalField(max_digits=6, decimal_places=2)
    Stock =     models.IntegerField(default=0)
    pub_date =  models.DateField('date publisehd')
    
    def __str__(self):
        return self.nombre