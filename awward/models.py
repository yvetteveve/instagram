from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to = 'awwapp/')
    bio = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,unique=True)
    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
class Image(models.Model):
    # image_pic = models.ImageField(upload_to = 'p/', default='Image')
    image = models.ImageField(upload_to = 'awwapp/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length =200)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    

    class Meta:
        ordering = ('-post_date',)

    def save_image(self):
        self.save()
    
    @classmethod
    def update_caption(cls, update):
        pass
    
    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)

    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

# class user(models.models)
#     Profile=models.CharField()
#     images = Image.objects.all()
    