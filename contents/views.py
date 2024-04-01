from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .serializer import ContentSerializer
from .permissions import IsSuperUser
from courses.models import Course
from .models import Content


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs.get("course_id"))
        serializer.save(course=course)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_queryset(self):
        try:
            Course.objects.get(id=self.kwargs.get("course_id"))
            Content.objects.get(id=self.kwargs.get("content_id"))
        except Course.DoesNotExist:
            print('course not found.')
            raise NotFound('course not found.')
        except Content.DoesNotExist:
            print('content not found.')
            raise NotFound('content not found.')
        
        return super().get_queryset()
    