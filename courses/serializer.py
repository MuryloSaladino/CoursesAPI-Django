from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Course


class CoursesSerializer(serializers.ModelSerializer):
    instructor = serializers.CharField(source="instructor.id", read_only=True, default=None)
    students_courses = serializers.StringRelatedField(many=True, read_only=True)
    contents = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Course
        exclude = ["students"]
        read_only_fields = ["id"]
        extra_kwargs = {
            'name': {'validators': [
                UniqueValidator(
                    queryset=Course.objects.all(),
                    message="course with this name already exists."
                )
            ]}
        }