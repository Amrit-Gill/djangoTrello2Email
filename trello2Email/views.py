from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from trello2Email.trelloApi.trello2Email import trello2Email

def thanks(request):
    return HttpResponse("Successful")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
			print(form.cleaned_data)
			trello2Email(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})