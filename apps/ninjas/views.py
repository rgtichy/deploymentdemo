from django.shortcuts import render, redirect

# Create your views here.
# def index(request):
#     context={}
#     return render(request,'ninjas/index.html',context)

def index(request, *args):
    context={}
    if not args:
            context['image'] = "/static/ninjas/TMNTs.gif"
            context['name'] = "Teenage Mutant Ninja Turles"
    else:
        arg = args[0]
        if arg == 'blue':
            context['image'] = "/static/ninjas/Leonardo.jpg"
            context['name'] = "Leonardo"
        elif arg == 'red':
            context['image'] = "/static/ninjas/Raphael.jpeg"
            context['name'] = "Raphael"
        elif arg == 'orange':
            context['image'] = "/static/ninjas/Michelangelo.jpg"
            context['name'] = "Michelangelo"
        elif arg == 'purple':
            context['image'] = "/static/ninjas/Donatello.jpeg"
            context['name'] = "Donatello"
        else:
            context['image'] = "/static/ninjas/April.jpg"

    return render(request,'ninjas/index.html',context)
