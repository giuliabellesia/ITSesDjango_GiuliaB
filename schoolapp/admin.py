from django.contrib import admin
from schoolapp.models import DayOfTheWeek, Classroom, Course

# Register your models here.
admin.site.register(DayOfTheWeek);
admin.site.register(Classroom);
admin.site.register(Course);