from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    #CASCADE means if the user is deleted then it will delete the profile,
    # but if only profile deleted then not the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #if we want to print the model
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        #after the model saved, now we overwrite the original adding neew funtionality
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
                    #to overwrite big image,
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



