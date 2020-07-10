from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic, AccessRecord, Webpage
from firstapp import forms

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
            print("successfully validated the post data")
            print("name: "+form.cleaned_data['name'])
            print("email: "+form.cleaned_data['email'])
            print("text: "+form.cleaned_data['text'])

    return render(request, 'firstapp/formpage.html', {'form':form})

def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record' : webpages_list}
    return render(request, 'firstapp/index.html', context=date_dict)