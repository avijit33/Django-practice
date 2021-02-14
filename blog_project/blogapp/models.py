from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=250, verbose_name="Put a title")
    blog_content = models.TextField(verbose_name="Write your blog")
    slug = models.SlugField(max_length=250, unique=True)
    blog_image = models.ImageField(upload_to='blog_image', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.comment

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')

    def __str__(self):
        return self.user + "likes" + self.blog

