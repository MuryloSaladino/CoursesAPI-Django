from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from .serializer import CoursesSerializer
from .permissions import IsAdminOrReadOnly
from accounts.models import Account
from .models import Course


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

    def perform_create(self, serializer):
        instructor_id = self.request.data.get("instructor", None)
        if instructor_id is not None:
            instructor = get_object_or_404(Account, pk=instructor_id)
            serializer.save(instructor=instructor)
        else:
            serializer.save()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        else:
            return Course.objects.filter(students__id=self.request.user.id)
        

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"