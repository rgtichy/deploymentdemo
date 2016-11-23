from django.shortcuts import render, redirect
from .models import Item
# Create your views here.
def index(request):
    context = {'items' : Item.objects.all().order_by('name'),
    }
    if 'errors' in request.session:
        request.session.pop('errors')
    if 'formdata' in request.session:
        request.session.pop('formdata')
    return render(request,'inventory/index.html', context)

def new(request):
    context = {'edit':False,}
    if 'errors' in request.session:
        context = { 'edit':False,
            'errors':request.session['errors'],
            'formdata':request.session['formdata'],
        }
    return render(request,'inventory/item.html', context=context)

def create(request):

    if request.method == "POST":
        (flag,data) = Item.objects.newItem(request.POST)
        # True = Item Created, False = Item has errors
        if flag == True:
            return redirect('inventory:index')
        else:
            request.session['formdata'] = {'name': request.POST['item'],
                'description': request.POST['description'],
                'price': request.POST['price'],
            }
            request.session['errors'] = data
            return redirect('inventory:new')
    return redirect('inventory:index')
# Not necessary, edit screen without change/update works.
def show(request):
    return redirect('inventory:index')
#
#   Presents the "edit" screen for user input before validations
#
def edit(request,id):

    if not 'errors' in request.session:
        context = {}
        item = Item.objects.get(id=id)
        context = { 'edit':True,
            'formdata':{  'name':item.name,
                'description': item.description,
                'price': item.price,
                'id': item.id,
            },
        }
    else:
        context = { 'edit':True, 'formdata':request.session['formdata'],
        'errors':request.session['errors']
        }

    return render(request,'inventory/item.html', context=context)
#
#   Performs validations before pushing user to "edit" screen (for errors)
#   or performs the update via editItem then sends user to "inventory:index"
#
def update(request,id):

    if request.method == "POST":
        (error,data) = Item.objects.editItem(request.POST,id)

        if error == True:
            request.session['formdata'] = {
                'name': request.POST['item'],
                'description': request.POST['description'],
                'price': request.POST['price'],'id': id,
            }
            request.session['errors'] = data
            return redirect('inventory:edit', id=id)
        else:
            # No errors, update completed
            return redirect('inventory:index')
    return redirect('inventory:index')
#
#   pull item toDelete in and perform delete()
#
def destroy(request,id):
    if request.method == "POST":
        toDelete = Item.objects.get(id=id)
        toDelete.delete()
    return redirect('inventory:index')
