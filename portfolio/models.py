from django.db import models

LOCATION_CHOICE = (
	('blog', 'Blog'),
	('pictures', 'Pictures'),
	('commisioned', 'Commisioned'),
	)

def user_directory_path(instance, filename):
	#print(filename)
	return '%s/%s'%(instance.location, instance.image_name)

class UploadImage(models.Model):
# Create your models here.
	image_name = models.CharField(max_length=50)
	location = models.CharField(max_length=50, choices=LOCATION_CHOICE)
	image = models.ImageField(upload_to=user_directory_path)

	def __str__(self):
		#image = models.ImageField(upload_to='%s/'%(self.location))
		return self.image_name