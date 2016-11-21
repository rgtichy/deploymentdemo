from django.shortcuts import render, redirect
import datetime, time, random
# Create your views here.
def index(request):
    content = {'time': datetime.datetime.now(), 'date': datetime.datetime.now()}
    print content
    # it implicitly assumes that I am already looking inside the templates folder of
    # the app path...
    return render(request,'timedisplay/index.html',content)

def randomWord(request):
    print 'randomWord'

    if not 'counter' in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    word = ''
    alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(0,14):
        word += alpha[random.randrange(0,52)]
    content={'word':word}
    return render(request,'timedisplay/random_word.html', content)
def randomWordButton(request):
    print 'randomWord Button pressed.'
    return redirect('/random_word')
