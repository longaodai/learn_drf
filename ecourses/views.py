from django.contrib.auth import authenticate
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Courses, Users, Lessons, Tags, Cares
from .serializers import CoursesSerializer, UsersSerializer, LessonsSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer

    @action(methods=['post'], detail=True, url_path='add-tag')
    def add_tag(self, request, pk):
        lesson = Lessons.objects.get(pk=pk)
        tags = request.data.get('tags')
        if tags is not None:
            for tag in tags:
                Tags.objects.get_or_create(name=tag, lessons_id=pk)

            return Response(self.serializer_class(lesson).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=True, url_path='add-care')
    def add_care(self, request, pk):
        lesson = Lessons.objects.get(pk=pk)
        cares_request = request.data.get('cares')

        if cares_request is not None:
            for care in cares_request:
                result_care, _ = Cares.objects.get_or_create(name=care)
                lesson.cares.add(result_care)

            lesson.save()

            return Response(self.serializer_class(lesson).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Users.objects.filter(is_active=True)
    serializer_class = UsersSerializer

    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request):
        user = authenticate(
            request,
            email=request.data.get('email'),
            password=request.data.get('password')
        )

        if user:
            refresh = TokenObtainPairSerializer.get_token(user)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response({
            'user': user,
            'error_message': 'Email or password is incorrect!',
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
