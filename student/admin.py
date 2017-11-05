from django.contrib import admin
from student.models import (
        Courses,
        Students,
        Faculty,
        Offers,
        Semester,
        Registers,
        UserProfile,
)
# Register your models here.

admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(Faculty)
admin.site.register(Offers)
admin.site.register(Semester)
admin.site.register(Registers)
admin.site.register(UserProfile)
