from django.db import models

# Create your models here.
class Task(models.Model):#models.Model: Tells Django this class is a database table.
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    #__str__: This is a "magic method" that ensures when we look at 
    # a task in the admin panel, we see the title instead of something 
    # generic like "Task object (1)".