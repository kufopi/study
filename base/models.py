from django.db import models

from django.contrib.auth.models import AbstractUser   #to create customised users




# Create your models here.


class User(AbstractUser):
    
    name = models.CharField(null=True, max_length=50)
    email  = models.EmailField(null=True, max_length=254, unique=True)
    bio  = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField( max_length=150)

    

    class Meta:
        verbose_name = ("topic")
        verbose_name_plural = ("topics")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("topic_detail", kwargs={"pk": self.pk})





class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey("Topic", on_delete=models.SET_NULL, null=True)
    name = models.CharField( max_length=50)
    description = models.TextField(null=True, blank=True)
    participants  = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField( auto_now_add=True)

    

    class Meta:
        verbose_name = ("room")
        verbose_name_plural = ("rooms")
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("room_detail", kwargs={"pk": self.pk})



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.body[0:25]

    # def get_absolute_url(self):
    #     return reverse("Message_detail", kwargs={"pk": self.pk})




