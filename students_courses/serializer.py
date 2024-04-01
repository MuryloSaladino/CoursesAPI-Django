from rest_framework import serializers
from .models import StudentCourse


class StudentCourseSerializer(serializers.Serializer):

    student_id = serializers.IntegerField(source="student.id", read_only=True)
    course_id = serializers.IntegerField(source="course.id", read_only=True)

    class Meta:
        model = StudentCourse
        read_only_fields = ["id"]
        exclude = ["student", "course"]