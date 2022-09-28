from rest_framework.serializers import ModelSerializer
from .models import Courses, Users, Lessons, Tags, Cares


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'created_date', 'updated_date']


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name', 'created_date', 'updated_date']


class CaresSerializer(ModelSerializer):
    class Meta:
        model = Cares
        fields = ['id', 'name', 'created_date', 'updated_date']


class LessonsSerializer(ModelSerializer):
    course = CoursesSerializer()
    tags = TagsSerializer(many=True)
    cares = CaresSerializer(many=True)

    class Meta:
        model = Lessons
        fields = ['id', 'name', 'description', 'image', 'created_date', 'updated_date', 'course_id', 'course', 'tags',
                  'cares']


class UsersSerializer(ModelSerializer):
    def create(self, validated_data):
        user = Users(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'is_active', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
