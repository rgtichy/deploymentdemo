from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):

    if not request.session['user_id']:
        return redirect('/home/')
    qcourses = models.CourseExtended.objects.all().order_by('course__title')
    course_data=[]
    for each in qcourses:
        ucount = 0
        for user in each.course.user.all():
            ucount += 1
        course_data.append({'students':ucount, 'description': each.description,
        'id': each.course.id, 'title':each.course.title
         })
    # qcourses = models.Course.objects.all().order_by('title')
    # course_data = []
    # for each in qcourses:
    #     eachX = models.CourseExtended.objects.get(course_id=each.id)
    #     ucount = 0
    #     for user in each.user.all():
    #         ucount += 1
    #     course_data.append({'students': ucount, 'description': eachX.description,
    #     'id':each.id, 'title':each.title,
    #      })
    #
    context={'users': models.User.objects.all(),
             'courses': qcourses,
             'user' : models.User.objects.get(id = request.session['user_id']),
             'course_stats' : course_data
    }
    return render(request, 'user_course/index.html',context=context)
def create(request):

    if not request.session['user_id']:
        return redirect('/home/')
    if not request.method=='POST':
        return redirect('registrar:index')
    ufid = int(request.POST['user'])
    cfid = int(request.POST['course'])
    uf = models.User.objects.get(id= ufid)
    cf = models.Course.objects.get(id= cfid)
    cf.user.add(uf)
    cf.save()
    return redirect('registrar:index')
