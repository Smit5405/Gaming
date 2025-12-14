from django.shortcuts import render,redirect
from django.contrib import auth


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        em = request.POST['email']
        fn = request.POST['fname']
        ln = request.POST['lname']
        un = request.POST['uname']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        print("VALUES:", em, fn, ln, un, p1, p2)    

        if p1 == p2:
            user = auth.get_user_model().objects.create_user(email=em, first_name=fn, last_name=ln, username=un, password=p1)
            user.save()
            print('User created successfully!')
            return redirect('/login/')
        else:
            print('Password not matching!!')
            return redirect('/register/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        un = request.POST['uname']
        p1 = request.POST['pass1']
        user = auth.authenticate(username=un, password=p1)
        # print(un,p1)
        # return
        if user is not None:
            auth.login(request,user)
            print('Login successful!')
            return redirect('/')
        else:
            print('Invalid username or password!!')
            redirect('/login/')

    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def logout(request): 
    auth.logout(request)
    print('Logout successfully!') 
    return redirect('/login/') 