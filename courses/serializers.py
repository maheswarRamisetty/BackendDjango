from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CourseInstance
        fields = '__all__'
        
    def create(self, validated_data):
        course_data = validated_data.pop('course')
    
        course, created = Course.objects.get_or_create(**course_data)
        
        course_instance = CourseInstance.objects.create(course=course, **validated_data)
        
        return course_instance