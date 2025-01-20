from django.db import models
from category.models import Category

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)  # Use DateTimeField
    categories = models.ManyToManyField('category.Category', related_name='tasks')

    def __str__(self):
        return self.taskTitle
