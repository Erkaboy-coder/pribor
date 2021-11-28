
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Group


class Category(models.Model):
	name=models.CharField(max_length=100,blank=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Categories"


class Subcategory(models.Model):
	name=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "SubCategories"


class ResponsiblePerson(models.Model):
	name=models.CharField(max_length=100,blank=True)
	tel_number=models.CharField(max_length=100,blank=True)
	email=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "ResponsiblePersons"

class Departments(models.Model):
	name=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Departments"

class Appliance(models.Model):
	category = models.ForeignKey(Category, blank=True,on_delete=models.CASCADE,related_name='categories')
	subcategory = models.ForeignKey(Subcategory, blank=True,on_delete=models.CASCADE,related_name='subcategories')
	department = models.ForeignKey(Departments, blank=True,on_delete=models.CASCADE,related_name='departments')
	name=models.CharField(max_length=100,blank=True)
	inv_number=models.CharField(max_length=100,blank=True)
	factory_number=models.CharField(max_length=100,blank=True)
	origin_country=models.CharField(max_length=100,blank=True)
	origin_factory=models.CharField(max_length=100,blank=True)
	origin_year=models.DateField(blank=True)
	used_year=models.DateField(blank=True)
	battery=models.BooleanField(default=False)
	status_battery=models.IntegerField(default=0)
	status_passport=models.IntegerField(default=0)
	passport = models.FileField(upload_to='index/data/files/', blank=True)
	compatibility_file = models.FileField(upload_to='index/data/files/', blank=True)
	status_compatibility_file_value=models.IntegerField(default=0)
	responsible_user=models.CharField(max_length=100,blank=True)
	info=models.TextField(blank=True)
	status = models.IntegerField(default=0)
	is_delete = models.IntegerField(default=0)

	def delete(self, *args, **kwargs):
		self.passport.delete(save=False)
		self.compatibility_file.delete(save=False)
		super(Appliance, self).delete(*args, **kwargs)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Appliances"



class Certificate(models.Model):
	issue_date = models.DateField(blank=True)
	expiry_date = models.DateField(blank=True)
	responsible_department = models.CharField(max_length=100, blank=True)
	checked_organization = models.CharField(max_length=100, blank=True)
	file = models.FileField(upload_to ='index/data/files/',blank=True)
	status = models.BooleanField(default=False)
	certificate_number=models.CharField(max_length=100,blank=True)
	last = models.IntegerField(default=0)
	appliance = models.ForeignKey(Appliance, blank=True, on_delete=models.CASCADE, related_name='appliances')

	def delete(self, *args, **kwargs):
		self.file.delete(save=False)
		super(Certificate, self).delete(*args, **kwargs)

	def __str__(self):
		return "Certificate"
	class Meta:
		verbose_name_plural = "Certificates"
		# ordering=['-id']

class BaseModel(models.Model):
  def save(self, *args, full_clean=True, **kwargs):
        # ensure that full_clean is called during save
        # note that this is done to validate data from both admin and drf in single place
    if full_clean:
      self.full_clean()
    super().save(*args, **kwargs)

  class Meta(object):
    abstract = True

class Profile(BaseModel):
	"""
    profile for user
    """
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.PROTECT,
		verbose_name="Related user",
		help_text="User linked to this profile",

	)
	company = models.CharField(verbose_name="Company", max_length=256)
	admin_type_select = [
		(0, 'user'),
		(1, 'admin'),
	]

	permission=models.BooleanField(default=False)

	admin_type = models.IntegerField(choices=admin_type_select, default=0)

	class Meta(object):
		verbose_name = "Profile"
		verbose_name_plural = "Profiles"

	def __str__(self):
		return self.user.username

class History(models.Model):
	date = models.DateField(blank=True)
	invalid_file = models.FileField(upload_to ='index/data/files/',blank=True)
	appliance = models.ForeignKey(Appliance, blank=True,on_delete=models.CASCADE,related_name='items')
	user = models.ForeignKey(User, blank=True,on_delete=models.CASCADE,related_name='users')
	status = models.IntegerField(default=0)
	comment = models.TextField(blank=True)
	def __str__(self):
		return self.user.username
	class Meta:
		verbose_name_plural = "Histories"
