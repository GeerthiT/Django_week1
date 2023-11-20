from django.shortcuts import render
from BlogApp.form import NewUserForm
# Create your views here.



def home(request):
    return render(request,'blogTemplates/home.html')

def post(request):
    return render(request,'blogTemplates/post_detail.html')

def register(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return home(request)
        else:
            print('ERROR: Form Invalid')

    return render(request,'blogTemplates/signup.html',{'form':form})