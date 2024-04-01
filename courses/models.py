from django.db import models
import uuid


class Course(models.Model):

    class Status(models.TextChoices):
        NOT_STARTED = "not started"
        IN_PROGRESS = "in progress"
        FINISHED = "finished"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=11, choices=Status.choices, default=Status.NOT_STARTED)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        default=None
    )
    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="my_courses"
    )

    def __str__(self) -> str:
        return f"{self.id}"