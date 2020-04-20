from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now) # create date is the date/time when a post is created
    published_date = models.DateTimeField(null=True, blank=True) # publish date is the date/time when a post is published or posted

    '''
        So in order to set the time for publishing on click of post button this method will be called
    '''
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    '''
        this method returns the list of comments that has been approved on this particular post 
        (filter method acts as where clause)
    '''
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    '''
        after the post is created; this method decides where to redirect the application; it will go to post_details ( a detal view) url
    '''
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    '''
        if a particular comment is to be aproves this method will be called to set the flag True
    '''
    def approve(self):
        self.approved_comment = True
        self.save()

    '''
        after the comment is created/made; this method decides where to redirect the application; it will go to post_list ( a list view) url
    '''
    def get_absolute_url(self):
        return reverse("blog:post_list", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.text

