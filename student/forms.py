from django import forms
from django.conf import settings
from student.models import UserProfile

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('description','city','website','image' )
