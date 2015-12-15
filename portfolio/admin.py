from django.contrib import admin

# Register your models here.
from .forms import UploadImageForm
from .models import UploadImage

class UploadImageAdmin(admin.ModelAdmin):
	list_display = ["__str__", "location"]
	form = UploadImageForm
	# class Meta:
	# 	model = SignUp


admin.site.register(UploadImage, UploadImageAdmin)