from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_bio = models.CharField(max_length=500)


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    date_publishshed = models.DateTimeField()
    post_content = models.TextField()
    create_by = models.ForeignKey(Author, on_delete=models.CASCADE)