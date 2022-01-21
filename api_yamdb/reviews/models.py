from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, default=None)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, default=None)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Title(models.Model):
    name = models.CharField(max_length=100, default=None)
    year = models.IntegerField(default=0)
    description = models.TextField(default=None)
    genre = models.ManyToManyField(
        Genre,
        related_name="titles", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="titles", blank=True, null=True
    )
    GRADES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
]
    rating = models.CharField(max_length=2, choices=GRADES, default=0)

    def __str__(self):
        return self.title
