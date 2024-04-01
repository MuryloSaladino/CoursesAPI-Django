from django.db import models
import uuid


class StudentCourse(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending"
        ACCEPTED = "accepted"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.PENDING)
    student = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="students_courses")
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="students_courses")