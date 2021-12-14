from django.db import models

# Create your models here.
class Comment(models.Model):
    site_name = models.CharField(max_length=500,default='')
    host = models.CharField(max_length=500,default='')
    your_post = models.CharField(max_length=500,default='')
    web_design = models.CharField(max_length=500,default='')
    work_field = models.CharField(max_length=500,default='')
    budget = models.CharField(max_length=500,default='')
    support = models.CharField(max_length=500,default='')

    cooperation = models.TextField(default='')
    details = models.TextField(default='')
    contacts = models.TextField(default='')

    site_system= models.CharField(max_length=200,default=1)
    budget_amount= models.CharField(max_length=200,default=1)
    who_support= models.CharField(max_length=200,default=1)
    content_technical= models.CharField(max_length=200,default=1)

    #date = models.DateTimeField(auto_now_add=True)

