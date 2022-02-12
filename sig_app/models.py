from django.db import models
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('blog_detail', args=[str(self.id)])


class Post(models.Model):
    title_ps = models.CharField(max_length=200)
    author_ps = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body_ps = models.TextField()

    def __str__(self):
        return self.title_ps

    def get_absolute_url(self):  # new
        return reverse('post_detail', args=[str(self.id)])


@receiver(post_save, sender=Blog)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(title_ps=f"ব্লগ থেকে  {instance}",
                            author_ps=instance.author,
                            body_ps=f"{instance.body} ব্লগ থেকে তৈরি ",
                            )
