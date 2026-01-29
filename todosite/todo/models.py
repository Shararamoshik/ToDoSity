from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    CATEGORY_CHOICES = [
        ('HIGH', 'Высокий'),
        ('MEDIUM', 'Средний'),
        ('LOW', 'Низкий'),
    ]
    priority = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True)
    due_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Срок выполнения",
        help_text="Срок выполнения задачи (необязательно)"
    )
    due_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Время выполнения",
        help_text="Время выполнения (необязательно)"
    )

    def __str__(self):
        return self.title
