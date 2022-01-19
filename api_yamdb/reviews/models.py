from django.db import models

""" from user.models import User """
from title.models import Title


SCORE = [(i, i) for i in range(11)]


class Review(models.Model):
    text = models.TextField(max_length=255)
    """ author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    ) """
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(max_length=2, choices=SCORE)
    pud_date = models.DateField(auto_now_add=True)

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
    """ author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    ) """
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pud_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
