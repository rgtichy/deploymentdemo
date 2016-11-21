from django.shortcuts import render, redirect
from . import models
def index(req):
    users = models.Users.objects.exclude(last_name='Rodriguez')
    # Add this line!
    print users.query
    print users
    users = models.Users.objects.filter(last_name='Rodriguez')|models.Users.objects.filter(first_name='Daniel')
    # Add this line!
    print users.query
    print users
    users = models.Users.objects.filter(last_name='Rodriguez').exclude(first_name='Madison')
    # Add this line!
    print users.query
    print users
    users = models.Users.objects.exclude(first_name='Daniel').exclude(first_name='Michael')
    # Add this line!
    print users.query
    print users
    users = models.Users.objects.filter(id=1)
    # Add this line!
    print users.query
    print users
    print users[0]
    users = models.Users.objects.select().filter(id=4).order_by('-first_name')    # Add this line!
    print users
    print "X"*78
    print "X"*78
    print users[0].id, users[0].first_name, users[0].last_name, users[0]
    rows = models.Friendships.objects.filter(friend=users[0])|models.Friendships.objects.filter(user=users[0]).order_by('user__last_name')

    rows = models.Friendships.objects.filter(friend=users[0])|models.Friendships.objects.filter(user=users[0])
    print rows.query
    for z in rows:
        print z.user.id,z.user.first_name, z.user.last_name, z.friend.id,z.friend.first_name, z.friend.last_name
    # print rows.first_name,rows.last_name
    #end of add
    context = {'users':users}
    return render(req, "friendapp/index.html",context)
