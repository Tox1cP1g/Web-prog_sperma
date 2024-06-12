from django.db import models


class Articles(models.Model):
  title = models.CharField(max_length = 120)
  body = models.TextField()
  date = models.DateTimeField()
  likes_count = models.IntegerField(default=0)

  def _str_(self):
    return self.title
