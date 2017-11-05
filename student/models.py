from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().order_by('phone')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(null=True ,blank=True,height_field='height_field',width_field='width_field')
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    order_byPhone = UserProfileManager()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('view_profile', kwargs={'pk': self.pk})

def create_profile( sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender = User)

class Courses(models.Model):
    courseNo = models.CharField(max_length = 10, default = '',primary_key = True)
    courseName = models.CharField(max_length = 100, default = '')
    credits = models.IntegerField(default = 0)



class Students(models.Model):
    studentId = models.IntegerField(default = 0, primary_key = True)
    studentName = models.CharField(max_length =100, default = '')
    progId = models.CharField(max_length =100, default ='')
    batch = models.CharField(max_length = 10, default = '')
    studentEmail = models.CharField(max_length = 100, default = '')


class Faculty(models.Model):
    facultyId = models.IntegerField(default = 0, primary_key = True)
    facultyName = models.CharField(max_length = 100, default = '')
    facultyEmail = models.CharField(max_length = 100, default = '')


class Semester(models.Model):
    acadYear = models.CharField(max_length = 10, default = '')
    semesterNo = models.IntegerField(default = 0)

    class Meta:
        unique_together = (('acadYear','semesterNo'),)




class Offers(models.Model):
    facultyId = models.ForeignKey(Faculty)
    courseNo = models.ForeignKey(Courses)
    acadYear = models.ForeignKey(Semester, null=True, related_name='acadYear+')
    semesterNo = models.ForeignKey(Semester, null=True, related_name='semesterNo+')

    class Meta:
        unique_together = (('facultyId','courseNo','acadYear','semesterNo'),)



class Registers(models.Model):
    studentId = models.ForeignKey(Students)
    facultyId = models.ForeignKey(Faculty)
    courseNo = models.ForeignKey(Courses)
    acadYear = models.ForeignKey(Semester, null=True, related_name='acadYear+')
    semesterNo = models.ForeignKey(Semester, null=True, related_name='semesterNo+')

    class Meta:
        unique_together = (('studentId','facultyId','courseNo','acadYear','semesterNo'),)
