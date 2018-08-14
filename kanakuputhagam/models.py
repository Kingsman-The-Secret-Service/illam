from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class Category(models.Model):
    INCOME = "INCOME"
    SAVING = "SAVING"
    EXPENSE = "EXPENSE"
    TYPE = (
        (INCOME, "INCOME"),
        (SAVING, "SAVING"),
        (EXPENSE, "EXPENSE")
    )

    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=9, choices=TYPE)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.type + ': ' + self.name

    class Meta:
        unique_together = ("user", "type", "name")
        ordering = ['type','name']

class Member(models.Model):
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("user", "name")
        ordering = ['name']

class Tag(models.Model):
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("user", "name")
        ordering = ['name']

class Budget(models.Model):
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("user", "start_date", "end_date")
        ordering = ['-start_date']

class Splitup(models.Model):
    INCOME = "INCOME"
    SAVING = "SAVING"
    EXPENSE = "EXPENSE"
    TYPE = (
        (INCOME, "INCOME"),
        (SAVING, "SAVING"),
        (EXPENSE, "EXPENSE")
    )

    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=9, choices=TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    amount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    
    class Meta():
        ordering = ['-created_on']

class Transaction(models.Model):
    INCOME = "INCOME"
    SAVING = "SAVING"
    EXPENSE = "EXPENSE"
    TYPE = (
        (INCOME, "INCOME"),
        (SAVING, "SAVING"),
        (EXPENSE, "EXPENSE")
    )

    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=9, choices=TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    amount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta():
        ordering = ['-date', '-created_on']