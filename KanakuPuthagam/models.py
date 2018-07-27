from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)


class Source(models.Model):
    source = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)    

    # class Meta:
    #     abstract = True
