from django.shortcuts import render
from waitinglist.forms import NewUserForm

def index(request):
    return render (request, 'home/index.html' )

def NewUserView(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')
    
    return render(request, 'waitinglist/index.html', {'form':form})
