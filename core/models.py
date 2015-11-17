from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

CATEGORY_CHOICES = (
(0, 'Fiction'),
(1, 'Mystery & Crime'),
(2, 'Poetry'),
(3, 'Romance'),
(4, 'Science Fiction'),
(5, 'Thrillers'),
(6, 'Childrens'),
(7, 'Nonfiction'),
)

RATING_CHOICES = (
(0, 'None'),
(1, '*'),
(2, '**'),
(3, '***'),
(4, '****'),
(5, '*****'),
)

class Post(models.Model):
  title = models.CharField(max_length=300)
  author = models.CharField(max_length=300)
  rating = models.IntegerField(choices=RATING_CHOICES, default=0)
  category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("post_detail", args=[self.id])

class Comment(models.Model):
  post = models.ForeignKey(Post)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  post = models.ForeignKey(Post, blank=True, null=True)
  comment = models.ForeignKey(Comment, blank=True, null=True)

  def __unicode__(self):
    return "%s upvoted" % (self.user.username)