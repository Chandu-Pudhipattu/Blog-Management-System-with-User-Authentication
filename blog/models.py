from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # auto_now_add will create a date when the post is created (issue is we cant update the date posted), however we can use default value as timezone.now
    # now() paranthesis not included becasue iam not executing here instead iam just passing as default value
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # whenever the user deletes his/her acc then their posts will be deleted automatically

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


