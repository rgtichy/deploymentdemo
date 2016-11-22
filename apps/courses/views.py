from django.shortcuts import render, redirect
from .models import Course, CourseExtended
# Create your views here.
def index(request):
    # User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
    # models.Users.objects.filter(id__lte=7) | models.Users.objects.filter(id__gte=9)
    # courses = models.CourseExtended.objects.all()
    context = { 'courses': CourseExtended.objects.all().order_by('course__title') }

    # for each in context['courses']:
    #     print each.course.title, each.description, each.created_at, each.updated_at


    return render(request,'courses/index.html', context)

def create(request):
    if request.method == 'POST':
        temp = Course.objects.create(title = request.POST['title'])
        CourseExtended.objects.create(course_id=temp.id, description = request.POST['description'])
    return redirect('courses:index')

def showCourse(request,id):
    if request.method == 'GET':
        blah = CourseExtended.objects.get(course_id = id)
        context = {'course':blah }
        return render(request,'courses/show.html',context)
    return redirect('courses:index')

def update(request,id):

    if request.method == 'POST':
        blah = Course.objects.get(id = id)
        blah.title = request.POST['title']
        blah.save()

        data = CourseExtended.objects.get(course_id = id)
        data.course.title = request.POST['title']
        data.description = request.POST['description']
        data.save()
        return redirect('courses:index')
    return redirect('courses:index')

def delete(request,id):
    if request.method == 'GET':
        data = CourseExtended.objects.get(course_id = id)
        context = {'course':data}
        return render(request,'courses/delete.html',context)
    else:
        delete = Course.objects.get(id = id)
        delete.delete()
        return redirect('courses:index')
    return redirect('courses:index')
