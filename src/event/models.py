from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver




def upload_location(instance, filename):
	file_path = 'event/{title}-{filename}'.format(
				title=str(instance.title), filename=filename)
	return file_path



class Event(models.Model):
	title 							= models.CharField(max_length=255, null=False, blank=False)
	sub_title 						= models.CharField(max_length=255, null=False, blank=False)
	description						= models.TextField(max_length=255, null=False, blank=False)
	photograph	 					= models.ImageField(upload_to=upload_location,null=False, blank=False)
	date_published 					= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 					= models.DateTimeField(auto_now=True, verbose_name="date updated")


	def __str__(self):
		return self.title


@receiver(post_delete, sender=Event)
def submission_delete(sender, instance, **kwargs):
    instance.photograph.delete(False) 