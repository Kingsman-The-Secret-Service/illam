from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)


class Source(models.Model):
    source = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)    

class Income(models.Model):
    date = models.DateField()
    name = models.ForeignKey('Member', on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    amount = models.IntegerField()
    description = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)
