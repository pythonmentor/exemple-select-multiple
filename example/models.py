from django.db import models


class Article(models.Model):
    title = models.CharField("article title", max_length=255)
    tags = models.ManyToManyField("Tag", related_name="articles")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField("tag", max_length=255)

    def __str__(self):
        return self.name
