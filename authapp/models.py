from django.db import models
from django.contrib.auth.models import User

    # here we create custom attributes to the user (built-in include username, email, password, first name and surname)
class UserProfileInfo(models.Model):

    #create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #add any additional attributes you want
    portfolio = models.URLField(blank=True) #black=true means it is not required if left in blank by user it's ok.
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) #we need to create a media subfolder called profile_pics for this to work
    
    def __str__(self):
        return self.user.username