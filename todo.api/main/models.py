from django.db import models

# Create your models here.
status_choices = (('todo', 'todo'), ('doing', 'doing'), ('done', 'done'))


class Task(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    deadline = models.DateField()
    user = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
