from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    query=models.TextField()
    date=models.DateField()


    def __str__(self):
        return self.name



# class Post(models.Model):
#     id=models.AutoField(primary_key=True)
#     author=models.CharField(max_length=100)
#     # email=models.EmailField(max_length=200)
#     # em=models.TextField(max_length=200)
#     title=models.CharField(max_length=200)
#     description=models.TextField()

class b_Post(models.Model):
    id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    
    title=models.CharField(max_length=200)
    description=models.TextField()