from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
	def create_user(
		self, 
		email, 
		username, 
		firstname,
		lastname,
		contactnumber,
		department,
		branch,
		batch,
		graduationyear,
		password=None):

		# Validation 
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not firstname:
			raise ValueError('Users must have a firstname')
		if not lastname:
			raise ValueError('Users must have a lastname')
		if not contactnumber:
			raise ValueError('Users must have a contact number')
		if not department:
			raise ValueError('Users must have a department')
		if not branch:
			raise ValueError('Users must have a brach')
		if not batch:
			raise ValueError('Users must have a batch')
		if not graduationyear:
			raise ValueError('Users must have a graduation year')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			firstname=firstname,
			lastname=lastname,
			contactnumber=contactnumber,
			department=department,
			branch=branch,
			batch=batch,
			graduationyear=graduationyear,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(
		self, 
		email, 
		username, 
		firstname,
		lastname,
		contactnumber,
		department,
		branch,
		batch,
		graduationyear,
		password):

		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			firstname=firstname,
			lastname=lastname,
			contactnumber=contactnumber,
			department=department,
			branch=branch,
			batch=batch,
			graduationyear=graduationyear,

		)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	firstname				= models.CharField(max_length=60)
	lastname				= models.CharField(max_length=60)
	contactnumber			= models.CharField(max_length=10, unique=True)
	department				= models.CharField(max_length=120)
	branch					= models.CharField(max_length=30)
	batch					= models.CharField(max_length=30)
	graduationyear			= models.CharField(max_length=30)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [
		'username',
		'firstname',
		'lastname',
		'contactnumber',
		'department',
		'branch',
		'batch',
		'graduationyear',

	]

	objects = AccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True