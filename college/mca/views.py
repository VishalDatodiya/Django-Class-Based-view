from django.shortcuts import render
from django.http import HttpResponse

# class based view imported
from django.views import View

# imported forms
from .forms import ContactForm

# Function Based View
def myView(equest):
    return HttpResponse('<h1>Function Based View</h1>')


# Class Based View
class MyView(View):
    def get(self, request):
        return HttpResponse('<h1>Class Based View</h1>')

class MyViewWithName(View):
    # hardcoded value
    name = "vishal"
    
    # We can also get Dynamic name from the URL in as_view method
    # check the url
    def get(self, request):
        return HttpResponse(self.name)


# Inherit the Used defined Class Based View
class MyViewChild(MyViewWithName):
    # it will print hardcoded value ( vishal ) 
    # not dynamic value which is passing in MyViewWithName class from url ("shivaay")
    def get(self, request):
        return HttpResponse(self.name)
    
    
#################   Templates ################################

class Home(View):
    context = {
        'msg': "Hello this is Class Based View",
    }
    
    def get(self, request):
        return render(request, 'mca/home.html', self.context)
    
####################  forms  #############################


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Form submitted successfully!")

    return render(request, 'mca/contact.html', {'form':form})


class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'mca/contact.html', {'form':form})
        
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Form submitted successfully!")




