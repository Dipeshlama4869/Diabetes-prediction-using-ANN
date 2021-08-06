from django.db import models

#import basic django user class
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager
	)

#creating user in database
class UserManager(BaseUserManager):
	def create_user(self, email, username, password=None, active=True):
		if not email:
			raise ValueError("Users must have an email address")
		if not password:
			raise ValueError("Users must have a password")

		user_obj = self.model(
			email = self.normalize_email(email), #normalize email is a builtin function
			username=username,
			)
		user_obj.is_staff = True
		user_obj.set_password(password)
		user_obj.save(using=self._db)
		return user_obj

	def create_superuser(self, email, username, password):
		user_obj = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			)
		user_obj.is_admin = True
		user_obj.is_staff = True
		user_obj.is_superuser = True
		user_obj.save(using=self._db)
		return user_obj


#Our custom user model
class User(AbstractBaseUser):
	email			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 		= models.CharField(max_length=30, unique=True)
	timestamp 		= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin		= models.BooleanField(default=False)
	is_active 		= models.BooleanField(default=True)	#can login
	is_staff 		= models.BooleanField(default=True)
	is_superuser	= models.BooleanField(default=False)


	USERNAME_FIELD = 'email' #username is email
	REQUIRED_FIELDS = ['username',]

	objects = UserManager()
	
	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
	


#class Profile(models.Model):
	#user = models.OneToOneField(User)
	#extra data can be extended here


