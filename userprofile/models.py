from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify
# Create your models here.

class Profile(models.Model):

    IDENTITY = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('LGBTQ+', 'LGBTQ+'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    identity = models.CharField(max_length=30, choices = IDENTITY, blank=True)
    title = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    location_customised = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=200,null= False, blank = False)
    longitude = models.CharField(max_length=200,null= False, blank = False)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/') # django auto creates 'avatars' folder
    facebook_link = models.CharField(max_length=200, blank=True)
    twitter_link = models.CharField(max_length=200, blank=True)
    instagram_link = models.CharField(max_length=200, blank=True)
    clinic_name = models.CharField(max_length=200, blank=True)
    education = models.CharField(max_length=400, blank=True)
    languages = models.CharField(max_length=400, blank=True)
    native_country = models.CharField(max_length=200, blank=True)
    working_hours = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    @property
    def get_username(self):
        return self.user.username

    @property
    def get_email(self):
        return self.user.email

    def save(self,*args, **kwargs):
        self.slug = slugify( "user--" + str(self.user.id))

        location = self.location.replace(',','') # remove commas
        location = location.replace(' ','')   # remove whitespaces
        self.location_customised = location

        super().save(*args, **kwargs) 


class Image(models.Model):

    def generate_filename(self, filename) -> str:
        url = "imgs/%s/%s" % (self.item.profile.user.username, filename)
        return url

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to=generate_filename)

    def __str__(self) -> str:
        return str(f"{self.profile}---{self.id}")

