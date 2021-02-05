from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Idea(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    dislikes = models.ManyToManyField(User, related_name='blogpost_dislike')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("idea-detail", kwargs={"pk": self.pk})

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()


    
    