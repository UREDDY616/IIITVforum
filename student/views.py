from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from student.models import Registers, Courses, Students
from student.forms import EditProfileForm

def home(request):
    if request.method == 'POST':
            print("helloooooooooooooooo")
            return redirect(reverse('home'))
    else:
        user = request.user
        courses = Registers.objects.filter(studentId = '201551081')
        args = {'courses' : courses}

        return render(request, 'student/home.html', args)

def sem_course(request, course_No):
    courses = Registers.objects.filter(studentId = '201551081')
    value = False
    if request.method == 'GET':
        for course in courses:
            if course_No in course.courseNo.pk:
                value = True
                break
        if value==True:
            args = {'course':course}
            return render(request, 'student/course_home.html', args)
        else:
            print("hellooooooo")
            return redirect(reverse('home'))
    else:
        return redirect(reverse('home'))


def view_profile(request,  pk = None):

    if pk:
        user = User.objects.get(pk=pk)

    else:
        user = request.user
    args = {'user': user}
    return render(request, 'student/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            url = redirect('view_profile')
            return url
    else:
        form =   EditProfileForm( instance=request.user)
        args = {'form': form}
        return render(request, 'student/edit_profile.html', args)


def classmates(request):
    prog = Students.objects.get(studentId='201551081')
    class_mates  = Students.objects.filter(progId=prog.progId, batch=prog.batch)
    args = {'class_mates':class_mates }
    return render(request, "student/classmates.html", args)


# Create your views here.
