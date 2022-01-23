from django.db import models

from users.models import User

SCORE = [(i, i) for i in range(11)]


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


class Review(models.Model):
    text = models.TextField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(choices=SCORE)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique review'
            ),
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
