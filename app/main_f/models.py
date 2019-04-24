from django.db import models


class User_list(models.Model):
    login = models.CharField(max_length=255, default='anon')
    password = models.CharField(max_length=255, default='password')

    def __str__(self):
        return self.login


class Message(models.Model):
    status = models.CharField(max_length=255, default='sended')
    text = models.TextField(default='no_text')
    reciever = models.CharField(max_length=255, default='anon')
    additional = models.CharField(max_length=255, default='no email')

    def __str__(self):
        return self.id
